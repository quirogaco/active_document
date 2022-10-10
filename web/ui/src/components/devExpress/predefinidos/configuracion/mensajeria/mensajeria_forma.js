import forma_generador_crud from '../../../forma/dinamico_parametros/forma_generador_crud.js';

const definicion = {
    "ruta"       : "mensajeria",
    "id"         : "forma",
    "fuente"     : "mensajeria",
    "tipofuente" : "remota",
    "titulo"     : "Información de Empresa de mensajeria",
    'campos'     : [
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
    
    "elementosBarra": window.$f.componentes_llamados_crud.botonesForma("mensajeria_forma"),
    
    "metodos": {}
}

let componente = forma_generador_crud.creaComponente(definicion);

export default componente;