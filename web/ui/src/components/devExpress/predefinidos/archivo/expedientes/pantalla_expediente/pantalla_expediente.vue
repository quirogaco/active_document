<template src="./pantalla_expediente.html">
</template>

<script setup lang="ts">
import { getCurrentInstance, ref, onMounted } from "vue"
import { DxLoadPanel } from 'devextreme-vue/load-panel'
import { DxToolbar } from 'devextreme-vue/toolbar'

import notify from 'devextreme/ui/notify'

import expediente_archivos from "../expediente_archivos/expediente_archivos.vue"
import pantalla_expediente_definiciones from 
    "./pantalla_expediente_definiciones.js"
import forma_campos from "./forma_campos"

// Este componente
let that = getCurrentInstance().ctx;
let name = 'pantalla_expediente';
let titulo = "Expediente";
that.dataForm = null;
let formRef = ref(null);
let barra = ref(null);
that.barra = barra;

// Indicador de tareas
let indicador_visible = ref(false);

// Ver pantalla archivos
let ref_expediente_archivos = ref(null);
let expediente_archivos_visible = ref(false);
let opciones_expediente_archivos = ref({});

// Metodos
that = $lib.assignAttributes(
    that, 
    pantalla_expediente_definiciones.metodos(that)
);

// Barra de acciones
let barra_botones = pantalla_expediente_definiciones.barra_botones(that);
that.barra_botones = barra_botones;

// Propiedades
const props = defineProps( $forma.forma_propiedades({}) );
let parametros = $forma.lee_propiedades(props, 'pantalla_expediente');
parametros = (parametros != undefined ? parametros.datos : {});
that.parametros = parametros;

// Forma
let atributos_forma = {
    config: {
        id: name,
        items: forma_campos.items(),
        colCount: 3   
    }                 
} 
that.atributos_forma = atributos_forma;

// Funcion llamada por evento mounted DataForma
async function dataFormaMounted(DataForm) { 
    that.dataForm = DataForm
}

that.parametros.counter_safety = 0;

onMounted(() => {   
    console.log("MOUNTED")     
    that.indicador_visible = false;
    that.forma = that.$refs.forma;
    that.barra = that.$refs.barra.instance;          
    that.notify = notify
    window.$pantalla_expediente = that;
    that.parametros.padre = "EXPEDIENTE";
    that.parametros.padre_id = that.parametros.expediente_id;
    that.parametros.padre_datos = that.parametros.expediente_datos; 
    that.expediente_archivos_parametros = that.parametros;
    window.$pantalla_expediente.serie_id = null;
    window.$pantalla_expediente.subserie_id = null;
    window.$pantalla_expediente.modo = that.parametros.modo;

    console.log("that.parametros>", that.parametros.expediente_datos);

    window.$pantalla_expediente.consulta = true;
    if (that.parametros.modo == "modificar") {    
        expediente_archivos_visible.value = true;  
        window.$pantalla_expediente.consulta = false;          
        setTimeout(() => {    
            let formData = that.dataForm.formData();
            window.$pantalla_expediente.serie_id = formData["serie_id"];
            window.$pantalla_expediente.subserie_id = formData["subserie_id"];
        }, 3000);
    };

    if (that.parametros.modo == "crear") {    
        window.$pantalla_expediente.consulta = false; 
    };

    // la instancia toma tiempo cuamdo es muy grande
    setTimeout(() => {
        that.dataForm.formData(parametros.expediente_datos)
    }, 1500);

    $save_params("datos_expediente", parametros.expediente_datos);  
    
    that.mostrar_botones()
})

let fieldDataChanged = function(e) {   
    //console.log("<<<<< PANTALLA EXPEDIENTE FORM DATOS CAMBIADOS >>>>", e)
}

let contentReady = function(e) {   
    that.parametros.counter_safety += 1;
    //console.log("++++++ PANTALLA EXPEDIENTE contentReady ++++", that.parametros.counter_safety, e)
}
</script>