<template>

    <div 
        v-if = "ver_visor"
    >  

        <iframe   
            width   = "100%"    
            :height = "alto"   
            :src    = "getFilePath"            
        >
        </iframe>

    </div>

</template>

<script>

export default {
    name: 'pdf_componente',
    props: {
        // Opciones del editor
        opciones: {
            type: Object,
            default: () => {
                return {                    
                }
            }
        },       

        nombrePdf  : String,

        buscarTexto: {
            type   : String,
            default: ""            
        },
        
        operacion  : {
            type   : String,
            default: "sistema"            
        },
        
        clase      : {
            type   : String,
            default: "sistema"            
        },
        
        descarga   : {
            type   : String,
            default: "sistema"            
        },
        
        datos      : {
            type   : Object,
            default: {}           
        },
        
        ruta     : {
            type   : String,
            default: "/src/components/pdfjs/pdfjs-2.7.570/web/viewer.html"            
        }
    },

    data() {
        return {
            ver_visor: false,
            alto     : this.alto_visor()
        }
    },

    mounted() {   
        if  ( (this.nombrePdf !== '') && (this.nombrePdf !== undefined) ) {
            this.ver_visor = true
        }
    },

    methods: {
        alto_visor() {
            return Math.trunc( window.innerHeight * 0.75 ).toString() + "px"
        },
    },

    computed:{ 
        getFilePath: function () {
            let urlCompleta = this.ruta
            //if  ( (this.nombrePdf !== '') && (this.nombrePdf !== undefined) ) {
            let ruta_visor = this.operacion + '/' + this.clase + '/' + this.descarga + '/'
            urlCompleta += '?file=' + window.$ruta_pdf + ruta_visor + this.nombrePdf + '?_=' + Date.now()// + "#page=1#zoom=150"; 
            if ( (this.buscarTexto !== undefined) && ((this.buscarTexto != "")) ) {
                urlCompleta += "#search=" + this.buscarTexto
            }                                                         
            //}

            return urlCompleta 
        }
    }
}
</script>