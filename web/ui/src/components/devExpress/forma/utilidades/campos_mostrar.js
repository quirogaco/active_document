import forma_objeto  from './forma_objeto.js';

// Genera definición para mostrar datos
const mostrar_datos = function(campos=[]) {
    let definiciones = []

    let campo, campo_data, tipo, titulo;
    for (const indice in campos) {
        campo      = campos[indice]
        campo_data = campo["campo"]
        tipo       = $lib.cargaAtributo(campo, "tipo", "texto")
        titulo     = $lib.cargaAtributo(campo, "titulo", "")

        switch (tipo) {
            case "texto_grande":
                definiciones.push(
                    forma_objeto.campo_objeto({
                        'campo'   : campo_data,
                        'titulo'  : titulo, 
                        'tipo'    : 'dxTextArea',
                        'alto'    : '50',
                        'editable': 'no'  
                    })
                )                
                break

            case "entero":
                definiciones.push(
                    forma_objeto.campo_objeto({
                        'campo'   : campo_data,
                        'titulo'  : titulo, 
                        'editable': 'no'  
                    })
                )
                break

            default:
                // Texto 
                definiciones.push(
                    forma_objeto.campo_objeto({
                        'campo'   : campo_data,
                        'titulo'  : titulo, 
                        'editable': 'no'  
                    })
                )  
                    
        }  
    }

    return definiciones
}


export default {
    mostrar_datos: mostrar_datos    
}