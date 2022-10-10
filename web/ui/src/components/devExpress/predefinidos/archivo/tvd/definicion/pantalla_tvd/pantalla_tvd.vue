<template src="./pantalla_tvd.html">
</template>

<script>
import { DxLoadPanel } from 'devextreme-vue/load-panel';
import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule
} from 'devextreme-vue/form';
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import DxButton              from 'devextreme-vue/button'
import notify                from 'devextreme/ui/notify'
import DxValidationGroup     from 'devextreme-vue/validation-group'

import fuenteDatos from '../../../../../remoto/fuenteDatos.js'

import pantalla_tvd_definiciones from "./pantalla_tvd_definiciones.js"

import tvd_arbol from "../tvd_arbol/tvd_arbol.vue"

let dependencia_tvd =  {
    name: 'dependencia_tvd',

    components: {
        // Tarea en ejecución
        DxLoadPanel,

        // Barra       
        DxItem,
        DxButton,        
        DxToolbar,

        // Forma
        DxForm,
        DxSimpleItem,
        DxEmptyItem,
        DxButtonItem,
        DxLabel,

        // Validadores
        DxRequiredRule, 
        DxStringLengthRule, 
        DxValidationGroup,
        
        // Arbol de definición
        tvd_arbol
    },

    props: {
        datos: ""
    },

    mounted() {
        this.indicador_visible = false
        this.forma             = this.$refs.forma.instance            
        this.barra             = this.$refs.barra.instance             
        this.notify            = notify  
        window.$pantalla_tvd   = this

        setTimeout(() => {
            this.arbol = this.$refs.componente_arbol
        }, 3000);

        // Datos tvd
        this.parametros        = JSON.parse(this.datos)
        if (this.parametros.accion == "modificar") {
            this.forma.option("formData", parametros.tvd_datos)
        }
        this.mostrar_botones()
    },

    methods: pantalla_tvd_definiciones.metodos,

    data() {
        return {    
            // Datos de la forma
            parametros: {
            },

            // Indicador de tareas
            indicador_visible: false,

            // Ver pantalla de dependencias, serie, subserie, etc
            arbol_visible: false,
            opciones_arbol: {},

            // Opciones CAMPOS
            opciones_fondo: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'agn_fondo_documental', 'agn_fondo_documental', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },

            opciones_fecha: {
                dateSerializationFormat: "yyyy-MM-dd",
                displayFormat          : "yyyy-MM-dd"
            },
    
            opciones_id: {
                visible: false
            },

            opciones_estado: {
                items : ["ACTIVO", "INACTIVO"],
                layout: "horizontal"
            },
            
            // Barra de acciones
            barra_botones: pantalla_tvd_definiciones.barra_botones(this)        
        }
    }
}

export default dependencia_tvd;

</script>