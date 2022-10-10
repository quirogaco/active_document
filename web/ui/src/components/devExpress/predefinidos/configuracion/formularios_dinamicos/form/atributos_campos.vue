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
                    datos: {
                        _campo: {},
                        titulo: ""
                    }
                }
            }
        },  
    },

    mounted() {        
        this.forma    = this.$refs.forma.instance;
        // Atributo de campos de seleccíon        
        this.opciones_elementos.visible = false;
        let campo                       = this.opciones.datos;
        let campos_elementos            = ["radio", "seleccion", "etiqueta"];
        if (campos_elementos.indexOf(campo.tipo) > -1) {
            this.opciones_elementos.visible = true;
        }
        window.$editor_atributos = this;
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
                }
            },

            // Boton de acción
            boton_opciones: {
                text    : "Aplicar cambios",
                type    : "success",
                disabled: false,
                onClick : () => {                    
                    let validacion = this.forma.validate();
                    console.log("this.opciones.datos:", this.opciones.datos)
                    if (validacion.isValid == true) {
                        // Titulo campo
                        this.opciones.datos._campo.label.text = this.opciones.datos.label;
                        // Codigo Campo
                        this.opciones.datos._campo.dataField  = this.opciones.datos.codigo;
                        this.opciones.datos._campo.name       = this.opciones.datos.codigo;
                        // Valor obligatorio
                        if (this.opciones.datos.obligatorio == "SI") {
                            this.opciones.datos._campo.isRequired = true;
                        }
                        else {
                            this.opciones.datos._campo.isRequired = false;
                        }      
                        // Items para campos de selccion
                        let items = [];
                        if (this.opciones.datos.elementos != undefined) {
                            items = this.opciones.datos.elementos.split(",");
                        }
                        this.opciones.datos._campo.editorOptions.items = items; 

                        $forma_diseno.cambia_campo(this.opciones.datos._campo);
                        $forma_diseno.forma_diseno.repaint();
                    }
                    else {
                        let mensaje = "ATRIBUTOS invalidos o incompletos de campo [ " + this.opciones.datos.titulo + " ] !! "
                        $sistema["notifica"](mensaje, "error")
                    }                       
                }
            }
        }
    }
}

export default atributos_campo;

</script>