<template src="./envios_plantilla.html">
</template>

<script>
import {
    DxDataGrid,
    DxColumn,    
    DxSelection,
    DxEditing,
} from 'devextreme-vue/data-grid';
import { DxButton } from 'devextreme-vue/button';

import DxDropDownButton from 'devextreme-vue/drop-down-button'
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'
import notify from 'devextreme/ui/notify'

import DataSource from 'devextreme/data/data_source';
import ArrayStore from 'devextreme/data/array_store';

// Columnas
import envios_columnas from './envios_columnas.js'
// Metodos
import envios_metodos from './envios_metodos.js'

// Ventana emergente SALIDAS
import ventana_emergente_envios from '../ventana_emergente/ventana_emergente_envios.vue'

// Ventana emergente PLANILLA
import ventana_planilla from '../ventana_planilla/ventana_planilla.vue'


// Grid de envios
let grid =  {
    created() {
        locale("es")
    },

    components: {
        DxDataGrid,
        DxColumn,
        DxSelection,
        DxEditing,
        DxButton,
        
        // Responsive box
        DxResponsiveBox,
        DxLocation,
        DxCol,
        DxRow,
        DxItem,


        DataSource,
        ArrayStore,

        // Ventana emergente
        ventana_emergente_envios,
        ventana_planilla
    },

    methods: envios_metodos.metodos,
    
    mounted() {
        setTimeout(() => {
            window.$grid_envios = this
        }, 3000);
        this.notify = notify        
        
        this.enviar_accion("cargar", {}) 
    },

    data() {
        return {
            screen(width) {
                return (width < 700) ? 'sm' : 'lg';
            }, 

            columnas      : envios_columnas.columnas, // Columnas grid

            fuente_datos  : new DataSource({
                store: new ArrayStore({
                    data: [],
                    key : 'id'
                })
            }),

            // Ventana SALIDAS
            emergente_key: 0,
            opciones_ventana: {
                visible: false
            },

            // Ventana PLANILLA
            emergente_planilla_key: 0,
            opciones_planilla: {
                visible: false
            },
            
            selectedItemKeys: [],
            selectionChanged: (data)=>{
                this.selectedItemKeys = data.selectedRowKeys;
            },      
            
            urlCompleta: window.$direcciones.servidorDatos + '/envio_acciones'   
        }
    }
}

export default grid

</script>