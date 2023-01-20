#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint, datetime

from aplicacion.datos.comunes.referencias import archivos, terceros

referencias = [
    # Sitio de radicaci�n 
    {
        "campoReferencia"    : "radicado_en_id",
        "atributosReferencia": [{
            "radicado_en_nombre": "nombre",
            "radicado_en_id"    : "id"
        }],
        "estructuraDestino": "ubicaciones",
        "externa"          : {
            "tipo_relacion": "SITIO_DE_RADICACION"            
        } 
    },

    # Usuario que radico 
    {
        "campoReferencia"    : "radicado_por_id",
        "atributosReferencia": [{
            "radicado_por_nombre": "nombre",
            "radicado_por_id"    : "id"
        }],
        "estructuraDestino": "usuarios",
        "externa"          : {
            "tipo_relacion": "RADICADOR"            
        } 
    },

    # Usuario DEPENDENCIA
    {
        "campoReferencia"    : "funcionario_responde_id",
        "atributosReferencia": [{
            "funcionario_responde_nombre": "nombre",
        }],
        "estructuraDestino": "usuarios"
    },

    # DEPENDENCIA
    {
        "campoReferencia"    : "dependencia_responde_id",
        "atributosReferencia": [{
            "dependencia_responde_nombre": "nombre",
        }],
        "estructuraDestino": "dependencias"
    },

    # Datos de gesti�n
    {
        "campoReferencia"    : "gestion_id",
        "atributosReferencia": [{
            "gestion_responsable_id"     : "responsable_id",   
            "gestion_responsable_nombre" : "responsable_nombre", 

            # Dependencia responsable
            "gestion_dependencia_id"     : "dependencia_id",
            "gestion_dependencia_nombre" : "dependencia_nombre",   

            # Petici�n
            "gestion_peticion_id"        : "peticion_id",  
            "gestion_peticion_nombre"    : "peticion_nombre",     

            # Terminos de respuesta basicos
            "gestion_horas_dias"         : "horas_dias", 
            "gestion_total_tiempo"       : "total_tiempo",  
            "gestion_prioridad"          : "prioridad", 

            # Estado, vencimiento
            "gestion_inicio"     : "gestion_inicio", 
            "gestion_vence_en"   : "vence_en", 
            "gestion_estado"     : "estado",  
        }],
        "estructuraDestino": "peticiones",    
        "campoDestino"     : "id",   
    },

    archivos.referencia_archivo,
    terceros.referencia_terceros
]