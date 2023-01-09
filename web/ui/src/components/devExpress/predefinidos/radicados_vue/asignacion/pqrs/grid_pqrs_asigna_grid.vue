<template src="./grid_pqrs_asigna_plantilla.html">
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
    DxExport,
} from 'devextreme-vue/data-grid';
 
import fuenteDatos from '../../../../remoto/fuenteDatos.js'

// Columnas
// Columnas
import ventanilla_radicado_columnas from '../../comunes/grid/grid_ventanilla_radicado_columnas.js'

// Metodos
import grid_pqrs_asigna_metodos from './grid_pqrs_asigna_metodos.js'

let basica = {
    "estructura": "radicados_entrada",
    "filtros_grid": [
        ["gestion_asignada_peticion", "=", "NO"],
        ["clase_radicado", "=", "PQRSD"]
    ],
    "titulo_grid": "PQRSD - Asignación y traslado de radicados"
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

    methods: grid_pqrs_asigna_metodos.metodos,
    
    mounted() {
        this.$refs.grid.instance.columnOption(
            "nro_radicado",
            {sortOrder: 'asc', sortIndex: 0} 
        );
    },

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