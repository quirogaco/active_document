#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from aplicacion.datos.comunes.referencias import archivos

referencias = [
    # Creador
    {
        "campoReferencia"    : "creado_por_id",
        "atributosReferencia": [{
            "creado_por_nombre": "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    },

    # Responsable 
    {
        "campoReferencia"    : "responsable_id",
        "atributosReferencia": [{
            "responsable_nombre"   : "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    },

    # Responsable anterior
    {
        "campoReferencia"    : "anterior_id",
        "atributosReferencia": [{
            "anterior_nombre"   : "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    },

    # Dependencia responsable
    {
        "campoReferencia"    : "dependencia_id",
        "atributosReferencia": [{
            "dependencia_nombre": "nombre",
            "sede_nombre"       : "ubicacion_nombre",
        }],
        "estructuraDestino": "dependencias",
        "campoDestino"     : "id",            
    },

    # Tipo de tramite
    {
        "campoReferencia"    : "peticion_id",
        "atributosReferencia": [{
            "peticion_nombre"   : "nombre",
        }],
        "estructuraDestino": "tipo_peticiones",
        "campoDestino"     : "id",            
    },

    # Logs
    {
        "campoReferencia"    : "id",
        "modo"               : "multiple",
        "atributosReferencia": [{
            "logs": "completo_"    
        }],
        "estructuraDestino": "logs",
        "campoDestino"     : "fuente_id",            
    },

    archivos.referencia_archivo
]