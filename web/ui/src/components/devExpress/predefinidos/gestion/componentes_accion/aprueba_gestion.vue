<template >

    <DxLoadPanel
        v-model:visible = "indicador_visible" 
        message         = "Por favor espere"               
        shading-color   = "rgba(0,0,0,0.4)"
    />

    <div class="bg_tab_panel">

        <div class="full-width-content ">
            <div class="dx-fieldset">

                <div class="dx-field">
                    <div class="dx-field-label">Comentario:</div>
                    <div class="dx-field-value">
                        <DxTextArea
                            :height       = "90"
                            v-model:value = "comentario"
                        />
                    </div>
                </div>

            </div>

        </div>  

        <DxToolbar>
            <DxItem
                :options = "accion_opciones"
                location = "after"
                widget   = "dxButton"
            />
        </DxToolbar>

    </div>  

</template>

<script>

{/* <div class="dx-field">
                    <div class="dx-field-label">Tipo de Respuesta:</div>
                    <div class="dx-field-value">
                        <DxRadioGroup
                            :items="tipos"     
                            v-model:value = "tipo"                       
                        />
                        
                    </div>
                </div> */}

import { DxLoadPanel } from 'devextreme-vue/load-panel'
import DxTextArea from 'devextreme-vue/text-area'
import DxRadioGroup from 'devextreme-vue/radio-group';
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import DxButton from 'devextreme-vue/button'
import notify from 'devextreme/ui/notify'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'

import fuenteDatos from '../../../remoto/fuenteDatos.js'

let aprueba_gestion =  {
    name: 'aprueba_gestion',

    components: {
        DxLoadPanel,
        DxTextArea,
        DxRadioGroup,
        DxButton,        
        DxToolbar,
        DxItem
    },

    created() {},

    props: {
        datos: {
            type: Object,
            default: () => {
                return {}
            }
        },  
    },

    mounted() {},

    methods: {
        retorna: function() {
            this.indicador_visible = false
            let acciones_grid = ["APROBAR_RADICAR", "ENVIAR_VISTO_BUENO"]
            let grid          = window.$grid_gestion   
            if (acciones_grid.indexOf(this.datos.accion) > -1) {
                this.$router.push({path: "gestion_basica_grid"})
            }
            this.$parent.$parent.$_instance.hide()
        }
    },

    data() {
        return {
            indicador_visible: false,
            fuente         : fuenteDatos.creaFuenteDatosUniversal("select", "usuario", "usuarios", null, [], []),
            tipos          : ['FINAL', 'PARCIAL', 'INCOMPLETA'],
            tipo           : 'FINAL',
            comentario     : "",
            accion_opciones: {
                text: this.datos.boton_mensaje,
                type: "success",
                onClick: () => {
                    if ( (this.comentario == null) || (this.tipo == "") ) {
                        notify(
                            {
                                message: "Comentario y tipo respuesta son obligatorios",                             
                                position: {
                                    my: 'center top',
                                    at: 'center top'
                                }
                            },
                            "warning", 
                        )
                    }
                    else {
                        let parametros = {
                            comentario: this.comentario,
                            tipo      : this.tipo,
                            peticiones: this.datos.elementos,
                            accion    : this.datos.accion
                        };
                        this.indicador_visible = true;
                        let urlCompleta = window.$direcciones.servidorDatos + '/gestion_acciones'; 
                        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "");   
                        this.$parent.$_instance.option("disabled", true);                                          
                    }
                }
            }
        }
    }
}

export default aprueba_gestion;

</script>