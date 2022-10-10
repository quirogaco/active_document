import forma_objeto from '../../../forma/utilidades/forma_objeto.js';
import ArrayStore from 'devextreme/data/array_store';

let remitenteItems = [
    forma_objeto.campo_objeto({
        'campo'      : 'nombre',
        'titulo'     : 'Nombre',  
        'editable'   : 'no',        
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'nroidentificacion',
        'titulo'     : 'Número de identificación',  
        'editable'   : 'no'            
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'direccion',
        'titulo'     : 'Dirección',   
        'editable'   : 'no'           
    }),
    
    
    forma_objeto.campo_objeto({
        'campo'      : 'correoelectronico',
        'titulo'     : 'Correo electrónico',     
        'editable'   : 'no'         
    }),
    
    forma_objeto.campo_objeto({
        'campo'      : 'telefonofijo',
        'titulo'     : 'Telefono fijo', 
        'editable'   : 'no'             
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'telefonomovil',
        'titulo'     : 'Telefono movil',   
        'editable'   : 'no'           
    }),
]

let grupoRemitente = forma_objeto.grupo_objeto({
    'titulo'     : 'Remitente información',
    'elementos'  : remitenteItems
});


let radicadoItems = [
    forma_objeto.campo_objeto({
        'campo'      : 'id',
        'titulo'     : 'Id registro',     
        'editable'   : 'no',
        'registrar'  : 'si',              
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'nro_radicado',
        'titulo'     : 'Número radicado',     
        'editable'   : 'no',         
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'tipo_radicado',
        'titulo'     : 'Tipo de radicado',   
        'editable'   : 'no'           
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'fecha_radicado',
        'titulo'     : 'Fecha radicado',  
        'editable'   : 'no',
        'registrar'  : 'si',               
    }),
    
    forma_objeto.campo_objeto({
        'campo'      : 'fecha_documento',
        'titulo'     : 'Fecha documento',   
        'editable'   : 'no'           
    }),
    
    forma_objeto.campo_objeto({
        'campo'      : 'folios',
        'titulo'     : 'Folios',        
        'editable'   : 'no'      
    }),

    
    forma_objeto.campo_objeto({
        'campo'      : 'asunto_form_web',        
        'titulo'     : 'Tema',     
        'editable'   : 'no'         
    }),
]

let grupoRadicado = forma_objeto.grupo_objeto({
    'titulo'     : 'Radicado información',    
    'elementos'  : radicadoItems
});

// Lista de logs del radicado
let grid_logs = forma_objeto.campo_objeto({
    'campo'        : 'logs',
    'tipo'         : 'dxDataGrid',
    'modo'         : 'grid',
    'titulo'       : '',  
    'tituloVisible': 'no',  
    'expandir'     : 2,
    'registrar'    : 'si',
    'ajustaPalabra': 'si',
    'editor'     : {      
        'columns': [
            {
                'dataField': 'fecha',
                'caption'  : 'Fecha',
                'width'    : 150,
            },
            {
                'dataField': 'accionante',
                'caption': 'De',
                'width'  : 230,
            },
            {
                'dataField': 'destinatario',
                'caption': 'Para',
                'width'  : 230,
            },
            {
                'dataField': 'descripcion',
                'caption': 'Descripción',
                'width'  : 340,
            },
            {
                'dataField': 'tipo_accionante',
                'caption': 'Tipo usuario',
                'width'  : 130,
            },
            {
                'dataField': 'estado',
                'caption': 'Estado',
                'width'  : 130,
            }
        ]
    }
});

let grupoLog = forma_objeto.grupo_objeto({
    'titulo'     : 'Registro Historico',
    'expandir'   : 2,
    'elementos'  : [grid_logs]
});

// Lista de anexos del radicado
let grid_anexos = forma_objeto.campo_objeto({
    'campo'        : 'anexos',
    'tipo'         : 'dxDataGrid',
    'modo'         : 'grid',
    'titulo'       : '..',
    'tituloVisible': 'no',  
    'expandir'     : 2,    
    'registrar'    : 'si',
    'ajustaPalabra': 'si',
    'editor'     : {      
        'columns': [
            {
                'dataField': 'fecha',
                'caption'  : 'Fecha',
                'width'    : 150,
            },
            {
                'dataField': 'accionante',
                'caption'  : 'Usuario',
                'width'    : 730,
            },
            {
                'dataField': 'tipo_documento',
                'caption'  : 'Tipo documento',
                'width'    : 150,
            },
            {
                'dataField': 'tipo_archivo',
                'caption'  : 'Tipo archivo',
                'width'   : 150,
            }
        ],

        'metodos': {
            'dobleClick':  function(e) {                
                console.log("anexos:", e.data)     
                let id_completo = e.data.idRadicado + "_" + e.data.fechaRadicado + "_" + e.data.id 
                
                // Datos especificos del visor
                let datos  = {
                    mostrar    : true, 
                    idArchivo  : id_completo,
                    operacion  : 'pqrs',
                    clase      : 'archivo', 
                    descarga   : 'evaluar', 
                    buscarTexto: "",
                    datos      : e.data
                }   
                
                // Parametros generales
                let parametros = {
                    'tipo_documento': e.data.tipo_archivo,
                    'modo'          : 'lectura',
                    'clase'         : 'sistema',
                    'datos'         : datos,                
                }

                // Llama rutina general
                window.$emitter.emit('mostrar_archivo', parametros)          
                
            } 
        },
    }
});

let grupoAnexo = forma_objeto.grupo_objeto({
    'titulo'     : 'Archivos anexos',
    'expandir'   : 2,
    'elementos'  : [grid_anexos]
});

let campos = [    
    grupoRadicado,
    grupoRemitente,
    forma_objeto.campo_objeto({
        'campo'      : 'asunto',
        'tipo'       : 'dxTextArea',
        'titulo'     : 'Detalle',  
        'expandir'   : 2,
        'alto'       : '150px',
    }),

    grupoAnexo,
    grupoLog,    
]

let definicion = {
    'estructura'   : 'radicado_pqr',
    "titulo"       : "Información del Radicado PQRS",
    'campos'       : campos,
    //'ajustaPalabra': 'si',
    //'lectura'   : 'si',
    'columnas'  : 2,
    'botones'   : {
        crea    : false, 
        modifica: false, 
        elimina : false, 
        regresa : true
    },
    "metodos"   : {
        "cambiaDatosEvento": function(forma, datos) {
            // Grid de logs
            window.scroll(0,0);
            let gridLog   = window.$ns["radicado_pqr_forma_logs"]
            let datosLog  = datos["logs"];            
            let fuenteLog = new ArrayStore({
                data: datosLog,
                key : 'id'
            })
            gridLog.option('dataSource', fuenteLog);
            
            // Grid de anexos
            let gridAnexo   = window.$ns["radicado_pqr_forma_anexos"]
            let datosAnexo  = datos["anexos"];            
            let fuenteAnexo = new ArrayStore({
                data: datosAnexo,
                key : 'id'
            })
            gridAnexo.option('dataSource', fuenteAnexo);
        }
    }
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;