#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes


campos = {
    "nombre"          : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120, "reporte": "SI"}),         
    "plantilla_juridica_id"    : tipos.clave(propiedades={"titulo": "Plantilla persona JURIDICA notificación", "longitud": 60}), 
    "plantilla_natural_id"     : tipos.clave(propiedades={"titulo": "Plantilla persona NATURAL notificación", "longitud": 60}), 
    "plantilla_anonima_id"     : tipos.clave(propiedades={"titulo": "Plantilla persona ANONIMA notificación", "longitud": 60}), 
    "plantilla_juridica_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Plantilla persona JURIDICA", "longitud": 250, "reporte": "SI"}),   
    "plantilla_natural_nombre" : tipos.texto(propiedades={"columna": "no", "titulo": "Plantilla persona NATURAL", "longitud": 250, "reporte": "SI"}),   
    "plantilla_anonima_nombre" : tipos.texto(propiedades={"columna": "no", "titulo": "Plantilla persona ANONIMA", "longitud": 250, "reporte": "SI"}),        
}

referencias = [
    {
        "campoReferencia": "plantilla_juridica_id",
        "atributosReferencia": [{
            "plantilla_juridica_nombre": "descripcion",
        }],
        "estructuraDestino": "plantillas",
        "campoDestino"     : "id",
    },

    {
        "campoReferencia": "plantilla_natural_id",
        "atributosReferencia": [{
            "plantilla_natural_nombre": "descripcion",
        }],
        "estructuraDestino": "plantillas",
        "campoDestino"     : "id",
    },

    {
        "campoReferencia": "plantilla_anonima_id",
        "atributosReferencia": [{
            "plantilla_anonima_nombre": "descripcion",
        }],
        "estructuraDestino": "plantillas",
        "campoDestino"     : "id",
    }
]

definicion = {
    "descripcion" : "Canales de comunicación",
    "clase"       : "config_canales_comunicacion",
    "estructura"  : "canales_comunicacion",
    "campos"      : campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {},
    "reporte"     : "SI" # Fuente de datos para REPORTES
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)