import forma_objeto          from '../../forma/utilidades/forma_objeto.js';

let forma_id = "asignar_pqrs_forma"  

let botones = [
    forma_objeto.boton_objeto({
        'titulo'   : 'Asignar',
        'ancho'    : '50%',
        'evt_click': function() {
            $lib.enviaForma(forma_id, "pqrs_gestion")
        }    
    }),

    forma_objeto.boton_objeto({
        'titulo'    : 'Regresar',
        'tipo'      : 'normal',  
        'ancho'     : '50%', 
        'evt_click' : function() {
            //let forma = window.$ns['asignar_pqrs_forma'];
            window.$router.push({path: "asignar_pqrs_grid"});
        },
    }),
]

let grupoAcciones = forma_objeto.grupo_objeto({
    'expandir' : 2,
    'columnas' : 2,
    'elementos': botones
});

export default {
    grupoAcciones: grupoAcciones
}