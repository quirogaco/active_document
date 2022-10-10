const barra_items = function(titulo_accion="", llamar=null) {

    let items = [
        {
            location: 'before',
            widget  : 'dxButton',            
            options : {
                icon: 'far fa-edit',
                hint: 'enviar',
                text: titulo_accion,
                type: 'success',
                onClick() {                       
                    llamar("salvar")
                },
            },
        }, 
    
        {
            location: 'before',
            widget  : 'dxButton',                                
            options : {
                icon: 'fas fa-window-close',
                hint: 'regresar',
                text: "Cerrar",
                type: 'normal',
                onClick() {         
                    llamar("salir")           
                },
            },
        }
    ]

    return items;
}

export default {
    items: barra_items
}