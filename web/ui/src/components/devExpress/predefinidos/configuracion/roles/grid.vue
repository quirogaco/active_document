<template src="./pantalla_grid.html">
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
import grid_columnas from './grid_columnas.js'
// Metodos
import grid_metodos from './grid_metodos.js'

let fuente_general = "roles"

// Grid de roles
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
        DxResponsiveBox
    },

    methods: grid_metodos.metodos,
    
    mounted() {
        this.notify = notify                          
    },

    data() {
        return {
            columnas      : grid_columnas.columnas, // Columnas grid
            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, fuente_general, fuente_general, [], []),            
            pageSizes     : [10, 25, 50, 100],                        
        }
    }
}

export default grid

</script>