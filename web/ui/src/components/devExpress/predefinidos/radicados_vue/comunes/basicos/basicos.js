import forma_definiciones     from "../../../comunes_vue/forma/forma.js"

const fecha_documento = function(id=null, atributos={}) {
    let id_campo  = $lib.valor_defecto(id, "fecha_documento")
    let base      = {titulo: 'Fecha del documento', 'obligatorio': true, ancho:150}
    var atributos = Object.assign({}, base);

    let campo = forma_definiciones.fecha(
        id_campo,
        atributos
    )

    return campo
}
    forma_definiciones.fecha('fecha_documento',   {titulo: 'Fecha del documento', 'obligatorio': true, ancho:150}),
    forma_definiciones.texto('radicado_responde', {titulo: 'Responde radicado', "mensaje": "Digite radicado de entrada",ancho:300}),
    forma_definiciones.entero('nro_folios',       {titulo: 'Número de folios', "mensaje": "Número de hojas fisicas", ancho:50}),
    forma_definiciones.texto_area('asunto',           {titulo: 'Asunto del documento', "mensaje": "Resumen del contenido del documento"}),
    forma_definiciones.texto_area('anexos',           {titulo: 'Anexos', "mensaje": "Anexos fisicos que vienen con el documemto (ej. Cd, libro, etc)"}),

export default {
    fecha     : fecha.campo,
    grupo     : grupo.campo,
    texto     : texto.campo,
    entero    : entero.campo,
    texto_area: texto_area.campo
}