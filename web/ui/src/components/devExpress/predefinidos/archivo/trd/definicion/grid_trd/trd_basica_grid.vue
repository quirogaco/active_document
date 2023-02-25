<template src="./trd_basica_plantilla.html">
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

import DxDropDownButton from 'devextreme-vue/drop-down-button';
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } 
from 'devextreme-vue/responsive-box';
import { locale, loadMessages, formatMessage } 
from 'devextreme/localization';
import notify from 'devextreme/ui/notify';

import fuenteDatos from '../../../../../remoto/fuenteDatos.js';

// Columnas
import trd_basica_columnas from './trd_basica_columnas.js';
// Metodos
import trd_basica_metodos from './trd_basica_metodos.js';
// Ventana emergente de TRD
import ventana_emergente_trd 
from './ventana_emergente_trd/ventana_emergente_trd.vue'

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

        ventana_emergente_trd
    },

    methods: trd_basica_metodos.metodos,
    
    mounted() {
        setTimeout(() => {
            window.$trd_grid = this.$refs.grid.instance
        }, 2000);
        this.notify = notify                           
    },

    data() {
        return {
            // Ventana formas TRD
            opciones_ventana: {
                visible: false,
                attributes_str: $lib.json_texto({
                    mode: "crear", 
                    "importar": true
                })
            },
            emergente_key: 0,
            titulo: "Manejo de tablas de retención",
            columnas: trd_basica_columnas.columnas, // Columnas grid
            fuente_datos: fuenteDatos.creaFuenteDatosConsulta(
                'grid', 
                null, 
                'agn_trd', 
                'agn_trd', 
                [], 
                []
            ),            
            pageSizes: [10, 25, 50, 100],                        
            onContentReady: function(e) {}
        }
    }
}

export default grid

</script>