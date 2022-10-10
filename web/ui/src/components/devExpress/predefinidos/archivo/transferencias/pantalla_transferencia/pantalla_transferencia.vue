<template src="./pantalla_transferencia.html">
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

import fuenteDatos from '../../../../remoto/fuenteDatos.js'

import pantalla_transferencia_definiciones from "./pantalla_transferencia_definiciones.js"

import transferencia_items from "../transferencia_items/transferencia_items.vue"

let transferencia_trd =  {
    name: 'transferencia_trd',

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
        transferencia_items
    },

    props: {
        datos: ""
    },

    mounted() {
        this.indicador_visible = false
        this.forma             = this.$refs.forma.instance            
        this.barra             = this.$refs.barra.instance             
        this.notify            = notify  
        window.$pantalla_transferencia = this  

        setTimeout(() => {
            this.grid_transferencia_expedientes = this.$refs.transferencia_items_expedientes
        }, 3000);

        // Datos trd
        this.parametros        = JSON.parse(this.datos)
        if (this.parametros.accion == "modificar") {
            this.forma.option("formData", parametros.transferencia_datos)
            this.transferencia_items_visible = true
        }
        this.mostrar_botones()
    },

    methods: pantalla_transferencia_definiciones.metodos,

    data() {
        return {    
            // Datos de la forma
            parametros: {
            },

            // Indicador de tareas
            indicador_visible: false,

            // Ver expedientes archivos
            transferencia_items_visible: false,
            opciones_transferencia_items: {},

            // Opciones CAMPOS
            opciones_dependencia: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'dependencias', 'dependencias', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },
            
            opciones_fecha: {
                dateSerializationFormat: "yyyy-MM-dd",
                displayFormat          : "yyyy-MM-dd"
            },

            // Barra de acciones
            barra_botones: pantalla_transferencia_definiciones.barra_botones(this)        
        }
    }
}

export default transferencia_trd;

</script>