import Guid              from 'devextreme/core/guid'

//  Este es invocado en App.vue y todavia nose carga main.js
let entregar_direccion = function() {
    return "http://" + _ambiente_.CFG_DATA_HOST + ":" + _ambiente_.CFG_DATA_PORT + "/entregar_archivo_parametros/archivo.docx/docx"
}

let salvar_direccion = function() {
    return "http://" + _ambiente_.CFG_DATA_HOST + ":" + _ambiente_.CFG_DATA_PORT + "/salvarOnlyOffice"
}

export default {
    tipo_documento: 'word', // 'cell', 'slide'
    //token         : new Guid().toString(), // Por ahora fijo                    
    tipo          : "desktop",
    ancho         : "1000px",
    alto          : "200px",
    documento     : {
        tipo_archivo: "docx",
        clave       : new Guid().toString(),
        titulo      : "Manejo de documento",
        // Esta esta asociada al documento especifico
        //lectura_url : window.$direcciones.servidorDatos + "/entregar_archivo_parametros/archivo.docx/docx",
        lectura_url : entregar_direccion(),
        permisos    : {
            "comment": true,
            "print"  : true
        }
    },
    editor     : {
        // Esta esta asociada al documento especifico 
        //salvar_url   : window.$direcciones.servidorDatos + "/salvarOnlyOffice",  
        lectura_url : salvar_direccion(),     
        lenguaje     : "es", 
        modo         : "view", // "edit", "view"   
        //region     : "",  
        personalizacion: {
            "chat"             : false,
            "comments"         : true,
            "zoom"             : 200,
            "compactToolbar"   : false,
            "compactHeader"    : true,
            "goback"           : false,
            "help"             : false,
            "leftMenu"         : false,
            "rightMenu"        : false,
            "toolbar"          : true,
            "header"           : true,
            "statusBar"        : true,
            "autosave"         : false,
            "forcesave"        : true,
            "commentAuthorOnly": false,
            "showReviewChanges": false
        }
    }
}