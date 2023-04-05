<template src="./trd_arbol.html">
</template>

<script>
import notify from 'devextreme/ui/notify'
import { 
    DxTreeList,
    DxFilterRow,
    DxSearchPanel,
    DxSelection,
    DxColumn,
} from 'devextreme-vue/tree-list'

import DxButtonGroup from 'devextreme-vue/button-group'
import DxToolbar     from 'devextreme-vue/toolbar'

import metodos        from './trd_arbol_metodos.js'
import botones_accion from './trd_arbol_atributos.js'

import ventana_emergente_trd from './ventana_emergente_trd/ventana_emergente_trd.vue'

export default {
    components: {
        DxButtonGroup,
        DxToolbar,
        DxTreeList,
        DxFilterRow,
        DxSearchPanel,
        DxSelection,
        DxColumn,

        ventana_emergente_trd
    },

    data() {
        return {
            // Datos del arbol
            trd_data: [],

            // Ventana formas TRD
            opciones_ventana: {
                visible: false
            },
            emergente_key: 0,

            // Registro padre seleccionado
            seleccionado_padre_id : "",
            seleccionado_tipo: "",
            seleccionado_id: "",
            seleccionado_nombre: "",

            // Botones de acción
            barra_elementos: [                                  
                {
                    widget  : "dxButtonGroup",
                    location: "after",                       
                    options : {                            
                        items      : botones_accion,  
                        onItemClick: this.boton_click
                    }
                }     
            ]
        }
    },

    mounted() {        
        this.barra = this.$refs.barra.instance 
        this.arbol = this.$refs.arbol.instance 
        window.$trd_arbol = this
        this.botones_accion = this.barra_elementos[0].options.items
        this.boton_dependencia = 0
        this.boton_serie = 1
        this.boton_subserie = 2
        this.boton_tipo = 3
        this.boton_limpia = 4
        this.boton_accesos = 5

        //this.seleccionado_tipo = window.$pantalla_trd.arbol.seleccionado_tipo
        this.seleccionado_padre_id = ""
        this.seleccionado_modo = ""     
        this.seleccionado_tipo = ""
        this.seleccionado_id = ""
        this.seleccionado_nombre = ""  
        this.boton_ocultar_todos()
        this.boton_visibilidad(this.boton_dependencia, true)      
        setTimeout(() => {
            //console.log("window.$pantalla_trd>>>>:", window.$pantalla_trd)
            //let pantalla_trd = $forma.lee_propiedades(window.$pantalla_trd)
            let pantalla_trd = window.$pantalla_trd
            console.log("pantalla_trd>>>>:", pantalla_trd)
            this.trd_data = pantalla_trd.registro.trd_arbol;
        }, 3000);
        this.notify = notify               
    },

    methods: metodos
}
</script>

<style>

</style>