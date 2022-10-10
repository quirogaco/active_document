// Definición eventos GRID
const eventos_grid = function(configuracion) {    
    let eventos = window.$librerias.cargaAtributo(configuracion, 'eventos', {});
    
    return eventos
}

export default {
    eventos_grid: eventos_grid
}