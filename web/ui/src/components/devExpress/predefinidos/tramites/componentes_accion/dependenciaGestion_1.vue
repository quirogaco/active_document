<template >
    <div class="">

        <div class="full-width-content ">
            <div class="dx-fieldset">

                <div class="dx-field">
                    <div class="dx-field-label">Dependencia:</div>
                    <div class="dx-field-value">
                        <DxSelectBox
                            :data-source    = "fuente"
                            v-model:value   = "dependencia"
                            display-expr    = "nombre_completo"
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

let dependencia_gestion =  {
    name: 'dependencia_gestion',
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
            let acciones_grid = ["TRASLADAR_DEPENDENCIA"]
            let grid          = window.$grid_gestion   
            if (acciones_grid.indexOf(this.datos.accion) > -1) {
                grid.refresh()    
                this.$router.push({path: "gestion_basica_grid"})
            }
            this.$parent.$parent.$_instance.hide()
        }
    },

    data() {
        return {
            indicador_visible: false,
            fuente         : fuenteDatos.creaFuenteDatosUniversal("select", "dependencia", "dependencias", null, [], []),
            comentario     : null,
            dependencia    : null,
            accion_opciones: {
                text: this.datos.boton_mensaje,
                type: "success",
                onClick: () => {
                    if ( (this.comentario == null) || (this.comentario == "") || (this.dependencia == null) ) {
                        notify(
                            {
                                message: "Comentario y dependencia son obligatorios",                             
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
                            comentario : this.comentario,
                            dependencia: this.dependencia,
                            peticiones : this.datos.elementos,
                            accion     : this.datos.accion
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

export default dependencia_gestion;

</script>