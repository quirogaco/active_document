<template >

    <div class="bg_tab_panel">

        <div class="full-width-content ">

            <DxLoadPanel
                v-model:visible = "indicador_visible" 
                message         = "Por favor espere"               
                shading-color   = "rgba(0,0,0,0.4)"
            />


            <DxForm
                ref        = "forma"
                id         = "subserie_tvd"
                :form-data = "opciones.datos"
            >

                <DxSimpleItem
                    :visible        = false
                    data-field      = "id"
                >                                     
                </DxSimpleItem>

                <DxSimpleItem
                    data-field      = "padre_id"
                    :visible        = false
                >                                     
                </DxSimpleItem>

                <DxSimpleItem
                    data-field      = "padre_tipo"
                    :editor-options = "opciones_padre_tipo"
                >
                    <DxLabel text="Padre tipo"/>                                   
                </DxSimpleItem>

                <DxSimpleItem
                    data-field      = "padre_nombre"
                    :editor-options = "opciones_padre_nombre"
                >
                    <DxLabel text="Padre nombre"/>                                   
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "codigo"
                    editor-type = "dxTextBox"
                >
                    <DxLabel text="Codigo"/>
                    <DxRequiredRule message="Codigo es obligatorio"/>   
                    <DxStringLengthRule
                        :max="30"
                        message="Maximo 30 caracteres"
                    />                 
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "nombre"
                    editor-type = "dxTextBox"
                >
                    <DxLabel text="Nombre"/>
                    <DxRequiredRule message="Nombre es obligatorio"/> 
                    <DxStringLengthRule
                        :max="200"
                        message="Maximo 200 caracteres"
                    />                      
                </DxSimpleItem>
                
                <DxSimpleItem
                    data-field  = "central"
                    editor-type = "dxNumberBox"
                >
                    <DxLabel text="Años en central"/>
                    <DxRequiredRule message="Valor obligatorio"/>                                      
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "eliminacion"
                    editor-type = "dxRadioGroup"
                    :editor-options = "opciones_eliminacion"
                >
                    <DxLabel text="Eliminación"/>
                    <DxRequiredRule message="Valor obligatorio"/>                                      
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "seleccion"
                    editor-type = "dxRadioGroup"
                    :editor-options = "opciones_seleccion"
                >
                    <DxLabel text="Selección"/>
                    <DxRequiredRule message="Valor obligatorio"/>                                      
                </DxSimpleItem>
                
                <DxSimpleItem
                    data-field  = "conservacion"
                    editor-type = "dxRadioGroup"
                    :editor-options = "opciones_conservacion"
                >
                    <DxLabel text="Conservación"/>
                    <DxRequiredRule message="Valor obligatorio"/>                                      
                </DxSimpleItem>
        
                <DxSimpleItem
                    data-field  = "micro_digitalizacion"
                    editor-type = "dxRadioGroup"
                    :editor-options = "opciones_micro_digitalizacion"
                >
                    <DxLabel text="Microfilmación/Digitalización"/>
                    <DxRequiredRule message="Valor obligatorio"/>                                      
                </DxSimpleItem>
            
                <DxEmptyItem/>
                <DxEmptyItem/>                
            </DxForm>

            <DxToolbar
                ref = "barra"
                :items = "barra_botones"
            />

        </div>  

    </div>  

</template>

<script>
import { DxLoadPanel } from 'devextreme-vue/load-panel';
import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule
} from 'devextreme-vue/form';


import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import pantalla_comunes      from './pantalla_comunes.js'

let tipo_estructura = "subserie"

let subserie_tvd =  {
    name: (tipo_estructura + '_tvd'),

    components: {
        // Tarea en ejecución
        DxLoadPanel,

        // Barra       
        DxItem,
        DxToolbar,

        // Forma
        DxForm,
        DxSimpleItem,
        DxEmptyItem,
        DxButtonItem,
        DxLabel,

        // Validadores
        DxRequiredRule, 
        DxStringLengthRule,        
    },

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {}
            }
        },  
    },

    mounted: pantalla_comunes.montar_componente(tipo_estructura),
    methods: pantalla_comunes.metodos, 

    data() {
        return {  
            // Opciones editores
            opciones_padre_nombre: {
                disabled: true
            },

            opciones_padre_tipo: {
                disabled: true
            },

            opciones_padre_id: {
                visible: false
            },

            opciones_id: {
                visible: false
            },

            opciones_eliminacion: {
                items : ["SI", "NO"],
                layout: "horizontal"
            },

            opciones_seleccion: {
                items : ["SI", "NO"],
                layout: "horizontal"
            },

            opciones_conservacion: {
                items : ["SI", "NO"],
                layout: "horizontal"
            },

            opciones_micro_digitalizacion: {
                items : ["SI", "NO"],
                layout: "horizontal"
            },
            
            // GENERALES
            // Datos tvd
            tvd_id : "",

            // Indicador de tareas
            indicador_visible: false,
            
            // Barra de acciones
            barra_botones: pantalla_comunes.barra_botones(this)
        }
    }
}

export default subserie_tvd;

</script>