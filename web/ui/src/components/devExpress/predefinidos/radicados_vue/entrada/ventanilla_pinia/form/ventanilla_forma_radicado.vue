<template src="./ventanilla_forma_radicado_plantilla.html">
</template>

<script setup lang="ts">
import { getCurrentInstance, ref, onMounted } from "vue";

// that <- this
let that = getCurrentInstance().ctx;

console.log("getCurrentInstance()", getCurrentInstance())

//**************************//
// Atributos del componente //
//**************************//

import forma_general from "../../../../comunes_vue/forma/forma.js";
import forma_definiciones from "./ventanilla_forma_radicado_definiciones.js";
import forma_campos from "./ventanilla_forma_radicado_campos.js";

let component_name = "ventanilla_radicado_forma";
let dataForma = ref(null);  // DataForma

that.basicas = {
    "forma_id": component_name
}
let campos = forma_campos.campos_forma(that, that.basicas);
console.log("CAMPOS:", campos["elementos"])
// definicion de forma
let atributos_forma = {
    config: {
        id: component_name,
        name: component_name,
        items: campos["elementos"], 
        colCount: 2  
    }                   
}; 

// envia datos servidor
async function enviar_datos() {};

let atributos_barra = {
    items: [
        // $forma.botonBarra({
        //     text: 'Ingresar',
        //     type: 'success',
        //     icon: 'fa-solid fa-arrow-right-to-bracket',
        //     click: enviar_datos
        // })
    ]
}; 

console.log("atributos_forma:", atributos_forma);

// funcion llamada por evento mounted DataForma
async function form_mounted(DataForma) {
    console.log("EVENT: Mounted -> THAT", that);     
    console.log("EVENT: Mounted -> DataForma", DataForma, DataForma.instance);    
    console.log("EVENT: Mounted -> THAT.$refs.formRef", that.$refs.dataForma); 
    console.log("EVENT: Mounted -> THAT.$refs.formRef.instance", that.$refs.dataForma.instance);     
};

onMounted(() => {
    //that.dataForm = that.$refs.formRef;
});
</script>

<style scoped>
</style>