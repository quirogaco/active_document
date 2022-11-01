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

let component_name = "ventanilla_radicado_forma";
let dataForma = ref(null);  // DataForma
// defineOptions({
//     name: 'yyyyyyyyyylogin_forma',
//     formRef: null,
//     barraRef: null
// })

// let name = 'login_forma';
// 
// let barraRef = ref(null);

// definicion de forma
let atributos_forma = {
    config: {
        id: component_name,
        name: component_name,
        items: [        
            {
                "componente" : "campo",
                "tipo": "texto",
                "id": "codigo",
                "titulo": "Codigo", 
                "obligatorio": true,
                "longitud": 120,
                "ancho": 250
            },
            
            {
                "componente": "campo",
                "tipo": "texto",
                'modo': 'password',
                "id": "clave",
                "titulo": "Clave", 
                "obligatorio": true,
                "longitud": 30,
                "ancho": 150
            }
        ],
        colCount: 2  
    }                   
}; 

// envia datos servidor
async function enviar_datos() {};

let atributos_barra = {
    items: [
        $forma.botonBarra({
            text: 'Ingresar',
            type: 'success',
            icon: 'fa-solid fa-arrow-right-to-bracket',
            click: enviar_datos
        })
    ]
}; 

console.log("atributos_forma:", atributos_forma);

// funcion llamada por evento mounted DataForma
async function form_mounted(DataForma) {
    console.log("EVENT: Mounted -> THAT", that);     
    console.log("EVENT: Mounted -> THAT.$refs.formRef", that.$refs.dataForma); 
    console.log("EVENT: Mounted -> THAT.$refs.formRef.instance", that.$refs.dataForma.instance);     
};

onMounted(() => {
    //that.dataForm = that.$refs.formRef;
});
</script>

<style scoped>
</style>