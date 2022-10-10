<template>
        <DxPopup
            ref                     = "popup"    
            v-model:visible         = "opciones.visible"        
            :drag-enabled           = "false"
            :close-on-outside-click = "false"
            :show-close-button      = "true"
            :show-title             = "true"            
            :width                  = "opciones.ancho"
            :height                 = "opciones.alto"
            :title                  = "opciones.titulo"            
            :element-attr           = "popupAttributes"
        >        

            <DxLoadPanel
                v-model:visible = "indicador_visible" 
                message         = "Por favor espere"               
                shading-color   = "rgba(0,0,0,0.4)"
            />


            <DxForm
                ref        = "forma"
                id         = "prestamo_expediente"
                :form-data = "opciones.datos"                
            >

                <DxSimpleItem
                    data-field      = "codigo"
                    editor-type     = "dxTextBox"
                    :visible        = "ver_usuario()"
                    :editor-options = "opciones_codigo"
                >
                    <DxLabel text="Codigo usuario"/>
                    <DxRequiredRule message="Codigo usuario obligatorio"/> 
                    <DxStringLengthRule
                        :max="50"
                        message="Maximo 50 caracteres"
                    />                      
                </DxSimpleItem>

                <DxSimpleItem
                    data-field      = "clave"
                    editor-type     = "dxTextBox"
                    :visible        = "ver_usuario()"
                    :editor-options = "opciones_clave"
                >
                    <DxLabel text="Clave usuario"/>
                    <DxRequiredRule message="Clave usuario obligatoria"/> 
                    <DxStringLengthRule
                        :max="50"
                        message="Maximo 50 caracteres"
                    />                      
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "anotacion"
                    editor-type = "dxTextArea"
                >
                    <DxLabel text="Anotación"/>
                    <DxRequiredRule message="Anotación obligatoria"/> 
                    <DxStringLengthRule
                        :max="256"
                        message="Maximo 200 caracteres"
                    />                      
                </DxSimpleItem>

                negar_prestamo

                <DxEmptyItem/>                

            </DxForm>

            <div class="centered">
                <DxButton
                    @click = "solicitar()"
                    icon   = "fas fa-edit"
                    :text   = "opciones.titulo_boton"
                    type   = "success"  
                />
            </div>

        </DxPopup>

    
</template>

<script>
import { DxButton } from 'devextreme-vue/button'
import { DxLoadPanel } from 'devextreme-vue/load-panel';
import { DxPopup } from 'devextreme-vue/popup'
import { DxScrollView } from 'devextreme-vue/scroll-view'

import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule
} from 'devextreme-vue/form';
import notify from 'devextreme/ui/notify'

let ventana =  {
    name: 'ventana_emergente_prestamo',

    components: {
        DxLoadPanel,
        DxPopup,
        DxScrollView,
        DxButton,
        DxForm,
        DxSimpleItem,
        DxEmptyItem,
        DxButtonItem,
        DxLabel,
        DxRequiredRule,
        DxStringLengthRule
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

    mounted() {    
        this.forma             = this.$refs.forma.instance
        this.notify            = notify 
        this.indicador_visible = false
        setTimeout(() => {
            window.$ventana_emergente_prestamo = this
        })
    },

    data() {
        return {
            popupAttributes: {
                id: 'ventana_emergente_prestamo',
                class: 'bg_tab_panel'
            },

            opciones_codigo: {

            },

            opciones_clave: {
                mode: "password"
                
            },

            indicador_visible: false
        }
    },

    methods: {
        retorna: function(parametros) {   
                this.opciones.visible = false   
                this.notify("Accion realizada correctamente", "success") 
                this.indicador_visible = false
        },

        solicitar(e) {
            let valido = this.forma.validate().isValid
            let datos  = this.forma.option("formData")
            if ( valido == true) {
                let parametros = {
                    datos       : {
                        "prestamos_id": datos.prestamos_id,
                        "usuario"     : datos.usuario,
                        "clave"       : datos.clave,
                        "anotacion"   : datos.anotacion
                    },
                    accion      : this.opciones.accion
                }               
            
                let urlCompleta        = window.$direcciones.servidorDatos + '/trd_acciones'   
                this.indicador_visible = true 
                window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")                                      
            }
            else {
                this.notify("Valores invalidos o incompletos", "error")     
            }
        },

        ver_usuario() {
            let visible = true
            if (this.opciones.accion == "negar_prestamo") {
                visible = false
            }
            console.log(">>>", this.opciones.accion, visible)
            
            return visible
        }
    }
}

export default ventana;

</script>