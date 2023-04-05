import grid_objeto                  from '../../grid/utilidades/grid_objeto.js'
import gestion_basica_columnas_grid from './gestion_basica_columnas_grid.js'

let definicion = {
    'estructura' : 'peticiones',
    'columnas'   : gestion_basica_columnas_grid.columnas,
    'nombre_grid': 'gestion_basica_grid',
    'adiciona'   : 'no',
    'titulos'    : {
        'principal': 'Peticiones en gestión'
    },

    'eventos': {
        'cargar_datos_antes': function (opciones, idComponente) {
            // Campos adicionales a traer
            let campos = (opciones.campos !== undefined ? opciones.campos : []);   
            if ( !campos.includes("dias_vencimiento") ){
                campos.push("dias_vencimiento")
                opciones.campos = campos;
            }

            
            return opciones;
        },

        'fila_preparada': function (e) {
            /*
            if (e.rowType == 'data' && e.data.estado_vencimiento == "VENCIDO") {  
                e.rowElement.style.backgroundColor = 'red';  
                e.rowElement.className = e.rowElement.className.replace("dx-row-alt", "");  
            } 
            */
        }
    },

    'metodos': {
        'plantilla_columna_estado': function(data) {
            let resultado =  ''
            if (data.value == "TERMINOS") {
                resultado =  '<i class="fas fa-traffic-light" style="color:green"></i> ' + data.value + " (" + data.data.dias_vencimiento + ")"
            }
            else {
                resultado =  '<i class="fas fa-traffic-light" style="color:red"></i> ' + data.value + " (" + data.data.dias_vencimiento + ")"
            }
            
            return resultado
        }
    }
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;