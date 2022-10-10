import librerias from '../../../../librerias/librerias.js';

// Define y crea columna de GRID
const columna_objeto = function(atributos={}) {
    let dataField = librerias.cargaAtributo(atributos, "campo",      "")  
    let dataType  = librerias.cargaAtributo(atributos, "tipo",       "string")  
    let caption   = librerias.cargaAtributo(atributos, "titulo",     "")  
    let width     = librerias.cargaAtributo(atributos, "ancho",      null)  
    let alignment = librerias.cargaAtributo(atributos, "alineacion", undefined) 
    let cssClase  = librerias.cargaAtributo(atributos, "cssClase", "encabezado-grid encabezado_filtro")
    let plantilla = librerias.cargaAtributo(atributos, "plantilla", null)

    let allowEditing  = librerias.cargaAtributo(atributos,  "editar",      true) 

    let allowSorting   = librerias.cargaAtributo(atributos, "ordena", 'no')
    allowSorting   = allowSorting   == "si" ? true : false;
    
    let allowFiltering = librerias.cargaAtributo(atributos, "filtra", 'no')
    allowFiltering = allowFiltering == "si" ? true : false;
    
    let allowGrouping  = librerias.cargaAtributo(atributos, "agrupa", 'no')
    allowGrouping = allowGrouping == "si" ? true : false;

    let visible   = librerias.cargaAtributo(atributos, "visible", 'si')
    visible = visible == "si" ? true : false;

    // Definición de la columna
    let definicion = {
        "dataField"     : dataField, 
        'dataType'      : dataType,
        'alignment'     : alignment,
        "caption"       : caption,  
        "width"         : width,
        'allowEditing'  : allowEditing,
        "allowSorting"  : allowSorting,
        "allowFiltering": allowFiltering,
        'allowGrouping' : allowGrouping,
        'cssClass'      : cssClase,
        'visible'       : visible,
        'plantilla'     : plantilla
    }

    return definicion;
}

// Fecha columna
const columna_fecha = function(atributos={}) {
    let definicion         = columna_objeto(atributos)
    definicion["dataType"] = 'date'
    definicion["format"]   = 'y-MM-dd'

    return definicion;
}

// Fecha columna
const columna_fecha_hora = function(atributos={}) {
    let definicion         = columna_objeto(atributos)
    definicion["dataType"] = 'date'
    definicion["format"]   = 'y/MM/dd H:m:s'

    return definicion;
}

// Texto columna
const columna_texto = function(atributos={}) {
    let definicion         = columna_objeto(atributos)
    definicion["dataType"] = 'string'

    return definicion;
}

// Columna lookup
const columna_opciones = function(atributos={}) {
    let definicion = columna_objeto(atributos)
    let elementos  = librerias.cargaAtributo(atributos, "elementos", [])

    definicion["lookup"] = {
        dataSource: {
            store: {
                type: 'array',
                data: elementos,
                key: "id"
            },
            pageSize: 10,
            paginate: true
        },
        valueExpr  : 'id', 
        displayExpr: 'nombre'
    }

    return definicion;
}


export default {
    columna_objeto    : columna_objeto,
    columna_texto     : columna_texto,
    columna_fecha     : columna_fecha,
    columna_fecha_hora: columna_fecha_hora,
    columna_opciones  : columna_opciones
}