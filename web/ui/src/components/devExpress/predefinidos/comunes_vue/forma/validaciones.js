const reglas_validacion = {
    "correo" :  {
        type   : "email",
        name   : "correo",
        message: "Correo es invalido"
    },

    "obligatorio" :  {
        type   : "required",
        name   : "obligatorio",
        message: "Valor es obligatorio "
    },

    "correo_multiple" : {
        type              : "custom",
        name              : "correo_multiple",
        validationCallback: function(e) {
            let validacion = true
            let expresion  = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            let correos    = e.value.trim()
            if (correos != "") {
                correos = correos.split(",")
                for (const indice in correos) {
                    let correo    = correos[indice].trim()
                    let resultado = expresion.test(correo)
                    if (resultado == false) {
                        validacion = resultado
                    }
                }
            }

            return validacion
        },
        message           : "Correo(s) invalido(s)"
    }
}


// Faltan maximo y minimo para numeros
const validaciones = function(atributos) {
    let titulo      = $librerias.cargaAtributo(atributos, 'titulo', "")
    let longitud    = $librerias.cargaAtributo(atributos, 'longitud', undefined)
    let validadores = $librerias.cargaAtributo(atributos, 'validadores', []) 
    let obligatorio = $librerias.cargaAtributo(atributos, 'obligatorio', undefined) 

    let validadores_campo = []

    // Valor es obligatorio
    if (obligatorio == true) {
        validadores_campo.push(
            {
                type   : "required",
                name   : "obligatorio",
                message:  titulo + " es obligatorio "
            }
        )
    }

    // Longitud, maximo numero de caracteres
    if (longitud != undefined) {
        validadores_campo.push(
            {
                type   : "stringLength",
                name   : "longitud",                
                max    : longitud,
                message: "Máximo (" + longitud + "), caracteres"
            }
        )
    }
    
    // Asigna validaciones
    for (const atributo in validadores) {
        let validador = validadores[atributo]
        
        // Nombre de la regla            
        if (typeof validador === 'string') {
            let regla = reglas_validacion[validador]
            if (regla != undefined) {
                validadores_campo.push(regla)
            }
        }

        // Objeto validador
        if (typeof validador === 'object') {
            validadores_campo.push(validador)
        }
    }

    return validadores_campo
}

export default {
    validaciones     : validaciones,
    reglas_validacion: reglas_validacion
}