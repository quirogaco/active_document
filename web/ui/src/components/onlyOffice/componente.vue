<!--
 * @Author: zhengxiaoxiao
 * @Date: 2020-06-18 15:38:59
   * @Description: Monitor report
-->
<template>

    <div class="editor"> 
        <div class="office">
            <editor :opciones="opciones"></editor>
        </div>
    </div>

</template>

<script>
    import editor         from "./editor.vue"

    export default {
        components: {                       
            editor        
        },

        data() {
            return {
                opciones: {
                    // Documento
                    documento: {
                        ancho   : "100%",
                        alto    : "800px",
                    },                    


                    salvar_url  : "http://192.168.0.6:9100/salvarOnlyOffice",
                    lectura_url : "http://192.168.0.6:9100/entregar_archivo_parametros/archivo.docx/docx",
                    edita       : false,
                    tipo_archivo: "docx",
                    titulo      : "Editor de prueba"
                }
            }
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                //console.log("CARGADO EDITOR")
            }            
        }
    }
</script>