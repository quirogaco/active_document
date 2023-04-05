<template src="./ventanilla_radicado_plantilla.html">
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

import fuenteDatos from '../../remoto/fuenteDatos.js'

import ventana_emergente_archivo from '../comunes/archivos/ventana_emergente_archivo.vue'

// Columnas
import ventanilla_radicado_columnas from './ventanilla_radicado_columnas.js'
// Metodos
import ventanilla_radicado_metodos from './ventanilla_radicado_metodos.js'

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

        // Ventana carga de archivos
        ventana_emergente_archivo
    },

    methods: ventanilla_radicado_metodos.metodos,
    
    mounted() {
        this.grid = this.$refs.grid.instance
        setTimeout(() => {
            //window.$trd_grid = this.$refs.grid.instance
        }, 3000);
        this.notify = notify                          
    },

    data() {
        return {
            columnas      : ventanilla_radicado_columnas.columnas, // Columnas grid
            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'radicados_entrada', 'radicados_entrada', [], []),            
            pageSizes     : [10, 25, 50, 100],

            //Ventana emergente archivos
            opciones_ventana_emergente_archivo: {
                visible : false,
                datos   : {},
                atributos: {
                    titulo_pantalla: "Cargar archivo",                   
                    titulo_boton   : "Salvar archivo",
                    mensaje_retorno: "Envio de archivo correcto!" 
                }
            },
            emergente_key: 0,
        }
    }
}

export default grid

</script>