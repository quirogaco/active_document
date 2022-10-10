import librerias            from '../../../../librerias/librerias.js';

const reglas = function(tipoEditor, atributos={}) {
    let dataField      = librerias.cargaAtributo(atributos, "campo",    "")  
    let mode           = librerias.cargaAtributo(atributos, "modo",     "text")  
    // Manejo de titulos
    let label          = librerias.cargaAtributo(atributos, "titulo", {})
    if (typeof label === 'string') {
        label = {
            text: label
        }
    }
    let titulo = librerias.cargaAtributo(label, 'text', dataField);

    // Reglas de validacion
    let validationRules = []
    let obligatorio     = librerias.cargaAtributo(atributos, "obligatorio", "no")   
    let validacion      = librerias.cargaAtributo(atributos, "validacion",  [])   

    // Email    
    if (mode == 'email') {
        validationRules.push({
            type   : "email",
            message: titulo + " Correo invalido"
        })
    }

    // Obligatorio
    if ( (obligatorio == "si") && (validacion.length == 0) ) {                
        // Obligatorio texto
        validationRules = [{
            type   : "required",
            message: titulo + " es obligatorio"
        }]        
    }
    else {
        if ( validacion.length > 0 ) {
            validationRules = validacion
        }
    }

    // Longitud
    let minimo = librerias.cargaAtributo(atributos, "minimo", null)   
    let maximo = librerias.cargaAtributo(atributos, "maximo", null)   
    // Organizar titulos
    if ( (minimo != null) || (maximo != null) ) {
        let mensaje = titulo + ", longitud invalida de caracteres"
        let regla = {
            'type'   : "stringLength",
            'trim'   : true
        }
        
        if (maximo != null) {            
            regla["max"] = maximo;
            mensaje     += ", maximo " + maximo + " caracteres"  
        };
        
        if (minimo != null) {
            regla["min"] = minimo;
            mensaje     += ", minimo " + minimo + " caracteres"  
        };

        regla["message"] = mensaje;
        
        validationRules.push(regla)
    }

    return validationRules;
}

export default {
    reglas: reglas
}