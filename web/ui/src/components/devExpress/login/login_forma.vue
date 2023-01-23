<template>
    <div class="container-fluid ">  
        <div class=" logo ">  
            <div class="vw-90 vh-90 "> 
                    
                    <div class="top40 shadow-sm p-3 mb-5 bg-body ">
                        <DataForma     
                            ref         = "formRef"  
                            :attributes = "atributos_forma"
                            @mounted    = "form_mounted"
                        />

                        <div class="linea_blanco"></div>  
                        <ToolBar    
                            ref         = "barraRef"  
                            :attributes = "atributos_barra"
                        />
                    </div>

            </div>
        </div>        
    </div> 
</template>

<script setup lang="ts">
import { getCurrentInstance, ref, onMounted } from "vue";
import crear_rutas_navegacion from 
'../../../librerias/crear_rutas_navegacion.js';

// Este componente
let that = getCurrentInstance().ctx;

//**************************//
// Atributos del componente //
//**************************//
let name = 'login_forma';
let formRef = ref(null);
let barraRef = ref(null);
let logo_ingreso = window.$direcciones.servidorDatos+"/logo_ingreso";
let image = "url(" + logo_ingreso + ")";

// definicion de forma
let atributos_forma = {
    config: {
        id: name,
        items: [        
            {
                "componente" : "campo",
                "tipo": "texto",
                "id": "codigo",
                "titulo": "Codigo", 
                "obligatorio": true,
                "mayuscula": "NO",
                "longitud": 120,
                "ancho": 250,
                //"alto": 30
            },
            
            {
                "componente": "campo",
                "tipo": "texto",
                'modo': 'password',
                "id": "clave",
                "titulo": "Clave", 
                "obligatorio": true,
                "mayuscula": "NO",
                "longitud": 30,
                "ancho": 150
            }
        ],
        colCount: 1
    }                   
}; 

// envia datos servidor
async function enviar_datos() {    
    let datos = that.dataForm.validateData(); 
    //console.log("LGIN DATOS:", datos) 
    if (datos.isValid == true) {
        window.$mostrar_esperar();
        let parametros = datos["formData"];                
        let urlCompleta = window.$direcciones.servidorDatos + '/ingreso_sistema';   
        let respuesta = window.$f.http.llamadoRestSincGet(urlCompleta, parametros);
        if (respuesta.error == "no") {
            window.$rutasNavegacion = crear_rutas_navegacion.creaRutasNavegacion(respuesta.datos.opciones);                   
            window._APLICACION_.use(window.$rutasNavegacion.ruta);
            window.$router = window.$rutasNavegacion.ruta;
            window.sessionStorage.setItem("usuario", JSON.stringify(respuesta.datos.usuario));
            window.sessionStorage.setItem("sesion", JSON.stringify(respuesta.datos.sesion));
            await window.$ns['aplicacion'].asignaRuta('cajon', 'components/devExpress/cajon/cajon.vue');  
            window.$ns['aplicacion'].asignaComponente('cajon');

            window.$usuario = JSON.parse(window.sessionStorage.getItem("usuario")); 
        }
        else {
            $sistema["notifica"](respuesta.mensaje, "error");
        }
        window.$ocultar_esperar();
    }    
};

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

// funcion llamada por evento mounted DataForma
async function form_mounted(DataForma) {
    that.dataForm = DataForma;
};

onMounted(() => {
});
</script>

<style scoped>
.logo {
  background-image: v-bind('image');
  background-size: 80%;
  background-position: center;
  background-repeat: no-repeat;
}

.top40 {
    position: absolute;
    top: 30%;
    left: 15%;
}
</style>