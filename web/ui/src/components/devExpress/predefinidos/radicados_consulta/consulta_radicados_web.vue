<template src="./consulta_radicados.html">
</template>

<script>
import { DxLoadPanel } from 'devextreme-vue/load-panel';
import { 
    DxForm,
    DxSimpleItem,
    DxGroupItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule,
    DxItem 
} from 'devextreme-vue/form'
import { DxScrollView }  from 'devextreme-vue/scroll-view'
import DxToolbar         from 'devextreme-vue/toolbar'
import DxButton          from 'devextreme-vue/button'
import notify            from 'devextreme/ui/notify'
import DxValidationGroup from 'devextreme-vue/validation-group'

import consulta_radicados_definiciones from "./consulta_radicados_definiciones.js"

let configura_radicacion =  {
    name: 'consulta_radicados',

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
        DxGroupItem,
        DxEmptyItem,
        DxButtonItem,
        DxLabel,

        // Validadores
        DxRequiredRule, 
        DxStringLengthRule, 
        DxValidationGroup
    },

    mounted() {
        this.indicador_visible = false
        this.forma             = this.$refs.forma.instance            
        this.barra             = this.$refs.barra.instance  
        this.notify            = notify          
    },

    methods: consulta_radicados_definiciones.metodos,

    data() {
        return {                
            grupo_datos_visible: false,
            campo_opciones: {
                readOnly : true
            },

            // Indicador de tareas
            indicador_visible: false,

            // Datos de la forma
            parametros: {},

            // Opciones CAMPOS
            opciones_estado: {},

            // Barra de acciones
            barra_botones: consulta_radicados_definiciones.barra_botones(this)        
        }
    }
}

export default configura_radicacion;
</script>