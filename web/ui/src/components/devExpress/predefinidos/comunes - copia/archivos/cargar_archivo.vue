<template >

    <div class="shadow-sm p-3 mb-3 bg-light rounded">

        <div class="container-fluid ">

            <DxLoadPanel
                v-model:visible = "indicador_visible" 
                message         = "Por favor espere"               
                shading-color   = "rgba(0,0,0,0.4)"
            />

                    <h3 class="fs-3 centered" >{{opciones.atributos.titulo_pantalla}}</h3>
                    <DxScrollView
                        width = "100%"
                        height= "100%"
                    >

                        <DxForm
                            ref        = "forma"
                            id         = "cargar_archivo"                        
                            :form-data = "opciones.datos"
                        >
                            <DxEmptyItem/>

                            <DxSimpleItem
                                data-field      = "archivos" 
                                editor-type     = "dxFileUploader"
                                :label          = "label"
                                :editor-options = "opciones_archivo"
                            >
                                <DxRequiredRule message="Archivo obligatorio"/>                                      
                            </DxSimpleItem>
                        </DxForm>

                    </DxScrollView> 

            <DxToolbar
                ref = "barra"
                :items = "barra_botones"
            />

        </div>  

    </div>  

</template>

<script>
import { DxLoadPanel }    from 'devextreme-vue/load-panel';
import { DxFileUploader } from 'devextreme-vue/file-uploader';
import DxToolbar          from 'devextreme-vue/toolbar'
import { DxScrollView }   from 'devextreme-vue/scroll-view'

import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxButtonItem,
    DxLabel,
    DxRequiredRule
} from 'devextreme-vue/form'

import cargar_archivo_definiciones from './cargar_archivo_definiciones.js'
let nombre = "cargar_archivo"

let cargar_archivo =  {
    name: nombre,

    components: {
        DxFileUploader,     
        // Tarea en ejecución
        DxLoadPanel,

        // Barra       
        DxToolbar,

        // Forma
        DxForm,
        DxSimpleItem,
        DxEmptyItem,
        DxButtonItem,
        DxLabel,

        DxScrollView,

        // Validadores
        DxRequiredRule, 
    },

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {
                    datos    : {},
                    atributos: {
                        titulo_pantalla: "Cargar archivo",
                        titulo_boton   : "Salvar archivo",
                        mensaje_retorno: "Envio de archivo correcto!",

                    }
                }
            }
        },  
    },

    mounted: cargar_archivo_definiciones.montar_componente(nombre),
    methods: cargar_archivo_definiciones.metodos, 

    data() {
        return {  
            // Indicador de tareas
            indicador_visible: false,
            
            // Barra de acciones
            barra_botones: cargar_archivo_definiciones.barra_botones(this),

            // Label
            label: {
                text: this.cargar_label()
            },

            // Opciones del archivo
            opciones_archivo: this.cargar_opciones()
        }
    }
}

export default cargar_archivo;

</script>