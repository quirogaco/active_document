const campo_componente = function(forma_id=null, campo_id=null) {
    let componente = undefined
    if ( (forma_id != null) && (campo_id != null) ) {
        componente = window.$componentes["_campos"][forma_id][campo_id].component
    }

    return componente
}

const forma_componente = function(forma_id=null) {
    let componente = undefined
    if (forma_id != null) {
        componente = window.$componentes["_formas"][forma_id] 
    }

    return componente
}

export default {
    campo_componente: campo_componente,
    forma_componente: forma_componente
}