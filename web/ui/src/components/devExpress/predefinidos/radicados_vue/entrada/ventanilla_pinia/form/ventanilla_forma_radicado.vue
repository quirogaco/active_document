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
import fuente from "../../../../comunes_vue/forma/fuente.js";
import forma_definiciones from "./ventanilla_forma_radicado_definiciones.js";
import forma_campos from "./ventanilla_forma_radicado_campos.js";
import pdf_componente from "../../../../../../pdfjs/pdf_componente.vue"

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
console.log("params:", params) 
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
//let pdf_existe = ref(false);
let pdf_ancho = ref("800px");
let pdf_alto = ref("200px");
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
            let anexos = params["archivos_anexos"];
            let fuente_anexos = fuente.fuente_arreglo(anexos) 
            forma_general.asigna_fuente(
                that, 
                "anexos_radicado", 
                fuente_anexos
            )   
            that.forma_datos(params);
            //nombre:"5293_correo_datos___roahhkmroys8ftvxnyeczw.pdf"
            const result = anexos.filter(archivo => archivo.nombre.includes("_correo_datos"));
            console.log("result:", result)
            that.verPdf= true; 
            let pdf_parametros = {
                titulo_general: "Pdf del Correo",
                archivo_id    : result[0].id, //"fd778b8e-fd7e-11ed-92d7-086266b539c1", 
                tipo_documento: "pdf",
                titulo        : "Pdf del Correo",
                modo          : "leer",
                descarga      : 'no'
            };     
            let parametros = window.$lib.prepara_parametros_archivo(pdf_parametros); 
            opciones_pdf.value.nombrePdf = parametros.datos.idArchivo;
            opciones_pdf.value.buscarTexto = parametros.datos.buscarTexto;
            opciones_pdf.value.operacion = parametros.datos.operacion;           
            opciones_pdf.clase = parametros.datos.clase;
            opciones_pdf.value.descarga = parametros.datos.descarga;
            opciones_pdf.value.titulo = parametros.datos.titulo_general; 
            repintar_pdf.value += 1;
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
        campos["elementos"][0].items[0].visible = false
    }
    else {
        campos["elementos"][0].items[0].visible = true
    }
});
</script>

<style scoped>
</style>