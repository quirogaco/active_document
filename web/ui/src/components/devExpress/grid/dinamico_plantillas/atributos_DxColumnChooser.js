const atributos = {    
    allowSearch:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si la búsqueda está habilitada en el selector de columnas."
    },

    emptyPanelText:{ 
        "tipo"       : "texto",
        "defecto"    : null,
        "descripcion": "Especifica el texto que muestra el selector de columnas cuando está vacío."
    },

    enabled:{ 
        "tipo"       : "logico",
        "defecto"    : false,
        "descripcion": "Especifica si un usuario puede abrir el selector de columnas."
    },

    height:{ 
        "tipo"       : "entero",
        "defecto"    : 260,
        "descripcion": "Especifica la altura del selector de columnas."
    },

    mode:{ 
        "tipo"       : "texto",
        "defecto"    : "dragAndDrop",
        "descripcion": "Especifica cómo gestiona un usuario las columnas mediante el selector de columnas."
    },

    searchTimeout:{ 
        "tipo"       : "entero",
        "defecto"    : 500,
        "descripcion": "Especifica un retraso en milisegundos entre el momento en que un usuario termina de escribir en el panel de búsqueda del selector de columnas y el momento en que se ejecuta la búsqueda."
    },

    title:{ 
        "tipo"       : "texto",
        "defecto"    : "Selector de columnas",
        "descripcion": "Especifica el título del selector de columnas."
    },

    width:{ 
        "tipo"       : "entero",
        "defecto"    : 250,
        "descripcion": "Especifica el ancho del selector de columnas."
    },   
}

export default {
    atributos: atributos
}