<template>
    <div 
        :id="editor_id"
    >
    </div>
</template>

<script>
import librerias from '../../librerias/librerias.js'
import {manejo_tipo_archivo} from "./tipo_archivos.js"
let configuracion = {}
let contador      = 0

export default {
    props: {      
        // Opciones del editor
        opciones: {
            type: Object,
            default: () => {

            }
        },        
    },

    data() {
        return {
            editor_id: "editor_1"
        }
    },

    mounted() {  
        // Configura editor
        if ( (this.opciones.documento) && (this.opciones.documento.lectura_url) ) {        
            this.configura_editor(this.opciones)           
        }
    },

    methods: {
        alto_editor() {
            return Math.trunc( window.innerHeight * 0.75 ).toString() + "px"
        },

        configura_editor(opciones) {     
            let documento = librerias.cargaAtributo(opciones, 'documento', {})
            let editor    = librerias.cargaAtributo(opciones, 'editor', {})
            configuracion = {
                // Globales   
                "documentType": librerias.cargaAtributo(opciones, 'tipo_documento', "word"),                             
                "token"       : librerias.cargaAtributo(opciones, 'id_extendido', "12345678"), 
                "type"        : librerias.cargaAtributo(opciones, 'tipo', "desktop"),  
                //"width"       : librerias.cargaAtributo(opciones, 'ancho', "1150px"), 
                "width"       : "100%",        

                //"width"     : "1450px",             
                //"height"      : librerias.cargaAtributo(opciones, 'alto', "500px"),  
                //"height"      : alto,   
                "height"      : this.alto_editor(),                    
                
                // Documento configuración
                "document": {
                    "fileType"   : librerias.cargaAtributo(documento, 'tipo_archivo', "docx"), 
                    "key"        : librerias.cargaAtributo(opciones, 'id_extendido', "abcdefghijb5"),
                    "title"      : librerias.cargaAtributo(documento, 'titulo', "Manejo de documento"), 
                    "url"        : librerias.cargaAtributo(documento, 'lectura_url', "/lee_$$$"),
                    "permissions": librerias.cargaAtributo(documento, 'permisos', {}),
                },

                "editorConfig": {        
                    "callbackUrl": librerias.cargaAtributo(editor, 'salvar_url', "/salvar_$$$"),   
                    "lang"       : librerias.cargaAtributo(editor, 'lenguaje', "es"),
                    "mode"       : librerias.cargaAtributo(editor, 'modo', "view"), // view
                    "location"   : "",                 
                    "user"       : {
                        "id"  : 'id',
                        "name": 'nombre'
                    },
                
                    "customization": librerias.cargaAtributo(editor, 'personalizacion', {
                        "chat"             : false,
                        "comments"         : true,
                        "zoom"             : 100,
                        "compactToolbar"   : false,
                        "compactHeader"    : true,
                        "goback"           : false,
                        "help"             : false,
                        "leftMenu"         : false,
                        "rightMenu"        : false,
                        "toolbar"          : true,
                        "header"           : true,
                        "statusBar"        : true,
                        "autosave"         : true,
                        "forcesave"        : true,
                        "commentAuthorOnly": false,
                        "showReviewChanges": false
                    })
                }
            }
            //console.log("configuracion---+++:", configuracion)
            let documento_editor = new DocsAPI.DocEditor(this.editor_id, configuracion)
        },

        mostrar_editor(opciones) {
            this.configura_editor(opciones)
        }
    }

}

</script>