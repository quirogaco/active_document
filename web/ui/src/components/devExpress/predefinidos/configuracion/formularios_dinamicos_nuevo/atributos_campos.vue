<template >
            <DxForm
                ref             = "forma"
                id              = "forma_atriutos_dinamicos"                
                :form-data      = "opciones.datos"
            >

                <DxSimpleItem
                    data-field  = "codigo"
                    editor-type = "dxTextBox"
                >
                    <DxLabel text="Codigo"/>
                    <DxRequiredRule message="Codigo del campo"/>   
                    <DxStringLengthRule
                        :max="30"
                        message="Maximo 30 caracteres"
                    />                 
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "label"
                    editor-type = "dxTextBox"
                >
                    <DxLabel text="Titulo"/>
                    <DxRequiredRule message="Titulo es obligatorio"/> 
                    <DxStringLengthRule
                        :max="200"
                        message="Maximo 200 caracteres"
                    />                      
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "obligatorio"
                    editor-type = "dxRadioGroup"                  
                    :editor-options = "opciones_obligatorio"
                >
                    <DxLabel text="Obligatorio" />
                    <DxRequiredRule message="Valor obligatorio" />                                      
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "elementos"
                    editor-type = "dxTextArea"    
                    :visible    = "opciones_elementos.visible"              
                    :editor-options = "opciones_elementos"
                >
                    <DxLabel text="Elementos de selección" />                                  
                </DxSimpleItem>


                <DxEmptyItem/>                

                <DxButtonItem
                    ref = "boton"
                    :button-options      = "boton_opciones"
                    horizontal-alignment = "center"
                />

            </DxForm>

</template>

<script>
import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule
} from 'devextreme-vue/form'
import DxRadioGroup from 'devextreme-vue/radio-group'
import DxTextArea   from 'devextreme-vue/text-area'
import notify       from 'devextreme/ui/notify'

let atributos_campo =  {
    name: 'atributos_campo',

    components: {
        // Forma
        DxForm,
        DxSimpleItem,
        DxEmptyItem,
        DxButtonItem,
        DxLabel,
        DxRadioGroup,
        DxTextArea,

        // Validadores
        DxRequiredRule, 
        DxStringLengthRule,        
    },

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {
                    datos: {}
                }
            }
        },  
    },

    mounted() {        
        // Atributo de campos de seleccíon
        this.opciones_elementos.visible = false        
        let campo            = this.opciones.datos
        let campos_elementos = ["radio", "selector", "selector_multiple"]
        if (campos_elementos.indexOf(campo.tipo) > -1) {
            this.opciones_elementos.visible = true
        }
        window.$editor_atributos = this
    },

    methods: {
        retorna: function() {}
    },

    data() {
        return {  
            opciones_obligatorio: {
                items : ["SI", "NO"],
                layout: "horizontal"
            },

            opciones_elementos: {
                placeholder: "Valores separados por coma",
                visible    : true,
                onFocusOut : function(object) {
                    let elementos = object.component.option("value").split(",")    
                    console.log("onFocusOut-1:", elementos)
                    window.$editor_atributos.opciones.datos.elementos = elementos                                    
                }
            },

            // Boton de acción
            boton_opciones: {
                text    : "Aplicar cambios",
                type    : "success",
                disabled: false,
                onClick : () => {
                    //window.$_disenador.cambia_grid()
                }
            }
        }
    }
}

export default atributos_campo;

</script>