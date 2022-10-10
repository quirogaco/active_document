<template src="./destinatarios_plantilla.html">
</template>

<script>
import {
    DxDataGrid,
    DxColumn,    
    DxSelection,
    DxEditing
} from 'devextreme-vue/data-grid'
import { DxButton } from 'devextreme-vue/button'
import DxDropDownButton from 'devextreme-vue/drop-down-button'
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box'
import notify from 'devextreme/ui/notify'

import DataSource from 'devextreme/data/data_source';
import ArrayStore from 'devextreme/data/array_store';

// Ventana emergente DESTINATARIOS
import ventana_emergente_destinatarios from '../ventana_emergente_destinatarios/ventana_emergente_destinatarios.vue'

// Columnas
import destinatarios_columnas from './destinatarios_columnas.js'
// Metodos
import destinatarios_metodos  from './destinatarios_metodos.js'

// Grid 
let grid =  {
    components: {
        DxDataGrid,
        DxColumn,
        DxSelection,
        DxEditing,
        DxButton,

        ventana_emergente_destinatarios,
    },
    
    methods: destinatarios_metodos.metodos,
    
    mounted() {  
        setTimeout(() => {
            window.$grid_destinatarios = this
        }, 3000);      
        this.notify = notify        
    },

    data() {
        return {
            columnas      : destinatarios_columnas.columnas,

            fuente_datos  : new DataSource({
                store: new ArrayStore({
                    data: [],
                    key : 'id'
                })
            }),

            // Ventana DESTINATARIOS
            emergente_key: 0,
            opciones_ventana: {
                visible: false
            }  
        }
    }
}

export default grid

</script>