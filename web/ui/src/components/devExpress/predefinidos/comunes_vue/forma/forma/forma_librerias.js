import fuente_manejo from './fuente.js'
import validaciones  from './validaciones.js'

const busca_item = function(elementos, campo_id, ruta=[], contador=0) { 
    let seguir = true;    
    let encontro = false;
    let tipos_complejos = ["group", "tabbed"];
    for (const indice in elementos) {
        let componente = elementos[indice];
        let tipoCampo = componente.itemType;
        let nombreComponente = ( componente.dataField != undefined ? componente.dataField: componente.name ); 
        seguir = ( nombreComponente == campo_id ? false: true );
        encontro = !seguir; 
        if (seguir == true) {
            ruta.push(nombreComponente);            
            if ( (tipos_complejos.indexOf(tipoCampo) > -1) && ((componente.items != undefined) || (componente.tabs!= undefined)) ) {
                contador = 0;
                let elementos = ( componente.items != undefined ? componente.items: componente.tabs );
                contador += 1;
                let retorna = busca_item(elementos, campo_id, ruta, contador);  
                seguir = retorna[0];
                ruta = retorna[1];  
                if (seguir == true) {
                    contador -= 1;
                    if (contador == 0) {
                        ruta = ruta.filter(elemento => elemento !=  nombreComponente);                  
                    }
                } 
                else break;                                
            }
            else ruta.pop();            
        }
        else {       
            ruta.push(nombreComponente);
            break
        }
    }

    return [seguir, ruta, encontro]
};

const busca_campo = function(forma, campo) {
    let ruta       = [];
    let retorna    = busca_item(forma.forma.option("items"), campo, ruta);
    let ruta_texto = retorna[1].join('.');
    
    return ruta_texto
};

const asigna_opcion_forma = function(forma=null, campos=[], opcion="", valor) {
    let nombre     = null;
    let ruta_texto = "";
    for (const indice in campos) {        
        nombre = campos[indice]
        if (nombre.indexOf(".") == -1) { 
            ruta_texto = busca_campo(forma, nombre);
        }
        else {
            let buscar = nombre.substring(nombre.indexOf(".")+1);
            ruta_texto = busca_campo(forma, buscar);
        }
        let items = forma.forma.option("items"); 
        forma.forma.itemOption(ruta_texto, opcion, valor);
    }
};

const lee_opcion_forma = function(forma=null, campos=[], opcion="") {
    let nombre     = null
    let ruta_texto = "" 
    let opciones   = {}   
    for (const indice in campos) {        
        nombre = campos[indice];
        /*        
        if (nombre.search(".") == -1) { 
            ruta_texto = busca_campo(forma, nombre)
        }
        else {
            ruta_texto = nombre
        }*/        
        ruta_texto       = busca_campo(forma, nombre)                
        opciones[nombre] = forma.forma.itemOption(ruta_texto)[opcion]
    }

    return opciones
}

const salva_validadores_forma = function(forma_id="", opcion="") {
    let forma  = window.$componentes["_formas"][forma_id]
    let campos = window.$componentes["_campos"][forma_id]
    for (const nombre in campos) {        
        let ruta_texto = busca_campo(forma, nombre)
        if (window.$componentes["_opciones"][forma_id] == undefined) {
            window.$componentes["_opciones"][forma_id] = {}
        }
        if (window.$componentes["_opciones"][forma_id][nombre] == undefined) {
            window.$componentes["_opciones"][forma_id][nombre] = {}
        }
        window.$componentes["_opciones"][forma_id][nombre][opcion] = forma.forma.itemOption(ruta_texto)[opcion]
    }
    
    return window.$componentes["_opciones"][forma_id]
}

const borra_validador = function(validador="", validadores=[]) {
    let validadores_copia = [...validadores]
    let validadores_nuevo = []
    for (const indice in validadores_copia) {   
        if (validadores_copia[indice].name != validador) {
            validadores_nuevo.push(validadores_copia[indice])
        }     
    }
    
    return validadores_nuevo
}

const asigna_validador_forma = function(forma, campos, validador) {
    //forma.forma.beginUpdate()
    let validadores = lee_opcion_forma(forma, campos, "validationRules")
    for (const indice in campos) {        
        let campo             = campos[indice]
        let validadores_campo = validadores[campo]
        let validador_nuevo   = [...validadores_campo]
        validador_nuevo.push(validaciones.reglas_validacion[validador])
        asigna_opcion_forma(forma, [campo], "validationRules", validador_nuevo)
    } 
    //forma.forma.endUpdate()   
}

const borra_validador_forma = function(forma, campos, validador) {
    //forma.forma.beginUpdate();
    let validadores = lee_opcion_forma(forma, campos, "validationRules");    
    for (const indice in campos) {        
        let campo             = campos[indice];
        let validadores_campo = validadores[campo];
        let validador_nuevo   = borra_validador(validador, validadores_campo);
        asigna_opcion_forma(forma, [campo], "validationRules", validador_nuevo);
    }    
    //forma.forma.endUpdate();
}

const limpia_archivos = function(forma) {}

const asigna_opcion = function(forma=null, campos=[], opcion="", valor) {
    let nombre     = null;
    let componente = undefined;
    for (const indice in campos) {
        nombre     = campos[indice];
        componente = forma._campos[nombre];
        if (componente != undefined) {
            componente.component.option(opcion, valor);
        }
    }
}

const crea_fuente = function(tipo, fuente, filtros=[], eventos=[]) {
    let fuente_datos = fuente_manejo.fuente_datos(tipo, {"fuente": fuente}, filtros=filtros, eventos=eventos)

    return fuente_datos
}

const asigna_fuente_datos = function(forma=null, campo="", tipo="", fuente="", filtros=[], eventos={}) {
    let fuente_datos = crea_fuente(tipo, fuente, filtros, eventos);
    let componente   = forma._campos[campo].component;    
    componente.option("dataSource", fuente_datos);
}

const asigna_fuente = function(forma=null, campo="", fuente_datos) {
    let componente   = forma._campos[campo].component;    
    componente.option("dataSource", fuente_datos);  
}

const limpia_campos = function(forma=null, campos=[]) {
    asigna_opcion(forma, campos, "value", null);    
}

const asigna_valor_campos = function(forma=null, campos_valor={}, valores={}) {
    for (const campo in campos_valor) {
        let campo_id = campos_valor[campo]
        asigna_opcion(forma, [campo_id], "value", valores[campo]) 
    }   
}

const asigna_valor = function(forma=null, campo_id="", valor=null) {
    asigna_opcion(forma, [campo_id], "value", valor) 
}

const oculta_campos = function(forma=null, campos=[]) {
    //let inicio = Date.now()
    //forma.forma.beginUpdate()
    asigna_opcion_forma(forma, campos, "visible", false)
    //forma.forma.endUpdate()
    //let final = Date.now()
    //console.log("millisegundos:", inicio, final,  final-inicio)   
}

const muestra_campos = function(forma=null, campos=[]) {
    //forma.forma.beginUpdate()
    asigna_opcion_forma(forma, campos, "visible", true)
    //forma.forma.endUpdate()
}

const forma_lee_datos = function(forma=null) {
    let datos = forma.forma.option("formData")

    return datos
}

const forma_carga_datos = function(forma=null, datos={}) {
    forma.forma.option("formData", datos)
}

// Valida datos de una forma
const validar_datos = function(forma_instancia) {
    let valido = forma_instancia.validate().isValid;
    if (valido == false) {
        $notify("Valores invalido o no completos", "error") 
    }

    return valido;
}

// Datos forma clone()
const forma_datos = function(forma) {
    /*
    // Si tiene archivos se pierde esa informacion
    let datos = forma.formData;
    for (const atributo in datos) {
        informacion = validaAtributo(informacion, atributo, dataSend[atributo])
    }
    */
    return JSON.parse( JSON.stringify(forma.formData) )
}

// Envio de datos
const envio_accion = function(url_accion="_sin_direccion_", parametros={}, funcion_retorno=null, funcion_error=null) {
    let urlCompleta = window.$direcciones.servidorDatos + '/' + url_accion;  
    window.$f["http"].llamadoRestPost( urlCompleta, parametros, funcion_retorno, null, funcion_error)   
}

const envio_accion_notifica = function(url_accion="_sin_direccion_", parametros={}, funcion_retorno=null) {
    const _retorna_ = function(retorna_datos) {
        $ocultar_esperar();
        funcion_retorno(retorna_datos);
    };

    const _retorna_error_ = function(retorna_datos) {
        $ocultar_esperar();      
        // ... 
    };

    $mostrar_esperar();
    envio_accion(url_accion, parametros, _retorna_, _retorna_error_);    
}

export default {
    // Funciones generales
    crea_fuente            : crea_fuente,
    limpia_campos          : limpia_campos,
    oculta_campos          : oculta_campos,
    muestra_campos         : muestra_campos,
    asigna_fuente_datos    : asigna_fuente_datos,
    asigna_fuente          : asigna_fuente,
    asigna_opcion          : asigna_opcion,
    asigna_opcion_forma    : asigna_opcion_forma,
    lee_opcion_forma       : lee_opcion_forma,
    salva_validadores_forma: salva_validadores_forma,
    borra_validador        : borra_validador,
    borra_validador_forma  : borra_validador_forma,
    asigna_validador_forma : asigna_validador_forma,
    asigna_valor_campos    : asigna_valor_campos,
    asigna_valor           : asigna_valor,
    limpia_archivos        : limpia_archivos,
    forma_lee_datos        : forma_lee_datos,
    forma_carga_datos      : forma_carga_datos,

    validar_datos          : validar_datos,
    forma_datos            : forma_datos,
    envio_accion           : envio_accion,
    envio_accion_notifica  : envio_accion_notifica,
}