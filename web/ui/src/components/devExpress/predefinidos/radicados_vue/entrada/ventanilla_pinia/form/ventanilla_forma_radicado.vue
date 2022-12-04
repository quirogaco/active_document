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

that = $lib.assignAttributes(that, forma_definiciones.metodos_forma(that));
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
        colCount: 2,
        items: campos["elementos"],
        fields_format: "devexpress"
    }                  
}; 

let atributos_barra = {
    items: campos["barra_botones"]
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
   console.log("RADICADO FORMA MONTADA:", that);
   $save_params(
        "_radica_dependencia_", 
        {"responsable": "correspondencia_id"} // pqrs_id
    );   
});
</script>

<style scoped>
</style>