<template src="./pantalla_trd.html">
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

import pantalla_trd_definiciones from "./pantalla_trd_definiciones.js"

import trd_arbol from "../trd_arbol/trd_arbol.vue"

let dependencia_trd =  {
    name: 'dependencia_trd',

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
        trd_arbol
    },

    props: {
        datos: ""
    },

    mounted() {
        this.indicador_visible = false
        this.forma             = this.$refs.forma.instance            
        this.barra             = this.$refs.barra.instance             
        this.notify            = notify  
        window.$pantalla_trd   = this  

        setTimeout(() => {
            this.arbol = this.$refs.componente_arbol
        }, 3000);

        // Datos trd
        this.parametros        = JSON.parse(this.datos)
        if (this.parametros.accion == "modificar") {
            this.forma.option("formData", parametros.trd_datos)
        }
        this.mostrar_botones()
    },

    methods: pantalla_trd_definiciones.metodos,

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
           
            opciones_estado: {
                items : ["ACTIVO", "INACTIVO"],
                layout: "horizontal"
            },
            
            // Barra de acciones
            barra_botones: pantalla_trd_definiciones.barra_botones(this)        
        }
    }
}

export default dependencia_trd;

</script>