<template src="./tvd_expediente_archivos.html">
</template>

<script>
import { DxButton } from 'devextreme-vue/button'
import notify from 'devextreme/ui/notify'
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

import DxButtonGroup from 'devextreme-vue/button-group'
import DxToolbar     from 'devextreme-vue/toolbar'
import { DxFileUploader } from 'devextreme-vue/file-uploader';

import fuenteDatos  from '../../../../../../components/devExpress/remoto/fuenteDatos.js';

// Columnas
import tvd_expediente_archivos_columnas from './tvd_expediente_archivos_columnas.js'
import tvd_metodos                      from './tvd_expediente_archivos_metodos.js'

import tvd_ventana_emergente_expediente from './tvd_ventana_emergente_expediente/tvd_ventana_emergente_expediente.vue'

export default {
    components: {
        DxButton,
        DxButtonGroup,
        DxToolbar,

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

        DxFileUploader,

        tvd_ventana_emergente_expediente
    },

    props: {
        datos: ""
    },

    data() {
        return {
            screen(width) {
                return (width < 700) ? 'sm' : 'lg';
            }, 
            // Ventana formas DOCUMENTOS POR EXPEDIENTE
            opciones_ventana: {
                visible: false
            },
            emergente_key: 0,
            columnas      : tvd_expediente_archivos_columnas.columnas, 
            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'agn_documentos_tvd', 'agn_documentos_tvd', [], []),
            pageSizes     : [10, 25, 50, 100],
        }
    },

    mounted() {
        setTimeout(() => {
            window.$tvd_grid_archivos_expediente = this.$refs.grid_archivos.instance  
        }, 2000);        
        this.notify = notify        
    },

    methods: tvd_metodos
}
</script>

<style>

</style>