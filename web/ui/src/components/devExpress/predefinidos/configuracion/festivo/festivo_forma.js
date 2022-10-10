import forma_generador_crud from '../../../forma/dinamico_parametros/forma_generador_crud.js';

const definicion = {
    "ruta"       : "festivo",
    "id"         : "forma",
    "fuente"     : "festivo",
    "tipofuente" : "remota",
    "titulo"     : "Información del Festivo",
    'campos'     : [
        
        {
            dataField: "festivo",
            editorType: "dxDateBox",
            editorOptions: { 
                dateSerializationFormat: "yyyy-MM-dd",
                displayFormat: "yyyy-MM-dd",
            },
            validationRules: [{
                type   : "required",
                message: "Fecha es obligatoria",
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
    
    "elementosBarra": window.$f.componentes_llamados_crud.botonesForma("festivo_forma"),
    
    "metodos": {}
}

let componente = forma_generador_crud.creaComponente(definicion);

export default componente;