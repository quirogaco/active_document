import forma_objeto from '../../../forma/utilidades/forma_objeto.js';

let campos = [
    forma_objeto.campo_objeto({
        'campo'      : 'nombre',
        'titulo'     : 'Nombre',
        'obligatorio': 'si'
    }),
    
    forma_objeto.radio_objeto({
        "campo"      : "estado_",
        "titulo"     : "Estado", 
        "elementos"  : ["ACTIVO", "INACTIVO"],
        'obligatorio': 'si'
    })
]

let definicion = {
    'estructura': 'empresa_mensajeria',
    "titulo"    : "Empresa de mensajería",
    'campos'    : campos,
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;