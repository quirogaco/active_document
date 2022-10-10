import forma_objeto      from '../../forma/utilidades/forma_objeto.js';

let basicos = forma_objeto.mostrar_datos([
    {
        "campo" : "clase_radicado",
        "titulo": "Clase de radicado"
    },
    {
        "campo" : "canal_radicado_nombre",
        "titulo": "Canal de recepción"
    },
    {
        "campo" : "nro_radicado",
        "titulo": "Número de radicado"
    },
    {
        "campo" : "fecha_radicado",
        "titulo": "Fecha de radicado"
    },
    {
        "campo"  : "radicado_remitente",
        "titulo" : "Radicado documento recibido"
    },
    {
        "campo"  : "fecha_documento",
        "titulo" : "Fecha documento recibido"
    },    
    {
        "campo" : "nro_folios",
        "titulo": "Número de folios"
    },   
    {
        "campo"  : "anexos",
        "titulo" : "Anexos",
        "tipo"   : "texto_grande"
    },
    {
        "campo"  : "asunto",
        "titulo" : "Asunto",
        "tipo"   : "texto_grande"
    },
    {
        "campo" : "empresa_mensajeria_nombre",
        "titulo": "Empresa mensajeria"
    },
    {
        "campo" : "numero_guia",
        "titulo": "Número de guia"
    },
    {
        "campo" : "medio_notificacion",
        "titulo": "Medio notificación"
    },
    {
        "campo"  : "radicado_en_nombre",
        "titulo" : "Radicado en", 
    },
    {
        "campo"  : "radicado_por_nombre",
        "titulo" : "Radicado por", 
    },
    {
        "campo"  : "entidad_traslada",
        "titulo" : "Entidad que traslada", 
    },
    {
        "campo"  : "persona_traslada",
        "titulo" : "Persona que traslada", 
    }
])

let grupoBasico = forma_objeto.grupo_objeto({
    'titulo'   : 'Información basica del documento',
    'elementos': basicos
});


export default {
    grupoBasico: grupoBasico
}