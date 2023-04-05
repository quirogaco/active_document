<template src="./formulario_constructor.html">
</template>

<script>
import DxForm, {
    DxGroupItem,
    DxSimpleItem,
    DxButtonItem,
    DxLabel
} from 'devextreme-vue/form'

import DxTextBox          from 'devextreme-vue/text-box'
import { DxNumberBox }    from 'devextreme-vue/number-box'
import DxDateBox          from 'devextreme-vue/date-box'
import DxButton           from 'devextreme-vue/button'
import { DxFileUploader } from 'devextreme-vue/file-uploader'
import DxSelectBox        from 'devextreme-vue/select-box'
import DxTagBox           from 'devextreme-vue/tag-box'
import DxTextArea         from 'devextreme-vue/text-area'
import DxButtonGroup      from 'devextreme-vue/button-group'


import atributos_campos from './atributos_campos.vue';

// Componentes disponibles
import { campos_tipo } from './lista_componentes.js'

// Metodos
import formulario_constructor_metodos from "./formulario_constructor_metodos.js" 

export default {
    components: {
        DxForm,
        DxGroupItem,        
        DxSimpleItem,
        DxButtonItem,        
        DxTextBox,    
        DxNumberBox,    
        DxDateBox,
        DxFileUploader,
        DxSelectBox,
        DxTagBox,
        DxTextArea,
        DxButton,
        DxButtonGroup,

        // Atributos de los campos
        atributos_campos
    },

    mounted() {
        this.forma_diseno    = this.$refs.forma_diseno.instance
        window.$forma_diseno = this
    
        // Eventos iniciales       
        formulario_constructor_metodos.drop_forma(this)    
        formulario_constructor_metodos.calcula_forma_tamano(this)    
    },

    data() {
        return {
            // Atributos contenedor elementos
            muestra_elementos: true,
            clase_elementos  : "container-fluid border border-2 p-1 col-sm-2",
            campos_tipo      : campos_tipo,
            
            // Atributos contenedor forma
            clase_forma    : "container-fluid border border-2 p-1 col-sm-7",
            forma_attributos: {
                id   : 'constructor_forma_id',
                class: 'bg-light'
            },

            // Atributos contenedor atributos
            muestra_atributos: true,
            clase_atributos  : "container-fluid border border-2 p-1 col-sm-3",

            // Id del contenedor de campos
            lista_ids: function(datos) {
                let contiene_id = "_contiene_" + datos.name

                return contiene_id
            },

            // Datos del campo drag
            datos_drag: null,

            // Campos de la forma
            campos: []
        }
    },

    methods: formulario_constructor_metodos.metodos, 
        
}
</script>

<style>
.dx-buttongroup-wrapper{
    flex-flow: column nowrap;
}
</style>