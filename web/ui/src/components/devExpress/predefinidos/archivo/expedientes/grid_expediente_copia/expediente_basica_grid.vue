<template src="./expediente_basica_plantilla.html">
</template>

<script>
import { DxLoadPanel } from 'devextreme-vue/load-panel'
import { DxButton } from 'devextreme-vue/button'
import {
    DxDataGrid,
    DxColumn,
    DxPager,
    DxPaging,
    DxSearchPanel,
    DxSelection,
    DxFilterRow,
    DxEditing,
    DxExport,
} from 'devextreme-vue/data-grid';

import DxDropDownButton from 'devextreme-vue/drop-down-button'
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box'
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../../remoto/fuenteDatos.js'
// Columnas
import expediente_basica_columnas from './expediente_basica_columnas.js'
// Metodos
import expediente_basica_metodos from './expediente_basica_metodos.js'
// Accesos permisos
import ventana_emergente_accesos from './ventana_emergente_accesos/ventana_emergente_accesos.vue'

const filtros = ["tabla", "=", "TRD"]

// Grid de gestión
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
        DxExport,
        
        // Responsive box
        DxResponsiveBox,
        DxLocation,
        DxCol,
        DxRow,
        DxItem,

        ventana_emergente_accesos
    },

    methods: expediente_basica_metodos.metodos,
    
    mounted() {        
        this.notify = notify    
        this.grid   = this.$refs.grid.instance                        
    },

    data() {
        return {
            columnas      : expediente_basica_columnas.columnas,

            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'agn_expedientes_trd', 'agn_expedientes_trd', filtros, {}),
            
            pageSizes     : [10, 25, 50, 100],

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