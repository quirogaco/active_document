<template src="./formulario_reporte.html">
</template>

<script>
import DxToolbar, {DxItem} from 'devextreme-vue/toolbar'
import DxButton from 'devextreme-vue/button'
import { DxScrollView } from 'devextreme-vue/scroll-view'
import { DxSortable } from 'devextreme-vue/sortable'
import DxSelectBox from 'devextreme-vue/select-box'
import ArrayStore from 'devextreme/data/array_store'
import DataSource from 'devextreme/data/data_source'

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

import forma_general from "../../comunes_vue/forma/forma.js";

import atributos_campos from './formulario_campos.vue'

// Metodos
import reporte_diseno_metodos from "./formulario_metodos.js" 

const nueva_fuente_datos = function(datos=[]) {
    const tienda = new ArrayStore({
        key: 'id',
        data: datos
    })

    return new DataSource({
        store: tienda
    })
}

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
        atributos_campos
    },

    props: {
        datos: ""
    },

    mounted() {
        this.forma          = this.$refs.forma.instance
        this.barra          = this.$refs.barra.instance         
        this.fuentes_select = this.forma.getEditor("fuentes")  
        this.grid_reporte   = this.$refs.grid_reporte.instance         
        
        this.nueva_fuente_datos = nueva_fuente_datos;       
        this.notify = notify;  
        this.leer_fuentes("leer_fuentes", {});
        window.$_disenador = this;
        
        // Datos reporte
        let datos = forma_general.lee_propiedades(
            this.$props, 
            "formulario_reportes_dinamicos"
        );
        this.parametros = datos.datos;
        this.datos_form = {};
        if (this.parametros.modo == "modificar") {
            this.datos_forma = {
                "id"     : this.parametros.reporte.id,
                "codigo" : this.parametros.reporte.codigo,
                "nombre" : this.parametros.reporte.nombre,
                "fuentes": this.parametros.reporte.diseno.diseno.fuente
            }
            setTimeout(() => {
                this.columnas_reporte = 
                    this.parametros.reporte.diseno.diseno.columnas;
                this.cambia_grid();
            }, 3000);            
        }
        this.mostrar_botones()                
    },

    data() {
        return {
            pageSizes: [10, 25, 50, 100],
            displayMode: 'full',
            showPageSizeSelector: true,
            showInfo: true,
            showNavButtons: true,

            // Prametros del reporte
            parametros: {},
            datos_forma: {},

            // Opciones CODIGO
            opciones_codigo: {
                label: {
                    text: "Codigo",
                    location: "top"
                }
            },

            // Opciones NOMBRE
            opciones_nombre: {
                label: {
                    text: "Nombre",
                    location: "top"
                }
            },

            // Opciones FUENTE
            opciones_fuente: {
                dataSource: nueva_fuente_datos([]),
                displayValue: "nombre",
                displayExpr: "nombre",
                searchExpr: "nombre",
                searchEnabled: true,
                valueExpr: "id",                
                label: {
                    text: "Fuente de datos",
                    location: "top"
                },
                onSelectionChanged: this.cambia_fuente,
            },

            // Lista de datos de campos
            lista_campos:[],
            disenador_atributos: {
                id: 'disenador'
            },

            // Lista de campos reporte
            columnas_reporte:[],
            reporte_atributos: {
                id: 'reporte'
            },
                              
            // Parametros para editor de atributos
            contador_campos: 0,
            emergente_key: 0,
            opciones_atributo: {
                visible: false,
                datos: {}
            },

            // Barra de acciones            
            barra_botones: reporte_diseno_metodos.barra_botones(this),   

            // Manejo de prevista
            prevista_grid: true,
            // Columnas grid reporte
            ver_grid: false,
            columnas_grid: [], 
            fuente_datos_grid: [],            
        }
    },

    methods: reporte_diseno_metodos.metodos
}
</script>

<style>
.lista {
    border-radius: 8px;
    margin: 5px;
    background-color: rgba(192, 192, 192, 0.4);
    vertical-align: top;
    white-space: normal;
    padding: 10px 10px 10px;
}

.lista-titulo {
    font-size: 20px;
    padding-left: 30px;
    margin-bottom: 10px;
    font-weight: bold;
    cursor: pointer;
    color: white;
    background-color: black;
}

.titulo-atributo {
    font-size: 15x;
    padding-left: 30px;
    margin-bottom: 10px;
    font-weight: bold;
    cursor: pointer;
    color: white;
    background-color: black;
}

.campo-fuente {
    font-size: 17px;
    padding-left: 30px;
    margin-bottom: 10px;
    font-weight: bold;
    cursor: pointer;
    color: black;
    background-color: white;
    border-radius: 4px;
}

.scrollable-componente {
    height: 200px
}

.card-componente {
    position: relative;
    background-color: white;
    box-sizing: border-box;
    width: 300px;
    padding: 10px 20px;
    margin: 10px;
    cursor: pointer;
}

.ordenable-forma {
    height: 1000px
}
</style>