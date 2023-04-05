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

    # Bucket MINIO
    "cubeta": {
        "titulo"     : "Cubeta de almacenamiento (bucket)",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 512,
        "tipoElastic": "clave_ordenado"
    },

    # RUTA, ruta completa del archivo
    "ruta": {
        "titulo"     : "Ruta completa del archivo",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 1024,
        "tipoElastic": "texto_ordenado"
    },
    
}
campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {}

camposElastic = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Archivos electronicos",
    "clase"       : "base_archivo_electronico",
    "estructura"  : "archivo_electronico",    
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