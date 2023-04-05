

// Carga datos a almacenamiento
const cargaDatosComponente = function(idComponente, datos) {  
    window.$datosComponentes[idComponente] = datos;
};

const leeDatosComponente = function(idComponente) {  
    let datos = window.$datosComponentes[idComponente];
    if (datos == undefined) {
        datos = {
            "opciones": {},
            "datos"   : {}
        }
    }
    return datos;
};

export default {
    cargaDatosComponente: cargaDatosComponente,
    leeDatosComponente  : leeDatosComponente
} 