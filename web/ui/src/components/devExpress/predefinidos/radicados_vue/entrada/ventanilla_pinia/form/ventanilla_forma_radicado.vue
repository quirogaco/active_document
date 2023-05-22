<template>
    <div class="shadow-sm bg-body rounded ">
        <div 
            :class ="clase_pdf"
            :width = "pdf_ancho"
            :height = "pdf_alto"  
            v-show = "verPdf"
        >                      
        
            <pdf_componente 
                ref          = "visor_pdf" 
                :nombrePdf   = "opciones_pdf.nombrePdf" 
                :buscarTexto = "opciones_pdf.buscarTexto" 
                :operacion   = "opciones_pdf.operacion" 
                :clase       = "opciones_pdf.clase" 
                :descarga    = "opciones_pdf.descarga"
                :datos       = "opciones_pdf.datos" 
                :opciones    = "opciones_pdf.opciones"  
                :key         = "repintar_pdf"                      
            />

        </div>

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
import { getCurrentInstance, ref, reactive, onMounted, onBeforeMount } from "vue";

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
// no funciona enmounted no es reactiva
let params = $get_params("ventanilla_radicado_forma")?.datos;  
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

// Visor de PDF
// Pdf
let verPdf = ref(true); 
let repintar_pdf = ref(0);
let pdf_existe = ref(false);
let pdf_ancho = ref("100%");
let pdf_alto = ref("100%");
//let clase_pdf = ref("col-12 shadow-sm p-3 mb-3 bg-body rounded");
let clase_pdf = ref("shadow-sm p-3 mb-3 bg-body rounded");
// Opciones visor PDF
let opciones_pdf = ref({});

// funcion llamada por evento mounted DataForma
async function form_mounted(DataForma) {
    that.forma = DataForma.instance;
    that.retorna = "ventanilla_radicado_grid";   
    if (params._modo_ == "CORREO") {
        that.retorna = "correos_grid";
        params["tercero_clase"] = "JURIDICA";
        params["es_pqrs"] = "DOCUMENTO";
        setTimeout(() => {
            that.forma_datos(params);
        }, 1500);
    }
    else {

    } 
};

onMounted(() => {});

onBeforeMount(() => {
    $save_params("_radica_dependencia_", {"responsable": "correspondencia_id"});
    $save_params("pqrs_filtro", "DOCUMENTO");
    if (params._modo_ != "CORREO") {
        campos["elementos"][3].items[0].visible = false;
    }
});
</script>

<style scoped>
</style>