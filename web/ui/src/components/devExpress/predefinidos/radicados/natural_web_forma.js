import { confirm }       from 'devextreme/ui/dialog';
import visores_archivo   from "../../../../librerias/visores_archivo.js"
import forma_objeto      from '../../forma/utilidades/forma_objeto.js';
import comunes_remitente from '../radicados_comunes/comunes_remitente.js';
import comunes_generales from '../radicados_comunes/comunes_generales.js';
import comunes_clasifica from '../radicados_comunes/comunes_clasifica.js';

let plantillaAtributos = forma_objeto.plantillaAtributos()

let identificacion = [    
    comunes_remitente.tipo_identificacion_id,
    comunes_remitente.nro_identificacion,
    comunes_remitente.nombres,
    comunes_remitente.apellidos
]

let grupoIdentificacion = forma_objeto.grupo_objeto({
    'titulo'     : 'Remitente identificación',
    'elementos'  : identificacion
});


let remitenteUbicacion = [
    comunes_generales.clase_radicado("PQRSD"),
    comunes_generales.medio_radicado("WEB"),
    comunes_generales.tipo_web("NATURAL"),
    comunes_generales.medio_notificacion,
    comunes_remitente.correo_electronico,
    comunes_remitente.direccion,
    comunes_remitente.telefono,
    comunes_remitente.ciudad_id
]


let grupoUbicacion = forma_objeto.grupo_objeto({
    'titulo'     : 'Remitente ubicación',
    'elementos'  : remitenteUbicacion
})

let grupoAnexos = forma_objeto.grupo_objeto({
    'titulo'     : 'Archivos anexos (word, excel, pdf, gif, png, zip), maximo 25 megas',
    'elementos'  : [
        comunes_generales.mensaje_archivo(plantillaAtributos),
        comunes_generales.archivos_anexos(plantillaAtributos)
    ]
})

let grupoInformacion = forma_objeto.grupo_objeto({
    'titulo'     : 'Política para el uso y tratamiento de datos personales',
    'elementos'  : [
        comunes_generales.mensaje_informacion(plantillaAtributos), 
        comunes_generales.manejo_informacion
    ]
})

let clasificacion = [
    comunes_clasifica.tipo_ciudadano_id,
    comunes_clasifica.discapacidad_id,
    comunes_clasifica.poblacion_id,
    comunes_clasifica.genero_id,
    comunes_clasifica.rango_id,    
]

let grupoClasificacion = forma_objeto.grupo_objeto({
    'titulo'     : 'Información Clasificación',
    'elementos'  : clasificacion
});

let campos = [
    // Falta datos de consulta
    grupoIdentificacion,
    grupoUbicacion,
    comunes_generales.asunto, 
    grupoAnexos,    
    grupoClasificacion,
    grupoInformacion
]

const limpia_forma = function(formaid) {
    let forma  = $lib.traer_componentes(formaid).formaInstancia
    forma.option("formData", {
        "clase_radicado": "PQRSD",
        "medio_radicado": "WEB",
        "tipo_web"      : "NATURAL",
    })
    let archivo = $lib.traer_componentes(formaid, "archivos_anexos")
    archivo.reset()
}

let forma_id   = "natural_web_forma"  
let definicion = {
    'estructura'  : 'radicados_entrada',
    "titulo"      : "Radicación Persona Natural",
    'campos'      : campos,
    'plantillaAtributos': plantillaAtributos,
    "nombre_forma": forma_id,
    "botones"     : {
        titulo_crea: "Registrar Petición",
        regresa    : false,
        modifica   : false,
        elimina    : false       
    },
    "metodos"     : {
        "retorno_envio": function(respuesta) {
            let nro_radicado = respuesta.resultados.datos.nro_radicado
            limpia_forma(forma_id)
            let resultado    = confirm(("Descarga PDF con información registrada ?"), "Petición " + nro_radicado)
            resultado.then(dialogo => {
                if (dialogo == true) {
                    visores_archivo.ver_descarga_archivo({
                        archivo_id    : ("ENTRADA__" + nro_radicado), 
                        tipo_documento: "pdf", 
                        descarga      : 'si',
                        operacion     : 'radicado_pdf'
                    })   
                }
            })
        }
    },
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;