const campos_basicos = function(forma, basicas) {
    let campos = {
        validacion_grupo: basicas["forma_id"],

        // Valores de definición        
        forma  : forma,
        basicas: basicas,
        
        // Parametros props del componente
        parametros: {}
    }

    return campos
}

export default {
    campos: campos_basicos
}