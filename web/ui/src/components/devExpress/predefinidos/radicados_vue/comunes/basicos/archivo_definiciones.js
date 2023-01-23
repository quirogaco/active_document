import forma_definiciones from "../../../comunes_vue/forma/forma.js";
import visores_archivo from "../../../../../../librerias/visores_archivo.js";

const mensaje_archivo = function(id=null, atributos={}) {
    let atributos_base = {
        "valor":  `
            <div class="shadow-sm p-3 m-3 rounded ">
                <div class="fs-6">
                    Los anexos permitidos son de tipo <b>(word, excel, pdf, gif, png, zip)</b>,      
                    <b>Tamaño individual maximo de 20 megas</b>,     
                    <b>Tamaño total maximo 25 megas (sumatoria de todos los archivos)</b>.
                    Prepare sus archivos en una carpeta comun.
                </div>
            </div>
        `,
        'template': "contenido-template"
    };
    
    return forma_definiciones.genera_campo("contenido", "mensaje_archivo", id, atributos_base, atributos)
};

let acepta_archivos = [
    ".doc", ".docx", ".xls", ".xlsx", ".pdf", ".zip",
    ".gif", ".png", ".bmp", ".jpg", ".jpeg",
    ".avi", ".mp3"
];
const archivos_anexos = function(id=null, atributos={}) {
    let atributos_base = {
        'titulo'       : 'Anexos electrónicos',
        "multiple"     : true,
        "tamano_maximo": 25000000,
        'extensiones'  : acepta_archivos
    }
    
    return forma_definiciones.genera_campo("archivo", "archivos", id, atributos_base, atributos)
};


// Anexos consulta
let columnas = [
    {
        'dataField': 'detalle',
        'caption'  : 'Descripción',
        'width'    : 350,
    },
    {
        'dataField': 'tipo_archivo',
        'caption'  : 'Tipo',
        'width'    : 60,
    },
    {
        'dataField': 'creado_en_',
        'caption'  : 'Creado en',
        'width'    : 150,
    },     
    {
        'dataField': 'tamano',
        'caption'  : 'Tamaño bytes',
        'width'    : 100,
    },     
    {
        'dataField': 'folios',
        'caption'  : 'Folios',
        'width'    : 60,
    },  
    {
        'dataField': 'creado_por_nombre',
        'caption'  : 'Creado por',
        'width'    : 300,
    },     
];

const anexos_radicado = function(id=null, atributos={}) {
    let atributos_base = {
        "columnas": columnas,
        "eventos": {
            "fila_doble_click": function(objecto, definicion, forma, forma_id) {
                visores_archivo.ver_descarga_archivo({
                    titulo_general: "Consulta de Documentos/Anexos RADICADO",
                    archivo_id    : objecto.data.id, 
                    tipo_documento: objecto.data.tipo_archivo, 
                    titulo        : objecto.data.detalle,
                    modo          : "leer",
                    descarga      : 'evaluar'
                })  
            },
        },
        "fuente": []
    }
    
    return forma_definiciones.genera_campo("grid", "anexos_radicado", id, atributos_base, atributos)
};

export default {
    archivos_anexos: archivos_anexos,
    mensaje_archivo: mensaje_archivo,
    anexos_radicado: anexos_radicado
}