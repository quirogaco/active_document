import grid_generador_crud from '../../../grid/dinamico_parametros/grid_generador_crud.js';

let elemento = "medio_envio"
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
            dataField     : "interna",
            caption       : "Mensajeria Interna",
            width         : 150,
            allowFiltering: true,
            allowGrouping : true,
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
        window.$f.componentes_llamados_crud.tituloCrud("Manejo de Medios de Envio de Correspondencia"),
        window.$f.componentes_llamados_crud.botonCrud(
            'Crear Medio de Envio de Correspondencia', 
            'medio_envio', 
            'medio_envio_grid', 
            'medio_envio_forma',         
            { "estado_"     : "ACTIVO" }
        )
    ],

    "metodos": {
        dobleClick: window.$f.componentes_llamados_crud.dobleClickGrid('medio_envio', 'medio_envio_grid', 'medio_envio_forma'),       
    }
}

let componente = grid_generador_crud.creaComponente(definicion);

export default componente;