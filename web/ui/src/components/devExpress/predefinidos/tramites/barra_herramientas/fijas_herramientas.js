import click_herramientas from "./click_herramientas.js"; 

// ************** //
// ACCIONES FIJAS //
// ************** //
let acciones = [
    {
        location: 'before',
        widget  : 'dxButton',            
        options : {
            icon   : 'fas fa-comment-dots',
            hint   : 'Crear comentario/anotación',
            text   : 'Comentario',
            type   : 'default',
            onClick() {       
                click_herramientas.accion_click(200)            
            },                       
        },
    }, 

    {
        location: 'before',
        widget  : 'dxButton',                                
        options : {
            icon: 'fas fa-file-upload',
            hint: 'Anexar un archivo',
            text: "Archivo",
            type: 'default',
            onClick() {       
                click_herramientas.accion_click(210)            
            },
        },
    }, 

    {
        location: 'before',
        widget  : 'dxButton',                                
        options : {
            icon: 'fas fa-folder-open',
            hint: 'Asignar Expediente',
            text: "Expediente",
            type: 'default',
            onClick() {       
                click_herramientas.accion_click(220)            
            },
        },
    },
    
    {
        location: 'before',
        widget  : 'dxButton',                                
        options : {
            icon: 'fas fa-file-word',
            hint: 'Crear borrador respuesta',
            text: "Borrador respuesta",
            type: 'default',
            onClick() {       
                click_herramientas.accion_click(230)            
            },
        },
    },
]

export default {
    acciones: acciones
}