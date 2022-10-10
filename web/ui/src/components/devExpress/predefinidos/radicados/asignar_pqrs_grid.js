import grid_objeto      from '../../grid/utilidades/grid_objeto.js';
import columnas_comunes from '../radicados_comunes/columnas_comunes.js';

let columnas = [
    columnas_comunes.clase_radicado,
    columnas_comunes.canal_medio,   
    columnas_comunes.nro_radicado,
    columnas_comunes.fecha_radicado,
    columnas_comunes.nombre_completo,
    columnas_comunes.asunto,
    columnas_comunes.correo_electronico,
    columnas_comunes.asignado_gestion
]

let definicion = {
    'estructura': 'radicados_entrada',
    'columnas'  : columnas,
    'nombreGrid': "asignar_pqrs_grid",
    "filtros"   : [
        ["gestion_asignada_peticion", "=", "NO"],
        'and',
        ["clase_radicado", "=", "PQRS"]
    ],    
    'titulos'   : {
        'principal': 'Asignación y traslado de PQRS',
        'crear'    : 'Radicar PQRS',        
    },
    'nombreLlamar': "asignar_pqrs_forma"
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;