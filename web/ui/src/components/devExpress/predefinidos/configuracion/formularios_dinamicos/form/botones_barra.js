
const getItems = function(params) {
    let prevista = {
        text : 'Prevista formulario',
        type : 'success',
        icon : 'fas fa-eye',
        click: function(e) {
            params.callBack(e, "prevista")
        },
    };

    let separador = {
        text : '',
        type : 'normal',
        icon : 'fas fa-braille'
    };

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

    let consulta =  {
        text : 'Consulta datos',
        type : 'success',
        icon : 'fas fa-eye',
        click: function(e) {
            params.callBack(e, "consulta")
        },
    };   

    let items = [];
    console.log("params.mode:", params.mode)
    if (params.mode == "crear") {
        items = [
            //$forma.botonBarra(consulta),
            //$forma.botonBarra(prevista),
            $forma.botonBarra(separador), 
            $forma.botonBarra(crear),
            $forma.botonBarra(regresar)
        ]
    }
    else {
        items = [
            //$forma.botonBarra(consulta),
            //$forma.botonBarra(prevista),
            $forma.botonBarra(separador),
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