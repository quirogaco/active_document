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

import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } 
from 'devextreme-vue/responsive-box'
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../../remoto/fuenteDatos.js'

// Notificar
import ventana_emergente_firma from 
'./ventana_emergente_gestion/ventana_emergente_gestion.vue'

// Anula
import ventana_emergente_anula from 
'./ventana_emergente_anula/ventana_emergente_anula.vue'
  

// Columnas
import grid_ventanilla_salida_columnas 
from '../../comunes/grid/grid_gestion_columnas.js'
// Metodos
import grid_ventanilla_salida_metodos 
from './grid_gestion_salida_metodos.js'

let filtros_grid = [ 
    ["dependencia_responde_id", "=", window.$usuario.dependencia_id],
    ["estado_gestion", "=", "PENDIENTE"], 
    ["estado_", "=", "ACTIVO"] 
]

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

        // Ventana notifica
        ventana_emergente_firma,

        // Ventana anula
        ventana_emergente_anula
    },

    methods: grid_ventanilla_salida_metodos.metodos,
    
    mounted() {
        this.grid = this.$refs.grid.instance;
        this.notify = notify;                       
    },

    data() {
        return {
            columnas: grid_ventanilla_salida_columnas.columnas,
            fuente_datos: fuenteDatos.creaFuenteDatosConsulta(
                'grid', 
                null, 
                'radicados_salida', 
                'radicados_salida', 
                filtros_grid, 
                {}
            ),            
            pageSizes: [10, 25, 50, 100],
            displayMode: 'full',
            showPageSizeSelector: true,
            showInfo: true,
            showNavButtons: true,

            // Ventanas emergentes
            opciones_ventana: {
                visible: false
            },
            emergente_key: 0,

            opciones_ventana_anula: {
                visible: false
            },            
            emergente_key_anula:0
        }
    }
}

export default grid

</script>