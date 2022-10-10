import librerias            from '../../../../librerias/librerias.js';

// OPCIONES
import opciones_archivo     from './opciones_archivo.js';
import opciones_grid        from './opciones_grid.js';
import opciones_general     from './opciones_general.js';

// EVENTOS
import eventos_select       from './eventos_select.js';
import eventos_radio        from './eventos_radio.js'

// REGISTRO
import registrar_componente from './registrar_componente.js'

const editor_opciones = function(tipoEditor, atributos={}) {
    let dataField   = librerias.cargaAtributo(atributos, "campo",  null)
    let nombre      = librerias.cargaAtributo(atributos, "nombre", null) 
    let tipo_editor = librerias.cargaAtributo(atributos, "tipo", "dxTextBox")  

    // EDITOR OPTIONS
    let editorOptions  = librerias.cargaAtributo(atributos, "editor", {})

    // Nombre del campo
    // Si no tiene datafield no es dato de la forma
    //      Nombre es necesario para registrarlo
    if (nombre !== null) editorOptions["nombre"] = nombre;

    if (tipoEditor == "radio") {
        // Manejo de composicion
        let layout         = librerias.cargaAtributo(atributos, "composicion", "horizontal")
        editorOptions["layout"] = layout;
    }
    
    // Elementos
    if (tipoEditor != "archivo") {
        let items          = librerias.cargaAtributo(atributos, "elementos", [])
        editorOptions["items"] = items;

        // valor
        let valor = librerias.cargaAtributo(atributos, "valor", "")  
        editorOptions["value"] = valor;
    }

    // Fuente
    editorOptions = opciones_general.crea_fuente(tipoEditor, editorOptions, dataField, atributos)

    // Muestra expresion
    editorOptions = opciones_general.seleccion_busqueda(tipoEditor, editorOptions, atributos)

    // Texto no datos
    if (tipoEditor != "archivo") {
        let noDataText = librerias.cargaAtributo(atributos, "sinDatos", "Sin datos")  
        editorOptions["noDataText"] = noDataText;
    }

    // FECHA
    if (tipo_editor == "dxDateBox") {
        editorOptions["dateOutOfRangeMessage"]   = "Fecha fuera de rango" 
        editorOptions["invalidDateMessage"]      = "Fecha/hora invalida" 
        editorOptions["dateSerializationFormat"] = librerias.cargaAtributo(atributos, "formato", "yyyy-MM-dd") 
        editorOptions["displayFormat"]           = librerias.cargaAtributo(atributos, "formato", "yyyy-MM-dd") 
        editorOptions["max"]                     = librerias.cargaAtributo(atributos, "fecha_maxima", undefined)    
        editorOptions["min"]                     = librerias.cargaAtributo(atributos, "fecha_minima", undefined)    
        editorOptions["openOnFieldClick"]        = true
    }

    // NUMERO
    if (tipo_editor == "dxNumberBox") {
        editorOptions["max"] = librerias.cargaAtributo(atributos, "valor_maximo", undefined)    
        editorOptions["min"] = librerias.cargaAtributo(atributos, "valor_minimo", undefined)    
    }
    
    // ARCHIVO
    if (tipoEditor == "archivo") {
        editorOptions = opciones_archivo.campo_archivo(atributos, editorOptions, dataField)        
    }

    // GRID:
    if (tipoEditor == "grid") {
        editorOptions = opciones_grid.campo_grid(atributos, editorOptions, dataField)
    }

    // ALTO, ANCHO
    editorOptions = opciones_general.alto_ancho(tipoEditor, editorOptions, atributos)

    // Registro de componentes, todo componente ndet se debe registrar
    let nombre_registro = dataField;
    if (nombre_registro == null) nombre_registro = nombre; 
    registrar_componente.registra_componente(tipoEditor, atributos, editorOptions, nombre_registro)
    
    editorOptions = opciones_general.seleccion_busqueda(tipoEditor, editorOptions, atributos)

    // Especificos de texto
    // Mayusculas, Modo de texto (mode), Editable, Placeholder, Label
    editorOptions = opciones_general.campo_texto(tipoEditor, editorOptions, dataField, atributos)    

    //###########
    // EVENTOS //
    //##########
    if ( (tipoEditor == "select") || (tipoEditor == "tag") ) {
        editorOptions = eventos_select.eventos(atributos, editorOptions)
    }

    if (tipoEditor == "radio") {
        editorOptions = eventos_radio.eventos(atributos, editorOptions)
    }

    return editorOptions;
}

export default {
    editor_opciones: editor_opciones
}