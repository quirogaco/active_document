<template src="./planilla_plantilla.html">
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

import fuenteDatos from '../../../remoto/fuenteDatos.js'

// Columnas
import planilla_columnas from './planilla_columnas.js'
// Metodos
import planilla_metodos from './planilla_metodos.js'

// Grid de planilla
let grid =  {
    created() {
        locale("es")
    },

    components: {
        DxDataGrid,
        DxColumn,
        DxSelection,
        DxButton
    },
    
    methods: planilla_metodos.metodos,
    
    mounted() {
        setTimeout(() => {
            window.$grid_planilla = this
        }, 3000);
        this.notify = notify        
    },

    data() {
        return {
            screen(width) {
                return (width < 700) ? 'sm' : 'lg';
            }, 

            columnas      : planilla_columnas.columnas, // Columnas grid

            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'planilla', 'planilla_envios_fisicos', [], []),

            selectedItemKeys: [],
            selectionChanged: (data)=>{
                this.selectedItemKeys = data.selectedRowKeys                
            },      
        }
    }
}

export default grid

</script>