<template src="./prestamo_basica_plantilla.html">
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
import espanol from "devextreme/localization/messages/es.json"

import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../../remoto/fuenteDatos.js'

// Prestamo
import ventana_emergente_prestamo from './ventana_emergente_prestamo/ventana_emergente_prestamo.vue'

// Columnas
import prestamo_basica_columnas from './prestamo_basica_columnas.js'
// Metodos
import prestamo_basica_metodos from './prestamo_basica_metodos.js'

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

        ventana_emergente_prestamo
    },

    methods: prestamo_basica_metodos.metodos,
    
    mounted() {        
        this.notify = notify      
        this.grid   = this.$refs.grid.instance          
    },

    data() {
        return {
            screen(width) {
                return (width < 700) ? 'sm' : 'lg';
            }, 

            columnas      : prestamo_basica_columnas.columnas, // Columnas grid

            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'agn_prestamos_trd', 'agn_prestamos_trd', [], []),
            
            pageSizes     : [10, 25, 50, 100],
                        
            onContentReady: function(e) {},

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