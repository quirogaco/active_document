import grid_generador_crud from '../../../grid/dinamico_parametros/grid_generador_crud.js';

let elemento = "peticion"
const definicion = {
    "ruta"       : elemento,
    "id"         : "grid",
    "fuente"     : elemento,
    "tipofuente" : "remota",

    'columnas'   : [
        {
            dataField     : "codigo",
            caption       : "Codigo",
            width         : 200,
            allowSorting  : true,        
            allowFiltering: true,
        },
        {
            dataField     : "nombre",
            caption       : "Nombre",
            allowFiltering: true,
        },
        {
            dataField     : "pqrs",
            caption       : "PQRS",
            allowFiltering: true,
            width         : 150
        }        
    ],
    
    "elementosBarra": [
        window.$f.componentes_llamados_crud.tituloCrud("Manejo de Tipos de Petición"),
        window.$f.componentes_llamados_crud.botonCrud(
            'Crear Tipo de Peticion', 
            'peticion',
            'peticion_grid', 
            'peticion_forma',             
            { "estado_"     : "ACTIVO" }
        )
    ],

    "metodos": {
        dobleClick: window.$f.componentes_llamados_crud.dobleClickGrid('peticion', 'peticion_grid', 'peticion_forma'),
    }
}

let componente = grid_generador_crud.creaComponente(definicion);

export default componente;