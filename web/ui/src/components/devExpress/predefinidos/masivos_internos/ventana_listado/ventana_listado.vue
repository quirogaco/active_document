<template src="./ventana_listado.html">
</template>

<script>
/*
Este modelo es totalmente abierto definiendo campo a campo sin usar items de la forma
*/

import fuenteDatos from '../../../remoto/fuenteDatos.js'

import DxForm      from 'devextreme-vue/form'
import DxTextBox   from 'devextreme-vue/text-box'
import DxSelectBox from 'devextreme-vue/select-box'
import { DxValidator,  DxRequiredRule } from 'devextreme-vue/validator'
import DxButton    from 'devextreme-vue/button'
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import { DxScrollView } from 'devextreme-vue/scroll-view'
import notify from 'devextreme/ui/notify'

import grid_destinatarios      from '../grid_destinatarios/destinatarios_grid.vue'
import ventana_listado_metodos from './ventana_listado_metodos.js'

let ventana_listado =  {
    name: 'ventana_listado',

    components: {
        DxForm,
        DxTextBox, 
        DxSelectBox,  
        DxValidator,
        DxRequiredRule,    
        DxButton,
        DxToolbar,
        DxItem,
        DxScrollView,

        // Listado de destinatarios
        grid_destinatarios,
    },

    props: {
        datos: ""
    },

    mounted() {
        this.parametros = JSON.parse(this.datos)
        this.notify     = notify
        if (this.parametros.modo == "modificar") {
            this.cargar_datos(this.parametros.listado_datos)
        }
    },

    methods: ventana_listado_metodos.metodos,

    data() {
        return {
            titulo         : "Creación de listados de destinatarios",
            // Datos formulario
            valores_formulario: {},
            
            //Parametros de invocación
            parametros: {},
            
            // Campos individuales
            dependencia_id: "",
            detalle       : "",

            // Url de servicios
            urlCompleta: window.$direcciones.servidorDatos + '/masivos_salidas',

            // Fuente de datos
            fuente    : fuenteDatos.creaFuenteDatosUniversal("select", "dependencia", "dependencias", null, [], []),

            // TOOLBAR atributos y Botones
            toolbarAtributos: {
                class: 'bg_tab_panel'
            },

            boton_salvar: {
                "text"   : "Salvar listado",
                "icon"   : "fas fa-save",
                "visible": this.es_visible("salvar"),
                "type"   : "success",
                "onClick": this.salvar
            },

            boton_modificar: {
                "text"   : "Modificar listado",
                "icon"   : "fas fa-edit",
                "visible": this.es_visible("modificar"),
                "type"   : "default",                
                "onClick": this.modificar
            },

            boton_borrar: {
                "text"   : "Borrar listado",
                "icon"   : "fas fa-minus-circle",
                "visible": this.es_visible("borrar"),
                "type"   : "danger",                
                "onClick": this.borrar
            },

            boton_regresar: {
                "text"   : "Regresar",
                "icon"   : "fas fa-backward",
                "type"   : "normal",                
                "onClick": this.regresar
            }
        }
    }
}

export default ventana_listado;

</script>

<style>
.dx-field-label{  
    text-align: right;  
    font-weight: bold;
} 
</style>