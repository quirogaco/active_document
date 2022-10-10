<template src="./web_anonimo_forma_radicado_plantilla.html">
</template>

<script>
import { DxForm }            from 'devextreme-vue/form'
import DxTextArea            from 'devextreme-vue/text-area'
import DxRadioGroup          from 'devextreme-vue/radio-group'
import DxTagBox              from 'devextreme-vue/tag-box'
import { DxFileUploader }    from 'devextreme-vue/file-uploader'
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import forma_general         from "../../../comunes_vue/forma/forma.js"

import forma_definiciones from "./web_anonimo_forma_radicado_definiciones.js"
import forma_campos       from "./web_anonimo_forma_radicado_campos.js"

// Definiciones basicas
const basicas = {
    "forma_id": "web_anonimo_radicacion",
    "titulo"  : "Formulario Anonimo",
    "columnas": 1 
}

let formulario =  {
    name: basicas["forma_id"],
    components: {                       
        DxForm,
        DxTextArea,
        DxRadioGroup,
        DxToolbar,
    },

    props: forma_general.forma_propiedades({}),

    mounted() {
        forma_general.forma_funciones.montado_general(this)
    },

    data() {        
        return forma_campos.campos_forma(this, basicas)        
    },

    methods: forma_definiciones.metodos
}

export default formulario;
</script>