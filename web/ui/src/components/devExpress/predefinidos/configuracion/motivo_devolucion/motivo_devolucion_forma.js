import forma_generador_crud from '../../../forma/dinamico_parametros/forma_generador_crud.js';

const definicion = {
    "ruta"       : "motivo_devolucion",
    "id"         : "forma",
    "fuente"     : "motivos_devolucion",
    "tipofuente" : "remota",
    "titulo"     : "Información de Motivos de Devolución de Correspondencia",
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
    
    "elementosBarra": window.$f.componentes_llamados_crud.botonesForma("motivo_devolucion_forma"),
    
    "metodos": {}
}

let componente = forma_generador_crud.creaComponente(definicion);

export default componente;