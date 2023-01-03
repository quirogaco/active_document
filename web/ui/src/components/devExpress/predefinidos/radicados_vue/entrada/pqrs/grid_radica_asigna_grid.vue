<template src="./grid_radica_asigna_plantilla.html">
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
    DxFilterRow,
    DxExport
} from 'devextreme-vue/data-grid';

import DxDropDownButton from 'devextreme-vue/drop-down-button'
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../../remoto/fuenteDatos.js'

// Columnas
import ventanilla_radicado_columnas from '../../comunes/grid/grid_ventanilla_radicado_columnas.js'

// Metodos
import grid_radica_asigna_metodos from './grid_radica_asigna_metodos.js'

let basica = {
    "estructura"  : "radicados_entrada",
    "filtros_grid": [
        //["gestion_asignada_peticion", "=", "NO"],
        ["clase_radicado", "=", "PQRSD"]
    ],
    "titulo_grid" : "PQRSD - Radicación y traslado de radicados"
}

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
        DxExport
    },

    methods: grid_radica_asigna_metodos.metodos,
    
    mounted() {},

    data() {
        return {
            basica        : basica,
            columnas      : ventanilla_radicado_columnas.columnas, // Columnas grid
            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, basica.estructura, basica.estructura, basica.filtros_grid, {})
        }
    }
}

export default grid
</script>