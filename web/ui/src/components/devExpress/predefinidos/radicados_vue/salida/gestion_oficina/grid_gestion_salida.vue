<template src="./grid_gestion_salida_plantilla.html">
</template>

<script>
import { DxButton } from 'devextreme-vue/button'
import {
    DxDataGrid,
    DxColumn,
    DxPager,
    DxPaging,
    DxSearchPanel,
    DxSelection,
    DxFilterRow
} from 'devextreme-vue/data-grid';

import DxDropDownButton from 'devextreme-vue/drop-down-button'
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../../remoto/fuenteDatos.js'

// Firmado
import ventana_emergente_firma from './ventana_emergente_gestion/ventana_emergente_gestion.vue'

// Columnas
import grid_ventanilla_salida_columnas from '../../comunes/grid/grid_gestion_columnas.js'
// Metodos
import grid_ventanilla_salida_metodos from './grid_gestion_salida_metodos.js'

// Grid de gestión
let grid =  {
    components: {
        DxButton,
        DxDataGrid,
        DxColumn,
        DxPager,
        DxPaging,
        DxSearchPanel,
        DxSelection,
        DxFilterRow,
        
        // Responsive box
        DxResponsiveBox,
        DxLocation,
        DxCol,
        DxRow,
        DxItem,

        // Ventana firma
        ventana_emergente_firma
    },

    methods: grid_ventanilla_salida_metodos.metodos,
    
    mounted() {
        this.grid = this.$refs.grid.instance;
        this.notify = notify;                       
    },

    data() {
        return {
            columnas      : grid_ventanilla_salida_columnas.columnas, // Columnas grid
            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta(
                'grid', 
                null, 
                'radicados_salida', 
                'radicados_salida', 
                [], 
                []
            ),            
            pageSizes           : [10, 25, 50, 100],
            displayMode         : 'full',
            showPageSizeSelector: true,
            showInfo            : true,
            showNavButtons      : true,

            // Ventana PRESTAMO
            opciones_ventana: {
                visible: false
            },
            emergente_key: 0,
        }
    }
}

export default grid

</script>