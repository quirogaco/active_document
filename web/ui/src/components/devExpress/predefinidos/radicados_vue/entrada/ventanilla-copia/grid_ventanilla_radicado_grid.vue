<template src="./grid_ventanilla_radicado_plantilla.html">
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
    DxToolbar
} from 'devextreme-vue/data-grid';

import DxDropDownButton from 'devextreme-vue/drop-down-button'
import { DxResponsiveBox, DxItem, DxLocation, DxCol, DxRow } from 'devextreme-vue/responsive-box'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'
import notify from 'devextreme/ui/notify'

import fuenteDatos from '../../../../remoto/fuenteDatos.js'

// Archivos
import ventana_emergente_archivo from '../../../comunes/archivos/ventana_emergente_archivo.vue'

// Recorridos
import ventana_emergente_recorrido from '../../../comunes/recorridos/ventana_emergente_recorrido.vue'

// Columnas
import ventanilla_radicado_columnas from '../../comunes/grid/grid_ventanilla_radicado_columnas.js'
// Metodos
import ventanilla_radicado_metodos from './grid_ventanilla_radicado_metodos.js'

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
        DxExport,
        DxToolbar,
        
        // Ventana carga de archivos
        ventana_emergente_archivo,

        // Ventana impresión de recorridos
        ventana_emergente_recorrido
    },

    methods: ventanilla_radicado_metodos.metodos,
    
    mounted() {
        this.grid = this.$refs.grid.instance;
        this.notify = notify;                          
    },

    data() {
        return {
            titulo: "Radicación ventanilla única",
            columnas      : ventanilla_radicado_columnas.columnas, // Columnas grid
            fuente_datos  : fuenteDatos.creaFuenteDatosConsulta('grid', null, 'radicados_entrada', 'radicados_entrada', [], []),            
            pageSizes           : [10, 25, 50, 100],
            displayMode         : 'full',
            showPageSizeSelector: true,
            showInfo            : true,
            showNavButtons      : true,

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

            //Ventana emergente recorrido
            opciones_ventana_emergente_recorrido: {
                visible  : false,
                datos    : {},
                atributos: {}
            },
            emergente_recorrido: 0,

            barra_elementos: [                   
                {name: "exportButton"},
                {name: "searchPanel"},
                {
                    widget  : "dxDropDownButton",
                    location: "after",
                    cssClass: "",
                    options : {
                        items      : [
                            { id: 1,  titulo: 'Imprimir sticker', icon: "fas fa-print" }
                        ],
                        displayExpr: 'titulo',
                        keyExpr    : 'id',
                        icon       : "fab fa-stack-exchange",  
                        stylingMode: 'contained',
                        keyExpr    : 'id',
                        text       : "Tareas especificas",    
                        onItemClick: this.accion_click,  
                        width      : 250,
                        stylingMode: 'filled',
                        type       : 'default'                                 
                    }                    
                }
            ],    
        }
    }
}

export default grid

</script>