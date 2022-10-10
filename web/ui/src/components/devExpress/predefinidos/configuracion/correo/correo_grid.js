import grid_generador_crud from '../../../grid/dinamico_parametros/grid_generador_crud.js';

let elemento = "correo"
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
            dataField     : "correo",
            caption       : "Correo",            
            allowSorting  : true,        
            allowFiltering: true,
        },

        {
            dataField     : "url_enlace",
            caption       : "Url de enlace",
            width         : 200,
            allowSorting  : true,        
            allowFiltering: true,
        },
    ],
    
    "elementosBarra": [
        window.$f.componentes_llamados_crud.tituloCrud("Manejo de Cuentas de Correo"),
        window.$f.componentes_llamados_crud.botonCrud(
            'Crear  Cuentas de Correo', 
            'correo',
            'correo_grid', 
            'correo_forma',             
            { "estado_"     : "ACTIVO" }
        )
    ],

    "metodos": {
        dobleClick: window.$f.componentes_llamados_crud.dobleClickGrid('correo', 'correo_grid', 'correo_forma'),
    }
}

let componente = grid_generador_crud.creaComponente(definicion);

export default componente;