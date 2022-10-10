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
                    <div class="dx-field-label">Seleccione expediente:</div>
                    <div class="dx-field-value">
                        <DxSelectBox
                            :data-source    = "fuente_expediente"
                            v-model:value   = "expediente"
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
                    <div class="dx-field-label">Seleccione tipo documental:</div>
                    <div class="dx-field-value">
                        <DxSelectBox
                            :data-source    = "fuente_tipo_documental"
                            v-model:value   = "tipo_documental"
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
            indicador_visible: false,
            fuente_expediente     : fuenteDatos.creaFuenteDatosUniversal("select", "agn_expedientes_trd",     "agn_expedientes_trd",     null, [], []),
            fuente_tipo_documental: fuenteDatos.creaFuenteDatosUniversal("select", "agn_tipo_documental_trd", "agn_tipo_documental_trd", null, [], []),
            expediente       : null,
            tipo_documental  : null,
            accion_opciones  : {
                text: this.datos.boton_mensaje,
                type: "success",
                onClick: () => {
                    if ( (this.expediente == null) || (this.tipo_documental == null)  ) {
                        notify(
                            {
                                message: "Expediente y tipo documental son obligatorios",                             
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
                            expediente     : this.expediente,
                            tipo_documental: this.tipo_documental,
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