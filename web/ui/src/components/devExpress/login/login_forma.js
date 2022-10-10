import forma_objeto           from '../forma/utilidades/forma_objeto.js';
import crear_rutas_navegacion from '../../../librerias/crear_rutas_navegacion.js'

let campos = [
    forma_objeto.campo_objeto({
        'campo'      : 'codigo',
        'titulo'     : 'Codigo',
        'ancho'      : 300,
        'obligatorio': 'si'
    }),
    
    forma_objeto.campo_objeto({
        'campo'      : 'clave',
        'titulo'     : 'Clave',
        'modo'       : 'password',
        'ancho'      : 200,
        'obligatorio': 'si'
    }),

    forma_objeto.boton_objeto({
        'titulo'     : 'Ingresar',
        'ancho'      : 200,    
        'evt_click'  : async function() {
            window.$mostrar_esperar()
            let formaComponente = window.$ns["login_forma"].formaComponente
            let formaInstancia  = window.$ns["login_forma"].formaInstancia
            let validacion      = formaInstancia.validate()

            if (validacion.isValid == true) {
                // Llamado REMOTO
                let datos       = formaComponente.formData;                
                let urlCompleta = window.$direcciones.servidorDatos + '/ingreso_sistema';   
                let respuesta   = window.$f.http.llamadoRestSincGet( urlCompleta, datos );
                window.$ocultar_esperar()
                // Rutas de navegación
                if (respuesta.error == "no") {
                    window.$rutasNavegacion = crear_rutas_navegacion.creaRutasNavegacion(respuesta.datos.opciones);                   
                    window._APLICACION_.use(window.$rutasNavegacion.ruta);
                    window.$router = window.$rutasNavegacion.ruta;
                    window.sessionStorage.setItem("usuario", JSON.stringify(respuesta.datos.usuario));
                    window.sessionStorage.setItem("sesion", JSON.stringify(respuesta.datos.sesion));
                    await window.$ns['aplicacion'].asignaRuta('cajon', 'components/devExpress/cajon/cajon.vue');  
                    window.$ns['aplicacion'].asignaComponente('cajon');

                    window.$usuario = JSON.parse(window.sessionStorage.getItem("usuario"));                   
                }
                else {
                    $sistema["notifica"](respuesta.mensaje, "error");
                }
            }
            window.$ocultar_esperar()
        }    
    }),
    
]

let grupo_login = forma_objeto.grupo_objeto({
    'titulo'     : 'Ingreso al Sistema',
    'elementos'  : campos
});


let definicion = {
    'estructura': 'login',
    "titulo"    : "",
    'campos'    : [grupo_login],
    'ancho'     : 500,
    'barraVisible': false,
    'botones'   : {
        crea    : false, 
        modifica: false, 
        elimina : false, 
        regresa : false
    },
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente 