const revisarItems = function(items, tipo, atributo, valores) {
    let campo, componente, nombreComponente, valor; 
    for (const indice in items) {        
        campo = items[indice];        
        if (campo.editorType == tipo) {
            nombreComponente = campo.ruta + "_" + campo.dataField;
            componente       = window.$ns[nombreComponente]; 
            if (componente != undefined) {
                valor = componente.option("value");        
                valores[atributo] = valor;                
            }            
        }

        if (campo.itemType ==  "group" ) {
            revisarItems(campo.items, tipo, atributo, valores)
        }
    }
}

const valoresForma = function(tipo, atributo, definicion) {
    let campos   = $lib.cargaAtributo(definicion, "campos", []);
    let valores  = {};
    revisarItems(campos, tipo, atributo, valores)

    return valores;
}

const validaValoresForma = function(tipo, atributos) {
    let campos   = $lib.cargaAtributo(atributos, "campos", []);
    let mensajes = [];
    let campo, componente, nombreComponente, reglas, regla, valor;    
    for (const indice in campos) {
        campo = campos[indice];
        if (campo.editorType == tipo) {
            nombreComponente = campo.ruta + "_" + campo.dataField;
            componente       = window.$ns[nombreComponente];    
            if (componente != undefined) {
                valor  = componente.option("value");        
                reglas = cargaAtributo(campo, "validationRules", []);
                for (const indice in reglas) {
                    regla = reglas[indice];
                    if (regla.type == 'required') {
                        if ( (valor == "") || (valor == null) || (valor == undefined) || (valor.length == 0) ) {
                            mensajes.push({message: regla.message})
                        }
                    }
                }                
            } 
        }                    
    }

    return mensajes;
}

const traer_componentes = function(formaid, elementos = null) {
    let elemento, campos;
    let resultado = null; 
    if (elementos != null) {
        campos = window.$ns[ (formaid + "_") ];        
        // Retorna elementos
        if (campos != undefined) {
            // Texto nombre de campo
            if (typeof elementos === 'string') {
                if (campos[elementos] != undefined) {
                    resultado = campos[elementos];
                }
            }
            else {
                // Lista con nombres de campo
                if (Array.isArray(elementos) == true) {                
                    resultado = {};
                    for (const indice in elementos) {
                        elemento = campos[ elementos[indice] ];
                        if (elemento != undefined) {
                            resultado[ elementos[indice]  ] = elemento;
                        }  
                    }
                    if (Object.keys(resultado).length == 0) resultado = null;                
                }
            }
        }
    }
    else {
        resultado = window.$ns[formaid];
    }

    return resultado;
}

const buscar_item = function(items, nombre) {
    let encontrado = null;
    let item;
    for (const indice in items) {
        item = items[indice]
        if (item.items != undefined) {  
            encontrado = buscar_item(item.items, nombre)
        }

        if ( (item.dataField == nombre) || (item.nombre == nombre) ){
            encontrado = item
        }
        if (encontrado != null) break;
    }

    return encontrado
}

const forma_atributo_item = function(formaid, nombre, atributo, valor, repaint=false) {
    let forma      = traer_componentes(formaid).formaInstancia;
    let items      = forma.option("items");            
    let encontrado = buscar_item(items, nombre);
    let atributos  = [];
    if (encontrado != null) {        
        if (atributo.indexOf(".") > 1) {
            atributos = atributo.split(".");
            encontrado[atributos[0]][atributos[1]] = valor;
        }
        else {
            encontrado[atributo] = valor;
        }
    }

    return encontrado;
}

const traer_fuente_datos = function(formaid, nombre) {
    let componente   = traer_componentes(formaid, nombre);
    let fuente_datos = null;
    fuente_datos     = componente.getDataSource();      
    
    return fuente_datos;
}

const forma_atributo_items = function(formaid, nombres, atributo, valor, repaint=true) {
    let nombre;
    for (const indice in nombres) {
        nombre = nombres[indice];
        forma_atributo_item(formaid, nombre, atributo, valor, repaint)
    }
    
    let forma = traer_componentes(formaid).formaInstancia;
    if (repaint == true) forma.repaint();
}

const forma_atributos = function(formaid, atributo, valor) {
    let forma       = traer_componentes(formaid).formaInstancia;
    forma.option(atributo, valor); 
    forma.repaint()   
}

// Valida atributos de una forma
const valida_forma_datos = function(forma_id) {
    let componente  = window.$ns[forma_id]
    let forma       = $lib.traer_componentes(forma_id).formaInstancia 
    let definicion  = window.$definiciones[forma_id]
    let datos_forma = JSON.parse( JSON.stringify( forma.option("formData") ) )
    let validacion  = forma.validate()      
    let validado    = validacion.isValid
    let mensajes    = validacion.brokenRules
    let resultado   = datos_forma


    // Validación y captura de archivos
    let archivos         = valoresForma("dxFileUploader", "archivos", definicion).archivos
    if ( (archivos != undefined) && (archivos.length > 0) ) {
        datos_forma['archivos'] = archivos
    }
    let archivosMensajes = validaValoresForma("dxFileUploader", definicion);
    if (archivosMensajes.length > 0) {
        validado = false
        mensajes = mensajes.concat(archivosMensajes)
    }

    if (validado == false) {                                
        componente.mensajeValidacion(mensajes)  
        resultado = false 
    }
    
    return resultado
}

const leer_forma_atributo_item = function(formaid, nombre, atributo) {
    let forma          = traer_componentes(formaid).formaInstancia;
    let items          = forma.option("items");            
    let encontrado     = buscar_item(items, nombre);
    let atributos      = [];
    let atributoObjeto = null;
    if (encontrado != null) {        
        if (atributo.indexOf(".") > 1) {
            atributos      = atributo.split(".");
            atributoObjeto = encontrado[atributos[0]][atributos[1]];
        }
        else {
            atributoObjeto = encontrado[atributo];
        }
    }

    return atributoObjeto;
}

const leer_forma_atributo_items = function(formaid, nombres, atributo) {
    let atributoObjeto = {};
    let nombre;
    for (const indice in nombres) {
        nombre = nombres[indice];
        atributoObjeto[nombre] = leer_forma_atributo_item(formaid, nombre, atributo)
    }
    
    return atributoObjeto;
}

const leer_forma_componente_opcion = function(formaid, nombre_componente, opcion) {
    let componentes = traer_componentes(formaid, [nombre_componente])
    let valor       = componentes[nombre_componente].option(opcion)

    return valor;
}

const forma_componente_opcion = function(formaid, nombre_componente, opcion, valor) {
    let componentes = traer_componentes(formaid, [nombre_componente])
    componentes[nombre_componente].option(opcion, valor)

    return valor;
}

const forma_componentes_opcion = function(formaid, nombres, opcion, valor) {
    let nombre;
    for (const indice in nombres) {
        nombre = nombres[indice];
        forma_componente_opcion(formaid, nombre, opcion, valor) 
    }    
}

export default {
    valoresForma                : valoresForma,
    validaValoresForma          : validaValoresForma,
    traer_componentes           : traer_componentes,
    forma_atributo_item         : forma_atributo_item,
    forma_atributo_items        : forma_atributo_items,
    forma_atributos             : forma_atributos,
    leer_forma_atributo_item    : leer_forma_atributo_item,
    leer_forma_atributo_items   : leer_forma_atributo_items,
    leer_forma_componente_opcion: leer_forma_componente_opcion,
    forma_componente_opcion     : forma_componente_opcion,
    forma_componentes_opcion    : forma_componentes_opcion,
    traer_fuente_datos          : traer_fuente_datos,
    valida_forma_datos          : valida_forma_datos,
}