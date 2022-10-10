import visores_archivo from "../../../../../librerias/visores_archivo.js"
import grid_objeto     from '../../../grid/utilidades/grid_objeto.js'

let columnas = [
    grid_objeto.columna_texto({
        campo : "ocr",
        titulo: "#",
        ancho : 30,
    }),

    grid_objeto.columna_texto({
        campo : "un_administrativa",
        titulo: "Unidad administrativa",
        ordena: "si",
        filtra: "si",
        ancho : 200,
    }),

    grid_objeto.columna_texto({
        campo : "un_productora",
        titulo: "Unidad productora",
        ordena: "si",
        filtra: "si",
        ancho : 200,
    }),

    grid_objeto.columna_texto({
        campo : "asunto",
        titulo: "Asunto",
        filtra: "si",
        ancho : 700,
    })
]

let definicion = {
    'estructura': 'archivo_historico_migrado',
    'columnas'  : columnas,
    'adiciona'  : 'no',
    'titulos'   : {
        'principal': 'Consulta archivo historico'
    },
    'metodos': {
        'dobleClick':  function(e) {
            let buscar = e.component.option('searchPanel').text;              
            visores_archivo.ver_descarga_archivo({
                archivo_id: e.data.id, 
                operacion : 'historico', 
                buscar    : buscar, 
                titulo    : e.data.asunto,
                //descarga  : 'si', 
            })
        } 
    },

    'eventos': {
        'cargar_datos_antes': function (opciones, idComponente) {
            // Campos adicionales a traer
            let campos = (opciones.campos !== undefined ? opciones.campos : []);   
            if ( !campos.includes("texto_ocr") ){
                campos.push("texto_ocr")
                opciones.campos = campos;
            }

            // Filtros adicionales             
            let grid   = window.$ns[idComponente];
            let buscar = grid.gridInstancia.option('searchPanel').text;                        
            opciones.resaltar = null;
            if ( (buscar != "") && (buscar !== undefined) ) {
                let filtros = (opciones.filter !== undefined ? opciones.filter : []);
                if (filtros.length > 0) {
                    filtros.push("or")
                }
                filtros.push([ "texto_ocr", "contains", buscar ])
                let resaltar = ["texto_ocr"]
                opciones.filter   = filtros;
                opciones.resaltar = resaltar;            
            }

            return opciones;
        },

        'cargar_datos_despues': function (resultado, idComponente) {
            let total = 0;
            let nuevosDatos = resultado.data.map(function(dato) {
                dato['ocr'] = dato._resaltados_.length;
                total      += dato._resaltados_.length;
                return dato
            });
            resultado.data = nuevosDatos;

            let grid = window.$ns[idComponente];
            if (total <= 0) {                                    
                grid.gridInstancia.columnOption('ocr', {'visible': false});
            }
            else {
                grid.gridInstancia.columnOption('ocr', {'visible': true});
            }

            return resultado
        }
    }
}

let componente = grid_objeto.grid_objeto_crud(definicion);

export default componente;