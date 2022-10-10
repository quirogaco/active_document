import fuenteDatos from '../../remoto/fuenteDatos.js';
import librerias   from '../../../../librerias/librerias.js';

const seleccion_busqueda = function(tipoEditor, editorOptions, atributos) {
    // Busqueda expresion
    if ( (tipoEditor != "radio") && (tipoEditor != "archivo") ) {
        let busqueda_expresion = librerias.cargaAtributo(atributos, "busqueda_expresion", "nombre")  
        if (busqueda_expresion != null) { 
            editorOptions["searchExpr"] = busqueda_expresion;
        }
    }

    // Muestra expresion
    if (tipoEditor != "archivo") {
        let muestra_expresion = librerias.cargaAtributo(atributos, "muestra_expresion", null) 
        if ( (tipoEditor != "radio") && (muestra_expresion == null) )  {
            muestra_expresion = 'nombre'
        }
        if (muestra_expresion != null) { 
            editorOptions["displayExpr"] = muestra_expresion;
        }

        // Valor expresion
        let valor_expresion = librerias.cargaAtributo(atributos, "valor_expresion", null)  
        if ( (tipoEditor != "radio") && (valor_expresion == null) )  {
            valor_expresion = 'id'
        }
        if (valor_expresion != null) { 
            editorOptions["valueExpr"] = valor_expresion;
        }
    }

    // Buscar
    if ( (tipoEditor != "radio") && (tipoEditor != "archivo") )  {
        let buscar         = librerias.cargaAtributo(atributos, "buscar", "si")  
        let searchEnabled  = true;
        if (buscar == "no") searchEnabled = false;
        editorOptions["searchEnabled"] = searchEnabled;
    }

    // Opciones del input tag
    editorOptions["noDataText"]         = "Sin Datos";
    editorOptions["showClearButton"]    = true;
    editorOptions["showDropDownButton"] = true;

    return editorOptions;
}

const crea_fuente = function(tipoEditor, editorOptions, dataField, atributos) {
    let eventos = librerias.cargaAtributo(atributos, "eventos", {})  
    
    if (tipoEditor != "archivo") {
        let filtros        = librerias.cargaAtributo(atributos, "filtros", []) 
        let fuente         = librerias.cargaAtributo(atributos, "fuente",  null) 
        if (fuente != null) { 
            if (Array.isArray(fuente) == true) {
                editorOptions["dataSource"] = fuenteDatos.creaFuenteDatosUniversal(tipoEditor, "", "", fuente)
            }
            else {
                if ( (tipoEditor == "select") && (tipoEditor == "tag") ) {               
                    editorOptions["dataSource"] = fuenteDatos.creaFuenteDatosConsulta(tipoEditor, null, fuente, fuente, [], [])
                }
                else {
                    editorOptions["dataSource"] = fuenteDatos.creaFuenteDatosUniversal(tipoEditor, dataField, fuente, null, filtros, eventos)
                }
            }        
        }
    }

    return editorOptions;
}

const alto_ancho = function(tipoEditor, editorOptions, atributos) {
    // Alto
    editorOptions["height"] = librerias.cargaAtributo(atributos, "alto", null)  

    // Ancho
    editorOptions["width"]  = librerias.cargaAtributo(atributos, "ancho", null)  

    return editorOptions;
}

const campo_texto = function(tipoEditor, editorOptions, dataField, atributos) {
    // Número maximode caracteres maximo
    let longitud = librerias.cargaAtributo(atributos, "longitud", 50)
    editorOptions["maxLength"] = longitud 


    // Manejo de titulos
    let titulo = null;
    
    let label         = librerias.cargaAtributo(atributos, "titulo", {})
    if (typeof label === 'string') {
        label = {
            text   : label
        }
    }
    titulo = librerias.cargaAtributo(label, 'text', dataField);    

    // Todo a mayusculas
    //editorOptions["inputAttr"] = {'style': 'text-transform: uppercase'}    

    // Modo de texto
    editorOptions['mode'] = tipoEditor;

    // Marcado del campo    
    let disabled = librerias.cargaAtributo(atributos, "editable", 'si')  
    disabled = disabled == "si" ? false : true;
    if ( (tipoEditor != "radio") && (tipoEditor != "archivo") && (disabled == false)) {
        let placeholder    = librerias.cargaAtributo(atributos, "marcador", "");
        //if (placeholder == "") placeholder = "Seleccione " + titulo;
        if (placeholder == "") placeholder = titulo;
        if (placeholder != "") {
            editorOptions["placeholder"] = placeholder;
        }  
    }

    return editorOptions
}

export default {
    seleccion_busqueda: seleccion_busqueda,
    crea_fuente       : crea_fuente,
    alto_ancho        : alto_ancho,
    campo_texto       : campo_texto  
}