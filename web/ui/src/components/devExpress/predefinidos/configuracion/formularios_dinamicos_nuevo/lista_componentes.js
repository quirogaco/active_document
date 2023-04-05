
/*
export const lista_componentes = [
    {
        'id'       : "chequeo",
        'titulo'   : 'Chequeo',
        'tipo'     : 'chequeo',
        'icono'    : 'far fa-check-square',
        'elementos': []
    },

    {
        'id'       : "radio",
        'titulo'   : 'Radio',
        'tipo'     : 'radio',
        'icono'    : 'fas fa-dot-circle',
        'elementos': []
    },

    {
        'id'       : "selector",
        'titulo'   : 'Selección',
        'tipo'     : 'selector',
        'icono'    : 'fas fa-angle-down',
        'elementos': []
    },

    {
        'id'       : "selector_multiple",
        'titulo'   : 'Selección multiple',
        'tipo'     : 'selector_multiple',
        'icono'    : 'fas fa-angle-double-down',
        'elementos': []
    },

    {
        'id'    : "archivo",
        'titulo': 'Archivo',
        'tipo'  : 'archivo',
        'icono' : 'fas fa-folder-plus'
    },
]
*/

export const campos_tipo = [
    {
        tipo       : 'texto',
        icon       : 'fas fa-font',        
        hint       : 'Campo de texto',
        text       : 'Texto',
        elementAttr: {
            id   : 'elemento_campo_texto',
            class: 'float-left'
        }

    },

    {
        tipo       : 'area_texto',
        icon       : 'far fa-sticky-note',
        hint       : 'Campo Area de Texto',
        text       : 'Area de Texto',
        elementAttr: {
            id   : 'elemento_campo_area',
            class: 'float-left'
        }
    },

    {
        tipo       : 'entero',
        icon       : 'fab fa-creative-commons-zero',
        hint       : 'Campo valor númerico entero',
        text       : 'Númerico entero',
        elementAttr: {
            id   : 'elemento_campo_entero',
            class: 'float-left'
        }
    },

    {
        tipo       : 'fecha',
        icon       : 'fas fa-calendar-day',
        hint       : 'Campo fecha',
        text       : 'Fecha',
        elementAttr: {
            id   : 'elemento_campo_fecha',
            class: 'float-left'
        }
    }
]