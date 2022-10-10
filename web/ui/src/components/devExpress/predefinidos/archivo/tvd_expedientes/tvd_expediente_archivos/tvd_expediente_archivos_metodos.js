import visores_archivo from "../../../../../../librerias/visores_archivo.js"

const tipo_nombre = function(tipo_archivo) {
    let tipo = tipo_archivo
    switch (tipo_archivo) {
        case "docx":
            tipo = "Word"
            break

        case "doc":
            tipo = "Word"
            break

        case "xlsx":
            tipo = "Excel"
            break

        case "xls":
            tipo = "Excel"
            break

        case "pdf":
            tipo = "Pdf"
            break
    } 

    return tipo
}

const tipo_icono = function(tipo_archivo) {
    let tipo  = tipo_nombre(tipo_archivo) 
    let icono = ''
    switch (tipo_archivo) {
        case "docx":
            icono = '<div style="cursor: pointer"> <i class="far fa-file-word" style="color:blue; cursor: pointer"></i> ' + tipo + "</div>"
            break

        case "doc":
            icono = '<div style="cursor: pointer"> <i class="far fa-file-word" style="color:blue"></i> ' + tipo + "</div>"
            break

        case "xlsx":
            icono = '<div style="cursor: pointer"> <i class="far fa-file-excel" style="color:blue"></i> ' + tipo + "</div>"
            break

        case "xls":
            icono = '<div style="cursor: pointer"> <i class="far fa-file-excel" style="color:blue"></i> ' + tipo + "</div>"
            break

        case "pdf":
            icono = '<div style="cursor: pointer"> <i class="far fa-file-pdf" style="color:blue"></i> ' + tipo + "</div>"
            break
        
        default:
            icono = '<div style="cursor: pointer"> <i class="fas fa-file"></i> ' + tipo  + "</div>"
            break
    } 

    return icono
}

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        })      
    },

    'fila_doble_click':  function(e) {
        console.log("fila_doble_click:", e)        
    },    

    'celda_doble_click':  function(e) {
        console.log("celda_doble_click:", e)
        if (e.column.dataField == "tipo_archivo") {
            let archivo = e.data.archivos[0]
            visores_archivo.ver_descarga_archivo({
                titulo_general: "Consulta de Expedientes TVD",
                archivo_id    : archivo.id, 
                tipo_documento: archivo.tipo_archivo, 
                titulo        : e.data.detalle,
                modo          : "leer",
                descarga      : 'evaluar'
            })   
        }
        else {
            // editar registro
        }
    },

    'crear':  function(e) {
        this.llamar_ventana({}, "crear")
    },

    mostrar_ventana(parametros) {
        this.emergente_key += 1;            
        this.opciones_ventana.alto               = parametros.alto 
        this.opciones_ventana.ancho              = parametros.ancho
        this.opciones_ventana.componente_visible = parametros.ventana  
        this.opciones_ventana.titulo             = parametros.titulo   
        this.opciones_ventana.accion             = parametros.accion  
        this.opciones_ventana.visible            = true
        this.opciones_ventana.modo               = this.seleccionado_modo        
        // Información del registro
        this.opciones_ventana.datos              = parametros.datos
    },

    llamar_ventana(datos={}, modo="crear") {
        let parametros         = {}
        this.seleccionado_modo = modo
        parametros = {
            //alto         : 650,
            ancho        : 800,
            ventana      : "tvd_archivo_expediente",
            titulo       : "Documento del Expediente",
            boton_mensaje: "Salvar Documento", 
            accion       : "salvar_documento", 
            datos        : datos
        }
        this.mostrar_ventana(parametros)      
    },    
    
    plantilla_icono: function(data) {
        let resultado =  tipo_icono(data.value)
        
        return resultado
    }
}

export default metodos;