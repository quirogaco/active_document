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

class DB_MIGRADO_TRAZABILIDAD_PQRS(base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa([
        'id', 
        'requ_id', 
        'usua_idejecutor', 
        'usua_idasignado', 
        'traz_fecha', 
        'traz_estado', 
        'traz_fechacambio', 
        'traz_registradopor', 
        'traz_procesoauditoria', 
        'traz_descripcion', 
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'id', 
        'requ_id', 
        'usua_idejecutor', 
        'usua_idasignado', 
        'traz_fecha', 
        'traz_estado', 
        'traz_fechacambio', 
        'traz_registradopor', 
        'traz_procesoauditoria', 
        'traz_descripcion', 
    ]

     
    id                    = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto, primary_key=True) 
    requ_id               = dbase.Column( dbase.Unicode(50),  index=True, nullable=True ) 
    usua_idejecutor       = dbase.Column( dbase.Unicode(50),  index=True, nullable=True ) 
    usua_idasignado       = dbase.Column( dbase.Unicode(50),  index=True, nullable=True ) 
    traz_fecha            = dbase.Column( dbase.DateTime,     nullable=True)
    traz_estado           = dbase.Column( dbase.Unicode(50),  nullable=True )
    traz_fechacambio      = dbase.Column( dbase.Unicode(50),     nullable=True) 
    traz_registradopor    = dbase.Column( dbase.Unicode(50),  nullable=True )
    traz_procesoauditoria = dbase.Column( dbase.Unicode(512), nullable=True )
    traz_descripcion      = dbase.Column( dbase.Text(),  nullable=True )

globales.carga_clase("db_migrado_trazabilidad_pqrs", DB_MIGRADO_TRAZABILIDAD_PQRS)


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

    "usua_idejecutor": {
        "titulo"     : "Id del usaurio ejecutor",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "usua_idasignado": {
        "titulo"     : "Id del usaurio asignado",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "usua_idasignado": {
        "titulo"     : "Id del usaurio asignado",
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

    "traz_fechacambio": {
        "titulo"     : "Fecha cambio",
        "tipo"       : "fecha",
    },  

    "traz_registradopor": {
        "titulo"     : "Id del registrador",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "traz_procesoauditoria": {
        "titulo"     : "Dato auditoria",
        "tipo"       : "texto",
        "longitud"   : 512,
        "defecto"    : ""
    },

    "traz_descripcion": {
        "titulo"     : "Descripción",
        "tipo"       : "texto",
        "longitud"   : 512,
        "defecto"    : ""
    },
}

#campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {}

#camposElastic = campos.copy()
#camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Trazabilidad",
    "clase"       : "db_migrado_trazabilidad_pqrs",
    "estructura"  : "traza_pqr",    
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

