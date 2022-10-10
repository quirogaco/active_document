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
                id         = "dependencia_tvd"
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
                    :visible        = "mostrar_padre()"
                    :editor-options = "opciones_padre_tipo"
                >                                                     
                </DxSimpleItem>

                <DxSimpleItem
                    data-field     = "padre_nombre"
                    :visible       = "mostrar_padre()"
                    editor-options = "opciones_padre_nombre"
                >                               
                </DxSimpleItem>
            
                <DxSimpleItem
                    data-field  = "codigo"
                    editor-type = "dxTextBox"
                >
                    <DxLabel text="Codigo dependencia"/>
                    <DxRequiredRule message="Codigo es obligatorio"/>   
                    <DxStringLengthRule
                        :max="30"
                        message="Maximo 30 caracteres"
                    />                 
                </DxSimpleItem>

                <DxEmptyItem/>

                <DxSimpleItem
                    data-field  = "nombre"
                    editor-type = "dxTextBox"
                >
                    <DxLabel text="Nombre dependencia"/>
                    <DxRequiredRule message="Nombre es obligatorio"/> 
                    <DxStringLengthRule
                        :max="200"
                        message="Maximo 200 caracteres"
                    />                      
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

let tipo_estructura = "dependencia"

let dependencia_tvd =  {
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
            // ESPEFICIFICOS Opciones editores
            opciones_padre_nombre: {
                disabled: true,
                visible : this.mostrar_padre(),
                label   : {
                    text    : "Padre nombre",
                    visible : this.mostrar_padre()
                }
            },

            opciones_padre_tipo: {
                disabled: true,
                visible : this.mostrar_padre(),
                label   : {
                    text    : "Padre tipo",
                    visible : this.mostrar_padre()
                }
            },

            opciones_padre_id: {
                visible: false
            },

            opciones_id: {
                visible: false
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

export default dependencia_tvd;

</script>