// Manejo de eventos
import mitt from 'mitt'
const emitter = mitt()
window.$emitter = emitter

// Visores de documentos
import visores from "./visores_archivo.js";
visores.iniciar()

// Librerias de forma
import librerias_forma                from "./librerias_forma.js"
import componentes_llamados_crud_form from "./componentes_llamados_crud_form.js"
import librerias_vue                  from "./librerias_vue.js"
import estructuras                    from "./estructuras.js"

const cargaAtributo = function(objeto, atributo, defecto=null) {
    let valor = defecto;
    if ( (objeto != undefined) && (objeto != null) ) {         
        if (objeto[atributo] != undefined) {
            valor = objeto[atributo];
        }
    }

    return valor;
}

const atributo = cargaAtributo;

const elimina_atributo = function(objeto, atributo) {
    let valor = objeto[atributo]
    try {
        delete objeto[atributo]
    } catch (error) {}

    return valor
}

let sin_valor = ["", null, "null", "NULL", "None", "NONE", "none", undefined, "undefined"];

const isObject = (item) => {
    return (
        item && 
        typeof item === 'object' && 
        !Array.isArray(item) && 
        item.constructor.name === "Object"
    );
}

const mezcla_profunda = (target, ...sources) => {
    if (!sources.length) return target;
        const source = sources.shift();

    if (isObject(target) && isObject(source)) {
        for (const key in source) {
            if (isObject(source[key])) {
            if (!target[key]) Object.assign(target, {
                [key]: {}
            });
            mezcla_profunda(target[key], source[key]);
            } else {
            Object.assign(target, {
                [key]: source[key]
            });
            }
        }
    }

    return mezcla_profunda(target, ...sources);
}

const uuidv4 = function() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

const valor_defecto = function(valor, defecto) {
    return valor != null ? valor : defecto
}

const definicion_defecto = function(id=null, id_base=null, atributos_base={}, atributos={}) {
    let id_campo          = $lib.valor_defecto(id, id_base)
    let atributos_campo   = Object.assign({}, atributos_base, atributos)
    atributos_campo["id"] = id_campo

    return {"id": id_campo, "atributos": atributos_campo}
}

const clone = function(original) {
    return JSON.parse(JSON.stringify(original))
}

// Para asignación a clases o componentes y no a objetos
const assignAttributes = function(destino, fuente) {
    for (const etiqueta in fuente) {
        destino[etiqueta] = fuente[etiqueta]
    }    

    return destino
}

const json_texto = function(objeto) {
    return JSON.stringify(objeto)
}

const texto_json = function(texto) {
    return JSON.parse(texto)
}

const llamar_componente = function(componente, parametros, texto=true) {
    let params;
    if (texto == true) {
        params = {
            attributes_str: $lib.json_texto(parametros)
        }       
    }
    else {
        params = {
            attributes: parametros
        } 
    }

    $router.push({
        name  : componente,        
        params: params    
    }) 
}

export default {
    sin_valor                   : sin_valor,
    cargaAtributo               : cargaAtributo,
    atributo                    : atributo,
    elimina_atributo            : elimina_atributo,
    valoresForma                : librerias_forma.valoresForma,
    validaValoresForma          : librerias_forma.validaValoresForma,
    traer_componentes           : librerias_forma.traer_componentes,
    forma_atributo_item         : librerias_forma.forma_atributo_item,
    forma_atributo_items        : librerias_forma.forma_atributo_items,
    forma_atributos             : librerias_forma.forma_atributos,
    leer_forma_atributo_item    : librerias_forma.leer_forma_atributo_item,
    leer_forma_atributo_items   : librerias_forma.leer_forma_atributo_items,
    leer_forma_componente_opcion: librerias_forma.leer_forma_componente_opcion,
    forma_componente_opcion     : librerias_forma.forma_componente_opcion,
    forma_componentes_opcion    : librerias_forma.forma_componentes_opcion,
    traer_fuente_datos          : librerias_forma.traer_fuente_datos,
    valida_forma_datos          : librerias_forma.valida_forma_datos,

    enviaForma                  : componentes_llamados_crud_form.enviaForma,

    // Operaciones estructuras
    leer_registro_id            :  estructuras.leer_registro_id,
    
    // Mezcla de objetos
    mezcla_profunda             : mezcla_profunda,

    // Visor archivos
    descargar_archivo_remoto    : visores.descargar_archivo_remoto,
    prepara_datos_visor_archivo : visores.prepara_datos_visor_archivo,
    prepara_parametros_archivo  : visores.prepara_parametros_archivo,
    unifica_datos_visor         : visores.unifica_datos_visor,

    // UIID
    uuidv4                      : uuidv4,

    valor_defecto               : valor_defecto,
    definicion_defecto          : definicion_defecto,

    // Librerias VUE
    forma_componente            : librerias_vue.forma_componente,

    // clone
    clone                       : clone,
    assignAttributes            : assignAttributes,
    json_texto                  : json_texto,
    texto_json                  : texto_json,
    llamar_componente           : llamar_componente,
    isObject                    : isObject
}