import forma_generador_crud from '../../../forma/dinamico_parametros/forma_generador_crud.js';
import fuenteDatos          from '../../../remoto/fuenteDatos.js';

const definicion = {
    "ruta"       : "peticion",
    "id"         : "forma",
    "fuente"     : "peticion",
    "tipofuente" : "remota",
    "titulo"     : "Información del Tipo de Petición",
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
            dataField: "nombre",
            validationRules: [{
                type   : "required",
                message: "Nombre es obligatorio"
            }]
        },

        {
            dataField: "total_dias",            
            editorType: "dxNumberBox",
            label     : {
                text: "Total en dias"
            },
            validationRules: [{
                type   : "required",
                message: "Total dias es obligatorio"
            }]
        },

        {
            dataField: "alertar_dias",            
            label     : {
                text: "Alertar en dias (separe valores por coma)"
            }
        },

        {
            dataField: "alertar_porcentaje",            
            label     : {
                text: "Alertar en porcentaje (separe valores por comas)"
            }
        },

        {
            dataField: "bloquear",            
            editorType: "dxNumberBox",
            label     : {
                text: "Bloquear traslado en dias"
            }
        },

        {
            dataField : "tipo_dias",
            editorType: "dxRadioGroup",
            validationRules: [{
                type   : "required",
                message: "Tipo dias es obligatorio"
            }],
            editorOptions: { 
                items : ["HABILES", "CALENDARIO"],    
                layout: "horizontal",              
            }
        },
    
        {
            dataField : "dependencia_id",            
            editorType: "dxSelectBox",           
            label     : {
                text: "Dependencia asociada"
            },
            editorOptions: { 
                dataSource   : fuenteDatos.creaFuenteDatosUniversal("selectBox", "dependencia_id", "dependencia"),
                searchEnabled: true,
                searchExpr   : "nombre",
                displayExpr  : "nombre",
                valueExpr    : "id",
                value        : "",
                noDataText   : "Sin datos"
            },            
        },

        {
            dataField : "pqrs",
            editorType: "dxCheckBox",           
            label     : {
                text: "Tipo de Petición"
            },
            validationRules: [{
                type   : "required",
                message: "Tipo de Petición es obligatorio"
            }],
            editorOptions: { 
                items : ["PQRSD", "TRAMITE", "DOCUMENTO"],    
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
    
    "elementosBarra": window.$f.componentes_llamados_crud.botonesForma("peticion_forma"),
    
    "metodos": {}
}

let componente = forma_generador_crud.creaComponente(definicion);

export default componente;