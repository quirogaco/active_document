
const getItems = function(params) {
    let crear = {
        text : 'Crear',
        type : 'success',
        icon : 'fas fa-plus-circle',
        click: function(e) {
            params.callBack(e, "crear")
        },
    };
    
    let modificar = {
        text : 'Modificar',
        type : 'default',
        icon : 'fas fa-pen-square',
        click: function(e) {
            params.callBack(e, "modificar")
        },
    };
    
    let borrar = {
        text : 'Borrar',
        type : 'danger',
        icon : 'fas fa-eraser',
        click: function(e) {
            params.callBack(e, "borrar")
        },
    };
    
    let regresar = {
        text : 'Regresar',
        type : 'normal',
        icon : 'fas fa-arrow-circle-left',
        click: function(e) {
            params.callBack(e, "regresar")
        },
    };    

    let items = [];
    if (params.mode == "nuevo") {
        items = [
            $forma.botonBarra(crear),
            $forma.botonBarra(regresar)
        ]
    }
    else {
        items = [
            $forma.botonBarra(modificar),
            $forma.botonBarra(borrar),
            $forma.botonBarra(regresar)
        ]
    }

    return items;
}

export default {
    getItems: getItems
}