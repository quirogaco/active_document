import grid_generador_crud from '../../../grid/dinamico_parametros/grid_generador_crud.js';

let elemento = "motivos_devolucion"
const definicion = {
    "ruta"       : elemento,
    "id"         : "grid",
    "fuente"     : elemento,
    "tipofuente" : "remota",

    'columnas'   : [
        {
            dataField     : "nombre",
            caption       : "Nombre",
            allowFiltering: true,
        },

        {
            dataField     : "estado_",
            caption       : "Estado",
            width         : 100,
            allowFiltering: true,
            allowGrouping : true,
        }
    ],
    
    "elementosBarra": [
        window.$f.componentes_llamados_crud.tituloCrud("Manejo de Motivos de Devolución de Correspondencia"),
        window.$f.componentes_llamados_crud.botonCrud(
            'Crear Motivos de Devolución de Correspondencia', 
            'motivo_devolucion', 
            'motivo_devolucion_grid', 
            'motivo_devolucion_forma',         
            { "estado_"     : "ACTIVO" }
        )
    ],

    "metodos": {
        dobleClick: window.$f.componentes_llamados_crud.dobleClickGrid('motivos_devolucion', 'motivo_devolucion_grid', 'motivo_devolucion_forma'),       
    }
}

let componente = grid_generador_crud.creaComponente(definicion);

export default componente;