import { 
    onMounted,    
    onUpdated,
    onActivated,
    getCurrentInstance
} from 'vue'

import DxButton from 'devextreme-vue/button';
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar';
import {
    DxDataGrid,
} from 'devextreme-vue/data-grid'

import { DxLoadIndicator }   from 'devextreme-vue/load-indicator'

import grid_generador_metodos   from './grid_generador_metodos.js'
import grid_generador_plantilla from './grid_generador_plantilla.js'
import grid_generador_atributos from './grid_generador_atributos.js'
import grid_generador_eventos   from './grid_generador_eventos.js'

// Definición basica del GRID
const claseDefinicion = function(configuracion) {    
    // Información basica del GRID
    let nombreGrid     = window.$librerias.cargaAtributo(configuracion, 'nombreGrid', null)
    let componente_id  = configuracion.ruta + '_' + configuracion.id
    if (nombreGrid != null) componente_id = nombreGrid

    // #############################
    // Variable generales del grid #
    // #############################

    let eventos          = grid_generador_eventos.eventos_grid(configuracion)
    
    // ##################
    // Metodos del GRID #
    // ##################
    const metodosCompletos = grid_generador_metodos.metodos(configuracion)

    // ######################
    // Componentes del GRID #
    // ######################
    let componentes = {
        "DxButton"       : DxButton,
        "DxDataGrid"     : DxDataGrid,
        "DxToolbar"      : DxToolbar,
        "DxItem"         : DxItem,   
        "DxLoadIndicator": DxLoadIndicator,
    };
    
    // Atributos GRID
    let atributos = grid_generador_atributos.atributos_grid(configuracion, eventos)
    
    let unoMismo;
    // ################
    // Clase del GRID #
    // ################
    const clase = {
        componente_id: componente_id,
        components   : componentes,
        template     : grid_generador_plantilla.crea_plantilla(configuracion),
        setup(props, context) {    
            props; 
            context;       

            onMounted(() => {
                unoMismo = getCurrentInstance();
                unoMismo.ctx.gridInstancia = unoMismo.refs.referencia.$_instance;
                window.$ns[componente_id]   = unoMismo.ctx;                 
            }) 

            onActivated(() => {}) 

            onUpdated(() => {})

            return atributos          
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