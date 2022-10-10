import grid_generador_crud from '../../../grid/dinamico_parametros/grid_generador_crud.js';

let elemento = "mensajeria"
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
        window.$f.componentes_llamados_crud.tituloCrud("Manejo de Empresa de mensajeria"),
        window.$f.componentes_llamados_crud.botonCrud(
            'Crear Empresa de mensajeria', 
            'mensajeria', 
            'mensajeria_grid', 
            'mensajeria_forma',         
            { "estado_"     : "ACTIVO" }
        )
    ],

    "metodos": {
        dobleClick: window.$f.componentes_llamados_crud.dobleClickGrid('mensajeria', 'mensajeria_grid', 'mensajeria_forma'),       
    }
}

let componente = grid_generador_crud.creaComponente(definicion);

export default componente;