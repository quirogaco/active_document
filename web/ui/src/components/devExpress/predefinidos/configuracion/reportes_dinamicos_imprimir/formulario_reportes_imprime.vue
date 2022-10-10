<template src="./formulario_reporte.html">
</template>

<script>
import DxToolbar, {DxItem} from 'devextreme-vue/toolbar'
import DxButton              from 'devextreme-vue/button'
import { DxScrollView }      from 'devextreme-vue/scroll-view'
import { DxSortable }        from 'devextreme-vue/sortable'
import DxSelectBox           from 'devextreme-vue/select-box'
import ArrayStore            from 'devextreme/data/array_store'
import DataSource            from 'devextreme/data/data_source'

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

import DxForm, {
    DxGroupItem,
    DxSimpleItem,
    DxButtonItem,
    DxEmptyItem,
    DxLabel,
    DxRequiredRule,
    DxCompareRule,
    DxRangeRule,
    DxStringLengthRule,
    DxPatternRule,
    DxEmailRule,
    DxAsyncRule
} from 'devextreme-vue/form'

import notify from 'devextreme/ui/notify'

import fuenteDatos  from '../../../remoto/fuenteDatos.js'

// Metodos
import reporte_diseno_metodos from "./formulario_metodos.js" 

export default {
    components: {
        DxSelectBox,

        DxToolbar,
        DxItem,
        DxButton,
        DxScrollView,
        DxSortable,

        DxDataGrid,
        DxColumn,
        DxPager,
        DxPaging,
        DxSearchPanel,
        DxSelection,
        DxFilterRow,
        DxExport,

        // Forma
        DxForm,
        DxGroupItem,
        DxSimpleItem,
        DxButtonItem,
        DxEmptyItem,
        DxLabel,
        DxRequiredRule,
        DxCompareRule,
        DxRangeRule,
        DxStringLengthRule,
        DxPatternRule,
        DxEmailRule,
        DxAsyncRule,

        // Atributos de los campos
        //atributos_campos
    },

    props: {
        datos: ""
    },

    mounted() {
        this.forma          = this.$refs.forma.instance
        this.barra          = this.$refs.barra.instance         
        this.grid_reporte   = this.$refs.grid_reporte.instance         
        
        this.notify             = notify  
        
        // Datos reporte
        this.parametros    = JSON.parse(this.datos)
        this.datos_forma   = {}
        let fuente         = this.parametros.datos.diseno.diseno.fuente 
        this.datos_forma = {
            "id"     : this.parametros.datos.id,
            "codigo" : this.parametros.datos.codigo,
            "nombre" : this.parametros.datos.nombre,
            "fuentes": fuente
        }
        window.$mostrar_esperar("Por favor espere..")
        setTimeout(() => {
            this.columnas_reporte = this.parametros.datos.diseno.diseno.columnas
            this.cambia_grid()
            this.fuente_datos_grid = fuenteDatos.creaFuenteDatosConsulta('grid', null, fuente, fuente, [], [])
            window.$ocultar_esperar()  
        }, 3000);            
        this.mostrar_botones()                
    },

    data() {
        return {
            // Prametros del reporte
            parametros : {},
            datos_forma: {},

            // Opciones CODIGO
            opciones_codigo: {
                readOnly: true,
                label: {
                    text    : "Codigo",
                    location: "top"
                }
            },

            // Opciones NOMBRE
            opciones_nombre: {
                readOnly: true,
                label: {
                    text    : "Nombre",
                    location: "top"
                }
            },

            // Opciones FUENTE
            opciones_fuente: {
                readOnly: true,
                label: {
                    text    : "Fuente",
                    location: "top"
                }
            },

            // Lista de campos reporte
            columnas_reporte:[],
            reporte_atributos: {
                id: 'reporte'
            },
                                    
            // Barra de acciones            
            barra_botones: reporte_diseno_metodos.barra_botones(this),   

            // Columnas grid reporte
            ver_grid         : false,
            columnas_grid    : [], 
            fuente_datos_grid: [],            
        }
    },

    methods: reporte_diseno_metodos.metodos
}
</script>

<style>
</style>