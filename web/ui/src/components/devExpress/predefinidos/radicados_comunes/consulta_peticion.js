import forma_objeto      from '../../forma/utilidades/forma_objeto.js';

let peticion = forma_objeto.mostrar_datos([
    {
        "campo" : "gestion_dependencia_nombre",
        "titulo": "Dependencia responsable"
    },
    {
        "campo" : "gestion_responsable_nombre",
        "titulo": "Funcionario responsable"
    },
    {
        "campo" : "gestion_peticion_nombre",
        "titulo": "Tipo de petición"
    },
    {
        "campo" : "gestion_horas_dias",
        "titulo": "Plazo en dias/horas"
    },
    {
        "campo" : "gestion_total_tiempo",
        "titulo": "Plazo total asignado"
    },
    {
        "campo" : "gestion_prioridad",
        "titulo": "Prioridad"
    },
    {
        "campo" : "reserva",
        "titulo": "Reserva"
    }
])

let grupoPeticion  = forma_objeto.grupo_objeto({
    'titulo'   : 'Petición',
    'elementos': peticion
});

export default {
    grupoPeticion: grupoPeticion
}