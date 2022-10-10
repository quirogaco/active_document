import forma_objeto from '../../../forma/utilidades/forma_objeto.js';

let campos = [
    forma_objeto.campo_objeto({
        'campo'      : 'codigo',
        'titulo'     : 'Codigo dependencia AQ233',
        'obligatorio': 'si'
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'nombre',
        'titulo'     : 'Nombre dependencia DERFF',
        'obligatorio': 'si'
    }),

    forma_objeto.select_objeto({
        "campo"      : "ubicacion_id",
        "obligatorio": "si",
        "titulo"     : "Territorial/Regional", 
        "fuente"     : "ubicaciones",
    }),

    forma_objeto.select_objeto({
        "campo"      : "jefe_id",
        "titulo"     : "Jefe dependencia/Area", 
        "fuente"     : "usuarios",
    }),

    forma_objeto.select_objeto({
        "campo"      : "archivo_id",
        "titulo"     : "Encargado de archivo", 
        "fuente"     : "usuarios",
    }),

    forma_objeto.select_objeto({
        "campo"      : "correspondencia_id",
        "titulo"     : "Encargado de correspondencia", 
        "fuente"     : "usuarios",
    }),

    forma_objeto.select_objeto({
        "campo"      : "pqrs_id",
        "titulo"     : "Encargado de PQRS/TRAMITES", 
        "fuente"     : "usuarios",
    }),

    forma_objeto.tag_objeto({
        "campo"      : "coordinadores_id",
        "titulo"     : "Coordinadores", 
        "fuente"     : "usuarios",
    }),

    forma_objeto.select_objeto({
        "campo"      : "padre_id",
        "titulo"     : "Dependencia padre", 
        "fuente"     : "dependencias",
    }),

    forma_objeto.radio_objeto({
        "campo"      : "estado_",
        "titulo"     : "Estado", 
        "elementos"  : ["ACTIVO", "INACTIVO"],
        //"valor"      : "ACTIVO",    
        'obligatorio': 'si'
    })
]

let definicion = {
    'estructura': 'dependencias',
    "titulo"    : "Información de la Dependencia",
    'campos'    : campos,
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;