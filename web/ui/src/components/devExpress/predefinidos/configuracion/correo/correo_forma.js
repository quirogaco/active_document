import forma_generador_crud from '../../../forma/dinamico_parametros/forma_generador_crud.js';

const definicion = {
    "ruta"       : "correo",
    "id"         : "forma",
    "fuente"     : "correo",
    "tipofuente" : "remota",
    "titulo"     : "Información de Cuenta de Correo",
    'campos'     : [
        {
            dataField: "codigo",
            editorOptions: { 
                width: "50%"
            },
            validationRules: [{
                type   : "required",
                message: "Codigo es obligatorio"
            }]
    
        },

        {
            dataField: "correo",
            label     : {
                text: "Correo electrónico"
            },
            validationRules: [{
                type   : "required",
                message: "Correo es obligatorio"
            }],
            editorOptions: {
                mode: "email"
            }            
        },
        
        {
            dataField: "url_enlace",
            label     : {
                text: "Url de enlace"
            },
            validationRules: [{
                type   : "required",
                message: "Url es obligatorio"
            }]
        },

        {
            dataField: "puerto_enlace",
            label     : {
                text: "Puerto de Url de enlace"
            },
            validationRules: [{
                type   : "required",
                message: "Puerto es obligatorio"
            }]
        },

        {
            dataField: "clave",
            editorOptions: {
                mode: "password"
            }
            
        },
        
        {
            dataField : "tipo_servicio",
            editorType: "dxRadioGroup",
            label     : {
                text: "Tipo de servicio"
            },
            validationRules: [{
                type   : "required",
                message: "Tipo de servicio es obligatorio"
            }],
            editorOptions: { 
                items : ["IMAP", "SMTP"],    
                layout: "horizontal",              
            }
        },
        
        {
            dataField : "estado_",
            editorType: "dxRadioGroup",
            validationRules: [{
                type   : "required",
                message: "Estado es obligatorio"
            }],
            editorOptions: { 
                items : ["ACTIVO", "INACTIVO"],    
                layout: "horizontal",              
            }
        },

    ],
    
    "elementosBarra": window.$f.componentes_llamados_crud.botonesForma("correo_forma"),
    
    "metodos": {}
}

let componente = forma_generador_crud.creaComponente(definicion);

export default componente;