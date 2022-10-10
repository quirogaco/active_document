import forma_objeto from '../../../forma/utilidades/forma_objeto.js';

let campos = [
    forma_objeto.campo_objeto({
        'campo'      : 'codigo',
        'titulo'     : 'Codigo',
        'obligatorio': 'si'
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'nombre',
        'titulo'     : 'Nombre',
        'obligatorio': 'si'
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'clave',
        'titulo'     : 'Clave',
        'modo'       : 'password',
        'obligatorio': 'si'
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'correo',
        'titulo'     : 'Correo electronico',
        'modo'       : 'email',
        'obligatorio': 'si'
    }),

    forma_objeto.select_objeto({
        "campo"      : "ubicacion_id",
        "titulo"     : "Territorial", 
        "fuente"     : "ubicaciones",
        'obligatorio': 'si',
        "filtros"    : [["estado_", "=", "ACTIVO"]]
    }),

    forma_objeto.select_objeto({
        "campo"      : "dependencia_id",
        "titulo"     : "Dependencia", 
        "fuente"     : "dependencias",
        //'obligatorio': 'si',
        "filtros"    : [["estado_", "=", "ACTIVO"]]
    }),

    forma_objeto.select_objeto({
        "campo"      : "reemplaza_id",
        "titulo"     : "Reemplaza/Encargo", 
        "fuente"     : "usuarios",
        //'obligatorio': 'si',
        "filtros"    : [["estado_", "=", "ACTIVO"]]
    }),

    forma_objeto.tag_objeto({
        "campo"      : "roles_id",
        "titulo"     : "Roles del usuario", 
        "fuente"     : "roles",
    }),

    forma_objeto.radio_objeto({
        "campo"      : "estado_",
        "titulo"     : "Estado", 
        "elementos"  : ["ACTIVO", "INACTIVO"],
        'obligatorio': 'si'
    })
]

let definicion = {
    'estructura': 'usuarios',
    "titulo"    : "Información del Usuario",
    'campos'    : campos,
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;