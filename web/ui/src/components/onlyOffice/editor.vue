<template>
    <div id="editorOffice"></div>
</template>

<script>
import {manejo_tipo_archivo} from "./tipo_archivos.js"

export default {
    props: {
        opciones: {
            type: Object,
            default: () => {
                return {}
            }
        }
    },

    data() {
        return {
            tipo_archivo: ''
        }
    },

    mounted() {
        if (this.opciones.lectura_url) {            
            this.configura_editor(this.opciones)
            console.log("EDITOR CARGADO - 02")
        }
    },

    methods: {
        configura_editor(opciones) {
            this.tipo_archivo = manejo_tipo_archivo(opciones.tipo_archivo);
            let configuracion = {
                // Globales    
                "height"      : "100%",
                "width"       : "100%",
                //"token"       : token,
                "token"       : "token",
                "type"        : "desktop",    
                "documentType": 'text',
                
                // Documento configuración
                "document": {
                    "title"     : "Gestión de documento",
                    //"url"       : archivoWord,
                    "url"       : "/lee",
                    //"changesUrl": (opciones.urlSistema + "change_office"),    
                    "changesUrl": "/change_office",     
                    "fileType"  : "docx",      
                    //"key"       : key,
                    "vkey": "abcdefghijb5",
                    "permissions": {
                        "comment": true,
                        "print"  : true
                    },        
                },
            
                "editorConfig": {        
                    "mode"       : "edit",
                    "lang"       : "es",        
                    //"callbackUrl": urlSalvar,
                    "callbackUrl": "/urlSalvar",
                    //"createUrl"  : (opciones.urlSistema + "create_office"),
                    "user"       : {
                        //"id"  : ac_utils.app_values['identity']['id'],
                        //"name": ac_utils.app_values['identity']['nombre']
                        "id"  : 'id',
                        "name": 'nombre'
                    },
                
                    "customization": {
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
                    }
                }
            }

            let documento_editor = new DocsAPI.DocEditor("editorOffice", configuracion);
            console.log("documento_editor:", documento_editor)
        }
    }
};

</script>