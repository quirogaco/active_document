<template src="./forma_salida_consulta_plantilla.html">
</template>

<script>
import { DxDataGrid }        from 'devextreme-vue/data-grid'
import { DxForm }            from 'devextreme-vue/form'
import DxTextArea            from 'devextreme-vue/text-area'
import DxRadioGroup          from 'devextreme-vue/radio-group'
import DxTagBox              from 'devextreme-vue/tag-box'
import { DxFileUploader }    from 'devextreme-vue/file-uploader'
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import forma_general         from "../../../comunes_vue/forma/forma.js"

import forma_definiciones from "./forma_salida_consulta_definiciones.js"
import forma_campos       from "./forma_salida_consulta_campos.js"

// Definiciones basicas
const basicas = {
    "forma_id"   : "forma_salida_consulta",
    "titulo"     : "Consulta de Salida",
    "columnas"   : 2,    
}

let formulario =  {
    name: basicas["forma_id"],
    components: {  
        DxDataGrid,                     
        DxForm,
        DxTextArea,
        DxRadioGroup,
        DxToolbar,
    },

    props: forma_general.forma_propiedades({}),

    mounted() {
        forma_general.forma_funciones.montado_general(this)
        console.log("this.parametros:", this.parametros)
    },

    data() {       
        return forma_campos.campos_forma(this, basicas)        
    },

    methods: forma_definiciones.metodos
}

export default formulario;
</script>