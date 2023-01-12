<template >
    
    <DxLoadPanel
        v-model:visible = "indicador_visible" 
        message         = "Por favor espere"               
        shading-color   = "rgba(0,0,0,0.4)"
    />


    <div class=" shadow-lg p-3 bg-light.bg-gradient rounded"> 

        <div class="dx-fieldset">

            <div class="dx-field">
                <div class="dx-field-label">Seleccione plantilla:</div>
                <div class="dx-field-value">
                    <DxSelectBox
                        :data-source    = "fuente"
                        v-model:value   = "plantilla"
                        display-expr    = "descripcion"
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
import DxTextArea      from 'devextreme-vue/text-area'
import DxButton        from 'devextreme-vue/button'
import DxSelectBox     from 'devextreme-vue/select-box'
import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
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

    props: {
        datos: {
            type: Object,
            default: () => {
                return {}
            }
        },  
    },

    methods: {
        retorna: function(parametros) {
            this.indicador_visible = false;
            //window.$pantalla_gestion.opciones_ventana.visible = false;
            window.$ventana_emergente.popup_visible = false;
            window.$pantalla_gestion.carga_borrador(parametros.archivo_id);
        }
    },

    data() {
        return {
            // Indicador de tareas
            indicador_visible: false,

            fuente: fuenteDatos.creaFuenteDatosUniversal(
                "select", 
                "plantillas", 
                "plantillas", 
                null, 
                [], 
                []
            ),
            plantilla: null,
            accion_opciones: {
                text: this.datos.boton_mensaje,
                type: "success",
                onClick: () => {
                    if ( (this.plantilla == null) || (this.plantilla == null) ) {
                        notify(
                            {
                                message: "Plantilla es obligatoria",                             
                                position: {
                                    my: 'center top',
                                    at: 'center top'
                                }
                            },
                            "warning", 
                        )
                    }
                    else {
                        window.$pantalla_gestion.verBorrador     = false
                        window.$pantalla_gestion.borrador_existe = false
                        this.indicador_visible = true
                        let parametros = {
                            plantilla : this.plantilla,
                            peticiones: this.datos.elementos,
                            accion    : this.datos.accion
                        }
                        let urlCompleta = window.$direcciones.servidorDatos + '/gestion_acciones'    
                        window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")              
                    }
                }
            }
        }
    }
}

export default usuario_gestion;

</script>