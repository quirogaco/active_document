import forma_objeto from '../../../forma/utilidades/forma_objeto.js';

const tipos_plantillas =  [
    { id: "ACTA",               nombre: "ACTA"},
    { id: "ACTA_ELIMINAR",      nombre: "ACTA ELIMINACIÓN"},
    { id: "ALERTA",             nombre: "ALERTA"},
    { id: "CORREO-FAX-PQRS",    nombre: "CORREO, FAX, PQRS"},
    { id: "ENTRADA_ENTREGA",    nombre: "RADICADOS DE ENTRADA, ENTREGA DOCUMENTO EN DEPENDENCIAS"},
    { id: "ENVIAR",             nombre: "LISTADO PARA ENTREGA DE DOCUMENTOS EN VENTANILLA, POR DEPENDENCIA"},
    { id: "HOJA_CONTROL",       nombre: "HOJA_CONTROL"},
    { id: "INDICE_ELECTRONICO", nombre: "INDICE_ELECTRONICO"},
    { id: "INTERNO",            nombre: "RADICADO INTERNO"},
    { id: "LABEL_ENTRADA",      nombre: "LABEL RADICADOS ENTRADA"},
    { id: "LABEL_INTERNO",      nombre: "LABEL RADICADOS INTERNO"},
    { id: "LABEL_SALIDA",       nombre: "LABEL RADICADOS SALIDA"},
    { id: "MENSAJERIA",         nombre: "PLANILLA DE MENSAJERIA"},
    { id: "MENSAJERO",          nombre: "PLANILLA DE MENSAJERO"},
    { id: "PQRS",               nombre: "PLANTILLA RADICADOS PQRS"},
    { id: "RECIBIDOS",          nombre: "RECIBIDOS"},
    { id: "SALIDA",             nombre: "PLANTILLA RADICADO DE SALIDA"},
    { id: "RESPUESTA_RAPIDA",   nombre: "PLANTILLA RADICADO DE RESPUESTA RAPIDA"}    
];

let ruta = 'plantilla';
let plantillaAtributos = forma_objeto.plantillaAtributos()

let campos = [
    forma_objeto.campo_objeto({
        //"ruta"       : ruta,
        "titulo"     : "Nombre", 
        'campo'      : 'nombre',
        'obligatorio': 'si'
    }),
       
    forma_objeto.select_objeto({
        //"ruta"       : ruta,
        "campo"      : "tipo",
        "titulo"     : "Tipo plantilla", 
        "fuente"     : tipos_plantillas,
        "obligatorio": 'si',
        "buscar"     : "si"
    }),

    forma_objeto.archivo_objeto({
        //"ruta"       : ruta,
        "campo"      : "archivos",
        "titulo"     : "Archivo plantilla", 
        "varios"     : "si",
        "obligatorio": 'si',
        "acepta"     : "application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document", 
        //"registrar"  : "si"             
    }, plantillaAtributos),

    forma_objeto.radio_objeto({
        //"ruta"       : ruta,
        "campo"      : "estado_",
        "titulo"     : "Estado", 
        "obligatorio": "si",
        "elementos"  : ["ACTIVO", "INACTIVO"],          
    })
]


let definicion = {
    'estructura'        : 'plantilla',
    "titulo"            : "Información de la plantilla",
    'campos'            : campos,
    'plantillaAtributos': plantillaAtributos,
    'metodos'           : {
        'valida_datos': function() {
            console.log("valida_forma..... función");
            return true;
        }
    }
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;