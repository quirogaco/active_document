import forma_objeto from '../../../forma/utilidades/forma_objeto.js';
import ArrayStore from 'devextreme/data/array_store';

let destinatarioItems = [
    forma_objeto.campo_objeto({
        'campo'      : 'nit',
        'titulo'     : 'Nit',  
        'editable'   : 'no'      
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'name',
        'titulo'     : 'Entidad',  
        'editable'   : 'no'      
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'sender',
        'titulo'     : 'Destinatario',  
        'editable'   : 'no'      
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'address',
        'titulo'     : 'Dirección',  
        'editable'   : 'no'            
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'phone',
        'titulo'     : 'Telefono',   
        'editable'   : 'no'           
    }),
    
    
    forma_objeto.campo_objeto({
        'campo'      : 'email',
        'titulo'     : 'Correo electrónico',     
        'editable'   : 'no'         
    }),
    
    forma_objeto.campo_objeto({
        'campo'      : 'cargo',
        'titulo'     : 'Cargo', 
        'editable'   : 'no'             
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'ciudad_name',
        'titulo'     : 'Ciudad',   
        'editable'   : 'no'           
    }),
]

let grupoDestinatario = forma_objeto.grupo_objeto({
    'titulo'     : 'Destinatario información',
    'elementos'  : destinatarioItems
});


let radicadoItems = [
    forma_objeto.campo_objeto({
        'campo'      : 'radicado_en',
        'titulo'     : 'Territorial',     
        'editable'   : 'no',         
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'nro_radicado',
        'titulo'     : 'Número radicado',     
        'editable'   : 'no',         
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'fecha_radicado',
        'titulo'     : 'Fecha radicado',  
        'editable'   : 'no'            
    }),
    
    
    forma_objeto.campo_objeto({
        'campo'      : 'nro_origen',
        'titulo'     : 'Radicado de origen',   
        'editable'   : 'no'           
    }),
    
    forma_objeto.campo_objeto({
        'campo'      : 'nro_guia',
        'titulo'     : 'Númerode guia',        
        'editable'   : 'no'      
    }),
    
    forma_objeto.campo_objeto({
        'campo'      : 'anexos',        
        'titulo'     : 'Anexos',     
        'editable'   : 'no'         
    }),
]

let grupoRadicado = forma_objeto.grupo_objeto({
    'titulo'     : 'Radicado Salida información',    
    'elementos'  : radicadoItems
});


let tramiteItems = [
    forma_objeto.campo_objeto({
        'campo'      : 'area_sender_name',
        'titulo'     : 'Dependencia remitente',     
        'editable'   : 'no',         
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'sender_name',
        'titulo'     : 'Remitente',  
        'editable'   : 'no'            
    }),
]

let grupoTramite = forma_objeto.grupo_objeto({
    'titulo'     : 'Remitente',    
    'elementos'  : tramiteItems
});

// Lista de anexos del radicado
let grid_anexos = forma_objeto.campo_objeto({
    'campo'        : 'archivos_anexos',
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
                'dataField': 'descripcion',
                'caption'  : 'Descripción',
                'width'    : 320,
            },
            {
                'dataField': 'filetype',
                'caption'  : 'Tipo archivo',
                'width'    : 100,
            }
        ],

        'metodos': {
            'dobleClick':  function(e) {
                console.log("anexos:", e.data) 
                
                // Datos especificos del visor
                let datos  = {
                    mostrar    : true, 
                    idArchivo  : e.data.id,
                    operacion  : 'ventanilla_entrada',
                    clase      : 'archivo', 
                    descarga   : 'evaluar', 
                    buscarTexto: "",
                    datos      : e.data
                }   
                
                // Parametros generales
                let parametros = {
                    'tipo_documento': e.data.filetype,
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
    grupoDestinatario,
    forma_objeto.campo_objeto({
        'campo'      : 'asunto',
        'tipo'       : 'dxTextArea',
        'titulo'     : 'Asunto',  
        'expandir'   : 2,
        'alto'       : '80px',
    }),
    grupoTramite,
    grupoAnexo,          
]

let definicion = {
    'estructura'   : 'salidas_ventanilla',
    "titulo"       : "Información del Radicado Salida",
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
            // Grid de anexos
            console.log("datos salida:", datos) // atributos_internos.archivos_anexos
            window.scroll(0,0);
            
            let gridAnexo       = window.$ns["salidas_ventanilla_archivos_anexos"]             
            let datosArchivos   = window.$librerias.cargaAtributo(datos, 'archivos_anexos', []);   
            let archivos_anexos = [];
            let anexo;
            datosArchivos.forEach(function(archivo) {
                archivos_anexos = archivo["versiones"].map(function(version) {
                    version['id']    = version['idFile']  
                    version['fecha'] = archivo['creado_en']   

                    return version
                })
            });

            console.log('archivos_anexos:', archivos_anexos)
            let fuenteAnexo = new ArrayStore({
                data: archivos_anexos,
                key : 'id'
            })
            gridAnexo.option('dataSource', fuenteAnexo);
            
            /*
            // Grid de logs
            let gridLog   = window.$ns["radicado_pqr_logs"]
            let datosLog  = datos["logs"];            
            let fuenteLog = new ArrayStore({
                data: datosLog,
                key : 'id'
            })
            gridLog.option('dataSource', fuenteLog);
            
            // Grid de anexos
            let gridAnexo   = window.$ns["radicado_pqr_anexos"]
            let datosAnexo  = datos["anexos"];            
            let fuenteAnexo = new ArrayStore({
                data: datosAnexo,
                key : 'id'
            })
            gridAnexo.option('dataSource', fuenteAnexo);
            */
        }
    }
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;