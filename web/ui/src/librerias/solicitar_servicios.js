import http from './http.js';
import crear_rutas_navegacion from './crear_rutas_navegacion.js'

// ######################################
// Solicita definiciones de componentes #
// ######################################
const cargarDefinicion = function(clase, idDefinición) {
    let urlCompleta = window.$direcciones.servidorDatos + '/definiciones_visuales/'; 
    urlCompleta += clase+ '/' + idDefinición; 

    let parametros = { }    
    let respuesta  = http.llamadoRestSincGet( urlCompleta, parametros );
    
    return respuesta;
}

// ##########################
// Soliita opciones de menu #
// ##########################
const llamaOpciones = function(urlCompleta, parametros) {
    let respuesta = http.llamadoRestSincGet( urlCompleta, parametros );

    return respuesta.datos;
}

const cargarOpciones = function(usuario_id) {
    let urlCompleta = window.$direcciones.servidorDatos + '/servicios/opciones_usuario';
    let parametros  = {
        "__accion__" : "leer",
        "usuario_id" : usuario_id
    }
    let respuesta       = llamaOpciones( urlCompleta, parametros);
    let rutasNavegacion = crear_rutas_navegacion.creaRutasNavegacion(respuesta);
    
    return rutasNavegacion;
}

export default {
    cargarDefinicion: cargarDefinicion,
    cargarOpciones  : cargarOpciones
};