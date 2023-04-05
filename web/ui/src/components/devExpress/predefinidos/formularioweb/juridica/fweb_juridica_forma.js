import forma_objeto from '../../../forma/utilidades/forma_objeto.js';

let identificacion = [
    forma_objeto.select_objeto({
        "campo"      : "tipo_entidad_id",
        "titulo"     : "Tipo de entidad", 
        "obligatorio": "si",        
        "fuente"     : "tipo_entidad",
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'nombre_entidad',
        'titulo'     : 'Razon social',
        'obligatorio': 'si'
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'nro_identificacion',
        'titulo'     : 'Nit',
        'obligatorio': 'si'
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'nombres',
        'titulo'     : 'Nombres remitente',
        'obligatorio': 'si'
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'apellidos',
        'titulo'     : 'Apellidos remitente',
        'obligatorio': 'si'
    }),
]

let grupoIdentificacion = forma_objeto.grupo_objeto({
    'titulo'     : 'Remitente identificación',
    'elementos'  : identificacion
});



let remitenteUbicacion = [
    forma_objeto.radio_objeto({
        "campo"      : "medio_notificacion",
        "titulo"     : "Medio notificación", 
        "elementos"  : ["CORREO", "DIRECCIÓN FISICA"],
        'obligatorio': 'si'
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'correo',
        'titulo'     : 'Correo electrónico',
        'obligatorio': 'si',
        'modo'       : 'email'
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'direccion',
        'titulo'     : 'Dirección',
        'obligatorio': 'si',
    }),

    forma_objeto.select_objeto({
        "campo"      : "ciudad_id",
        "obligatorio": "si",
        "titulo"     : "Ciudad", 
        "fuente"     : "ciudad",
    }),
]


let grupoUbicacion = forma_objeto.grupo_objeto({
    'titulo'     : 'Remitente ubicación',
    'elementos'  : remitenteUbicacion
});

let asunto = forma_objeto.campo_objeto({
    'campo'      : 'detalle',
    'tipo'       : 'dxTextArea',
    'titulo'     : 'Detalle',  
    'expandir'   : 2,
    'obligatorio': 'si',
    'alto'       : '200'      
});

// CAMPOS ANEXO
let anexos = {
    dataField : "archivo",            
    editorType: "dxFileUploader",
    name      : "archivo",
    obligatorio: 'si',
    label     : {
        text: "Archivos anexos"
    },
    editorOptions: { 
        uploadCustomData           : {
            "datos1": "01",
            "datos2": "02",
        },
        /*
        elementAttr: {
            id  : 'plantilla_archivo',
            name: 'plantilla_archivo',
        },  
        */              
        name                       : "archivos",
        uploadMode                 : "useForm",
        multiple                   : true,
        accept                     : "application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        labelText                  : "O soltar archivo aquí",
        selectButtonText           : "Seleccione archivos anexos",                
        invalidFileExtensionMessage: "El tipo de archivo no está permitido",
        invalidMaxFileSizeMessage  : "El archivo es demasiado grande",
        invalidMinFileSizeMessage  : "El archivo es demasiado pequeño",
        readyToUploadMessage       : "Listo para subir",
        uploadedMessage            : "Subido",
        uploadFailedMessage        : "Subida fallida",
        uploadUrl                  : (window.$direcciones.servidorDatos + "recibirArchivos"), 
        onContentReady             : function(e) {                          
            let componente = e.component;
            window.$ns["plantilla_archivo"] = componente;
        },

    }
}

let campos = [
    // Falta datos de consulta
    grupoIdentificacion,
    grupoUbicacion,
    asunto,
    anexos
]

let definicion = {
    'estructura': 'fweb_juridica',
    "titulo"    : "Radicación Persona JURIDICA",
    'campos'    : campos,
    //'columnas'  : 2,

    //"elementosBarra": window.$f.componentes_llamados_crud.botonesForma("fweb_juridica"),
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;