<template>

    <div class="container-fluid">
        <DxPopup
            ref = "popup"
            :visible="popup_visible"
            :drag-enabled="false"
            :hide-on-outside-click="true"
            :show-close-button="true"
            :show-title="true"
            :width="opciones.ancho"
            :height="opciones.alto"
            :title="opciones.titulo"   
            container=".dx-viewport"         
        >

            <DxScrollView
                width = "100%"
                height= "100%"
            >
                <component
                    v-bind:is="opciones.componente_visible"
                    :datos="datos"
                >
                </component>     
            </DxScrollView>

        </DxPopup>
    </div>

</template>

<script>
import {ref} from 'vue';
import { DxPopup } from 'devextreme-vue/popup';
import DxButton from 'devextreme-vue/button';
import { DxScrollView } from 'devextreme-vue/scroll-view';

import comentarioGestion from '../componentes_accion/comentario_gestion.vue';
import dependenciaGestion from '../componentes_accion/dependencia_gestion.vue';
import usuarioGestion from '../componentes_accion/usuario_gestion.vue';
import borradorGestion from '../componentes_accion/borrador_gestion.vue';
import trdGestion from '../componentes_accion/trd_gestion.vue';
import trdTemaSubtema from '../componentes_accion/trd_tema_subtema.vue';
import anexarGestion from '../componentes_accion/anexar_gestion.vue';
import apruebaGestion from '../componentes_accion/aprueba_gestion.vue';
import ventanilla_salida_forma 
from '../../radicados_vue/salida/radicacion_formulario/salida_forma_radicado.vue';
import ventanilla_interno_forma 
from '../../radicados_vue/interno/radicacion_formulario/interno_forma_radicado.vue';
import gestion_datos_consulta 
from '../gestion_datos/gestion_datos_consulta.vue';
import ventanilla_radicado_consulta 
    from '../../radicados_vue/comunes/consulta/forma_radicado_consulta.vue';


// Ventana emergente
let ventana =  {
    name: 'ventana_emergente',

    components: {
        DxPopup,
        DxButton,
        DxScrollView,

        comentarioGestion,
        dependenciaGestion,
        usuarioGestion,
        borradorGestion,
        trdGestion,
        trdTemaSubtema,
        anexarGestion,
        apruebaGestion,

        gestion_datos_consulta,
        ventanilla_salida_forma,
        ventanilla_interno_forma,
        ventanilla_radicado_consulta
    },

    created() {},

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {}
            }
        }        
    },

    created() {
        this.datos = this.opciones;
    },
    
    mounted() {
        this.popup_visible = ref(this.opciones.visible)
        let that = this;
        switch (this.opciones.accion) {
            case "RADICAR_DOCUMENTO":
                this.datos = JSON.stringify(this.opciones)
                break; 
                
            case "CONSULTA_RADICADO":
                // los datos se pasan desde forma de gestion
                break; 

            case "CONSULTA_GESTION":
                this.datos = JSON.stringify({"datos": this.opciones})
                break; 
            
            default:
                this.datos = this.opciones
                break;
        }       
    },

    data() {
        return {
            popup_visible: ref(false),
            componente_visible: "",
            datos: {}
        }
    }
}

export default ventana;

</script>