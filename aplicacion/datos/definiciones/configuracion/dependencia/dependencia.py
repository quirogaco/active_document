#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from aplicacion.datos.clases.clases_base    import base_general_campos
from aplicacion.datos.definiciones._comunes import elementos_comunes

campos = {
    "codigo"            : elementos_comunes.codigo_obligatorio({}),
    "nombre"            : elementos_comunes.nombre_obligatorio({}),
    "ubicacion_id"      : elementos_comunes.id_obligatorio( {"titulo": "Territorial/Regional"}),
    "jefe_id"           : elementos_comunes.id_obligatorio( {"titulo": "Jefe"}),
    "archivo_id"        : elementos_comunes.id_obligatorio( {"titulo": "Encargado del archivo"}),
    "correspondencia_id": elementos_comunes.id_obligatorio( {"titulo": "Encargado de la correspondencia"}),
    "pqrs_id"           : elementos_comunes.id_obligatorio( {"titulo": "Encargado de los peticiones y tramites"}),
    "coordinadores_id"  : elementos_comunes.ids({"titulo": "Coordinadores"}),
    "padre_id"          : elementos_comunes.id_obligatorio({"titulo": "Dependencia padre"}),
    "_estado_"          : elementos_comunes.estado_obligatorio({})
}
campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {
    "ubicacion_nombre"      : elementos_comunes.elastic_texto,
    "jefe_nombre"           : elementos_comunes.elastic_texto,
    "archivo_nombre"        : elementos_comunes.elastic_texto,
    "correspondencia_nombre": elementos_comunes.elastic_texto,
    "pqrs_nombre"           : elementos_comunes.elastic_texto,
    "coordinadores_nombres" : elementos_comunes.elastic_texto,
    "padre_nombre"          : elementos_comunes.elastic_texto,
}
camposElastic = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Dependencia",
    "clase"       : "base_general",
    "estructura"  : "dependencia",    
    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,

    # Referencias a otras estructuras
    "referencias" : [
        # Territorial
        {
            "campoReferencia"    : "ubicacion_id",
            "atributosReferencia": [{
                "ubicacion_nombre"   : "nombre",
            }],
           "estructuraDestino": "ubicacion",
            "campoDestino"     : "id",            
        },

        # JEFE DE LA DEPENDENCIA  
        {
            "campoReferencia"    : "jefe_id",
            "atributosReferencia": [{
                "jefe_nombre"   : "nombre",
            }],
            "estructuraDestino": "usuario",
            "campoDestino"     : "id",            
        },

        # ENCARGADO DE ARCHIVO 
        {
            "campoReferencia"    : "archivo_id",
            "atributosReferencia": [{
                "archivo_nombre"   : "nombre",
            }],
            "estructuraDestino": "usuario",
            "campoDestino"     : "id",            
        },

        # ENCARGADO DE CORRESPONDENCIA
        {
            "campoReferencia"    : "correspondencia_id",
            "atributosReferencia": [{
                "correspondencia_nombre"   : "nombre",
            }],
            "estructuraDestino": "usuario",
            "campoDestino"     : "id",            
        },

        # ENCARGADO PQRS
        {
            "campoReferencia"    : "pqrs_id",
            "atributosReferencia": [{
                "pqrs_nombre"   : "nombre",
            }],
            "estructuraDestino": "usuario",
            "campoDestino"     : "id",            
        },

        # COORDINADORES
        {
            "campoReferencia"    : "coordinadores_id",
            "atributosReferencia": [{
                "coordinador_nombre"   : "nombre",
            }],            
            "estructuraDestino": "usuario",
            "campoDestino"     : "id",  
            "modo"             : "lista"          
        },

        # DEPENDENCIA PADRE
        {
            "campoReferencia"    : "padre_id",
            "atributosReferencia": [{
                "padre_nombre"   : "nombre",
            }],
            "estructuraDestino": "dependencia",
            "campoDestino"     : "id",            
        },
    ],
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# PROCESAMIENTO ESTRUCTURA
elementos_comunes.procesaBaseGeneral(definicion)