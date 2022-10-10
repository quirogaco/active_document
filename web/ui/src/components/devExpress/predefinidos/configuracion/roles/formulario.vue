<template src="./pantalla_formulario.html">
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
    DxStringLengthRule,
    DxItem 
} from 'devextreme-vue/form'
import DxToolbar         from 'devextreme-vue/toolbar'
import DxButton          from 'devextreme-vue/button'
import notify            from 'devextreme/ui/notify'
import DxValidationGroup from 'devextreme-vue/validation-group'
import ArrayStore        from 'devextreme/data/array_store'
import DataSource        from 'devextreme/data/data_source'

import fuenteDatos           from '../../../remoto/fuenteDatos.js'
import pantalla_definiciones from "./pantalla_definiciones.js"

let forma_id = 'roles_forma'

let forma =  {
    name: forma_id,

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
        DxValidationGroup
    },

    props: {
        datos: ""   
    },

    mounted() {
        this.indicador_visible = false
        this.forma             = this.$refs.forma.instance            
        this.barra             = this.$refs.barra.instance  
        this.notify            = notify  
        this.parametros        = JSON.parse(this.datos)
        this.mostrar_botones()
    },

    methods: pantalla_definiciones.metodos,

    data() {
        return {    
            forma_id : forma_id,
            // Indicador de tareas
            indicador_visible: false,
            // Datos de la forma
            parametros: {},
            // Barra de acciones
            barra_botones: pantalla_definiciones.barra_botones(this),
            
            // Opciones CAMPOS
            opciones_opciones: {
                dataSource       : fuenteDatos.creaFuenteDatosConsulta('select', null, 'opciones_sistema', 'opciones_sistema', [], []),
                displayValue     : "nombre",
                displayExpr      : "nombre",
                searchExpr       : "nombre",
                valueExpr        : "id",
                hideSelectedItems: true
            }      
        }
    }
}

export default forma;

</script>