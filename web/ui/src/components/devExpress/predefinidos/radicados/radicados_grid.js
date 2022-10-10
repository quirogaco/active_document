import grid_objeto      from '../../grid/utilidades/grid_objeto.js';
import columnas_comunes from '../radicados_comunes/columnas_comunes.js';

let columnas = [
    columnas_comunes.clase_radicado,    
    columnas_comunes.nro_radicado,
    columnas_comunes.fecha_radicado,
    columnas_comunes.nombre_completo,
    columnas_comunes.correo_electronico,
    columnas_comunes.canal_medio,
    columnas_comunes.asunto    
]

let definicion = {
    'estructura'  : 'radicados_entrada',
    'columnas'    : columnas,
    'nombreGrid'  : "radicado_general_grid",
    'nombreLlamar': "radicado_juridica_forma",
    'titulos'   : {
        'principal': 'Radicados de Entrada Persona Juridica',
        'crear'    : 'Radicar Juridica',        
    }   
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;