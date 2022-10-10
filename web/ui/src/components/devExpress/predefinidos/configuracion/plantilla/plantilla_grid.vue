<template src="./plantilla_plantilla.html">
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

import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../remoto/fuenteDatos.js'

// Columnas
import plantilla_columnas from './plantilla_columnas.js'
// Metodos
import plantilla_metodos from './plantilla_metodos.js'

// Grid de plantilla
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
    },

    methods: plantilla_metodos.metodos,
    
    mounted() {
        setTimeout(() => {
            //window.$trd_grid = this.$refs.grid.instance
        }, 3000);
        this.notify = notify                          
    },

    data() {
        return {
            screen(width) {
                return (width < 700) ? 'sm' : 'lg';
            }, 

            columnas      : plantilla_columnas.columnas, // Columnas grid

            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'plantillas', 'plantillas', [], []),
            
            pageSizes     : [10, 25, 50, 100],
                        
            onContentReady: function(e) {}
        }
    }
}

export default grid

</script>