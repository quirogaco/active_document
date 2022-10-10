import forma_objeto from '../../../forma/utilidades/forma_objeto.js';

let campos = [
    forma_objeto.campo_objeto({
        'campo'      : 'codigo',
        'obligatorio': 'si'
    }),

    forma_objeto.campo_objeto({
        'campo'      : 'nombre',
        'obligatorio': 'si'
    }),
       
    forma_objeto.select_objeto({
        "campo"      : "departamento_id",
        "titulo"     : "Departamento", 
        "fuente"     : "departamentos",
        'obligatorio': 'si',
        "filtros"    : [["estado_", "=", "ACTIVO"]]
    }),

    forma_objeto.radio_objeto({
        "campo"      : "estado_",
        "titulo"     : "Estado", 
        "elementos"  : ["ACTIVO", "INACTIVO"],        
    })
]

let definicion = {
    'estructura': 'ciudades',
    "titulo"    : "Información de la Ciudad",
    'campos'    : campos,
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;