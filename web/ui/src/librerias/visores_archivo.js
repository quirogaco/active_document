//#####################################
// Maneja llamado de visores archivos #
//#####################################
import descarga_archivo_clase from './descarga_archivo';
import librerias from './librerias';

const descargar_archivo_remoto = function(url, datos, title, method="get", llamar_funcion=null) {    
    window.$ns['aplicacion'].asignaAtributoDinamico("mensaje_carga", "Descargando archivo, por favor esperar")
    window.$ns['aplicacion'].asignaAtributoDinamico("indicador_visible", true)
    window.$ns['aplicacion'].indicador_visible = true
    const descarga = new descarga_archivo_clase({
        data     : datos,
        url      : url,
        autoStart: true,
        filename : title,
        method   : method
    })
    .then(function () {
        window.$ns['aplicacion'].asignaAtributoDinamico("indicador_visible", false)
        window.$ns['aplicacion'].indicador_visible = false
        if (llamar_funcion != null) {
            llamar_funcion()
        } 
    })
    .catch(function (error) {
        window.$ns['aplicacion'].asignaAtributoDinamico("indicador_visible", false)
        window.$ns['aplicacion'].indicador_visible = false
    });
}

const tipo_documento = function(tipo_documento) {
    let tipo = tipo_documento
    if (tipo_documento == "pdf") {
        tipo = "pdf"
    }
    else {
        //
    }

    return tipo
}

let contador_archivos = 0;
const descargar_archivo = function(e) {
    let datos  = ( e.datos.datos !== undefined) ? e.datos.datos : {};
    let url    = "";
    let tipo   = tipo_documento(e.tipo_documento);
    let titulo = 'archivo_descargado_' + contador_archivos + "." + e.tipo_documento;
    if ( tipo == "pdf" ) {
        // '/manejo_pdf/{operacion}/{clase}/{descarga}/{pdf_id}'
        url = window.$ruta_pdf;        
    }
    else {
        //  '/manejo_archivo/{operacion}/{clase}/{descarga}/{archivo_id}'
        url = window.$ruta_archivos;
    }    
    let operacion = (e.datos.operacion !== undefined) ? e.datos.operacion : "sistema"
    let clase     = (e.datos.clase     !== undefined) ? e.datos.clase     : "archivo"
    let descarga  = (e.datos.descarga  !== undefined) ? e.datos.descarga  : "no"
    // e.datos.operacion = funcion remota a llamar desde $ruta_pdf o $ruta_archivo
    // e.datos.clase     = tipo de elemento por defecto "archivo"
    // e.datos.descarga  = Si descarga el archivo si,no
    // e.datos.idArchivo = identificador unico del archivos
    url += operacion + '/' + clase + '/' + descarga + '/' + e.datos.idArchivo + '?_=' + Date.now();
    descargar_archivo_remoto(url, datos, titulo, "get", e.datos.llamar_funcion)    
}

let tipos_visor_archivo = [
    "doc",
    "docx",
    "xls",
    "xlsx"
]

const evaluar_modo = function(parametros) {
    let llamar = "descargar"
    if ( tipos_visor_archivo.indexOf( parametros.tipo_documento ) > -1 ) { 
        llamar = "visor_archivo"
    }
    else{
        if (parametros.tipo_documento == "pdf") {
            llamar = "visor_pdf"
        }
    }

    return llamar
}

const llama_visor_descarga = function(e) {  
    contador_archivos += 1;
    e.tipo_documento   = e.tipo_documento.toLowerCase()
    let descarga       = ( (e.datos.descarga == "no") || (e.datos.descarga == "si") || (e.datos.descarga == "evaluar") ? e.datos.descarga : "si");
    if (descarga == "evaluar") {
        let llamar = evaluar_modo(e)
        e.datos.descarga = "no"
        e.editor         = 'sistema'
        switch (llamar) {
            case "visor_pdf":                
                window.$emitter.emit('mostrar_pdf_sistema', e.datos)
                break

            case "visor_archivo":
                let datos_visor = window.$lib.prepara_datos_visor_archivo(e)
                window.$ns['aplicacion'].mostrar_visor_archivos_sistema(datos_visor)
                break

            default:
                e.datos.descarga = "si";
                descargar_archivo(e)  
                break
        }
    }
    else {
        // Validar valor descarga
        if (descarga == "no") {        
            if (  (e.tipo_documento == 'pdf') && (e.editor == 'sistema') ) {
                window.$emitter.emit('mostrar_pdf_sistema', e.datos)
            } 
        }
        else {
            // Evaluar descarga archivos,descarga == "evaluar"
            e.datos.descarga = "si";
            descargar_archivo(e)        
        }
    }
}

const iniciar = function() {
    window.$emitter.on(
        'mostrar_archivo', 
        llama_visor_descarga
    )
}

const ver_descarga_archivo = function(
    {
        archivo_id     = null, 
        tipo_documento = 'pdf', 
        operacion      = 'sistema', 
        clase          = 'archivo', 
        descarga       = 'no', 
        buscar         = '',
        modo           = 'lectura',
        editor         = 'sistema',
        titulo         = "",
        titulo_general = "",
        llamar_funcion = null     
    } = {},
) {
    
    let parametros = window.$lib.prepara_parametros_archivo(
        {
            archivo_id     : archivo_id, 
            tipo_documento : tipo_documento, 
            operacion      : operacion, 
            clase          : clase, 
            descarga       : descarga, 
            buscar         : buscar,
            modo           : modo, 
            editor         : editor,
            titulo         : titulo,
            titulo_general : titulo_general,
            llamar_funcion : llamar_funcion
        }
    )    
    window.$emitter.emit('mostrar_archivo', parametros)
}

//********************************//
// LIBRERIAS: Visor de documentos //
//********************************//
let word_tipo = [
    "doc",
    "docx"
]

let excel_tipo = [
    "xls",
    "xlsx"
]

let definir_tipo_documento = function(extension) {
    let tipo = "word"
    if ( excel_tipo.indexOf( extension ) > -1 ) { 
        tipo = "cell"
    }

    return tipo
}

let definir_modo_visor = function(modo) {
    let respuesta = "view"
    if ( modo == "editar" ) { 
        respuesta = "edit"
    }

    return respuesta
}

const prepara_datos_visor_archivo = function(parametros) {
    let lectura_base   = ( parametros.lectura != undefined )   ? parametros.lectura  : "entregar_archivo_minio"
    let escritura_base = ( parametros.escritura != undefined ) ? parametros.escritura: "salvar_archivo_minio"
    let id_extendido   = parametros.datos.idArchivo + "___" + librerias.uuidv4()
    let lectura        = window.$direcciones.servidorDatos + "/" + lectura_base + "/" + id_extendido
    let escritura      = window.$direcciones.servidorDatos + "/" + escritura_base

    let datos = {
        id_extendido  : id_extendido,
        titulo        : parametros.titulo_general, // titulo general                
        tipo_documento: definir_tipo_documento(parametros.tipo_documento),
        archivo_id    : parametros.datos.idArchivo,
        documento     : {
            tipo_archivo: parametros.tipo_documento,
            titulo      : parametros.titulo,
            lectura_url : lectura,
            clave       : parametros.datos.idArchivo,
        },

        editor        : {
            modo      : definir_modo_visor(parametros.modo),
            salvar_url: escritura
        }
    }

    return datos
}

const prepara_parametros_archivo = function({
    archivo_id     = null, 
    tipo_documento = 'pdf', 
    operacion      = 'sistema', 
    clase          = 'archivo', 
    descarga       = 'no', 
    buscar         = '',
    modo           = 'lectura',
    editor         = 'sistema',
    titulo         = "",
    titulo_general = "",
    llamar_funcion = null
} = {}) {
    // Datos especificos del visor
    let datos  = {
        idArchivo     : archivo_id, // id objeto a descargar o mostrar
        operacion     : operacion, // funcion remota que descarga los archivos
        clase         : clase, // archivo por ahora
        descarga      : descarga, // opcional, no por defecto
        buscarTexto   : ( (buscar != "") && (buscar !== undefined) ? buscar : ""), // buscar en pdf
        titulo        : titulo,
        titulo_general: titulo_general,
        llamar_funcion: llamar_funcion         
    }   
    
    // Parametros generales
    let parametros = {
        'tipo_documento': tipo_documento,
        'modo'          : modo,
        'editor'        : editor,
        'titulo'        : titulo,
        'titulo_general': titulo_general,
        'datos'         : datos     
    }

    return parametros
}

const unifica_datos_visor = function({
    archivo_id     = null, 
    tipo_documento = 'pdf', 
    operacion      = 'sistema', 
    clase          = 'archivo', 
    descarga       = 'no', 
    buscar         = '',
    modo           = 'lectura',
    editor         = 'sistema',
    titulo         = "",
    titulo_general = ""     
} = {}) {

    let parametros = prepara_parametros_archivo(
        {
            archivo_id     : archivo_id, 
            tipo_documento : tipo_documento, 
            operacion      : operacion, 
            clase          : clase, 
            descarga       : descarga, 
            buscar         : buscar,
            modo           : modo, 
            editor         : editor,
            titulo         : titulo,
            titulo_general : titulo_general
        }
    )
    parametros = prepara_datos_visor_archivo(parametros)

    return parametros
}


export default {
    iniciar                    : iniciar,
    descargar_archivo_remoto   : descargar_archivo_remoto,
    ver_descarga_archivo       : ver_descarga_archivo,
    prepara_datos_visor_archivo: prepara_datos_visor_archivo,
    prepara_parametros_archivo : prepara_parametros_archivo,
    unifica_datos_visor        : unifica_datos_visor,
}