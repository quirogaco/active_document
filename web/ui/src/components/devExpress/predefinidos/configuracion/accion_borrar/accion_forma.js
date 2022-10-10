import forma_generador_crud from '../../../forma/dinamico_parametros/forma_generador_crud.js';

const definicion = {
    "ruta"       : "accion",
    "id"         : "forma",
    "fuente"     : "accion",
    "tipofuente" : "remota",
    "titulo"     : "Información de la Acción",
    'campos'     : [
        {
            dataField: "codigo",
            validationRules: [{
                type   : "required",
                message: "Codigo es obligatorio"
            }]
    
        },
        
        {
            dataField: "nombre",
            validationRules: [{
                type   : "required",
                message: "Nombre es obligatorio"
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
    
    "elementosBarra": window.$f.componentes_llamados_crud.botonesForma("accion_forma"),
    
    "metodos": {}
}

let componente = forma_generador_crud.creaComponente(definicion);

export default componente;