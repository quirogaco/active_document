import forma_objeto from './forma_objeto.js';

// Prepara definición del GRID
const forma_prepara = function(definicion={}) {
    definicion = definicion.datos    
    let campos_base = [];
    let campos      = window.$librerias.cargaAtributo(definicion, 'campos', []); 
    let campo, tipoeditor;    
    for (const indice in campos) {
        campo      = campos[indice];
        tipoeditor = window.$librerias.cargaAtributo(campo, 'tipoeditor', 'texto');
        if (tipoeditor == "texto") {
            campo['tipo'] = 'dxTextBox'
            campos_base.push( forma_objeto.campo_objeto(campo) )
        }

        if (tipoeditor == "entero") {
            campo['tipo'] = 'dxNumberBox'
            campos_base.push( forma_objeto.campo_objeto(campo) )
        }

        if (tipoeditor == "fecha") {
            campo['tipo'] = 'dxTextBox'
            campo['modo'] = 'date'
            campos_base.push( forma_objeto.campo_objeto(campo) )
        }

        if (tipoeditor == "radio") {
            campos_base.push( forma_objeto.radio_objeto(campo) )
        }

        if (tipoeditor == "chequeo") {
            campos_base.push( forma_objeto.radio_objeto(campo) )
        }

        if (tipoeditor == "select") {
            campos_base.push( forma_objeto.select_objeto(campo) )
        }

        if (tipoeditor == "tag") {
            campos_base.push( forma_objeto.tag_objeto(campo) )
        }
    }    
    definicion["campos"] = campos_base;
    let componente = forma_objeto.forma_objeto_crud(definicion);

    return componente;
}


// Define 
export default {
    forma_prepara: forma_prepara
}