
let css_boton_accion = "tw-bg-blue-400 hover:tw-bg-white hover:tw-shadow boton_accion_font";
//let css_boton_accion = "";

let botones_accion = [    
    {
        icon       : 'fas fa-sitemap',
        code       : "dependencia",
        elementAttr: {
            class: css_boton_accion
        },
        text       : 'Nueva Dependencia'
    },

    {
        icon       : 'fas fa-archive',
        code       : "serie",
        elementAttr: {
            class: css_boton_accion
        },
        text       : 'Nueva Serie'
    },

    {
        icon       : 'fas fa-inbox',
        code       : "subserie",
        elementAttr: {
            class: css_boton_accion
        },
        text       : 'Nueva Subserie'
    },

    {
        icon       : 'fas fa-file-contract',
        code       : "tipo",
        elementAttr: {
            class: css_boton_accion
        },
        text       : 'Nuevo Tipo Documental'
    } ,
    
    {
        icon       : 'far fa-times-circle',
        code       : "limpia",
        elementAttr: {
            class: css_boton_accion
        },
        text       : 'Limpia seleccion'
    }   
]  

export default botones_accion;