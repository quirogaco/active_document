<template src="./pantalla_expediente.html">
</template>

<script>
import { DxLoadPanel } from 'devextreme-vue/load-panel'
import { 
    DxForm,
    DxGroupItem,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule
} from 'devextreme-vue/form'
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import DxButton              from 'devextreme-vue/button'
import notify                from 'devextreme/ui/notify'
import DxValidationGroup     from 'devextreme-vue/validation-group'

import fuenteDatos from '../../../../remoto/fuenteDatos.js'

import pantalla_expediente_definiciones from "./pantalla_expediente_definiciones.js"

import expediente_archivos from "../expediente_archivos/expediente_archivos.vue"

let expediente_pantalla =  {
    name: 'expediente_pantalla',

    components: {
        // Tarea en ejecución
        DxLoadPanel,

        // Barra       
        DxItem,
        DxButton,        
        DxToolbar,

        // Forma
        DxForm,
        DxGroupItem,
        DxSimpleItem,
        DxEmptyItem,
        DxButtonItem,
        DxLabel,

        // Validadores
        DxRequiredRule, 
        DxStringLengthRule, 
        DxValidationGroup,
        
        // Arbol de definición
        expediente_archivos
    },

    props: {
        parametros_texto: ""
    },

    mounted() {
        this.indicador_visible = false
        this.forma             = this.$refs.forma.instance            
        this.barra             = this.$refs.barra.instance             
        this.notify            = notify  
        window.$pantalla_expediente = this  

        // Datos expediente
        this.parametros             = JSON.parse(this.parametros_texto)
        this.parametros.padre       = "EXPEDIENTE"
        this.parametros.padre_id    = this.parametros.expediente_id
        this.parametros.padre_datos = this.parametros.expediente_datos  
        this.expediente_archivos_parametros = this.parametros
        if (this.parametros.accion == "modificar") {
            this.forma.option("formData", this.parametros.expediente_datos)
        }

        // Botones de la forma
        this.mostrar_botones()
    },

    methods: pantalla_expediente_definiciones.metodos,

    data() {
        return {    
            // Datos de la forma
            parametros: {
                expediente_datos: {}
            },

            titulo: "Expediente",

            // Indicador de tareas
            indicador_visible: false,

            // Ver pantalla archivos
            expediente_archivos_visible: false,
            opciones_expediente_archivos: {},

            // Opciones CAMPOS
            opciones_lectura: {
                readOnly: true
            },

            opciones_serie: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'agn_serie_trd', 'agn_serie_trd', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },

            opciones_serie: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'agn_serie_trd', 'agn_serie_trd', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },

            opciones_subserie: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'agn_subserie_trd', 'agn_subserie_trd', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },

            opciones_id: {
                visible: false
            },

            // Barra de acciones
            barra_botones: pantalla_expediente_definiciones.barra_botones(this)        
        }
    }
}

export default expediente_pantalla;
</script>