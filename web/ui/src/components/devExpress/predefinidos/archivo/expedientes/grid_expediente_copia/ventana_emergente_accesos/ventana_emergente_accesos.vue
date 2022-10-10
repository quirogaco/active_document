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
                    data-field  = "autorizacion"
                    editor-type = "dxRadioGroup"
                    :editor-options = "opciones_autorizacion"
                >
                    <DxLabel text="Autorización"/>
                    <DxRequiredRule message="Autorización obligatoria"/>                                      
                </DxSimpleItem>

                <DxSimpleItem                
                    data-field      = "usuarios"
                    editor-type     = "dxTagBox"
                    :editor-options = "opciones_usuarios"
                >
                    <DxLabel text="Usuarios autorizados"/>
                </DxSimpleItem>

                <DxSimpleItem                
                    data-field      = "grupos"
                    editor-type     = "dxTagBox"
                    :editor-options = "opciones_grupos"
                >
                    <DxLabel text="Grupos autorizados"/>
                </DxSimpleItem>

                <DxEmptyItem/>                

            </DxForm>

            <div class="centered">
                <DxButton
                    @click = "solicitar()"
                    icon   = "fas fa-plus-square"
                    text   = "Asignar accesos"
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

import fuenteDatos from '../../../../../remoto/fuenteDatos.js'

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

            opciones_autorizacion: {
                items : ["RESERVADA", "CLASIFICADA", "PUBLICA"],
                layout: "horizontal"
            },

            opciones_usuarios: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'usuarios', 'usuarios', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },

            opciones_grupos: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'grupo_usuarios', 'grupo_usuarios', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },

            indicador_visible: false
        }
    },

    methods: {
        retorna: function(parametros) {   
                this.opciones.visible = false   
                this.notify("Accesos asignados", "success") 
                this.indicador_visible = false
        },

        solicitar(e) {
            let valido = this.forma.validate().isValid
            let datos  = this.forma.option("formData")
            if ( valido == true) {
                let parametros = {
                    datos       : {
                        "padre_id"      : datos.seleccionados_id[0],
                        "padre_tipo"    : datos.padre_tipo,
                        "autorizacion"  : datos.autorizacion,
                        "usuarios"      : datos.usuarios,
                        "grupos"        : datos.grupos,
                    },
                    accion      : "salvar_acceso"
                }               
            
                let urlCompleta        = window.$direcciones.servidorDatos + '/trd_acciones'   
                this.indicador_visible = true 
                window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna, "")                                      
            }
            else {
                this.notify("Valores invalidos o incompletos", "error")     
            }
        },
    }
}

export default ventana;

</script>