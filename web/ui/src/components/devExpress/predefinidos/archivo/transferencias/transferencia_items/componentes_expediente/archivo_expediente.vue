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
            >

                <DxSimpleItem
                    :visible        = false
                    data-field      = "id"
                >                                     
                </DxSimpleItem>

                <DxSimpleItem                
                    data-field      = "tipo_id"
                    editor-type     = "dxSelectBox"
                    :editor-options = "opciones_tipo"
                >
                    <DxLabel text="Tipo documental"/>
                    <DxRequiredRule message="Tipo es obligatorio"/>
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
                >
                    <DxLabel text="Folios fisicos"/>
                    <DxRequiredRule message="Folios fisicos obligatorio"/>                                      
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
                    data-field  = "soporte"
                    editor-type = "dxRadioGroup"
                    :editor-options = "opciones_soporte"
                >
                    <DxLabel text="Soporte"/>
                    <DxRequiredRule message="Soporte obligatorio"/>                                      
                </DxSimpleItem>

                <DxSimpleItem
                    data-field  = "archivos" 
                    editor-type = "dxFileUploader"
                    :editor-options = "opciones_anexo"
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
import { DxLoadPanel } from 'devextreme-vue/load-panel';
import { DxFileUploader } from 'devextreme-vue/file-uploader';
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

import fuenteDatos  from '../../../../../../../components/devExpress/remoto/fuenteDatos.js';


let tipo_estructura = "archivo_base"

let archivo_base_trd =  {
    name: (tipo_estructura + '_trd'),

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

    mounted: pantalla_comunes.montar_componente(tipo_estructura),
    methods: pantalla_comunes.metodos, 

    data() {
        return {  
            // Opciones editores
            opciones_id: {
                visible: false
            },

            opciones_tipo: {
                dataSource  : fuenteDatos.creaFuenteDatosConsulta('select', null, 'agn_tipo_documental_trd', 'agn_tipo_documental_trd', [], []),
                displayValue: "nombre",
                displayExpr : "nombre",
                searchExpr  : "nombre",
                valueExpr   : "id"
            },

            opciones_fecha: {
                dateSerializationFormat: "yyyy-MM-dd",
                displayFormat          : "yyyy-MM-dd",
                onFocusIn              : function(e) {
                    e.component.open()
                }
            },

            opciones_soporte: {
                items : ["FISICO", "ELECTRONICO"],
                layout: "horizontal"
            },            

            opciones_anexo: {
                selectButtonText: "Seleccione archivo",
                uploadMode      : "useForm"
            },
            
            // GENERALES
            // Indicador de tareas
            indicador_visible: false,
            
            // Barra de acciones
            barra_botones: pantalla_comunes.barra_botones(this)
        }
    }
}

export default archivo_base_trd;

</script>