import { confirm } from 'devextreme/ui/dialog';
import visores_archivo from "../../../../librerias/visores_archivo.js"
import forma_objeto from '../../forma/utilidades/forma_objeto.js';
import comunes_remitente from '../radicados_comunes/comunes_remitente.js';
import comunes_generales from '../radicados_comunes/comunes_generales.js';

let plantillaAtributos = forma_objeto.plantillaAtributos()

let identificacion = [
    comunes_remitente.busca_remitente,    
    comunes_remitente.tipo_tercero_id,
    comunes_remitente.razon_social,
    comunes_remitente.nit_nro_identificacion,
    comunes_remitente.nombres,
    comunes_remitente.apellidos
]

let grupoIdentificacion = forma_objeto.grupo_objeto({
    'titulo': 'Remitente identificación',
    'elementos': identificacion
});


let remitenteUbicacion = [
    comunes_generales.clase_radicado("PQRSD"),
    comunes_generales.medio_radicado("WEB"),
    comunes_generales.tipo_web("JURIDICA"),
    comunes_generales.medio_notificacion,
    comunes_remitente.correo_electronico,
    comunes_remitente.direccion,
    comunes_remitente.telefono,
    comunes_remitente.ciudad_id,   
]


let grupoUbicacion = forma_objeto.grupo_objeto({
    'titulo'     : 'Remitente ubicación',
    'elementos'  : remitenteUbicacion
});

let grupoAnexos = forma_objeto.grupo_objeto({
    'titulo'     : 'Archivos anexos',
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


let campos = [
    // Falta datos de consulta
    grupoIdentificacion,
    grupoUbicacion,
    comunes_generales.asunto, 
    grupoAnexos,
    grupoInformacion
]

const limpia_forma = function(formaid) {
    let forma  = $lib.traer_componentes(formaid).formaInstancia
    forma.option("formData", {
        "clase_radicado": "PQRSD",
        "medio_radicado": "WEB",
        "tipo_web": "JURIDICA",
    })
    let archivo = $lib.traer_componentes(formaid, "archivos_anexos")
    archivo.reset()
}

let forma_id = "radicado_juridica_forma"
let definicion = {
    'estructura'  : 'radicados_entrada',
    "titulo"      : "Radicación Persona JURIDICA",
    'campos'      : campos,
    'plantillaAtributos': plantillaAtributos,
    "nombre_forma": "radicado_juridica_forma",   
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
    "eventos"     : {        
        "montado": function(objeto) {    
            //$lib.forma_atributo_item("radicado_juridica_forma", "busca_remitente", "visible", false);          
            let forma = $lib.traer_componentes(forma_id).formaInstancia 

            // Campos obligatorios            
            $lib.forma_atributo_item(forma_id, "tercero_nro_identificacion", "validationRules", [{type: "required", message: "Nit es obligatorio"}], false);
            $lib.forma_atributo_item(forma_id, "tercero_correo_electronico", "validationRules", [{type: "required", message: "Correo es obligatorio"}], false);
            $lib.forma_atributo_item(forma_id, "medio_notificacion", "validationRules", [{type: "required", message: "Medio de notificación es obligatorio"}], false);
            $lib.forma_atributo_items(forma_id, ["tercero_nro_identificacion", "tercero_correo_electronico", "medio_notificacion"], "isRequired", true, false); 
            forma.repaint()        

            // Tipo de tercero filtro
            let ds = $lib.traer_fuente_datos(forma_id, "tercero_tipo_tercero_id")
            ds.filter(["tipo", "=", "JURIDICA"])             
        }
    }
}

let componente = forma_objeto.forma_objeto_crud(definicion);

export default componente;