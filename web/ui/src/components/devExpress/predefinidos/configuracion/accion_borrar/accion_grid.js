import grid_generador_crud from '../../../grid/dinamico_parametros/grid_generador_crud.js';

let elemento = "accion"
const definicion = {
    "ruta"       : elemento,
    "id"         : "grid",
    "fuente"     : elemento,
    "tipofuente" : "remota",

    'columnas'   : [
        {
            dataField     : "codigo",
            caption       : "Codigo",
            width         : 400,
            allowSorting  : true,        
            allowFiltering: true,
        },
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
        window.$f.componentes_llamados_crud.tituloCrud("Manejo de Acciones del Sistema"),
        window.$f.componentes_llamados_crud.botonCrud(
            'Crear Acción del Sistema', 
            'accion', 
            'accion_grid', 
            'accion_forma',         
            { "estado_"     : "ACTIVO" }
        )
    ],

    "metodos": {
        dobleClick: window.$f.componentes_llamados_crud.dobleClickGrid('accion', 'accion_grid', 'accion_forma'),       
    }
}

let componente = grid_generador_crud.creaComponente(definicion);

export default componente;