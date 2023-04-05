import forma_objeto          from '../../forma/utilidades/forma_objeto.js';
import comunes_remitente     from './comunes_remitente.js';
import comunes_generales     from './comunes_generales.js';

// ### Grupo identificacion //
let identificacion = [
    comunes_remitente.tipo_entidad_id,
    comunes_remitente.razon_social,
    comunes_remitente.nit,
    comunes_remitente.nombres,
    comunes_remitente.apellidos
]

let grupoIdentificacion = forma_objeto.grupo_objeto({
    'titulo'     : 'Remitente identificación',
    'elementos'  : identificacion
});

// ### Grupo ubicación //
let remitenteUbicacion = [
    comunes_generales.clase_radicado("PQRS"),
    comunes_generales.canal_radicado("WEB"),
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

// ### Grupo detalle anexos //
let detalleAnexos = [
    comunes_generales.asunto, 
]

let grupoDetalle = forma_objeto.grupo_objeto({
    'titulo'     : 'Detalle y Anexos',
    'elementos'  : detalleAnexos
});

export default {
    grupoIdentificacion: grupoIdentificacion,
    grupoUbicacion     : grupoUbicacion,
    grupoDetalle       : grupoDetalle,
}