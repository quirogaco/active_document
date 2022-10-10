//Fuente de datos 
import CustomStore from "devextreme/data/custom_store"

//###########################################
//#  PREPARA PARAMETROS EN DATOS Y ARCHIVOS #
//###########################################

const esArchivo = function(valor) {
    let esArchivo = false;
    if (Array.isArray(valor)) {
        for (const indice in valor) {
            let elemento = valor[indice];
            if (elemento instanceof File) {
                esArchivo = true
            }
        }
    }
    else {
        if (valor instanceof File) {
            esArchivo = true
        }
    }

    return esArchivo;
};

const validaAtributo = function(archivos, nombre, valor) {
    let archivo = false;
    if (esArchivo(valor) == true) {
        archivo = true;
        if (Array.isArray(valor)) {
            for (const indice in valor) {
                let elemento = valor[indice];
                archivos.push(elemento)                
            }
        }
        else {
            archivos.push(valor)
        }
    }
    
    return archivo;
};

let prepararOpciones = function( datos ) {  
    let archivos  = []; 
    let eliminar  = [];
    let esArchivo = false;
    // Extrae archivos
    for (const atributo in datos) {
        esArchivo = validaAtributo(archivos, atributo, datos[atributo]);
        if (esArchivo == true) {
            eliminar.push(atributo)
        }
    }

    // Elimina archivos en datos originales
    for (const atributo in eliminar) {
        delete datos[ eliminar[atributo] ]
    }
    
    return archivos 
};

//###########################
//#  FUENTES DE DATOS FORMA #
//###########################
const retornaEnviaDatosForm = function(resultado, idComponente=null) {    
    if (idComponente != null) {
        if ( (window.$ns[idComponente] != undefined) && (window.$ns[idComponente].retornaEnvio != undefined) ) {
            window.$ns[idComponente].retornaEnvio(resultado)   
        }
    } 
}

const enviarDatosForma = function(accion, opcionesCarga, tipoComponente, idComponente, estructura) {
    let urlCompleta = window.$direcciones.servidorDatos + '/estructuras/comandos/' + estructura;   
    opcionesCarga['_usuario_'] = window.$usuario
    // Archivos
    let archivos = prepararOpciones( opcionesCarga );
    
    let controles   = {
        "__accion__"      : accion,            
        "__estructura__"  : estructura,
        "__idComponente__": idComponente,
        "__opciones__"    : {},
        "datos"           : opcionesCarga,
        "archivos"        : archivos
    }

    let data        = window.$f["http"].llamadoRestPost( urlCompleta, controles, retornaEnviaDatosForm, idComponente );  
    
    return data;
};

const fuenteDatosGlobalForma = function(tipoComponente, tipoFuente, idComponente, estructura, key="id") { 
    const fuente = new CustomStore({
        key  : key,

        insert: (valores) => {    
            let metodo = $lib.cargaAtributo(valores, "__peticion__", "insertar")
            return enviarDatosForma(metodo, valores, tipoComponente, idComponente, estructura)
        },

        update: function (key, valores) {
            valores["_id_"] = key;
            return enviarDatosForma("modificar", valores, tipoComponente, idComponente, estructura)
        },

        remove: function (key) {
            let valores = {
                "id": key
            }
            return enviarDatosForma("eliminar", valores, tipoComponente, idComponente, estructura)
        },
        
    });

    return fuente;
};

const creaFuenteDatosForma = function(tipoComponente, tipoFuente, idComponente, estructura) {    
    let dataSource = fuenteDatosGlobalForma(tipoComponente, tipoFuente, idComponente, estructura);

    return dataSource
};

export default {
    creaFuenteDatosForma    : creaFuenteDatosForma,
}