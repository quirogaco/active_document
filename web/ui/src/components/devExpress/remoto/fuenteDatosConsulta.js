//Fuente de datos 
import CustomStore from "devextreme/data/custom_store";

//##########################
//#  FUENTES DE DATOS GRID #
//##########################
const array_simple = function( arreglo ) {
    let simple = true
    for (const indice in arreglo) {
        if (Array.isArray(arreglo[indice])) simple = false;
    }

    return simple
};

const cargaDatosConsulta = function(
    opcionesCarga, 
    tipoComponente, 
    idComponente, 
    rutaRemota, 
    filtrosFijos=[], 
    eventos={}, 
    ordenar_campos=[]
) {  
    // Copia filtros basicos
    let filtrosTemp = []
    if ( (opcionesCarga.filter != null) && (opcionesCarga.filter != undefined) ) {
        filtrosTemp = opcionesCarga.filter.map((x) => x)
    };    

    let filtrosCompletos = []
    let longitud = filtrosFijos.length 
    if (longitud > 0) {
        if (array_simple( filtrosFijos ) == true) {
            filtrosCompletos.push(filtrosFijos)
        }
        else {
            filtrosCompletos = filtrosFijos.map((x) => x)
        }            
        
        if (filtrosTemp.length > 0) {
            filtrosCompletos.push(filtrosTemp)
        }
    }
    else {
        filtrosCompletos = filtrosTemp
    };
    
    // Agrupaciones
    let grupos = [];
    if ( (opcionesCarga.group != null) && (opcionesCarga.group != undefined) ) 
        grupos = opcionesCarga.group;

    // Desde
    let desde = 0;
    if ( (opcionesCarga.skip != null) && (opcionesCarga.skip != undefined) ) 
        desde = opcionesCarga.skip;

    // Hasta
    //let hasta = 10000;
    let hasta = 200;
    if ( (opcionesCarga.take != null) && (opcionesCarga.take != undefined) ) 
        hasta = opcionesCarga.take;

    // Campo de busqueda
    let campoBusqueda = null;
    if ( (opcionesCarga.searchExpr != null) && (opcionesCarga.searchExpr != undefined) ) 
        campoBusqueda = opcionesCarga.searchExpr;

    // Operación de busqueda
    let operacionBusqueda = null;
    if ( (opcionesCarga.searchOperation != null) && (opcionesCarga.searchOperation != undefined) ) 
        operacionBusqueda = opcionesCarga.searchOperation;

    // Valor de busqueda
    let valorBusqueda = null;
    if ( (opcionesCarga.searchValue != null) && (opcionesCarga.searchValue != undefined) ) 
        valorBusqueda = opcionesCarga.searchValue;

    // Ordenamientos
    let ordenamientos = [];
    function creaOrdenamiento(element, index, array) {
        let valorOrden = (element.desc == true ? 0 : 1)
        let orden = {
            [element.selector]: valorOrden
        }
        ordenamientos.push(orden)
    }

    // Campos a retornar
    let campos = [];
    if ( (opcionesCarga.campos != null) && (opcionesCarga.campos != undefined) ) 
        campos = opcionesCarga.campos;

    // Resaltar busquedas inner, las no inner?
    let resaltar = [];
    if ( (opcionesCarga.resaltar != null) && (opcionesCarga.resaltar != undefined) ) 
        resaltar = opcionesCarga.resaltar;

    if (opcionesCarga.sort != null) {  
        // Ordenamiento especifico de la libreria
        opcionesCarga.sort.forEach(creaOrdenamiento)
    }

    // Ordenamiento por parametros
    ordenar_campos.forEach(creaOrdenamiento)

    let enviar = {
        'desde'        : desde,
        'hasta'        : hasta,
        'grupos'       : grupos,        
        'ordenamientos': ordenamientos,
        'filtros'      : filtrosCompletos,
        'campos'       : campos,
        'resaltar'     : resaltar,

        // Usados para selectbox 
        'campoBusqueda'    : campoBusqueda,
        'operacionBusqueda': operacionBusqueda,
        'valorBusqueda'    : valorBusqueda,
        '_usuario_'        : window.$usuario
    }    
   
    // post es necesarios para que interprete bien los arrays de objetos
    let urlCompleta = window.$direcciones.servidorDatos + '/estructuras/consulta/' + rutaRemota;     
    let data        = window.$f["http"].post(urlCompleta,  {params: enviar}).then(respuesta => {              
        const resultado = respuesta.data.data;
        let datos = [];        
        if (resultado.items.agrupado == true) {
            datos = resultado.items            
        }
        else {
            let resaltados = (resultado.resaltados !== undefined ? resultado.resaltados : []);
            datos = {
                "totalCount": resultado.total,
                "data"      : resultado.items,
                "resaltados": resaltados
            }
        }
        
        if (tipoComponente == "grid") {
            return datos;
        }
        else {
            return datos.data;
        }        
    }).
    catch( error => {
        let response = {};
        if (error.response) {
            response = {
                type : "app",
                error: error.response
            }
        } else if (error.request) {
            response = {
                type : "request",
                error: error.request
            }
        } else {
            response = {
                type : "unkwon",
                error: error.message
            }
        }
        window.$f["http"].errorFunction(response);

        return {}
    })

    return data;    
};

const fuenteDatosGlobalConsulta = function(
    tipoComponente, 
    idComponente, 
    estructura, 
    key="id", 
    filtros=[], 
    eventos={}, 
    ordenar=[], 
    campos=[]) 
{  
    // Eventos
    const cargar_datos_antes = 
        (eventos.cargar_datos_antes !== undefined ? eventos.cargar_datos_antes: null);
    const cargar_datos_despues = 
        (eventos.cargar_datos_despues !== undefined ? eventos.cargar_datos_despues: null);      
    
    let fuente = new CustomStore({
        key: key,
        cacheRawData: false,

        load: (opcionesCarga) => {   
            let datos = []             
            if (opcionesCarga.searchOperation != "NO_BUSCAR") {  
                opcionesCarga.campos = campos;                  
                datos = cargaDatosConsulta(
                    opcionesCarga, 
                    tipoComponente, 
                    idComponente, 
                    estructura, 
                    filtros, 
                    eventos, 
                    ordenar
                )   
            }
            
            return datos;            
        },

        byKey: (key) => {   
            let opcionesCarga = {
                searchExpr     : "id",
                searchOperation: "=",
                searchValue    : key,
                campos         : campos
            };

            let datos = [];                      
            datos = cargaDatosConsulta(
                opcionesCarga, 
                tipoComponente, 
                idComponente, 
                estructura, 
                filtros, 
                eventos, 
                ordenar
            )

            return datos;  
        },
        
        onLoading: function (opciones) {
            let componente = window.$ns[idComponente];
            if ( (componente != undefined) && (tipoComponente == "grid") ) {
                opciones["campos"] = componente.nombresColumnas;              
            };

            if (cargar_datos_antes != null) {
                opciones = cargar_datos_antes(opciones, idComponente)
            } 
            return opciones;
        },

        onLoaded: function (resultado) {
            if (cargar_datos_despues != null) {
                resultado = cargar_datos_despues(resultado, idComponente)
            }         
            
            return resultado
        }
    })

    return fuente;
}
                                        
const creaFuenteDatosConsulta = function(
    tipoComponente, 
    tipoFuente, 
    idComponente, 
    estructura, 
    filtros=[], 
    eventos={}, 
    ordenar=[], 
    campos=[]
) {  
    let dataSource = fuenteDatosGlobalConsulta(
        tipoComponente, 
        idComponente, 
        estructura, 
        "id", 
        filtros, 
        eventos, 
        ordenar, 
        campos
    )

    return dataSource
}

const creaFuenteDatosUniversal = function(
    tipo, 
    idComponente, 
    estructura, 
    datos=null, 
    filtros=[], 
    eventos={}, 
    ordenar=[], 
    campos=[]
) {    
    if (datos == null) {                
        let dataSource = fuenteDatosGlobalConsulta(
            tipo, 
            idComponente, 
            estructura, 
            "id", 
            filtros, 
            eventos, 
            ordenar, 
            campos
        )
        return dataSource

    }
    else {
        return datos
    }
}

export default {
    creaFuenteDatosConsulta : creaFuenteDatosConsulta,
    creaFuenteDatosUniversal: creaFuenteDatosUniversal,
    cargaDatosConsulta      : cargaDatosConsulta
}