#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base                import globales
from librerias.datos.validacion          import valida 
from librerias.datos.elastic             import elastic_utilidades
from librerias.datos.elastic             import elastic_operaciones
from aplicacion.datos.clases.clases_base import base_general_campos
from aplicacion.datos.estructuras        import baseGeneral_estructura
from aplicacion.datos.estructuras        import baseGeneral_estructura

campos = {

    # Define el tipo de relación ej. "FORMULARIO_WEB", anexos de los formularios web
    "tipo_relacion": {
        "titulo"     : "Tipo relación",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 128,
        "tipoElastic": "clave_ordenado"
    },

    # Cardinalidad de la relacion:
    # "uno"   : uno a uno
    # "varios": varios 
    "cardinalidad": {
        "titulo"     : "Cardinalidad de la relación",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 30,
        "tipoElastic": "clave"
    },

    ##########
    # ORIGEN #
    ##########
    # Estructura origen de la relación
    "origen": {
        "titulo"     : "Estructura origen",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 128,
        "tipoElastic": "clave_ordenado"
    },

    # ID de la Estructura origen de la relación
    "origen_id": {
        "titulo"     : "ID de la Estructura origen",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 60,
        "tipoElastic": "clave"
    },

    # ROLE de la Estructura origen de la relación
    "origen_role": {
        "titulo"     : "Role de la Estructura origen",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 60,
        "tipoElastic": "clave_ordenado"
    },

    ###########
    # DESTINO #
    ###########    
    # Estructura destino de la relación
    "destino": {
        "titulo"     : "Estructura origen",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 128,
        "tipoElastic": "clave_ordenado"
    },

    # ID de la Estructura destino de la relación
    "destino_id": {
        "titulo"     : "ID de la Estructura origen",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 60,
        "tipoElastic": "clave"
    },

    # ROLE de la Estructura destino de la relación
    "destino_role": {
        "titulo"     : "Role de la Estructura origen",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 60,
        "tipoElastic": "clave_ordenado"
    },
}
campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {}

camposElastic = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Relación a archivos",
    "clase"       : "base_relacion_archivo",
    "estructura"  : "archivos_relacion",    
    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,

    # Referencias a otras estructuras
    "referencias" : [],

    "campoIndice" : "id",
    "indexa"      : "si",

    "indexamiento": {}
}

# Publica definicion de estructura
globales.carga_definicion(definicion["estructura"], definicion)

##### VALIDACIÓN #######
# Genera modelo de validación
validador = valida.definirModelo(definicion["estructura"], definicion["campos"])
# Publica modelo de validacion
globales.carga_validador(definicion["estructura"], validador)

##### ELASTIC #######
# Genera modelo de elastic
elastic_modelo = elastic_utilidades.generaModelo(camposElastic, definicion["indexamiento"])
# Registra modelo de elastic
elastic_utilidades.registraModelo(
    definicion["estructura"], 
    elastic_modelo, 
    definicion["indexamiento"], 
    definicion.get("campoIndice", "id") 
)
elastic_operaciones.creaIndice(definicion["estructura"], "base")

# PROCESAMIENTO ESTRUCTURA
globales.carga_procesamiento(definicion["estructura"], "armar_estructura",     baseGeneral_estructura.armar_estructura)
globales.carga_procesamiento(definicion["estructura"], "normaliza_estructura", baseGeneral_estructura.normaliza_estructura)