<template src="./tvd_pantalla_expediente.html">
</template>

<script>
import { DxLoadPanel } from 'devextreme-vue/load-panel'
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

import tvd_pantalla_expediente_definiciones from "./tvd_pantalla_expediente_definiciones.js"

import tvd_expediente_archivos from "../tvd_expediente_archivos/tvd_expediente_archivos.vue"

let tvd_expediente_trd =  {
    name: 'tvd_expediente_trd',

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
        
        // Grilla de archivos
        tvd_expediente_archivos
    },

    props: {
        datos: ""
    },

    mounted() {
        this.indicador_visible = false
        this.forma             = this.$refs.forma.instance            
        this.barra             = this.$refs.barra.instance             
        this.notify            = notify  
        window.$tvd_pantalla_expediente = this  

        setTimeout(() => {
            this.$grid_archivos_expediente_tvd = this.$refs.expediente_archivos
        }, 3000);

        // Datos trd
        this.parametros        = JSON.parse(this.datos)
        if (this.parametros.accion == "modificar") {
            this.forma.option("formData", parametros.tvd_expediente_datos)
        }
        this.mostrar_botones()
    },

    methods: tvd_pantalla_expediente_definiciones.metodos,

    data() {
        return {    
            // Datos de la forma
            parametros: {
            },

            // Indicador de tareas
            indicador_visible: false,

            // Ver pantalla archivos
            expediente_archivos_visible: false,
            opciones_expediente_archivos: {},

            // Opciones CAMPOS
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
            barra_botones: tvd_pantalla_expediente_definiciones.barra_botones(this)        
        }
    }
}

export default tvd_expediente_trd;

</script>