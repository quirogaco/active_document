<template>

    <div 
        id = "aplicacion" 
    >

        <DxLoadPanel
            v-model:visible = "indicador_visible" 
            :message        = "mensaje_carga_muestra()"  
            :width          = 500
            :height         = 400            
            shading-color   = "rgba(0,0,0,0.4)"
        />

        <div>
            <popup_pdf/>
        </div>  

        <div>
            <popup_onlyoffice 
                :opciones = "opciones_onlyoffice"
                :key      = "emergente_onlyoffice"
            />
        </div>

        <div class="container-fluid vh-100"  >      
            <component v-bind:is="componenteVisible"></component>
        </div>
        
    </div>

</template>

<script>
import { 
    createWebHashHistory,
    createRouter 
} from "vue-router"

import { 
    onMounted, 
    ref,
    getCurrentInstance
} from 'vue'

import { DxLoadPanel }  from 'devextreme-vue/load-panel'
import { alert }        from "devextreme/ui/dialog";
import http             from './librerias/http.js'

import crear_rutas_navegacion from './librerias/crear_rutas_navegacion.js'
import popup_onlyoffice from './components/onlyOffice/popup_onlyoffice.vue'
import popup_pdf        from './components/pdfjs/popup_pdf.vue'
let componentes = {}

export default {
    name      : 'Aplicacion principal',  
    
    components: {
        DxLoadPanel,    
        popup_pdf,    
        popup_onlyoffice
    },

    mounted() {
        window.$ns['aplicacion'] = this
        window.$mostrar_esperar  = this.mostrar_esperar
        window.$ocultar_esperar  = this.ocultar_esperar
        window.$alertar          = alert
    },

    data() {
        return {  
            componenteVisible: null,     
            
            // Visor onlyoffice
            opciones_onlyoffice: {
                visible: false,
                editor : {}
            },
            emergente_onlyoffice: 0,

            // Panel de carga general
            indicador_visible: false,
            mensaje_carga    : "Por favor esperar....",
            mensaje_temporal : null,
            rutas            : []         
        }
    },

    methods: {
        muestraComponente(nombreComponente) {   
            this.componenteVisible = nombreComponente;
        },

        async createRoute(nombreComponente, rutaComponente) {   
            let ruta = {};
            await import( ("./" + rutaComponente) ).then((modulo) => {                
                ruta = {
                    path     : ("/" + nombreComponente),
                    name     : nombreComponente,
                    component: modulo.default, 
                    props    : true     
                }   
                 this.$.components[nombreComponente] = modulo.default               
            })

            return ruta;
        },

        async asignaRuta(nombreComponente, rutaComponente) {   
            let ruta = await this.createRoute(nombreComponente, rutaComponente);
            this.rutas.push(ruta);               
        },

        asignaComponente(nombreComponente) {               
            this.componenteVisible = nombreComponente;
        },

        crea_enrutador() {
            let routes = this.rutas; 
            window.$rutasNavegacion = {
                ruta        : crear_rutas_navegacion.creaEnrutador(routes),
                navegaciones: routes
            };
            window._APLICACION_.use(window.$rutasNavegacion.ruta);
            window.$router = window.$rutasNavegacion.ruta; 
        },

        asignaAtributoDinamico(atributo, valor) {
            this[atributo] = valor;
        },

        mostrar_visor_archivos_sistema(datos_visor) {
            this.opciones_onlyoffice["editor"]  = datos_visor
            this.opciones_onlyoffice["visible"] = true
            this.emergente_onlyoffice += 1
        },

        mensaje_carga_muestra() {
            let mostrar = this.mensaje_carga
            if (this.mensaje_temporal != null) {
                mostrar = this.mensaje_temporal
            }

            return mostrar
        },

        mostrar_esperar(mensaje=null) {
            this.mensaje_temporal  = mensaje
            this.indicador_visible = true
        },

        ocultar_esperar() {
            this.mensaje_temporal  = null
            this.indicador_visible = false
        }
    }
}
</script>