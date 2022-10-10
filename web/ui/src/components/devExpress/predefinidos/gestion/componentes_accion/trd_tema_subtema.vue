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
                    <div class="dx-field-label">Seleccione tema:</div>
                    <div class="dx-field-value">
                        <DxSelectBox
                            :data-source    = "fuente"
                            v-model:value   = "tema"
                            display-expr    = "nombre"
                            value-expr      = "id"
                            :showClearButton = "true"
                        >
                            <DxValidator>
                                <DxRequiredRule />                            
                            </DxValidator>
                        </DxSelectBox>
                        
                    </div>
                </div>

                <div class="dx-field">
                    <div class="dx-field-label">Seleccione subtema:</div>
                    <div class="dx-field-value">
                        <DxSelectBox
                            :data-source    = "fuente"
                            v-model:value   = "subtema"
                            display-expr    = "nombre"
                            value-expr      = "id"
                            :showClearButton = "true"
                        >
                            <DxValidator>
                                <DxRequiredRule />                            
                            </DxValidator>
                        </DxSelectBox>
                        
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
import { DxLoadPanel } from 'devextreme-vue/load-panel'
import DxTextArea from 'devextreme-vue/text-area'
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import DxButton from 'devextreme-vue/button'
import DxSelectBox from 'devextreme-vue/select-box'
import DxValidator, {
    DxRequiredRule,    
} from 'devextreme-vue/validator'
import notify from 'devextreme/ui/notify'
import { locale, loadMessages, formatMessage } from 'devextreme/localization'

import fuenteDatos from '../../../remoto/fuenteDatos.js'

let usuario_gestion =  {
    name: 'usuario_gestion',

    components: {
        DxLoadPanel,
        DxTextArea,
        DxRequiredRule,
        DxValidator,
        DxButton,
        DxSelectBox,
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
            //this.$parent.$_instance.option("disabled", false);
            this.$parent.$parent.$_instance.hide()
        }
    },

    data() {
        return {
            // Indicador de tareas
            indicador_visible: false,

            fuente         : fuenteDatos.creaFuenteDatosUniversal("select", "usuario", "usuarios", null, [], []),
            tema           : null,
            subtema        : null,
            accion_opciones: {
                text: this.datos.boton_mensaje,
                type: "success",
                onClick: () => {
                    if ( (this.tema == null) || (this.subtema == null)  ) {
                        notify(
                            {
                                message: "Tema y subtema son obligatorios",                             
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
                            tema           : this.tema,
                            subtema        : this.subtema,
                            peticiones     : this.datos.elementos,
                            accion         : this.datos.accion
                        }
                        this.indicador_visible = true
                        let urlCompleta = window.$direcciones.servidorDatos + '/gestion_acciones'    
                        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")   
                        this.$parent.$_instance.option("disabled", true);                                          
                    }
                }
            }
        }
    }
}

export default usuario_gestion;

</script>