<template src="./pantalla_trd.html">
</template>

<script setup lang="ts">
import { getCurrentInstance, ref, onMounted } from "vue";

// Este componente
let that = getCurrentInstance().ctx;

//**************************//
// Atributos del componente //
//**************************//
import trd_arbol from "../trd_arbol/trd_arbol.vue";

let name = 'trd_definicion_forma';
let formRef = ref(null);
let barraRef = ref(null);
that.dataForm = null; 

// Propiedades
const props = defineProps( $forma.forma_propiedades({}) );
let attributes = $forma.lee_propiedades(props, "trd_pantalla");
attributes = (attributes != undefined ? attributes.datos : {});
console.log("attributes:", attributes)


// Ver pantalla de dependencias, serie, subserie, etc
let arbol_visible = ref(false);
let opciones_arbol = {};

// Retorna a llamador
const retorna_grid = function() {
    $lib.llamar_componente("trd_basica_grid", {});
}

const cerrar_emergente = function() {
    if ($ventana_emergente_trd_importa) {
        $ventana_emergente_trd_importa.opciones.visible = false;
    }
}

// Retorna de envio post de datos
const retorna_envio = function(retorna_datos) {
    retorna_grid();
    cerrar_emergente();
}

// Envia datos servidor
async function enviar_datos(modo) {
    let datos = that.dataForm.validateData();
    if (datos.isValid == true) {
        let parametros = {
            "datos" : datos["formData"],
            "accion": modo
        }
        $forma.envio_accion_notifica("trd_acciones", parametros, retorna_envio)   
    }    
}

// Acciones barra botones (Crear, Modificar, Regresar)
function callBackButtons(evento, modo) {   
    switch (modo) {
        case "regresar":
            retorna_grid();
            cerrar_emergente();
            break;
        
        default:
            enviar_datos(modo);
    }         
}

// Funcion llamada por evento mounted DataForma
async function dataFormaMounted(DataForma) {
    //that.dataForm = DataForma.instance;
    that.dataForm = DataForma;
    that.dataForm.formData(attributes.datos);  
};

window.$pantalla_trd = that;

onMounted(() => {            
    atributos_forma.config.formData = attributes.registro;
    that.registro = attributes.registro;
    if (attributes.mode == "modificar") {
        arbol_visible.value = true        
    };
    setTimeout(() => {
        that.arbol = that.$refs.componente_arbol
    }, 3000);
    
})

// Atributos forma y barra
import forma_campos from "./forma_campos"
import forma_barra from "./forma_barra"

let atributos_forma = {
    config: {
        id: name,
        formData: {},
        items: forma_campos.items(attributes.importar),
        colCount: 1    
    }                 
} 

let atributos_barra = {
    items   : forma_barra.getItems({
        "mode": attributes.mode,
        "callBack": callBackButtons
    })
}  
</script>