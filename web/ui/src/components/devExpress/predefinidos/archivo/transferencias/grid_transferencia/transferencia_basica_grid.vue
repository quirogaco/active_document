<template src="./transferencia_basica_plantilla.html">
</template>

<script>
import { DxButton } from 'devextreme-vue/button'
import { DxLoadPanel } from 'devextreme-vue/load-panel'
import {
    DxDataGrid,
    DxColumn,
    DxPager,
    DxPaging,
    DxSearchPanel,
    DxSelection,
    DxEditing,
    DxFilterRow
} from 'devextreme-vue/data-grid';

import DxDropDownButton from 'devextreme-vue/drop-down-button'
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box'
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../../remoto/fuenteDatos.js'
// Columnas
import transferencia_basica_columnas from './transferencia_basica_columnas.js'
// Metodos
import transferencia_basica_metodos from './transferencia_basica_metodos.js'

import ventana_emergente_accesos from './ventana_emergente_accesos/ventana_emergente_accesos.vue'

// Grid 
let grid =  {
    components: {
        DxLoadPanel,
        DxButton,
        DxDataGrid,
        DxColumn,
        DxPager,
        DxPaging,
        DxSearchPanel,
        DxSelection,
        DxFilterRow,
        DxEditing,
        
        // Responsive box
        DxResponsiveBox,
        DxLocation,
        DxCol,
        DxRow,
        DxItem,

        ventana_emergente_accesos
    },

    methods: transferencia_basica_metodos.metodos,
    
    mounted() {        
        this.notify = notify    
        this.grid   = this.$refs.grid.instance                        
    },

    data() {
        return {
            screen(width) {
                return (width < 700) ? 'sm' : 'lg';
            }, 

            columnas      : transferencia_basica_columnas.columnas, // Columnas grid

            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'agn_transferencias_trd', 'agn_transferencias_trd', [], []),
            
            pageSizes     : [10, 25, 50, 100],
                        
            onContentReady: function(e) {},

            // Ventana formas TRD
            opciones_ventana: {
                visible: false
            },
            emergente_key: 0,

            // Indicador de tareas
            indicador_visible: false
        }
    }
}

export default grid

</script>