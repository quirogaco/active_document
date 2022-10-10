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

        <BpmnComponente
            ref         = "bpmnRef"
            :attributes = "atributos_bpmn" 
        />        
    </div> 
</template>

<script setup lang="ts">
import { getCurrentInstance, ref, onMounted } from "vue";

// Este componente
let that = getCurrentInstance().ctx;

//**************************//
// Atributos del componente //
//**************************//
import BpmnComponente from "../bpmn/bpmn_componente.vue";
import { DxBox, DxItem } from 'devextreme-vue/box';

import forma_campos from "./forma_campos";
import forma_barra  from "./forma_barra";
let name     = 'flujos_dinamicos_forma';
let formRef  = ref(null);
let barraRef = ref(null);
let bpmnRef  = ref(null);
that.dataForm = null; 
that.bpmn     = null; 

// Propiedades
const props    = defineProps($forma.forma_propiedades({}));
let attributes = $forma.lee_propiedades(props);

// Opciones de DataForma
let atributos_forma = {
    id      : "flujos_dinamicos_forma",
    formData: {},
    items   : forma_campos.items,
    colCount: 1                     
}  

// Retorna a llamador
const retorna_grid = function() {
    $lib.llamar_componente("flujos_dinamicos_grid", {});
}

// Retorna de envio post de datos
const retorna_envio = function(retorna_datos) {
    console.log("flujos_dinamicos_forma->retorna_datos:", retorna_datos);
    //retorna modo para validar que hacer
    retorna_grid();
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
}

// Barra de acciones funcion asociada al click del boton
function callBackButtons(evento, modo) {   
    switch (modo) {
        case "regresar":
            retorna_grid();
            break;
        
        default:
            enviar_datos(modo);
    }     
}

let atributos_barra = {
    id      : "barra_emergente_gestion",
    items   : forma_barra.getItems({
        "mode"    : attributes.mode,
        "callBack": callBackButtons
    })
}  

// Funcion llamada por evento mounted DataForma
async function dataFormaMounted(DataForma) {
    console.log("MONTADO--->>>>", attributes)
    // aqui that.dataForm no existe todavia
};

// Opciones de Bpmn
let atributos_bpmn = {
    xml: attributes.datos.bpmn
}  

async function leer_bpmn() {
    const xml = await that.bpmn.leer_flujo();
    return xml;
}

// Eventos locales 
async function datos_registro() {
    let datos = await $lib.leer_registro_id("tramites", attributes["id"]);

    return datos;
} 

onMounted(() => {
    // Este componente montada
    that.dataForm = that.$refs.formRef;
    that.bpmn     = that.$refs.bpmnRef;    
    that.dataForm.formData(attributes.datos);
})
</script>