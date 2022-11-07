<template>
    <div class="shadow-sm bg-body rounded ">
        <DataForma                 
            ref="dataForma"  
            :attributes="atributos_forma"
            @mounted="form_mounted"

        >            
        </DataForma>

        <div class="linea_blanco"></div>  
        <ToolBar    
            ref="barraRef"  
            :attributes="atributos_barra"
        />
    </div>
</template>

<script setup lang="ts">
import { getCurrentInstance, ref, onMounted } from "vue";

// that <- this
let that = getCurrentInstance().ctx;

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
// elementos ya viene en formato devexpress
let campos = forma_campos.campos_forma(that, that.basicas);
// parametros para dataforma
let atributos_forma = {
    config: {
        id: component_name,
        name: component_name,
        items: campos["elementos"], 
        //items: [], 
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

// funcion llamada por evento mounted DataForma
async function form_mounted(DataForma) {
    that.forma = DataForma.instance;
    console.log("EVENT: Mounted -> THAT", that);     
    console.log("EVENT: Mounted -> DataForma.dxForm", that.forma.option);    
    console.log("EVENT: Mounted -> THAT.$refs.formRef", that.$refs.dataForma); 
    console.log("EVENT: Mounted -> THAT.$refs.formRef.instance", that.$refs.dataForma.instance);     
};

onMounted(() => {
   // that.forma = that.$refs.dataForma;
});
</script>

<style scoped>
</style>