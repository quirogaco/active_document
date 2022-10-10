export const campos_tipo = [
    {
        tipo       : 'texto',
        icon       : 'fas fa-font',        
        hint       : 'Campo de texto',
        text       : 'Texto',
        elementAttr: {
            id   : 'elemento_campo_texto',
            class: 'shadow-sm  rounded mb-2'
        }

    },

    {
        tipo       : 'correo',
        icon       : 'fas fa-envelope-square',        
        hint       : 'Campo de correo electrónico',
        text       : 'Correo electrónico',
        elementAttr: {
            id   : 'elemento_campo_correo',
            class: 'shadow-sm rounded mb-2'
        }

    },

    {
        tipo       : 'area_texto',
        icon       : 'far fa-sticky-note',
        hint       : 'Campo Area de Texto',
        text       : 'Area de Texto',
        elementAttr: {
            id   : 'elemento_campo_area',
            class: 'shadow-sm rounded mb-2'
        }
    },

    {
        tipo       : 'entero',
        icon       : 'fab fa-creative-commons-zero',
        hint       : 'Campo valor númerico',
        text       : 'Númerico',
        elementAttr: {
            id   : 'elemento_campo_entero',
            class: 'shadow-sm rounded mb-2'
        }
    },

    {
        tipo       : 'fecha',
        icon       : 'fas fa-calendar-day',
        hint       : 'Campo fecha',
        text       : 'Fecha',
        elementAttr: {
            id   : 'elemento_campo_fecha',
            class: 'shadow-sm rounded mb-2'
        }
    },

    {
        tipo       : 'fecha_hora',
        icon       : 'fas fa-calendar-week',
        hint       : 'Campo fecha hora',
        text       : 'Fecha hora',
        elementAttr: {
            id   : 'elemento_campo_fecha_hora',
            class: 'shadow-sm rounded mb-2'
        }
    },

    {
        tipo       : 'chequeo',
        icon       : 'fas fa-check-square',
        hint       : 'Campo chequeo',
        text       : 'Chequeo',
        elementAttr: {
            id   : 'elemento_campo_chequeo',
            class: 'shadow-sm rounded mb-2'
        }
    },

    {
        tipo       : 'opciones',
        icon       : 'fas fa-list-alt',
        hint       : 'Campo opciones',
        text       : 'Opciones',
        elementAttr: {
            id   : 'elemento_campo_opciones',
            class: 'shadow-sm rounded mb-2'
        }
    },

    {
        tipo       : 'seleccion',
        icon       : 'fas fa-list',
        hint       : 'Campo selección',
        text       : 'Selección',
        elementAttr: {
            id   : 'elemento_campo_seleccion',
            class: 'shadow-sm rounded mb-2'
        }
    },

    {
        tipo       : 'seleccion_multiple',
        icon       : 'fas fa-tasks',
        hint       : 'Campo selección multiple',
        text       : 'Selección multiple',
        elementAttr: {
            id   : 'elemento_campo_seleccion_multiple',
            class: 'shadow-sm rounded mb-2'
        }
    },

    {
        tipo       : 'archivo',
        icon       : 'fas fa-file-upload',
        hint       : 'Campo archivo',
        text       : 'Archivo(s)',        
        elementAttr: {
            id   : 'elemento_campo_archivo',
            class: 'shadow-sm rounded mb-2'
        }
    }
]