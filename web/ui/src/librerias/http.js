import axios from 'axios';

import { formatMessage, loadMessages } from 'devextreme/localization';
let messages = {
    "en": {
        "applicationError": "Application error",
        "networkError"    : "Network error",
        "uknownError"     : "Unknown error",
    },
    "es": {
        "applicationError": "Error del aplicativo",
        "networkError"    : "Error de red",
        "uknownError"     : "Error desconocido"
    }
}
loadMessages(messages)

function nl2br(str) {
    return str.replace(/(?:\r\n|\r|\n)/g, '<br>');
}

let errorFunction = function(response) {     
    let mensaje = "";
    let formato = "";
    switch (response.type) {
        case "app":
            if (response.error.data.error == undefined) {
                mensaje = "metodo: <b>" + response.error.config.method + "</b>";
                mensaje += "<br>status: <b>" + response.error.status + "</b>";
                mensaje += "<br>statusText: <b>" + response.error.statusText + "</b>";
                mensaje += "<br>url: <b>" + response.error.config.url + "</b>";                
                formato = formatMessage("applicationError", "");
            }
            else {
                mensaje = nl2br(response.error.data.error);
                formato = formatMessage("applicationError", "");
            }
            break

        case "request":
            if (response.error.readyState == 4 && response.error.status == 0) {
                mensaje = formatMessage("uknownError", "");
                formato = formatMessage("networkError", "");
            }
            else {
                mensaje = response.error;
                formato = formatMessage("networkError", "");
            }
            break

        case "unkwon":
            mensaje = response.error;
            formato = formatMessage("uknownError", "");
            break
    } 
    
    if (mensaje.length > 1500) {
        mensaje =  mensaje.slice(-1500)
    }
    
    $alert(mensaje, formato)
}

function deepFindCallback(obj, matcher, cb) {
    // Call the matcher function
    if (matcher(obj)) {
        // If match, call the callback
        cb(obj);
    }
    // If not match, recursively call deepFindCallback
    for (let key in obj) {
        if (typeof obj[key] === 'object') {
            deepFindCallback(obj[key], matcher, cb);
        }
    }
}

const esArchivo = function(valor) {
    let esArchivo = false;
    if (Array.isArray(valor)) {
        for (const indice in valor) {
            let elemento = valor[indice];
            if (elemento instanceof File) {
                esArchivo = true
            }
        }
    }
    else {
        if (valor instanceof File) {
            esArchivo = true
        }
    }

    return esArchivo;
};

const validaAtributo = function(informacion, nombre, valor) {
    if (esArchivo(valor) == true) {
        if (Array.isArray(valor)) {
            for (const indice in valor) {
                let elemento = valor[indice];
                informacion["archivos"].push(elemento)                
            }
        }
        else {
            informacion["archivos"].push(valor)
        }
    }
    else {
        informacion["datos"][nombre] = valor;
    }
    
    return informacion;
};

let prepararOpciones = function( url, dataSend, tipo ) {  
    var method   = tipo.toLocaleLowerCase();
    
    let informacion = {
        'datos'   : {
            '_usuario_': window.$usuario
        },
        'archivos': []
    }

    // Archivos información primer nivel, raiz
    for (const atributo in dataSend) {
        informacion = validaAtributo(informacion, atributo, dataSend[atributo])
    }
    
    // Archivos 
    let archivos = []
    const matcher = function(elemento) {
        return (elemento instanceof File) 
    }
    const cb = function(elemento) {
        archivos.push(elemento)
    }    
    deepFindCallback(dataSend, matcher, cb)
    
    // Forma de datos
    let formaData = new FormData();
    if (method == "post") {        
        formaData.append("datos", JSON.stringify(informacion["datos"]))  
        for (const indice in archivos) {
            formaData.append("archivos", archivos[indice])  
        }
    }
    else {
        //formaData.append("archivos", [])
    }
    
    // Opciones del ajax axios
    const options = {
        method : method,
        url    : url,
        timeout: 600000
    };
    
    if (method == "get") {
        options.headers = { 'content-type': 'application/x-www-form-urlencoded;charset=UTF-8' }
        options.params  = formaData
    }
    else {        
        options.headers = { 'Content-Type': 'multipart/form-data' }
        options.data    = formaData
    }

    return options    
};

let llamadoRest = function( url, params, callback=null, tipo="POST", componente_id=null, error_function_user=null ) {    
    // Opciones de llamado axios
    const options = prepararOpciones( url, params, tipo )
    // Ejecuta llamado
    let data = axios( options ).
        then( respuesta => { 
            const resultado = respuesta.data;
            if (callback != null) {
                callback(resultado, componente_id);
            }

            return resultado;
        }).
        catch( error => {
            /*
            let respuesta = error.response
            if (error_function != null) {
                error_function(respuesta)
            }
            */
    
            let response = {};
            if (error.response) {
                response = {
                    type : "app",
                    error: error.response
                }
            } else if (error.request) {
                response = {
                    type : "request",
                    error: error.request
                }
            } else {
                response = {
                    type : "unkwon",
                    error: error.message
                }
            }

            errorFunction(response);
            
            if (error_function_user != null) {                
                error_function_user(response)
            }            
        })
    
    return data;
};

let llamadoRestGet = function( url, params, callback ) {    
    return llamadoRest( url, params, callback, "GET" );
};

let llamadoRestPost = function( url, params, callback=null, componente_id=null, error_function=null ) {
    return llamadoRest( url, params, callback, "POST", componente_id, error_function)
};

// Llamado sincronico, se usa XMLHttpRequest
let llamadoRestSincGet = function( url, params) {    
    let parametros = '?';
    for (const p in params) {
        parametros += `${p}=${params[p]}&`;
    }
    parametros = parametros.slice(0, -1);
    let ruta   = url + parametros;
    let requerimiento = new XMLHttpRequest();
    requerimiento.open("GET", ruta, false);
    requerimiento.send(null);
    let respuesta;
    if (requerimiento.status === 200) {
        respuesta = requerimiento.responseText;
    }
    
    return JSON.parse(respuesta);
};

var cargaJS = function(url, implementationCode, location){
    var scriptTag = document.createElement('script');
    scriptTag.src = url;

    scriptTag.onload = implementationCode;
    scriptTag.onreadystatechange = implementationCode;

    location.appendChild(scriptTag);
};

export default {
    //prepararParametros : prepararParametros,
    errorFunction      : errorFunction, 
    prepararOpciones   : prepararOpciones,

    http               : axios,
    get                : axios.get,
    post               : axios.post,
    
    llamadoRest        : llamadoRest,
    llamadoRestGet     : llamadoRestGet,
    llamadoRestPost    : llamadoRestPost,
    post_              : llamadoRestPost,

    llamadoRestSincGet : llamadoRestSincGet,

    cargaJS            : cargaJS
};