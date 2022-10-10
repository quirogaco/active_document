import librerias           from '../../../../librerias/librerias.js';
import grid_columna        from './grid_columna.js';
import grid_generador_crud from '../dinamico_parametros/grid_generador_crud.js';

// Define y crea grid CRUD por atributos
const grid_objeto_crud = function(atributos={}) {
    let estructura   = librerias.cargaAtributo(atributos, "estructura",   "SIN_ESTRUCTURA")  
    let titulos      = librerias.cargaAtributo(atributos, "titulos",      {})  
    let idGrid       =  librerias.cargaAtributo(atributos, "id",          "grid")   
    let tipofuente   = librerias.cargaAtributo(atributos, "tipofuente",   "remota")
    let columnas     = librerias.cargaAtributo(atributos, "columnas",     [])
    let eventos      = librerias.cargaAtributo(atributos, "eventos",      {})
    let metodos      = librerias.cargaAtributo(atributos, "metodos",      {})
    let nombreGrid   = librerias.cargaAtributo(atributos, "nombreGrid",   null)
    let nombreLlamar = librerias.cargaAtributo(atributos, "nombreLlamar", null)
    let filtros      = librerias.cargaAtributo(atributos, "filtros",     [])

    let busqueda   = librerias.cargaAtributo(atributos, 'busqueda',   "si");
    busqueda = busqueda == "si" ? true : false;

    let agrupa     = librerias.cargaAtributo(atributos, 'agrupa',     "no");
    agrupa = agrupa == "si" ? true : false;

    let adiciona   = librerias.cargaAtributo(atributos, 'adiciona',   "si");
    adiciona = adiciona == "si" ? true : false;
    
    // Barra de acciones    
    if (nombreGrid   == null) nombreGrid   = estructura+'_grid'; 
    if (nombreLlamar == null) nombreLlamar = estructura+'_forma';
    //console.log("idGrid:", nombreGrid, nombreLlamar)

    //let valorDefecto = {};
    let valorDefecto = null;

    let elementosBarra = [
        window.$f.componentes_llamados_crud.tituloCrud(titulos.principal),
    ];

    // Boton de barra superior
    let adicionaBoton = window.$f.componentes_llamados_crud.botonCrud(
        titulos.crear, 
        estructura,
        nombreGrid, 
        nombreLlamar,              
        valorDefecto
    )
    if (adiciona == true) {
        elementosBarra.push(adicionaBoton)
    }


    // Barra de acciones
    if (metodos.dobleClick == undefined) {
        metodos['dobleClick'] = window.$f.componentes_llamados_crud.dobleClickGrid(estructura, nombreGrid, nombreLlamar)                                                                  
    }

    // Definición del grid
    let definicion = {
        'ruta'          : estructura,
        'id'            : idGrid ,
        'nombreGrid'    : nombreGrid,
        'fuente'        : estructura,
        'tipofuente'    : tipofuente,
        'columnas'      : columnas,
        'elementosBarra': elementosBarra,
        "metodos"       : metodos,
        'busqueda'      : busqueda,
        'agrupa'        : agrupa,
        'eventos'       : eventos,
        'filtros'       : filtros
    }

    let componente = grid_generador_crud.creaComponente(definicion);

    return componente;
}

export default {
    grid_objeto_crud  : grid_objeto_crud,
    columna_objeto    : grid_columna.columna_objeto,
    columna_texto     : grid_columna.columna_texto,
    columna_fecha     : grid_columna.columna_fecha,
    columna_fecha_hora: grid_columna.columna_fecha_hora,
    columna_opciones  : grid_columna.columna_opciones
}