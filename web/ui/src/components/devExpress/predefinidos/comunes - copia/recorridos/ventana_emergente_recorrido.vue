<template>
    <DxPopup
        ref                     = "popup"    
        v-model:visible         = "opciones.visible"        
        :drag-enabled           = "false"
        :close-on-outside-click = "true"
        :show-close-button      = "true"
        :show-title             = "true"            
        :width                  = "800"
        :height                 = "300"
        :title                  = "opciones.titulo"            
        :element-attr           = "popupAttributes"
    >        
        <h3 class="fs-3 centered" >{{titulo_pantalla}}</h3>

        <DxScrollView
            width = "100%"
            height= "100%"
        >
            <DxForm
                ref        = "forma"
                id         = "imprime_recorrido"                        
                :form-data = "opciones.datos"
            >
                <DxEmptyItem/>

                <DxSimpleItem 
                    ref             = "plantillas"
                    data-field      = "plantillas_recorridos"
                    editor-type     = "dxSelectBox"
                    :isRequired     = "true"                    
                    :editor-options = "opciones_recorridos"
                >
                    <DxLabel text="Seleccione la plantilla del reporte"/>
                </DxSimpleItem>

                <DxEmptyItem/>

            </DxForm>

            <DxToolbar
                ref = "barra"
                :items = "barra_botones"
            />
        </DxScrollView>  
                                
    </DxPopup>
    
</template>

<script>
import { DxPopup }      from 'devextreme-vue/popup'
import { DxScrollView } from 'devextreme-vue/scroll-view'
import DxToolbar        from 'devextreme-vue/toolbar'
import { 
    DxForm,
    DxSimpleItem,
    DxEmptyItem,
    DxLabel 
}      from 'devextreme-vue/form'

import forma_definiciones from "../../comunes_vue/forma/forma.js"

let ventana_emergente_recorrido =  {
    name: 'ventana_emergente_recorrido',

    components: {
        DxPopup,
        DxScrollView,

        DxForm,
        DxSimpleItem,
        DxEmptyItem,
        DxLabel,
        DxToolbar
    },

    created() {},

    props: {
        opciones: {
            type: Object,
            default: () => {
                return {
                    visible : false,
                    datos   : {},
                    atributos: {}
                }
            }
        }        
    },
    
    mounted() {        
        setTimeout(() => {
            window.$ventana_emergente_recorrido = this
        })
        this.forma      = this.$refs.forma.instance
        this.plantillas = this.$refs.plantillas
        this.leer_plantillas()        
    },

    data() {
        return {            
            titulo_pantalla: "Imprimir recorrido",
            popupAttributes: {
                id   :  'ventana_emergente_archivo',
                class: 'bg_tab_panel'
            },

            // Opciones PLANTILLAS recorridos
            opciones_recorridos: {
                dataSource  : [],
                displayValue: "descripcion",
                displayExpr : "descripcion",
                searchExpr  : "descripcion",
                showClearButton   : true,
                showDropDownButton: true,
                valueExpr   : "id"
            },

            barra_botones: [       
                { 
                    widget  : "dxButton",           
                    options : {
                        icon       : 'fas fa-print',
                        type       : 'success',
                        text       : "Imprimir", 
                        onClick    : this.imprimir,
                    } 
                }
            ]
        }
    },

    methods: {
        imprimir() {
            console.log("IMPRIMIR...")
            let datos_forma   = this.forma.option("formData")
            let datos_validos = this.forma.validate() 
            console.log("FORMA:", datos_forma, datos_validos)
            if (datos_validos.isValid ==  true) {
                let parametros = {
                    "accion": "genera_recorrido",
                    "datos" : datos_forma
                }
                let urlCompleta = window.$direcciones.servidorDatos + '/especifico_acciones'                            
                window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_remoto, "")         
                window.$mostrar_esperar("Por favor espere..")

            }
            else {
                $sistema["notifica"]("Datos invalidos o incompletos !!", "error")
            }            
        },

        retorna_remoto(retorna) {
            let plantillas = retorna.datos.plantillas
            window.$ocultar_esperar()        
            let accion = retorna.accion
            switch (accion) {
                case 'radicar_ventanilla': 
                    break;

                case 'genera_recorrido':
                    break

                default:                   
                    let fuente_datos = forma_definiciones.crea_fuente("select", plantillas)
                    let componente   = this.forma.getEditor("plantillas_recorridos")
                    componente.option("dataSource", fuente_datos)          
                    break;
            }
        },

        leer_plantillas() {
            let parametros = {
                "accion": "listado_plantillas_recorrido",
                "datos" : {}
            }
            let urlCompleta = window.$direcciones.servidorDatos + '/especifico_acciones'                            
            window.$f["http"].llamadoRestPost( urlCompleta, parametros, this.retorna_remoto, "")         
            window.$mostrar_esperar("Por favor espere..")
            
        }
    }
}

export default ventana_emergente_recorrido
</script>