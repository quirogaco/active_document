<template >
            <DxForm
                ref             = "forma"
                id              = "forma_atriutos_dinamicos"                
                :form-data      = "opciones.datos"
            >

                <DxSimpleItem
                    data-field  = "titulo"
                    editor-type = "dxTextBox"
                >
                    <DxLabel text="Titulo"/>
                    <DxRequiredRule message="Titulo es obligatorio"/> 
                    <DxStringLengthRule
                        :max="200"
                        message="Maximo 200 caracteres"
                    />                      
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
} from 'devextreme-vue/form';
import DxRadioGroup from 'devextreme-vue/radio-group';
import notify                from 'devextreme/ui/notify'

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

    mounted() {},

    methods: {
        retorna: function() {}
    },

    data() {
        return {  
            // Boton de acción
            boton_opciones: {
                text    : "Aplicar cambios",
                type    : "success",
                disabled: false,
                onClick : () => {
                    window.$_disenador.cambia_grid()
                }
            }
        }
    }
}

export default atributos_campo;

</script>