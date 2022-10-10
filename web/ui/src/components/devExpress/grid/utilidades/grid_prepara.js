import grid_objeto from './grid_objeto.js';

// Prepara definición del GRID
const grid_prepara = function(definicion={}) {
    definicion = definicion.datos;
    let definicion_base = {};
    let columnas_base   = [];
    let columnas        = window.$librerias.cargaAtributo(definicion, 'columnas', []); 
    let columna, tipo;
    for (const indice in columnas) {
        columna = columnas[indice];
        tipo    = window.$librerias.cargaAtributo(columna, 'tipo', "texto");
        if (tipo == "texto") {
            columnas_base.push( grid_objeto.columna_texto(columna) )
        }

        if (tipo == "fecha") {
            columnas_base.push( grid_objeto.columna_fecha(columna) )
        }

    }    
    definicion["columnas"] = columnas_base;

    if (definicion["nombreGrid"] == undefined) definicion["nombreGrid"] = definicion["componente"];
    
    let componente = grid_objeto.grid_objeto_crud(definicion);

    return componente;
}


// Define 
export default {
    grid_prepara : grid_prepara
}