let items = [
    {
        location: 'before',
        widget  : 'dxButton',            
        options : {
            icon: 'far fa-edit',
            hint: 'enviar',
            text: 'Enviar',
            type: 'success',
            onClick() {                       
            },
        },
    }, 

    {
        location: 'before',
        widget  : 'dxButton',                                
        options : {
            icon: 'fas fa-undo',
            hint: 'regresar',
            text: "Regresar",
            type: 'normal',
            onClick() {                    
            },
        },
    }
]

export default {
    items: items
}