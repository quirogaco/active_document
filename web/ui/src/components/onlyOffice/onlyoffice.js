
// Definición basica de la FORMA
const claseDefinicion = function(configuracion) {
    const componente_id = configuracion.ruta + '_' + configuracion.id;
    
    // ################################
    // Variable generales de la forma #
    // ################################

    // ###########
    // Plantilla #
    // ###########
    let _plantilla = `
    <div>   
        {{ titulo }}   
    </div>    
    `;

    // #############
    // Componentes #
    // #############
    /*
    import { DxPopup }           from 'devextreme-vue/popup';
    let componentes = {
        "DxPopup"        : DxPopup,
    };
    */

    // #########
    // Metodos #
    // #########
    let _metodos = {
        asignaAtributoDinamico(atributo, valor) {        
            this[atributo] = valor;      
            if (atributo == "formaDatos") {
                this.alCambiarDatos(this.formaComponente, valor)
            }
        }
    }

    // ###########
    // Atributos #
    // ###########
    let _atributos = {            
        // Referencias
        referencia           : ref(null),        
        referenciaToolbar    : ref(null),

    }

    // #######
    // Clase #
    // #######
    const clase = {
        //componente_id: componente_id,
        //components   : componentes_forma.componentes,
        template     : _plantilla,

        props: {
            titulo: String
        },

        setup(props, context) {    
            props; 
            context;       

            onMounted(() => {
                // Referencia a este componente
                este                      = getCurrentInstance().ctx;  
                este.este                 = este;  
                //window.$ns[componente_id] = este; 
     
            }) 

            return {}        
        },
        
        //methods: metodosCompletos

    };

    return clase
};

// Genera componente
const creaComponente = function(configuracion) {
    let clase       = claseDefinicion(configuracion);
    // Crea Componente
    //window._APLICACION_.component(clase.componente_id,  clase);
    window._APLICACION_.component("onlyOffice",  clase);
    // Recupera Componente
    //let componente = window._APLICACION_.component(clase.componente_id);
    
    return componente
};

export default {
    creaComponente  : creaComponente
}


    