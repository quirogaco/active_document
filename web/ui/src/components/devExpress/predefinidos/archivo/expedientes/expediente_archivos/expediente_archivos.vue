<template src="./expediente_archivos.html">
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
    DxFilterRow,
    DxEditing,
} from 'devextreme-vue/data-grid';
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } 
from 'devextreme-vue/responsive-box'

import DxButtonGroup from 'devextreme-vue/button-group'
import DxToolbar     from 'devextreme-vue/toolbar'
import { DxFileUploader } from 'devextreme-vue/file-uploader'

import fuenteDatos  
from '../../../../../../components/devExpress/remoto/fuenteDatos.js'

// Columnas
import expediente_archivos_columnas from './expediente_archivos_columnas.js'
import metodos from './expediente_archivos_metodos.js'
import archivo_expediente 
from './componentes_expediente/archivo_expediente.vue'

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
        DxEditing,

        // Responsive box
        DxResponsiveBox,
        DxLocation,
        DxCol,
        DxRow,
        DxItem,

        DxFileUploader,

        archivo_expediente
    },

    props: {
        // Pasan object cuando es componente embebido en otro
        parametros: [Object, String],
    },

    data() {
        return {             
            // Ventana formas DOCUMENTOS POR EXPEDIENTE
            opciones_ventana: {
                visible: false,
                datos: {}
            },
            emergente_key: 0,
            columnas: expediente_archivos_columnas.columnas, 
            fuente_datos: [],
            pageSizes: [10, 25, 50, 100],
            
            // Editable grilla
            opciones_grilla: {
                editable: false,
                borrable: false
            }
        }
    },

    mounted() {
        window.$grid_archivos_expediente = this.$refs.grid_archivos.instance
        this.grid_archivos = this.$refs.grid_archivos.instance
        window.$expediente_archivos = this
        //console.log("EXPEDIENTE MONTADO --> ARCHIVOS:", this.parametros)    
        this.notify = notify        
        let filtros = []
        if (this.parametros.padre == "EXPEDIENTE") {
            filtros = [ ["expediente_id", "=", this.parametros.padre_id] ]
            this.opciones_grilla.editable = true
            this.opciones_grilla.borrable = true
            this.columnas[4].editable     = true
        }
        else {
            filtros = [ ["carpeta_id", "=", this.parametros.padre_id] ]
            this.opciones_grilla.editable = false
            this.opciones_grilla.borrable = false
            this.columnas[4].editable     = false
        }

        let eventos = {
            "cargar_datos_despues": function (resultado, idComponente) {
                let total = 1;
                let nuevosDatos = resultado.data.map(function(dato) {
                    dato['consecutivo'] = total;
                    total  += 1;
                    return dato
                });
                resultado.data = nuevosDatos;

                return resultado
            }
        }

        this.fuente_datos = fuenteDatos.creaFuenteDatosConsulta(
            'grid', 
            null, 
            'agn_documentos_trd', 
            'agn_documentos_trd', 
            filtros, 
            eventos
        )        
    },

    methods: metodos
}
</script>

<style>

</style>