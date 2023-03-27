<template>

    <div 
        id = "aplicacion" 
        class = "fondo"
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
} from "vue-router";

import { 
    onMounted, 
    ref,
    getCurrentInstance
} from 'vue';

import { defineStore } from 'pinia';

import { DxLoadPanel }  from 'devextreme-vue/load-panel';
import { alert }        from "devextreme/ui/dialog";
import http             from './librerias/http.js';

import crear_rutas_navegacion from './librerias/crear_rutas_navegacion.js';
import popup_onlyoffice from './components/onlyOffice/popup_onlyoffice.vue';
import popup_pdf        from './components/pdfjs/popup_pdf.vue';
let componentes = {};

export default {
    name      : 'Aplicacion principal',  
    
    components: {
        DxLoadPanel,    
        popup_pdf,    
        popup_onlyoffice
    },

    mounted() {
        window.$ns['aplicacion'] = this
        window.$mostrar_esperar = this.mostrar_esperar
        window.$ocultar_esperar = this.ocultar_esperar;
        window.$alertar = alert

        // storage params
        window.$get_params = this.get_params
        window.$save_params = this.save_params
        // storage component
        window.$get_component = this.get_component
        window.$save_component = this.save_component

        const globalStore = defineStore('globalStore', {
            state: () => {
                return { 
                    component_parameters: {},
                    components: {}                   
                }
            },
            // could also be defined as
            // state: () => ({ count: 0 })
            actions: {
                save_params(componente_name, params) {
                    this.component_parameters[componente_name] = params
                },

                get_params(componente_name) {
                    return this.component_parameters[componente_name]
                },

                save_component(componente_name, component) {
                    this.components[componente_name] = component
                },

                get_component(componente_name) {
                    return this.components[componente_name]
                }
            },
        })
        window._APLICACION_.config.globalProperties.globalStore = globalStore();
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
        },

        get_params(componente_name) {            
            let globalStore = window._APLICACION_.config.globalProperties.globalStore;
            let datos = globalStore.get_params(componente_name);

            return datos;
        },

        save_params(componente_name, params) {            
            let globalStore = window._APLICACION_.config.globalProperties.globalStore;
            globalStore.save_params(componente_name, params);         
        },

        get_component(componente_name) {            
            let globalStore = window._APLICACION_.config.globalProperties.globalStore;
            let datos = globalStore.get_component(componente_name);

            return datos;
        },

        save_component(componente_name, component) {            
            let globalStore = window._APLICACION_.config.globalProperties.globalStore;
            globalStore.save_component(componente_name, component);         
        }

    }
}
</script>