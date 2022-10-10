<template src="./correos_plantilla.html">
</template>

<script>
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

import fuenteDatos from '../../remoto/fuenteDatos.js'

// Columnas
import correos_columnas from './correos_columnas.js'
// Metodos
import correos_metodos from './correos_metodos.js'
// Eventos de la fuente de datos
let eventos = {
    'cargar_datos_antes': function (opciones, idComponente) {
        return opciones;
    },
}
// Filtros de la fuente de datos
let filtros = ["estado", "=", "PENDIENTE"]

// Grid de gestión
let grid =  {
    components: {
        DxDataGrid,
        DxColumn,
        //DxLookup,
        DxPager,
        DxPaging,
        DxSearchPanel,
        DxSelection,
        DxFilterRow,
        
        // Acciones
        DxDropDownButton,

        // Responsive box
        DxResponsiveBox,
        DxLocation,
        DxCol,
        DxRow,
        DxItem
    },

    methods: correos_metodos.metodos,
    
    mounted() {
        window.$correo_datos = {}
        console.log("mounted this.$refs.grid.instance:", this.$refs.grid.instance)
        setTimeout(() => {
            window.$grid_correos = this.$refs.grid.instance
        }, 3000);
        this.notify = notify                  
    },

    unmounted() {
        //console.log("unmounted-0:", window.$grid_correos)
        //window.$grid_correos = undefined
        //console.log("unmounted-1:", window.$grid_correos)
    },

    data() {
        return {
            columnas      : correos_columnas.columnas, 
            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'correos_descargados', 'correos_descargados', filtros, eventos),
            pageSizes     : [10, 25, 50, 100],            
        }
    }
}

export default grid

</script>