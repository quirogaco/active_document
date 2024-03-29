// Estilos boostrap
//import '../gestor/css/bootstrap.min.css'
import '../gestor/css/bootstrap_custom.css';

// Estilos devexpress
import 'devextreme/dist/css/dx.common.css';
import 'devextreme/dist/css/dx.light.css';

// Font awesome
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/all.js';

// ############################
// # CONFIGURACIÓN DEVEXPRESS #
// ############################
// Grid estilos
import '../gestor/css/estilos.css';

// store
import { createPinia } from 'pinia';

// Necesario para que funciones Handlebars
window.global = window;

/*global $lib*/

// ######################################
// # ALMACENAMIENTO DE DATOS Y OPCIONES #
// ######################################
// Definición de objetos para almacenar información general
window.$ns          = {}; // Guarda componentes por nombre (ruta_id), ej. terceros_nombre
window.$direcciones = {  // Direccciones de datos para servicios ip:puerto, ej. "192.168.0.13:9100"
    "servidorDatos": "http://" + _ambiente_.CFG_DATA_HOST + ":" + _ambiente_.CFG_DATA_PORT
};
window.$definiciones          = {}; // Definiciones de componentes para fuentes de datos
window.$componentes           = {
    "_formas"     : {},
    "_campos"     : {},
    "_definicion" : {},
    "_opciones"   : {}
}; // Rutinas de creacion dinamica parametros de componentes
window.$clases                = {};
window.$componentesDef        = {}; // Definiciones de componentes por ruta + "_" + id
window.$componentesRutas      = {}; // Guarda rutas de importación de componentes desde librerias
window.$datosComponentes      = {}; // Almacena informacion de datos de los componentes
window.$f                     = {}; // Funciones generales importadas
window.$temporales            = {}; // Guarda valores tetmprales para campos regsitrados
window.$componentesNDET       = {}; // Componente NDE (NO DEVELOPER EXPRESS) o componente creados por template, por forma
window.$globales              = {}; // Espacio para variables globales necesarias
window.$usuario               = {}; // Información del usuario
window.$sistema               = {}; // Componentes universales del sistema
window.$campos                = {}; // Campos de las formas
window.$cmp                   = {}; // Componentes

// #############################################
// # RUTAS DE ARCHIVO PARA VISORES Y DESCARGAR #
// ############################################
window.$ruta_pdf      = window.$direcciones.servidorDatos + '/manejo_pdf/';
window.$ruta_archivos = window.$direcciones.servidorDatos + '/manejo_archivo/'; 

// ###############################
// # Carga funciones universales #
// ###############################
// Librerias de llamados de componentes
import componentes_llamados_crud from './librerias/componentes_llamados_crud.js';
window.$f["componentes_llamados_crud"] = componentes_llamados_crud;

// Llamados http axios, y sincronicos
import http from './librerias/http.js';
window.$f["http"] = http;
window.$http = http;

// ################################
// # Carga componenetes generales #
// ################################
// Fuentes de datos
import fuenteDatos from './components/devExpress/remoto/fuenteDatos.js';
window.$sistema["fuenteDatos"] = fuenteDatos;

// Notificaciones
import notify from 'devextreme/ui/notify';
import { alert } from "devextreme/ui/dialog";
window.$sistema["notifica"] = notify;
window.$notify = notify;
window.$alert  = alert;

// Formas
import forma from "./components/devExpress/predefinidos/comunes_vue/forma/forma.js";
window.$forma = forma;

// ###################
// # CREA APLICACIÓN #
// ###################
// Importa utilidades
import registrar from './librerias/registrar.js';

import { createApp } from 'vue';
import App from './App.vue';

// tailwindcss
import './index.css'; // Debe ir aqui despues de App
const pinia = createPinia()
window._APLICACION_ = createApp(App);
window._APLICACION_.use(pinia)
registrar.registrar_componentes(window._APLICACION_);
window._APLICACION_.mount('#aplicacion');

// ###################################
// # IMPORTA COMPONENTES Y LIBRERIAS #
// ###################################
// Importa utilidades
import librerias from './librerias/librerias.js';
window.$librerias = librerias; // Librerias 
window.$lib       = window.$librerias; // Librerias 

// IDIOMA ESPAÑOL
import { locale, loadMessages } from 'devextreme/localization';
import espanol from "devextreme/localization/messages/es.json";
locale("es");
loadMessages(espanol);

// Carga rutas de componentes predefinidos en archivo VUE
import rutas_predefinidos from './rutas/rutas_predefinidos.js'

// ################
// # ONLY OFFCICE #
// ################
var validaApi = function() {
    console.log("******>>> urlOnlyOffice - MAIN:", urlOnlyOffice)
    console.log("******>>> urlOnlyOffice->DocsAPI - MAIN:", DocsAPI)
}
// let urlOnlyOffice = (
//     "https://" + 
//     _ambiente_.CFG_SERVICIOS_URL + 
//     ":" + 
//     _ambiente_.CFG_ONLYOFFICE_PORT + 
//     "/web-apps/apps/api/documents/api.js"
// );
let urlOnlyOffice = (
    "http://" + 
    _ambiente_.CFG_NGINX_HOST + 
    ":" + 
    _ambiente_.CFG_NGINX_PORT + 
    "/web-apps/apps/api/documents/api.js"
);
http.cargaJS(urlOnlyOffice, validaApi, document.body);

// Enlace pagina WEB SERVICIO AL CIUDADANO
let busqueda = window.location.search;
busqueda = busqueda.replace('?', '');
busqueda = busqueda.replace('/', '');
let opciones   = busqueda.split('=');
let formularios = ["anonimo", "natural", "juridica", "consulta"];
let ruta       = opciones[0];
let formulario = opciones[1];

// IMPRESIÓN
import printjs from 'print-js';
window.$print = printjs;

// RUTAS
import rutas_cortas from './rutas/rutas_cortas.js';
let aplicacion = window.$ns['aplicacion'];

// Muestra formulario
if ( (ruta == "formulario") && (formularios.indexOf(formulario) > -1) ) {
    window.$componentesRutas = rutas_cortas.rutas_componentes;   
    window.$ns['aplicacion'].crea_enrutador(); 
    if (formulario == "anonimo")
        await window.$ns['aplicacion'].asignaRuta(
            'anonimo_web_forma', 
            'components/devExpress/predefinidos/radicados_vue/entrada/web_anonimo_formulario/web_anonimo_forma_radicado.vue'
        );   
        window.$ns['aplicacion'].asignaComponente('anonimo_web_forma');
    
    if (formulario == "natural") {
        await window.$ns['aplicacion'].asignaRuta(
            'natural_web_forma', 
            'components/devExpress/predefinidos/radicados_vue/entrada/web_natural_formulario/web_natural_forma_radicado.vue'
        ); 
        window.$ns['aplicacion'].asignaComponente('natural_web_forma');
    }

    if (formulario == "juridica") {
        await window.$ns['aplicacion'].asignaRuta(
            'radicado_juridica_forma', 
            'components/devExpress/predefinidos/radicados_vue/entrada/web_juridica_formulario/web_juridica_forma_radicado.vue'
        ); 
        window.$ns['aplicacion'].asignaComponente('radicado_juridica_forma');
    }

    if (formulario == "consulta") {
        await window.$ns['aplicacion'].asignaRuta(
            'consulta_radicados_web', 
            '/components/devExpress/predefinidos/radicados_consulta/consulta_radicados_web.vue'
        ); 
        window.$ns['aplicacion'].asignaComponente('consulta_radicados_web');
    }
}
else {   
    // CARGA APLICATIVO    
    window.$componentesRutas = rutas_predefinidos.rutas_componentes
    //window.$ns['aplicacion'].crea_enrutador();
    await window.$ns['aplicacion'].asignaRuta('login_forma', 'components/devExpress/login/login_forma.vue');  
    window.$ns['aplicacion'].asignaComponente('login_forma');
    
    
    /* Especificos ára ruebas        
    window.sessionStorage.setItem("usuario", JSON.stringify({
        //"id": "0a83bbe0-cddd-11eb-bc8f-acfdce646f0d",
        "id": "46de06e8-d5f5-11ec-ba28-005056862cfc",
        "codigo": "PROFESIONAL",
        "nombre": "HUMBERTO OSPINA -PROFESIONAL",
        "correo": "QUIROGACO@GMAIL.COM",
        "dependencia_id": "d46a3fa2-af81-11eb-92af-006073b60f8a",
        "dependencia_nombre": "coordinacion academica",
        "ubicacion_id": "be776b15-ab68-11eb-b9de-006073b60f8a",
        "ubicacion_nombre": "sede central bogota",
        "reemplaza_id": null,
        "roles_especificos": ['JEFE', 'ARCHIVO', 'CORRESPONDENCIA', 'PQRSD']
    }))
    window.$usuario = JSON.parse(window.sessionStorage.getItem("usuario"));
    //await window.$ns['aplicacion'].asignaRuta('cajon', '/components/devExpress/cajon/cajon.vue');  
    
    // await window.$ns['aplicacion'].asignaRuta(
    //     'trd_basica_grid',  
    //     '/components/devExpress/predefinidos/archivo/trd/definicion/grid_trd/trd_basica_grid.vue'
    // );   

    // await window.$ns['aplicacion'].asignaRuta(
    //     'trd_pantalla',  
    //     '/components/devExpress/predefinidos/archivo/trd/definicion/pantalla_trd/pantalla_trd.vue'
    // );   
    
    await window.$ns['aplicacion'].asignaRuta(
        'expediente_basica_grid',  
        '/components/devExpress/predefinidos/archivo/expedientes/grid_expediente/expediente_basica_grid.vue'
    );   

    await window.$ns['aplicacion'].asignaRuta(
        'pantalla_expediente',  
        '/components/devExpress/predefinidos/archivo/expedientes/pantalla_expediente/pantalla_expediente.vue'
    );   

    // await window.$ns['aplicacion'].asignaRuta(
    //     'expediente_transfiere_grid',  
    //     '/components/devExpress/predefinidos/archivo/expedientes/grid_transferencia/expediente_basica_grid.vue'
    // );   

    // await window.$ns['aplicacion'].asignaRuta(
    //     'expediente_disposicion_grid',  
    //     '/components/devExpress/predefinidos/archivo/expedientes/grid_disposicion/expediente_disposicion_grid.vue'
    // ); 

    // await window.$ns['aplicacion'].asignaRuta(
    //     'gestion_basica_grid',  
    //     '/components/devExpress/predefinidos/gestion/grid_gestion/gestion_basica_grid.vue'
    // ); 

    // await window.$ns['aplicacion'].asignaRuta(
    //     'gestion_pantalla',  
    //     '/components/devExpress/predefinidos/gestion/gestion_pantalla/gestion_pantalla.vue'
    // ); 


    // await window.$ns['aplicacion'].asignaRuta(
    //     'flujos_dinamicos_forma',  
    //     '/components/devExpress/predefinidos/configuracion/flujos/forma/flujos_dinamicos_forma.vue'
    // );

    // await window.$ns['aplicacion'].asignaRuta(
    //     'flujos_dinamicos_grid',  
    //     '/components/devExpress/predefinidos/configuracion/flujos/grid/flujos_dinamicos_grid.vue'
    // );
    
    // await window.$ns['aplicacion'].asignaRuta(
    //     'ventanilla_radicado_forma',  
    //     '/components/devExpress/predefinidos/radicados_vue/entrada/ventanilla_pinia/form/ventanilla_forma_radicado.vue'
    // );

    // await window.$ns['aplicacion'].asignaRuta(
    //     'ventanilla_radicado_grid',  
    //     '/components/devExpress/predefinidos/radicados_vue/entrada/ventanilla_pinia/grid/grid_ventanilla_radicado_grid.vue'
    // );

    // await window.$ns['aplicacion'].asignaRuta(
    //     'forma_radicado_consulta', 
    //     '/components/devExpress/predefinidos/radicados_vue/comunes/consulta/forma_radicado_consulta.vue'
    // ),

    // await window.$ns['aplicacion'].asignaRuta(
    //     'grid_pqrs_asigna_grid',  
    //     '/components/devExpress/predefinidos/radicados_vue/asignacion/pqrs/grid_pqrs_asigna_grid.vue'
    // );

    // await window.$ns['aplicacion'].asignaRuta(
    //     'forma_pqrs_asigna', 
    //     '/components/devExpress/predefinidos/radicados_vue/asignacion/pqrs/forma_pqrs_asigna.vue'
    // ),

    window.$ns['aplicacion'].crea_enrutador();
    await window.$ns['aplicacion'].asignaRuta('cajon', '/components/devExpress/cajon/cajon.vue');      
    window.$ns['aplicacion'].asignaComponente('cajon');
    
    setTimeout(() => {
        $router.push({
            //path: "trd_basica_grid"
            path: "expediente_basica_grid",
            //path: "pantalla_expediente",
            //path: "expediente_transfiere_grid"
            //path: "expediente_disposicion_grid"
            //path: "gestion_basica_grid"
            //path: "flujos_dinamicos_grid"
            //path: "ventanilla_radicado_grid",
            //path: "ventanilla_radicado_forma",            
            //path: "usuarios_grid"

            //path: "grid_pqrs_asigna_grid",
        })
    }, 1000);  
    */
}