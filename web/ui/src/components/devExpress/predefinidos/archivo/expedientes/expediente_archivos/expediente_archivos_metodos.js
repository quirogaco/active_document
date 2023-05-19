import visores_archivo from "../../../../../../librerias/visores_archivo.js";
import fuenteDatos 
from '../../../../../../components/devExpress/remoto/fuenteDatos.js';

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

        case "pptx":
            tipo = "Ppoint"
            break

        case "ppt":
            tipo = "Ppoint"
            break


        case "pdf":
            tipo = "Pdf"
            break
    } 

    return tipo
}

const tipo_icono = function(tipo_archivo) {
    let tipo  = tipo_nombre(tipo_archivo) 
    let icono = '<div style="cursor: pointer"> '
    switch (tipo_archivo) {
        case "docx":
            icono += '<i class="far fa-file-word" style="color:blue"></i> '
            break

        case "doc":
            icono += '<i class="far fa-file-word" style="color:blue"></i> '
            break

        case "xlsx":
            icono += '<i class="far fa-file-excel" style="color:blue"></i> '
            break

        case "xls":
            icono += '<i class="far fa-file-excel" style="color:blue"></i> '
            break

        case "pptx":
            icono += '<i class="far fa-file-powerpoint" style="color:blue"></i> '
            break

        case "ppt":
            icono += '<i class="far fa-file-powerpoint" style="color:blue"></i> '
            break

        case "pdf":
            icono += '<i class="far fa-file-pdf" style="color:blue"></i> '
            break

        case "":
            icono += '<i class="far fa-window-close" ></i>  '
            break
        
        default:
            icono += '<i class="far fa-file" style="color:blue"></i> '
            break
    }
    icono += tipo + "</div>"

    return icono
}

async function traer_registro(estructura, id) {

    async function traer_datos(estructura, id) {            
        let opciones_carga = {
            searchExpr     : "id",
            searchOperation: "=",
            searchValue    : id
        }
        
        /// Trae datos del registro del GRID
        async function traeDatos() { 
            let datos = await fuenteDatos.cargaDatosConsulta(
                opciones_carga, 
                "tree", 
                null, 
                estructura
            );
            
            return datos;
        }
        let datos = await traeDatos();
    
        return datos[0];
    }

    return await traer_datos(estructura, id)
}

let metodos = {
    onToolbarPreparing(e) {
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearButton'
        });  
        
        e.toolbarOptions.items.push({
            location: 'after',
            template: 'crearAnexoButton'
        }); 
    },

    mostrar_ventana(parametros) {
        console.log("mostrar_ventana(parametros):", parametros);
        this.emergente_key += 1;
        this.opciones_ventana.alto = parametros.alto;
        this.opciones_ventana.ancho = parametros.ancho;
        this.opciones_ventana.titulo = parametros.titulo;   
        this.opciones_ventana.accion = parametros.accion; 
        this.opciones_ventana.visible = true;
        this.opciones_ventana.modo = this.seleccionado_modo;       
        // Información del registro
        this.opciones_ventana.datos = parametros.datos;
    },

    llamar_ventana(datos={}, modo="crear") {
        let parametros = {};
        this.seleccionado_modo = modo;
        parametros = {
            alto: 560,
            ancho: 800,
            ventana: "archivo_expediente",
            titulo: "Documento del expediente",
            boton_mensaje: "Salvar Documento", 
            accion: "salvar_documento", 
            datos: datos
        }
        this.mostrar_ventana(parametros);      
    },    

    'celda_click': async function(e) {
        //console.log("celda_click:", e)
    },

    'celda_doble_click': async function(e) {
        if (e.column.dataField == "tipo_archivo") {
            let archivo = e.data.archivos[0];
            visores_archivo.ver_descarga_archivo({
                titulo_general: "Consulta de Expedientes",
                archivo_id    : archivo.id, 
                tipo_documento: archivo.tipo_archivo, 
                titulo        : e.data.detalle,
                modo          : "leer",
                descarga      : 'evaluar'
            })   
        }
        else {
            let datos_archivo = await traer_registro(
                "agn_documentos_trd", 
                e.data.id
            );
            delete datos_archivo["datos_archivo"];
            this.parametros["datos_archivo"] = datos_archivo;
            this.parametros["datos_archivo"]["padre_id"] = null;
            this.parametros["datos_archivo"]["padre_nombre"] = null;
            this.llamar_ventana(this.parametros, "modificar");
        }
    },

    'crear':  function(e) {
        this.parametros["datos_archivo"] = {
            "padre_id": null,
            "padre_nombre": null
        }
        this.llamar_ventana(this.parametros, "crear")
    },


    'crearAnexo':  function(e) {
        let seleccionados = this.grid_archivos.getSelectedRowsData();
        if (seleccionados.length > 0) {                                    
            let seleccionado = seleccionados[0];
            console.log("--> crearAnexo <--", seleccionado)
            let padre_id = (
                seleccionado.padre_id ? 
                    seleccionado.padre_id : seleccionado.id
            );
            let padre_nombre = (
                seleccionado.detalle + " - "+ seleccionado.tipo_nombre 
            );
            this.parametros["datos_archivo"] = {   
                "padre_id": padre_id,
                "padre_nombre": padre_nombre 
            }
            this.llamar_ventana(this.parametros, "crear")
        }
        else {
            this.notify("Seleccione un documento !", "warning") 
        }
    },

    ejecutar_operacion(operacion, padre_id, datos) {
        switch (operacion) {
            case 'salvar': 
                if (padre_id =="") {
                    this.insertar_nodo(-1, datos)
                }
                else {
                    this.insertar_nodo(padre_id, datos)
                } 
                break

            case 'modificar': 
                this.modificar_nodo(padre_id, datos)
                break  

            case 'borrar': 
                this.borrar_nodo(padre_id, datos)
                break 
        }
        window.$ventana_emergente_trd.opciones.visible = false   
        this.notify("Operación realizada correctamente", "success") 
    },
    
    plantilla_icono: function(data) {
        let resultado =  tipo_icono(data.value)        
        return resultado
    }
}

export default metodos;