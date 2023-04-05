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

    forma_objeto.tag_objeto({
        "campo"      : "opciones_id",
        "titulo"     : "Opciones del Menu", 
        "fuente"     : "opciones_sistema",
        "busqueda_expresion": "titulo",
        "muestra_expresion" : "titulo",
    }),

    forma_objeto.tag_objeto({
        "campo"      : "acciones_id",
        "titulo"     : "Acciones del Sistema", 
        "fuente"     : "acciones_sistema"
    }),
    
    forma_objeto.radio_objeto({
        "campo"      : "estado_",
        "titulo"     : "Estado", 
        "elementos"  : ["ACTIVO", "INACTIVO"],
        'obligatorio': 'si'
    })
]

let definicion = {
    'estructura': 'roles',
    "titulo"    : "Información del Role",
    'campos'    : campos,
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;