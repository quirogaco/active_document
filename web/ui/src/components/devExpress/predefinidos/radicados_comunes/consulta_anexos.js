import forma_objeto    from '../../forma/utilidades/forma_objeto.js'
import visores_archivo from "../../../../librerias/visores_archivo.js"

let columnas = [
    {
        'dataField': 'detalle',
        'caption'  : 'Descripción',
        'width'    : 550,
    },
    {
        'dataField': 'tipo_archivo',
        'caption'  : 'Tipo',
        'width'    : 50,
    },
    {
        'dataField': 'creado_en_',
        'caption'  : 'Creado en',
        'width'    : 150,
    },     
    {
        'dataField': 'tamano',
        'caption'  : 'Tamaño bytes',
        'width'    : 100,
    },     
    {
        'dataField': 'folios',
        'caption'  : 'Folios',
        'width'    : 60,
    },  
    {
        'dataField': 'creado_por_nombre',
        'caption'  : 'Creado por',
        'width'    : 300,
    },     
]

let metodos = {
    'dobleClick':  function(e) {
        visores_archivo.ver_descarga_archivo({
            titulo_general: "Consulta de Documentos/Anexos RADICADO",
            archivo_id    : e.data.id, 
            tipo_documento: e.data.tipo_archivo, 
            titulo        : e.data.detalle,
            modo          : "leer",
            descarga      : 'evaluar'
        })               
    } 
}  

// Lista de anexos del radicado
let grid_archivos = forma_objeto.campo_objeto({
    'campo'        : 'archivos',
    'tipo'         : 'dxDataGrid',
    'modo'         : 'grid',
    'titulo'       : '.',
    'tituloVisible': 'no',  
    'registrar'    : 'si',
    'ajustaPalabra': 'si',
    'editor'     : {  
        'columns': columnas,
        'metodos': metodos
    }
})

let grupoArchivos = forma_objeto.grupo_objeto({
    'titulo'   : 'Documento y anexos',
    'elementos': [
        grid_archivos
    ]
})

let grid_anexos = forma_objeto.campo_objeto({
    'campo'        : 'archivos_anexos',
    'tipo'         : 'dxDataGrid',
    'modo'         : 'grid',
    'titulo'       : '.',
    'tituloVisible': 'no',  
    'registrar'    : 'si',
    'ajustaPalabra': 'si',
    'editor'     : {  
        'columns': columnas,
        'metodos': metodos
    }
})

let grupoAnexos = forma_objeto.grupo_objeto({
    'titulo'   : 'Documento y anexos',
    'elementos': [
        grid_anexos
    ]
})

export default {
    grupoAnexos  : grupoAnexos,
    grupoArchivos: grupoArchivos
}