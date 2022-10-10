<template src="./configura_parametros_generales.html">
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
import ArrayStore        from 'devextreme/data/array_store'
import DataSource        from 'devextreme/data/data_source'

import fuenteDatos       from '../../../remoto/fuenteDatos.js'
import onlyoffice_editor from '../../../../onlyOffice/onlyoffice_editor.vue'

import configura_parametros_generales_definiciones from "./configura_parametros_generales_definiciones.js"

let configura_radicacion =  {
    name: 'configura_parametros_generales',

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
        DxValidationGroup,

        DxScrollView,
        onlyoffice_editor
    },

    mounted() {
        this.indicador_visible = false
        this.forma             = this.$refs.forma.instance            
        this.barra             = this.$refs.barra.instance  
        this.notify            = notify   
        this.cargar_datos()       
    },

    methods: configura_parametros_generales_definiciones.metodos,

    data() {
        return {                
             // Indicador de tareas
            indicador_visible: false,

            // Datos de la forma
            parametros: {},

            // Opciones CAMPOS
            opciones_web: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'canales_comunicacion', 'canales_comunicacion', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },

            // Opciones PLANTILLAS recorridos
            opciones_recorridos: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'plantillas', 'plantillas', [], []),
                displayValue: "descripcion",
                displayExpr : "descripcion",
                searchExpr  : "descripcion",
                valueExpr   : "id"
            },

            opciones_notificacion_servidor_smtp: {},
            opciones_notificacion_puerto_smtp: {},
            opciones_notificacion_usuario: {},
            opciones_notificacion_clave: {
                mode: "password"
            },
            opciones_certificado_correo: {},

            opciones_inactividad: {},

            // Opciones prestamo expedientes
            prestamos_maximo: {},

            // Opciones prestamo renovación
            renovacion_maximo: {},

            // Opciones maxima renovaciónes
            renovacion_numero: {},

            // Barra de acciones
            barra_botones: configura_parametros_generales_definiciones.barra_botones(this)        
        }
    }
}

export default configura_radicacion;
</script>