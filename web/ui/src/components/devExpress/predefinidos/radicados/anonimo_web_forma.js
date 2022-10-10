
import { confirm }       from 'devextreme/ui/dialog';
import visores_archivo   from "../../../../librerias/visores_archivo.js"
import forma_objeto      from '../../forma/utilidades/forma_objeto.js';
import comunes_remitente from '../radicados_comunes/comunes_remitente.js';
import comunes_generales from '../radicados_comunes/comunes_generales.js';

let plantillaAtributos = forma_objeto.plantillaAtributos()

let remitenteUbicacion = [
    comunes_generales.clase_radicado("PQRS"),
    comunes_generales.medio_radicado("WEB"),
    comunes_generales.tipo_web("ANONIMO"),
    comunes_remitente.correo_electronico
]

let grupoUbicacion = forma_objeto.grupo_objeto({
    'titulo'     : 'Remitente ubicación',
    'elementos'  : remitenteUbicacion
});

let grupoAnexos = forma_objeto.grupo_objeto({
    'titulo'     : 'Archivos anexos (word, excel, pdf, gif, png, zip), maximo 25 megas',
    'elementos'  : [
        comunes_generales.mensaje_archivo(plantillaAtributos),
        comunes_generales.archivos_anexos(plantillaAtributos), 
    ]
});

let grupoInformacion = forma_objeto.grupo_objeto({
    'titulo'     : 'Política para el uso y tratamiento de datos personales',
    'elementos'  : [
        comunes_generales.mensaje_informacion(plantillaAtributos), 
        comunes_generales.manejo_informacion
    ]
});

let campos = [
    grupoUbicacion,
    comunes_generales.asunto, 
    grupoAnexos,
    grupoInformacion
]

const limpia_forma = function(formaid) {
    let forma  = $lib.traer_componentes(formaid).formaInstancia
    forma.option("formData", {
        "clase_radicado": "PQRS",
        "medio_radicado": "WEB",
        "tipo_web"      : "ANONIMO",
    })
    let archivo = $lib.traer_componentes(formaid, "archivos_anexos")
    archivo.reset()
}

let forma_id   = "anonimo_web_forma"  
let definicion = {
    'estructura'  : 'radicados_entrada',
    "titulo"      : "Radicación Anonimo",
    'campos'      : campos,
    'plantillaAtributos': plantillaAtributos,
    "nombre_forma": forma_id,
    "botones"     : {
        titulo_crea: "Registrar PeticiÃ³n",
        regresa    : false,
        modifica   : false,
        elimina    : false
    },
    "metodos"     : {
        "retorno_envio": function(respuesta) {
            let nro_radicado = respuesta.resultados.datos.nro_radicado
            limpia_forma(forma_id)
            let resultado    = confirm(("Descarga PDF con información registrada ?"), "PeticiÃ³n " + nro_radicado)
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