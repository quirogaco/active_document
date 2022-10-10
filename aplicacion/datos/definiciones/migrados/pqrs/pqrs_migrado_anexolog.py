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

class DB_MIGRADO_ANEXOLOG_PQRS(base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa([
        'id', 
        'requ_id',
        'repo_id', 
        'adju_nombre', 
        'adju_fechacambio', 
        'adju_registradopor', 
        'adju_procesoauditoria', 
        'adju_final', 
        'traz_id', 
        'usua_idejecutor', 
        'usua_idasignado', 
        'traz_fecha', 
        'traz_estado', 
        'descripcion', 
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'id', 
        'requ_id',
        'repo_id', 
        'adju_nombre', 
        'adju_fechacambio', 
        'adju_registradopor', 
        'adju_procesoauditoria', 
        'adju_final', 
        'traz_id', 
        'usua_idejecutor', 
        'usua_idasignado', 
        'traz_fecha', 
        'traz_estado', 
        'descripcion', 
    ]
     
    id                    = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto, primary_key=True) 
    requ_id               = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto) 
    repo_id               = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto)
    adju_nombre           = dbase.Column( dbase.Unicode(512), nullable=True ) 
    adju_fechacambio      = dbase.Column( dbase.DateTime,     nullable=True)
    adju_registradopor    = dbase.Column( dbase.Unicode(50),  default="")
    adju_procesoauditoria = dbase.Column( dbase.Unicode(512), nullable=True )
    adju_final            = dbase.Column( dbase.Unicode(60), nullable=True )
    traz_id               = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto) 
    usua_idejecutor       = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto) 
    usua_idasignado       = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto)
    traz_fecha            = dbase.Column( dbase.Unicode(50),  nullable=True)
    traz_estado           = dbase.Column( dbase.Unicode(50),  default="") 
    descripcion           = dbase.Column( dbase.Text(),       nullable=True )    

globales.carga_clase("db_migrado_anexolog_pqrs", DB_MIGRADO_ANEXOLOG_PQRS)


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

    "requ_id": {
        "titulo"     : "Id del requerimiento",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "repo_id": {
        "titulo"     : "Id del reositorio",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "adju_nombre": {
        "titulo"     : "Nombre del adjunto",
        "tipo"       : "texto",
        "longitud"   : 512,
        "defecto"    : ""
    },

    "adju_fechacambio": {
        "titulo"     : "Fecha del cambio",
        "tipo"       : "fecha",
    }, 

    "adju_registradopor": {
        "titulo"     : "Nombre del registrador",
        "tipo"       : "texto",
        "longitud"   : 512,
        "defecto"    : ""
    }, 

    "adju_procesoauditoria": {
        "titulo"     : "Auditoria",
        "tipo"       : "texto",
        "longitud"   : 512,
        "defecto"    : ""
    }, 

    "adju_final": {
        "titulo"     : "Estado final",
        "tipo"       : "texto",
        "longitud"   : 512,
        "defecto"    : ""
    }, 

    "traz_id": {
        "titulo"     : "Id de la traza",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "usua_idejecutor": {
        "titulo"     : "Id del ejecutor",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "usua_idasignado": {
        "titulo"     : "Id del asignado",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "traz_fecha": {
        "titulo"     : "Fecha traza",
        "tipo"       : "fecha",
    },  

    "traz_estado": {
        "titulo"     : "Estado de la traza",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "descripcion": {
        "titulo"     : "Descripción",
        "tipo"       : "texto",
        "longitud"   : 512,
        "defecto"    : ""
    }
}

#campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {}

#camposElastic = campos.copy()
#camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Trazabilidad anexos",
    "clase"       : "db_migrado_anexolog_pqrs",
    "estructura"  : "traza_anexo_pqr",    
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
