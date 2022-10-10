<template>

        <DxPopup        
            ref                     = "popup_componente"    
            v-model:visible         = "visible"    
            :drag-enabled           = "false"
            :close-on-outside-click = "true"
            :show-close-button      = "true"
            :show-title             = "true"            
            :width                  = "ancho"
            :height                 = "alto"
            :title                  = "titulo"            
            :element-attr           = "popupAttributes"
        >
            <div class="col-12 shadow p-3 rounded">

                <pdf_componente     
                    ref = "pdf_componente"        
                    :nombrePdf   = "nombrePdf" 
                    :buscarTexto = "buscarTexto" 
                    :operacion   = "operacion" 
                    :clase       = "clase" 
                    :descarga    = "descarga"
                    :datos       = "datos" 
                    :key         = "repintar_pdf" 
                />
                
            </div> 

        </DxPopup> 
    
</template>

<script>    
    import pdf_componente   from './pdf_componente.vue'
    import DxButton         from 'devextreme-vue/button'
    import { DxPopup }      from 'devextreme-vue/popup'
    import { DxScrollView } from 'devextreme-vue/scroll-view'

    import librerias from '../../librerias/librerias.js'

    import { 
        onMounted,    
        getCurrentInstance,
        ref
    } from 'vue'

    export default {
        components: {        
            DxPopup,
            DxButton,
            DxScrollView,
            pdf_componente
        },

        methods: {
            mostrarPdf(e) {                                       
                this.visible      = true
                this.nombrePdf    = e.idArchivo
                this.buscarTexto  = e.buscarTexto
                this.operacion    = e.operacion           
                this.clase        = e.clase
                this.descarga     = e.descarga
                this.titulo       = e.titulo
                this.datos        = librerias.cargaAtributo(e, "datos", {})   
                this.repintar_pdf += 1          
            }
        },

        setup(props, context) {    

            onMounted(() => {                     
                let unoMismo = getCurrentInstance().ctx    
                window.$emitter.on(
                    'mostrar_pdf_sistema', 
                    function(e) {    
                        unoMismo.mostrarPdf(e); 
                    }  
                )                
            }) 

            return { 
                visible     : ref(false),
                repintar_pdf: 0,
                nombrePdf   : ref(''), 
                buscarTexto : ref(''), 
                operacion   : ref(''), 
                clase       : ref(''), 
                descarga    : ref(''),
                datos       : {},
                ancho       : ref("90%"), 
                alto        : ref("90%"), 
                titulo      : ref('Visor de Pdf'), 
                popupAttributes: {
                    id   : 'ventana_emergente_visor_pdf'
                }
            }
        }
    }
</script>