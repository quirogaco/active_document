const campo_grid = function(atributos, editorOptions, dataField) {
    let alternanciaDeFilas = window.$librerias.cargaAtributo(atributos, 'alternanciaDeFilas', 'si');
    editorOptions["rowAlternationEnabled"] = (alternanciaDeFilas == "si" ? true : false);

    let focoResaltado = window.$librerias.cargaAtributo(atributos, 'focoResaltado', 'si');
    editorOptions["focusedRowEnabled"] = (focoResaltado == "si" ? true : false);

    let ajustaPalabra      = window.$librerias.cargaAtributo(atributos, 'ajustaPalabra', 'si');
    editorOptions["wordWrapEnabled"] = (ajustaPalabra == "si" ? true : false);

    // Metodos
    let metodos    = window.$librerias.cargaAtributo(editorOptions, 'metodos', {});
    // Dobleclick
    let dobleClick = window.$librerias.cargaAtributo(metodos, 'dobleClick', null);
    if ( dobleClick != null) editorOptions["onRowDblClick"] = dobleClick;

    // Key atributo
    //let keyExpr = "id"
    //editorOptions["keyExpr"] = keyExpr
    
    return editorOptions;
}

export default {
    campo_grid: campo_grid
}