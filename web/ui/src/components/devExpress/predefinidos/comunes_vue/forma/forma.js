import fecha            from './fecha.js';
import texto            from './texto.js';
import correo           from './correo.js';
import entero           from './entero.js';
import texto_area       from './texto_area.js';
import chequeo          from './chequeo.js';
import seleccion        from './seleccion.js';
import etiqueta         from './etiqueta.js';
import radio            from './radio.js';
import archivo          from './archivo.js';
import contenido        from './contenido.js';
import grid             from './grid.js';
import grupo            from './grupo.js';
import pestana          from './pestana.js';
import pestana_panel    from './pestana_panel.js';
import boton            from './boton.js';
import botonBarra       from './botonBarra.js';
import botonGrupoBarra  from './botonGrupoBarra.js';
import seleccionBarra   from './seleccionBarra.js';
import dropDownButtonBarra from './dropDownButtonBarra.js';
import forma_librerias  from './forma_librerias.js';
import forma_propiedades_funciones from './forma_propiedades_funciones.js';

const genera_campos_lectura = function(forma, campos) {
    let campos_lectura = []
    let atributos      = {
        forma: forma
    }
    for (const indice in campos) {
        let campo = campos[indice]
        let atributos_base = {
            'titulo' : campo['titulo'],
            'lectura': true
        }
        let tipo        = $librerias.cargaAtributo(campo, 'tipo', "texto")
        let campo_nuevo = genera_campo(tipo, campo['id'], null, atributos_base, atributos)
        campos_lectura.push(campo_nuevo)
    }

    return campos_lectura
}

const campos_anidados = function(definicion) {
    let nuevosElementos = [];
    let elementos       = definicion.atributos.elementos;
    if (elementos != undefined) {
        for (let index in elementos) {
            nuevosElementos.push( campo(elementos[index]) )
        }
    }    

    definicion.atributos.elementos = nuevosElementos

    return definicion
};

const genera_campo = function(
    tipo, 
    id_base=null, 
    id=null, 
    atributos_base={}, 
    atributos={}
) {
    let definicion = $lib.definicion_defecto(
        id, 
        id_base, 
        atributos_base, 
        atributos
    );  
    let campo = null
    definicion["atributos"]["tipo"] = tipo;    
    switch (tipo) {
        case "grupo":     
            definicion = campos_anidados(definicion);
            campo = grupo.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "fecha":            
            campo = fecha.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "texto":
            campo = texto.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "correo":
            campo = correo.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "entero":
            campo = entero.campo(
                definicion["id"],
                definicion["atributos"]
            );            
            break

        case "texto_area":
            campo = texto_area.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "seleccion":
            campo = seleccion.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "etiqueta":
            campo = etiqueta.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "radio":
            campo = radio.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break
                
        case "chequeo":
            campo = chequeo.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "archivo":
            campo = archivo.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "contenido":
            campo = contenido.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "boton":
            campo = boton.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break

        case "grid":
            campo = grid.campo(
                definicion["id"],
                definicion["atributos"]
            );
            break
    }  

    return campo
}

const campo = function(atributos) {
    let tipo    = $librerias.atributo(atributos, 'tipo', "texto");
    let id_base = $librerias.atributo(atributos, 'id', "id_");

    return genera_campo(tipo, id_base, null, atributos, {})
}

export default {
    // Campos de la forma
    fecha                : fecha.campo,
    texto                : texto.campo,
    entero               : entero.campo,
    texto_area           : texto_area.campo,
    chequeo              : chequeo.campo,
    seleccion            : seleccion.campo,
    etiqueta             : etiqueta.campo,
    radio                : radio.campo,
    archivo              : archivo.campo,
    contenido            : contenido.campo,
    grid                 : grid.campo,
    grupo                : grupo.campo,
    pestana              : pestana.campo,
    pestana_panel        : pestana_panel.campo,  
    boton                : boton.campo,
    botonBarra           : botonBarra.campo,
    botonGrupoBarra      : botonGrupoBarra.campo,
    seleccionBarra       : seleccionBarra.campo,
    dropDownButtonBarra  : dropDownButtonBarra.campo,
    genera_campo         : genera_campo,
    campo                : campo,
    genera_campos_lectura: genera_campos_lectura,

    // Funciones de la forma
    forma_funciones  : forma_propiedades_funciones.forma_funciones,
    lee_propiedades  : forma_propiedades_funciones.lee_propiedades,
    // Propiedadess de la forma        
    forma_propiedades: forma_propiedades_funciones.forma_propiedades,

    // Funciones generales de forma inicial general
    crea_fuente            : forma_librerias.crea_fuente,
    limpia_campos          : forma_librerias.limpia_campos,
    oculta_campos          : forma_librerias.oculta_campos,
    muestra_campos         : forma_librerias.muestra_campos,
    asigna_fuente_datos    : forma_librerias.asigna_fuente_datos,
    asigna_fuente          : forma_librerias.asigna_fuente,
    asigna_opcion          : forma_librerias.asigna_opcion,
    asigna_opcion_forma    : forma_librerias.asigna_opcion_forma,
    lee_opcion_forma       : forma_librerias.lee_opcion_forma,
    lee_valor              : forma_librerias.lee_valor,
    salva_validadores_forma: forma_librerias.salva_validadores_forma,
    borra_validador        : forma_librerias.borra_validador,
    borra_validador_forma  : forma_librerias.borra_validador_forma,
    asigna_validador_forma : forma_librerias.asigna_validador_forma,
    asigna_valor_campos    : forma_librerias.asigna_valor_campos,
    asigna_valor           : forma_librerias.asigna_valor,
    limpia_archivos        : forma_librerias.limpia_archivos,
    forma_lee_datos        : forma_librerias.forma_lee_datos,
    forma_carga_datos      : forma_librerias.forma_carga_datos,
    validar_datos          : forma_librerias.validar_datos,
    forma_datos            : forma_librerias.forma_datos,
    envio_accion           : forma_librerias.envio_accion,
    envio_accion_notifica  : forma_librerias.envio_accion_notifica,

    // Funciones de forma directa ultimo diseño con script setup 
    formData               : forma_propiedades_funciones.formData, 
    forma_validacion       : forma_propiedades_funciones.forma_validacion
}