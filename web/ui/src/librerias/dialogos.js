import { custom, confirm } from 'devextreme/ui/dialog';

const crea_mi_dialogo = function() {
    let miDialogo = new custom({
        title      : "Confirme por favor",
        messageHtml: "<b><i>Esta seguro ?</i></b>",
        buttons: [
            {
                text: "SI",
                onClick: (e) => {
                    return { respuesta: e.component.option("text") }
                }
            }, 
            {
                text: "NO",
                onClick: (e) => {
                    return { respuesta: e.component.option("text") }
                }
            }
        ]
    });   
    
    return miDialogo;
};

const creaMensaje = function(titulo, mensaje) {
    let miDialogo = new custom({
        title      : titulo,
        messageHtml: mensaje,
        buttons: [
            {
                text: "LEIDO",
            }
        ]
    });  
    miDialogo.show();      
};

async function confirmar(title, message) {
    let confirmado = false;
    let resultado = confirm(message, title);                   
    await resultado.then(dialogo => {
        if (dialogo == true) {
            confirmado = true;
        }
    });
    
    return confirmado;
};

export default {    
    miDialogo: crea_mi_dialogo,
    miMensaje: creaMensaje,
    confirmar: confirmar
} 