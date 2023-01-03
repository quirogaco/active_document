import grid_objeto      from '../../grid/utilidades/grid_objeto.js'
import columnas_comunes from '../radicados_comunes/columnas_comunes.js'
import estructuras      from '../../../../librerias/estructuras.js'
import componentes_llamados_crud_comunes from '../../../../librerias/componentes_llamados_crud_comunes.js'

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
    'nombreGrid'  : "pqrs_radicado_grid",
    'nombreLlamar': "pqrs_radicado_forma",
    'titulos'     : {
        'principal': 'PQRSD Radicación',
        'crear'    : 'Radicar'       
    },
    'metodos'     : {
        'dobleClick': async function(e) {
            let datos = await estructuras.leer_registro_id("radicados_entrada", e.data.id)
            //console.log("CONSLAU ´´rqrsdefgg")
            console.log(datos)
            componentes_llamados_crud_comunes.llamarComponenteCrud(
                "radicados_entrada", 
                "pqrs_radicado_grid", 
                "ventanilla_radicado_consulta", 
                datos,  
                "consulta", 
                null);
        } 
    },

}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;