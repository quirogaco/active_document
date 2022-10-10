import forma_generador_crud from '../../../forma/dinamico_parametros/forma_generador_crud.js';

const definicion = {
    "ruta"       : "medio_envio",
    "id"         : "forma",
    "fuente"     : "medio_envio",
    "tipofuente" : "remota",
    "titulo"     : "Información de Medios de Envio de Correspondencia",
    'campos'     : [
       
        {
            dataField: "nombre",
            validationRules: [{
                type   : "required",
                message: "Nombre es obligatorio"
            }]
        },

        {
            dataField: "interna",
            editorType: "dxRadioGroup",
            editorOptions: { 
                items : ["SI", "NO"],    
                layout:"horizontal"                           
            },
            validationRules: [{
                type   : "required",
                message: "Valor es obligatorio"
            }]
        },

        {
            dataField: "estado_",
            editorType: "dxRadioGroup",
            editorOptions: { 
                items : ["ACTIVO", "INACTIVO"],    
                layout:"horizontal"                           
            }
        },
    ],
    
    "elementosBarra": window.$f.componentes_llamados_crud.botonesForma("medio_envio_forma"),
    
    "metodos": {}
}

let componente = forma_generador_crud.creaComponente(definicion);

export default componente;