<template src="./tvd_basica_plantilla.html">
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

import fuenteDatos from '../../../../../remoto/fuenteDatos.js'

// Columnas
import tvd_basica_columnas from './tvd_basica_columnas.js'
// Metodos
import tvd_basica_metodos from './tvd_basica_metodos.js'

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
    },

    methods: tvd_basica_metodos.metodos,
    
    mounted() {
        setTimeout(() => {
            //window.$tvd_grid = this.$refs.grid.instance
        }, 3000);
        this.notify = notify                          
    },

    data() {
        return {
            screen(width) {
                return (width < 700) ? 'sm' : 'lg';
            }, 

            columnas      : tvd_basica_columnas.columnas, // Columnas grid

            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'agn_tvd', 'agn_tvd', [], []),
            
            pageSizes     : [10, 25, 50, 100],
                        
            onContentReady: function(e) {}
        }
    }
}

export default grid

</script>