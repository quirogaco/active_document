#!/usr/bin/python
# -*- coding: iso-8859-15 -*-


import builtins
import pprint

from librerias.utilidades import basicas  

# Definiciones sql
from librerias.datos.sql                 import sqalchemy_declarativa_base as dbase

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general

from librerias.datos.base                import globales
from librerias.datos.validacion          import valida 

#####################################
#              CLASE                #
# MIGRADO PQRS, Clase ANEXO DE LOGS #
#####################################

class DB_MIGRADO_ANEXO_PQRS(base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa([
        'id', 
        'radicado_id',
        'tipoarchivofisico', 
        'repo_id',
        'adju_nombre'
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'id', 
        'radicado_id',
        'tipoarchivofisico', 
        'repo_id',
        'adju_nombre'
    ]
     
    id                = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto, primary_key=True) 
    radicado_id       = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto) 
    tipoarchivofisico = dbase.Column( dbase.Unicode(50),  nullable=True )
    repo_id           = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto) 
    adju_nombre       = dbase.Column( dbase.Unicode(512),  nullable=True )
    
globales.carga_clase("db_migrado_anexo_pqrs", DB_MIGRADO_ANEXO_PQRS)


##################################
#           ESTRUCTURA           #
##################################

campos = {
    "id": {
        "titulo"     : "Id del registro",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "radicado_id": {
        "titulo"     : "Id del radicado",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "tipoarchivofisico": {
        "titulo"     : "Tipo del archivo",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "repo_id": {
        "titulo"     : "Id del repositorio",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "adju_nombre": {
        "titulo"     : "Nombre del adjunto",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    }
}

#campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {}

#camposElastic = campos.copy()
#camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Trazabilidad anexo",
    "clase"       : "db_migrado_anexo_pqrs",
    "estructura"  : "anexo_pqr",    
    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,

    # Referencias a otras estructuras
    "referencias" : [],

    "campoIndice" : "id",
    "indexa"      : "no",

    "indexamiento": {}
}

# Publica definicion de estructura
globales.carga_definicion(definicion["estructura"], definicion)

##### VALIDACIÓN #######
# Genera modelo de validación
validador = valida.definirModelo(definicion["estructura"], definicion["campos"])
# Publica modelo de validacion
globales.carga_validador(definicion["estructura"], validador)
