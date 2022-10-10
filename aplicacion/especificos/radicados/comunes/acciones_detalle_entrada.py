#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

acciones_entrada = {
    # RADICACION (TODOS)
    "RADICAR": {
        "PROCESO"       : "RADICACION",
        "ACCION"        : "RADICAR",
        "MENSAJE"       : "RADICACIÓN, %s ",     
        "MEZCLA"        : "SI",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI", # PQRS O VENTANILLA
        "ESTADO"        : "RADICADO",
        "MENSAJE_ESTADO": "DOCUMENTO RADICADO" 
    },

    # RADICACION Y ASIGNACIÓN DE DEPENDENCIA RESPONSABLE (PQRS, VENTANILLA)
    "RADICAR_ASIGNAR_DEPENDENCIA": {
        "PROCESO"       : "RADICACION",
        "ACCION"        : "ASIGNA DEPENDENCIA",
        "MENSAJE"       : "SE ASIGNA DEPENDENCIA AL RADICADAR",     
        "MEZCLA"        : "SI",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "ASIGNADO",
        "MENSAJE_ESTADO": "ASIGNADO DEPENDENCIA" 
    },

    # RADICACION Y TRASLADO PARA ASIGNACIÓN (PQRS, VENTANILLA)
    "RADICAR_TRASLADA_DEPENDENCIA": {
        "PROCESO"       : "RADICACION",
        "ACCION"        : "TRASLADA DEPENDENCIA",
        "MENSAJE"       : "SE TRASLADA A DEPENDENCIA PARA SU ASIGNACIÓN",     
        "MEZCLA"        : "SI",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "TRASLADADO",
        "MENSAJE_ESTADO": "TRASLADADO DEPENDENCIA" 
    },

    "ASIGNAR_DEPENDENCIA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "ASIGNAR DEPENDENCIA",
        "MENSAJE"       : "SE ASIGNA DEPENDENCIA POR COMPETENCIA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "ASIGNADO_DEPENDENCIA",
        "MENSAJE_ESTADO": "ASIGNAR RESPONSABLE"
    },

    "ASIGNAR_RESPONSABLE": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "ASIGNAR PETICIÓN RESPONSABLE",
        "MENSAJE"       : "SE ASIGNA RESPONSABLE COMPETENCIA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",   
        "ESTADO"        : "ASIGNADO_RESPONSABLE",
        "MENSAJE_ESTADO": "GESTION"     
    },

    "SELECCION_PLANTILLA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "ASIGNAR BORRADOR RESPUESTA",
        "MENSAJE"       : "SE ASIGNA BORRADOR RESPUESTA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",   
        "ESTADO"        : "ASIGNADO_RESPONSABLE",
        "MENSAJE_ESTADO": "GESTION"     
    },

    "HABILITAR_RESPUESTA_RAPIDA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "HABILITAR RESPUESTA RAPIDA",
        "MENSAJE"       : "SE ASIGNA RESPONSABLE POR COMPETENCIA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "ASIGNADO_RESPONSABLE",
        "MENSAJE_ESTADO": "GESTION"          
    },

    "DEVOLVER_DEPENDENCIA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "DEVOLVER A DEPENDENCIA ASIGNADORA",
        "MENSAJE"       : "SE DEVUELVE A DEPENDENDENCIA ASIGNADORA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "DEVUELTO_ASIGNADORA",
        "MENSAJE_ESTADO": "ASIGNAR DEPENDENCIA"          
    },

    "DEVOLVER_ASIGNADOR": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "DEVOLVER A FUNCIONARIO ASIGNADOR",
        "MENSAJE"       : "SE DEVUELVE A FUNCIONARIO ASIGNADOR",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "DEVUELTO_ASIGNADOR",
        "MENSAJE_ESTADO": "ASIGNAR RESPONSABLE"           
    },

    "TRASLADAR_DEPENDENCIA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "TRASLADAR A DEPENDENCIA",
        "MENSAJE"       : "SE TRASLADA A DEPENDENCIA RESPONSABLE",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "TRASLADO_DEPENDENCIA",
        "MENSAJE_ESTADO": "ASIGNAR RESPONSABLE"          
    },

    "FINALIZAR_MANUAL": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "FINALIZA GESTIÓN",
        "MENSAJE"       : "FINALIZA GESTIÓN DE LA PETICIÓN",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "NO",
        "ESTADO"        : "FINALIZADO_MANUAL",
        "MENSAJE_ESTADO": "FINALIZADO"        
    },

    "ENVIAR_VISTO_BUENO": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "SE ENVIA A VISTO BUENO",
        "MENSAJE"       : "SE ENVIA A VISTO BUENO",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "VISTO_BUENO",
        "MENSAJE_ESTADO": "VISTO BUENO"         
    },

    "SOLICITAR_RESPUESTA_COLABORATIVA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "SOLICITAR RESPUESTA COLABORATIVA",
        "MENSAJE"       : "SE SOLICITA RESPUESTA COLABORATIVA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "SOLICITADO_COLABORATIVA",
        "MENSAJE_ESTADO": "ASIGNAR RESPONSABLE"          
    },

    "HABILITAR_RESPUESTA_RAPIDA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "HABILITAR RESPUESTA RAPIDA",
        "MENSAJE"       : "SE HABILITA RESPUESTA RAPIDA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "HABILITADO_RAPIDA",
        "MENSAJE_ESTADO": "GESTION"       
    },

    "DEVOLVER_REVISION": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "DEVOLVER PARA REVISIÓN",
        "MENSAJE"       : "SE DEVUELVE PARA REVISIÓN",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "DEVUELTO_REVISION",
        "MENSAJE_ESTADO": "DEVUELTO REVISIÓN"              
    },
    
    "APROBAR_RADICAR": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "APROBAR PARA RADICAR",
        "MENSAJE"       : "SE APRUEBA PARA RADICACIÓN",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "APROBADO_RESPUESTA",
        "MENSAJE_ESTADO": "APROBADO RESPUESTA" 
    },

    "RADICAR_DOCUMENTO": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "RADICAR DOCUMENTO",
        "MENSAJE"       : "SE RADICA DOCUMENTO",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "RADICADO_DOCUMENTO",
        "MENSAJE_ESTADO": "DOCUMENTO RADICADO"          
    },

    "ASIGNAR_RESPONSABLE_RESPUESTA_COLABORATIVA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "ASIGNAR RESPONSABLE RESPUESTA COLABORATIVA",
        "MENSAJE"       : "SE ASIGNA RESPONSABLE RESPUESTA COLABORATIVA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "ASIGNADO_RESPONSABLE_COLABORATIVA",
        "MENSAJE_ESTADO": "GESTION"          
    },

    "FINALIZAR_RESPUESTA_COLABORATIVA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "FINALIZAR RESPUESTA COLABORATIVA",
        "MENSAJE"       : "SE FINALIZA RESPUESTA COLABORATIVA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",        
        "ESTADO"        : "FINALIZADA_COLABORATIVA",
        "MENSAJE_ESTADO": "FINALIZADA"         
    }
    
}