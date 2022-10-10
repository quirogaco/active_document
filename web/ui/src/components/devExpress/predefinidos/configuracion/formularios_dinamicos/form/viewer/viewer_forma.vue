<template>   
    <div class="container  ">         
        <DataForma     
            ref         = "formRef"  
            :attributes = "atributos_forma"
            @mounted    = "dataFormaMounted"
        />

        <ToolBar    
            ref         = "barraRef"  
            :attributes = "atributos_barra"
        />
    </div> 
</template>

<script setup lang="ts">
import { getCurrentInstance, ref, onMounted } from "vue";

// Este componente
let that = getCurrentInstance().ctx;

//**************************//
// Atributos del componente //
import { DxBox, DxItem } from 'devextreme-vue/box';


import forma_general from "../../../../comunes_vue/forma/forma.js"
import viewer_barra  from "./viewer_barra";
let name      = 'visor_forma_dinamica';
let formRef   = ref(null);
let barraRef  = ref(null);
that.dataForm = null; 

// properties
const props          = defineProps(forma_general.forma_propiedades({}));
let atributos_forma  = forma_general.lee_propiedades(props);
that.atributos_forma = atributos_forma;
console.log("--**that.atributos_forma-***", that.atributos_forma);

const retorna_envio = function(retorna_datos) {
    console.log("visor_forma_dinamica->retorna_datos:", retorna_datos);
}

// Envia datos servidor
async function enviar_datos(modo) {
    let datos = that.dataForm.validateData();
    if (datos.isValid == true) {
        // Datos de la forma
        datos["formData"]["flujo"] = {
            "bpmn"       : await leer_bpmn(),
            "notifica_id": datos["formData"]["notifica_id"]
        }
        // Parametros 
        let parametros = {
            "datos" : datos["formData"],
            "accion": modo
        }
        $forma.envio_accion_notifica("flujo_acciones", parametros, retorna_envio)   
    }    
};

// Funcion llamada por evento mounted DataForma
async function dataFormaMounted(DataForma) {
    console.log("MONTADO VIEWER FORMA--->>>>", atributos_forma)
};

const emit = defineEmits(['mounted'])

onMounted(() => {
    // Este componente montada
    that.dataForm = that.$refs.formRef;
    that.dataForm.formData(atributos_forma.datos);
    that.$emit('mounted', that.dataForm);
})
</script>