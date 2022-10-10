import { 
    onMounted,    
    onUnmounted, 
    getCurrentInstance,
} from 'vue'

import notify              from 'devextreme/ui/notify'

import metodos_forma     from './metodos_forma.js';
import plantilla_forma   from './plantilla_forma.js';
import atributos_forma   from './atributos_forma.js';
import componentes_forma from './componentes_forma.js';

// Definición basica de la FORMA
const claseDefinicion = function(configuracion) {
    // Información basica de la FORMA
    let nombre_forma  = window.$librerias.cargaAtributo(configuracion, 'nombre_forma', null);   
    let componente_id = configuracion.ruta + '_' + configuracion.id;
    if (nombre_forma != null) componente_id = nombre_forma; 
    
    // ################################
    // Variable generales de la forma #
    // ################################
    // Atributos especificos JCR !!
    let metodosParametros = window.$librerias.cargaAtributo(configuracion, 'metodos', {}); 

    // Objeto que contiene el componente FORMA
    let este, formaComponente, formaInstancia, toolbarComponente;
    
    // Metodos
    const metodosCompletos = Object.assign(metodos_forma.metodos, metodosParametros);

    // Publica atributos
    window.$definiciones[componente_id] = configuracion;

    // Publica repositorio de componentes no developer express o creados por template para esta forma
    window.$componentesNDET[componente_id] = {}

    // ###################
    // Clase de la FORMA #
    // ###################
    const clase = {
        componente_id: componente_id,
        components   : componentes_forma.componentes,
        template     : plantilla_forma.crea_plantilla(configuracion),

        setup(props, context) {    
            
            onMounted(() => {
                // Referencia a este componente
                este                      = getCurrentInstance().ctx;  
                este.este                 = este;  
                // Componente de la forma                           
                formaComponente           = este.$refs.referencia;
                // Instancia de la forma
                formaInstancia            = formaComponente.$_instance;
                // Toolbar de la forma
                toolbarComponente         = este.$refs.referenciaToolbar;
                // Valores de uno mismo
                este.formaComponente      = formaComponente;  
                este.formaInstancia       = formaInstancia;  
                este.toolbarComponente    = toolbarComponente;  
                window.$ns[componente_id] = este; 

                // Notificaciones
                este.notify               = notify;

                // LLama evento al montar 
                let evento = este.eventos["montado"];
                if (evento != undefined) {
                    evento(este)
                }
            })

            onUnmounted(() => {                
                // LLama evento al montar 
                let evento = este.eventos["desmontado"];
                if (evento != undefined) {
                    evento()
                }
            })

            return  atributos_forma.creaAtributos(componente_id, configuracion) //, {este: este})          
        },
        
        methods: metodosCompletos

    };

    return clase
};

// Genera componente
const creaComponente = function(configuracion) {
    let clase       = claseDefinicion(configuracion);
    window._APLICACION_.component(clase.componente_id,  clase);    
    window.$clases[clase.componente_id] = clase;
    let componente = window._APLICACION_.component(clase.componente_id);
    
    return componente
};

export default {
    creaComponente  : creaComponente,
    claseDefinicion : claseDefinicion
}