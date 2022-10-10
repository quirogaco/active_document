import grid_objeto      from '../../grid/utilidades/grid_objeto.js'
import columnas_comunes from '../radicados_comunes/columnas_comunes.js'
import estructuras      from '../../../../librerias/estructuras.js'
import componentes_llamados_crud_comunes from '../../../../librerias/componentes_llamados_crud_comunes.js'

let columnas = [
    columnas_comunes.nro_radicado,
    //columnas_comunes.fecha_radicado,
    columnas_comunes.nombre_completo,
    columnas_comunes.asunto
]

let definicion = {
    'estructura'  : 'radicados_salida',
    'columnas'    : columnas,
    'nombreGrid'  : "ventanilla_salida_grid",
    'nombreLlamar': "ventanilla_salida_forma",
    'titulos'     : {
        'principal': 'Ventanilla Radicación',
        'crear'    : 'Radicar'       
    },
    'metodos'     : {
        'dobleClick': async function(e) {
            let datos = await estructuras.leer_registro_id("radicados_salida", e.data.id)
            console.log(datos)
            componentes_llamados_crud_comunes.llamarComponenteCrud(
                "radicados_salida", 
                "ventanilla_salida_grid", 
                "ventanilla_salida_consulta", 
                datos,  
                "consulta", 
                null);
        } 
    },

}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;