#!/usr/bin/python
# -*- coding: utf-8 -*-
 
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

    "ANEXA_ARCHIVO": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "ANEXA ARCHIVO ELECTRONICO",
        "MENSAJE"       : "SE ANEXA ARCHIVO",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "NO",   
        "ESTADO"        : "ASIGNADO_RESPONSABLE", # Informar como mantener el mismo estado
        "MENSAJE_ESTADO": "ANEXA ARCHIVO"     
    },
    
    "PDF_BORRADOR": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "VER PDF BORRADOR",
        "MENSAJE"       : "VER PDF BORRADOR",
        "ACCIONANTE"    : "NO",
        "DESTINATARIO"  : "NO",   
        "ESTADO"        : "ASIGNADO_RESPONSABLE", # Informar como mantener el mismo estado
        "MENSAJE_ESTADO": "VER PDF BORRADOR"     
    },

    "CREA_COMENTARIO": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "CREA COMENTARIO DE GESTIÓN",
        "MENSAJE"       : "CREA COMENTARIO",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "NO",   
        "ESTADO"        : "ASIGNADO_RESPONSABLE", # Informar como mantener el mismo estado
        "MENSAJE_ESTADO": "ANEXA ARCHIVO"     
    },

    "ASIGNA_TRD": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "ASIGNA EXPEDIENTE Y TIPO DOCUMENTAL (TRD)",
        "MENSAJE"       : "ASIGNA EXPEDIENTE Y TIPO DOCUMENTAL (TRD)",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "NO",   
        "ESTADO"        : "ASIGNADO_RESPONSABLE", # Informar como mantener el mismo estado
        "MENSAJE_ESTADO": "ASIGNA EXPEDIENTE Y TIPO DOCUMENTAL"     
    },

    "SELECCION_PLANTILLA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "ASIGNAR BORRADOR",
        "MENSAJE"       : "SE ASIGNA BORRADOR",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",   
        "ESTADO"        : "ASIGNADO_RESPONSABLE",
        "MENSAJE_ESTADO": "GESTION"     
    },

    "HABILITAR_RESPUESTA_RAPIDA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "HABILITAR RAPIDA",
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

    "FINALIZAR_PRIMER_CONTACTO": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "FINALIZA GESTIÓN",
        "MENSAJE"       : "FINALIZA GESTIÓN DE LA PETICIÓN, EN PRIMER CONTACTO",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "NO",
        "ESTADO"        : "FINALIZAR_PRIMER_CONTACTO",
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

    "CREA_COLABORATIVA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "SOLICITAR COLABORATIVA",
        "MENSAJE"       : "SE SOLICITA COLABORATIVA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "SOLICITADO_COLABORATIVA",
        "MENSAJE_ESTADO": "ASIGNAR RESPONSABLE"          
    },

    "HABILITAR_RESPUESTA_RAPIDA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "HABILITAR RAPIDA",
        "MENSAJE"       : "SE HABILITA RAPIDA",
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
        "MENSAJE_ESTADO": "APROBADO" 
    },

    "RADICAR_DOCUMENTO": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "RADICAR DOCUMENTO",
        "MENSAJE"       : "SE RADICA DOCUMENTO",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "DOCUMENTO_RADICADO"          
    },

    "ASIGNAR_RESPONSABLE_RESPUESTA_COLABORATIVA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "ASIGNAR RESPONSABLE COLABORATIVA",
        "MENSAJE"       : "SE ASIGNA RESPONSABLE COLABORATIVA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",
        "ESTADO"        : "ASIGNADO_RESPONSABLE_COLABORATIVA",
        "MENSAJE_ESTADO": "GESTION"          
    },

    "FINALIZAR_RESPUESTA_COLABORATIVA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "FINALIZAR COLABORATIVA",
        "MENSAJE"       : "SE FINALIZA COLABORATIVA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",        
        "ESTADO"        : "FINALIZADA_COLABORATIVA",
        "MENSAJE_ESTADO": "FINALIZADA"         
    },

    # BORRADORES
    "CREA_BORRADOR_SALIDA": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "CREA BORRADOR DE SALIDA",
        "MENSAJE"       : "SE CREA BORRADOR DE SALIDA",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",   
        "ESTADO"        : "ASIGNADO_RESPONSABLE",
        "MENSAJE_ESTADO": "GESTION BORRADOR SALIDA"     
    },

    "CREA_BORRADOR_INTERNO": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "CREA BORRADOR INTERNO",
        "MENSAJE"       : "SE CREA BORRADOR INTERNO",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "SI",   
        "ESTADO"        : "ASIGNADO_RESPONSABLE",
        "MENSAJE_ESTADO": "GESTION BORRADOR INTERNO"     
    },

    # FIRMA ELECTRONICA
    "FIRMA_BORRADOR": {
        "PROCESO"       : "GESTION",
        "ACCION"        : "FIRMA DOCUMENTO",
        "MENSAJE"       : "SE FIRMA DOCUMENTO",
        "ACCIONANTE"    : "SI",
        "DESTINATARIO"  : "NO",   
        "ESTADO"        : "FIRMADO",
        "MENSAJE_ESTADO": "GESTION FIRMA DOCUMENTO"     
    }
}