<template >

    <div class="shadow-sm p-3 mb-3 bg-light rounded">

        <div class="container-fluid ">

            <DxLoadPanel
                v-model:visible = "indicador_visible" 
                message         = "Por favor espere"               
                shading-color   = "rgba(0,0,0,0.4)"
            />


            <DxForm                       
                ref        = "forma"
                id         = "documento_expediente_base"
                :form-data = "opciones.datos"
                :key       = "forma_key"
                :col-count = "columnas"
            >

                <DxSimpleItem
                    :visible        = false
                    data-field      = "id"
                >                                     
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "soporte"
                    editor-type = "dxRadioGroup"
                    :editor-options = "opciones_soporte"
                >
                    <DxLabel text="Soporte"/>
                    <DxRequiredRule message="Soporte obligatorio"/>                                      
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "detalle"
                    editor-type = "dxTextBox"
                >
                    <DxLabel text="Descripción"/>
                    <DxRequiredRule message="Descripción es obligatorio"/> 
                    <DxStringLengthRule
                        :max="200"
                        message="Maximo 200 caracteres"
                    />                      
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "folios_fisicos"                    
                    editor-type = "dxNumberBox"
                    :isRequired = "opciones_folios.obligatorio"  
                    :visible    = "opciones_folios.visible" 
                    :editor-options = "opciones_folios.editor"  
                >
                    <DxLabel text="Folios fisicos"/>                                                 
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "fecha_creacion"
                    editor-type = "dxDateBox"
                    :editor-options = "opciones_fecha"                   
                >
                    <DxLabel text="Fecha creación"/>
                    <DxRequiredRule message="Fecha es obligatoria"/>                                   
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "archivos" 
                    editor-type = "dxFileUploader"
                    :isRequired = "opciones_anexo.obligatorio"  
                    :visible    = "opciones_anexo.visible" 
                    :editor-options = "opciones_anexo.editor" 
                >
                    <DxLabel text="Archivo electrónico"/>
                    <DxRequiredRule message="Archivo obligatorio"/>                                      
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
import { DxLoadPanel } from 'devextreme-vue/load-panel'
import { DxFileUploader } from 'devextreme-vue/file-uploader'
import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule,
    DxStringLengthRule
} from 'devextreme-vue/form'

import DxToolbar, { DxItem } from 'devextreme-vue/toolbar'
import tvd_pantalla_comunes      from './tvd_pantalla_comunes.js'

import fuenteDatos  from '../../../../../../../components/devExpress/remoto/fuenteDatos.js'


let tipo_estructura = "archivo_base"

let forma =  {
    name: (tipo_estructura + '_tvd'),

    components: {
        DxFileUploader,     
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

    mounted: tvd_pantalla_comunes.montar_componente(tipo_estructura),
    methods: tvd_pantalla_comunes.metodos, 

    data() {
        return {  
            forma_key: 0,
            columnas : 1,

            // Opciones editores
            opciones_id: {
                visible: false
            },

            opciones_soporte: {
                items : ["DIGITALIZADO", "ELECTRONICO", "FISICO"],
                layout: "horizontal",
                required: true,
                onValueChanged: function(obj) {
                    switch (obj.value) {
                        case "FISICO":
                            window.$archivo_expediente_tvd.opciones_anexo.visible  = false
                            window.$archivo_expediente_tvd.opciones_folios.visible = true
                            window.$archivo_expediente_tvd.columnas = 2
                            window.$archivo_expediente_tvd.columnas = 1
                            break  

                        case "ELECTRONICO":
                            window.$archivo_expediente_tvd.opciones_folios.visible = false
                            window.$archivo_expediente_tvd.opciones_anexo.visible  = true
                            window.$archivo_expediente_tvd.columnas = 2
                            window.$archivo_expediente_tvd.columnas = 1
                            break 

                        default:
                            window.$archivo_expediente_tvd.opciones_folios.visible = true
                            window.$archivo_expediente_tvd.opciones_anexo.visible  = true
                            window.$archivo_expediente_tvd.columnas = 2
                            window.$archivo_expediente_tvd.columnas = 1
                            break  
                    }    
                }
            },            

            opciones_folios: {
                visible    : true,
                obligatorio: true
            },

            opciones_fecha: {
                dateSerializationFormat: "yyyy-MM-dd",
                displayFormat          : "yyyy-MM-dd",
                onFocusIn              : function(e) {
                    e.component.open()
                }
            },

            opciones_anexo: {
                visible    : true,
                obligatorio: true,
                editor: {
                    selectButtonText: "Seleccione archivo",
                    uploadMode      : "useForm"
                }
            },
            
            // GENERALES
            // Indicador de tareas
            indicador_visible: false,
            
            // Barra de acciones
            barra_botones: tvd_pantalla_comunes.barra_botones(this)
        }
    }
}

export default forma

</script>