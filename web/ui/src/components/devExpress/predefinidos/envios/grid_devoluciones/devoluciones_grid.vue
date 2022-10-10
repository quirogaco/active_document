<template src="./devoluciones_plantilla.html">
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
import devoluciones_columnas from './devoluciones_columnas.js'
// Metodos
import devoluciones_metodos from './devoluciones_metodos.js'

// Grid de devoluciones
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
        ArrayStore
    },

    props: {
        planilla_id: "",
    },


    methods: devoluciones_metodos.metodos,
    
    mounted() {
        setTimeout(() => {
            window.$grid_envios = this
        }, 3000);
        this.notify = notify        
        
        this.enviar_accion("cargar_envios", this.planilla_id) 
    },

    data() {
        return {
            screen(width) {
                return (width < 700) ? 'sm' : 'lg';
            }, 

            columnas      : devoluciones_columnas.columnas, // Columnas grid

            fuente_datos  : new DataSource({
                store: new ArrayStore({
                    data: [],
                    key : 'id'
                })
            }),

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