import datagrid from "../dxDataGrid.js";

const grid_definicion = {
    "tipo"      : "dxDataGrid",
    "dataSource": "fuente",
    "ruta"      : "base",
    "id"        : "grid",
    "keyExpr"   : "EmployeeID",
    
    "columnChooser": {
        "allowSearch"   : true,
        "emptyPanelText": "Sin columnas",
        "enabled"       : true,
        "title"         : "Selecciona columnas"
    },

    "columns": [
        {
            "dataField"     : "nombre",
            "allowSearch"   : true,
            "allowSorting"  : true,
        },
        {
            "dataField"     : "apellidos",
            "allowSearch"   : false,
            "allowSorting"  : false,
        },
    ]
};

datagrid.genera_plantilla(grid_definicion);