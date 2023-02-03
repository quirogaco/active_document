#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint, datetime

referencias_web_natural = [
    # Discapacidad       "
    {
        "campoReferencia"    : "discapacidad_id",
        "contenido_en"       : "atributos_",
        "atributosReferencia": [{
            "discapacidad_nombre": "nombre",
        }],
        "estructuraDestino": "discapacidad"        
    },

    # Poblacion
    {
        "campoReferencia"    : "poblacion_id",
        "contenido_en"       : "atributos_",
        "atributosReferencia": [{
            "poblacion_nombre": "nombre",
        }],
        "estructuraDestino": "tipo_poblacion"
    },

    # Rango
    {
        "campoReferencia"    : "rango_id",
        "contenido_en"       : "atributos_",
        "atributosReferencia": [{
            "rango_nombre": "nombre",
        }],
        "estructuraDestino": "rango_edad"
    },

    # Genero    
    {
        "campoReferencia"    : "genero_id",
        "contenido_en"       : "atributos_",
        "atributosReferencia": [{
            "genero_nombre": "nombre",
        }],
        "estructuraDestino": "genero"
    }
] 

from aplicacion.datos.comunes.referencias import archivos, terceros

referencias = [
    # Sitio de radicacion 
    {
        "campoReferencia"    : "radicado_en",
        "atributosReferencia": [{
            "radicado_en_nombre": "nombre"
        }],
        "estructuraDestino": "ubicaciones"
    },

    # Usuario que radico 
    {
        "campoReferencia"    : "radicado_por",
        "atributosReferencia": [{
            "radicado_por_nombre": "nombre"
        }],
        "estructuraDestino": "usuarios"
    },

    # Canal de radicacion
    {
        "campoReferencia"    : "canal_radicado_id",
        "contenido_en"       : "atributos_",
        "atributosReferencia": [{
            "canal_radicado_nombre": "nombre"
        }],
        "estructuraDestino": "canales_comunicacion",
        "campoDestino"     : "id"         
    },

    # Empresas de mensajeria
    {
        "campoReferencia"    : "empresa_mensajeria_id",
        "contenido_en"       : "atributos_",
        "atributosReferencia": [{
            "empresa_mensajeria_nombre": "nombre"
        }],
        "estructuraDestino": "empresas_mensajeria"
    },

    # Tema
    {
        "campoReferencia"    : "tema_dependencia_id",
        "contenido_en"       : "atributos_",
        "atributosReferencia": [{
            "tema_dependencia_nombre": "nombre"
        }],
        "estructuraDestino": "temas"
    },

    # SubTema
    {
        "campoReferencia"    : "subtema_dependencia_id",
        "contenido_en"       : "atributos_",
        "atributosReferencia": [{
            "subtema_dependencia_nombre": "nombre",
        }],
        "estructuraDestino": "subtemas"
    },

    archivos.referencia_archivo,
    terceros.referencia_terceros
]

referencias.extend(referencias_web_natural)