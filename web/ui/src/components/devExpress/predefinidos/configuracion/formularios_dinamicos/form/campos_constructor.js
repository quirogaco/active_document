import { confirm }    from 'devextreme/ui/dialog';
import campos_tipo    from './campos_tipo.js';
import campos_eventos from './campos_eventos.js';

// Carga valores a la forma de edicion de atributo
const carga_atributos = function(forma, campo) {
    // Campo completo
    forma.opciones_atributo.datos._campo = campo;
    // Tipo
    forma.opciones_atributo.datos.tipo   = campo._tipo;
    // Titulo general
    forma.opciones_atributo.datos.titulo = campo.label.text;
    // Titulo campo
    forma.opciones_atributo.datos.label  = campo.label.text;
    // Codigo Campo
    forma.opciones_atributo.datos.codigo = campo.dataField;
    // Valor obligatorio
    if (campo.isRequired == true) {
        forma.opciones_atributo.datos.obligatorio = "SI";
    }
    else {
        forma.opciones_atributo.datos.obligatorio = "NO";
    }
    // Elementos de seleccion, opciones
    forma.opciones_atributo.datos.elementos = campo.editorOptions.items.toString();
}

const limpia_atributos = function(forma) {
    forma.opciones_atributo.datos = {
        titulo: ""
    }
}

// Item creado
const item_listo_forma = function(forma) {
    const item_listo = function(objeto) {
        let componente = objeto.component;
        let nombre     = componente.option("name");
        campos_eventos.drag_eventos(forma, "_contiene_" + nombre);
    }

    return item_listo
}

const activa_atributos = function(forma, campo) {
    forma.muestra_atributos = true;
    forma.muestra_key      += 1;
    forma.calcula_forma_tamano();
    limpia_atributos(forma)
    carga_atributos(forma, campo)        
}

const desactiva_atributos = function(forma) {    
    forma.muestra_atributos = false;
    forma.calcula_forma_tamano();
    limpia_atributos(forma)
}

const click_campo_accion = function(forma, tipo, campo_accion) {
    // Icono editar de un campo
    const click_campo_editar = function(objeto) {
        activa_atributos(forma, campo_accion);      
    }

    // Icono borrar de un campo
    const click_campo_borrar = function(objeto) {
        let borrar = -1
        for (const indice in forma.campos) {
            let campo = forma.campos[indice]
            if (campo.name == campo_accion.name) borrar = indice;
        }
    
        if (borrar != -1) {            
            let resultado = confirm("Esta seguro borrar ? <b>" + campo_accion.name + "</b>", "Borrar campo!" );
            resultado.then((dialogo_resultado) => {
                if (dialogo_resultado == true) {
                    forma.campos.splice(borrar, 1);
                    forma.forma_diseno.repaint();
                    desactiva_atributos(forma);
                }
            })
        }        
    }

    let accion = null
    if (tipo == "editar") accion = click_campo_editar;
    if (tipo == "borrar") accion = click_campo_borrar;

    return accion
}

// Creacion de campo nuevo
let contador = 0
const campo_nuevo = function(forma, datos) {
    // Evento Foco del item
    const item_foco = function(objeto) {
        //let componente = objeto.component;
        //let nombre     = componente.option("name");
        //activa_atributos(forma, nuevo_campo);     
    }

    //Evento Pierde Foco del item
    const item_pierde_foco = function(objeto) {
        //let componente = objeto.component;
        //let nombre     = componente.option("name");
        //desactiva_atributos(forma);
    }

    // Nombre defecto
    contador   += 1;
    let nombre =  forma.datos_drag.tipo + "_" + contador;
    
    // Crea campo
    let nuevo_campo = campos_tipo.crear_definicion(nombre, forma.datos_drag, $lib.uuidv4());  
    nuevo_campo.editorOptions.onContentReady = item_listo_forma(forma);
    nuevo_campo.editorOptions.onFocusIn      = item_foco;
    nuevo_campo.editorOptions.onFocusOut     = item_pierde_foco;

    return nuevo_campo
}

// Mover campo visualmente
const campo_insertar = function(forma, datos) {
    let nuevo_campo = campo_nuevo(forma, datos);
    
    if (forma.campos.length == 0) {
        forma.campos.push(nuevo_campo);
    }
    else {
        if (datos.sobre == true) {
            forma.campos.splice(datos.posicion, 0, nuevo_campo);
        }
        else {
            forma.campos.splice((datos.posicion+1), 0, nuevo_campo);
        }
    }        
    forma.forma_diseno.repaint();
}

export default {
    click_campo_accion: click_campo_accion,
    campo_insertar    : campo_insertar,
    campo_mover       : campos_eventos.campo_mover,
    drag_eventos      : campos_eventos.drag_eventos
}