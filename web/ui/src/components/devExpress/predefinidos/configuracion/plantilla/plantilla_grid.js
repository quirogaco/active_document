import grid_generador_crud from '../../../grid/dinamico_parametros/grid_generador_crud.js';

let elemento = "plantilla"
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
            dataField     : "tipo",
            caption       : "Tipo plantilla",
            width         : 250,
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
        window.$f.componentes_llamados_crud.tituloCrud("Manejo de Plantillas"),
        window.$f.componentes_llamados_crud.botonCrud(
            'Crear Plantillas', 
            'plantilla', 
            'plantilla_grid', 
            'plantilla_forma', 
            {"estado_"     : "ACTIVO" }
        )
    ],

    "metodos": {
        dobleClick:     window.$f.componentes_llamados_crud.dobleClickGrid(elemento, 'plantilla_grid', 'plantilla_forma'),
    }
}

let componente = grid_generador_crud.creaComponente(definicion);

export default componente;