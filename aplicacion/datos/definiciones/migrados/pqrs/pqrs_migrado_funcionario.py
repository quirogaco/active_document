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

###################################
#              CLASE              #
# MIGRADO PQRS, Clase FUNCIONARIO #
###################################

class DB_MIGRADO_FUNCIONARIO_PQRS(base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa([
        'id', 
        'carg_id',
        'unid_id',
        'func_primernombre',
        'func_primerapellido', 
        'func_estado'
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'id', 
        'carg_id',
        'unid_id',
        'func_primernombre',
        'func_primerapellido', 
        'func_estado'
    ]
     
    id                  = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto, primary_key=True)
    carg_id             = dbase.Column( dbase.Unicode(50),  nullable=True )  
    unid_id             = dbase.Column( dbase.Unicode(50),  nullable=True ) 
    func_primernombre   = dbase.Column( dbase.Unicode(128), nullable=True ) 
    func_primerapellido = dbase.Column( dbase.Unicode(128), nullable=True ) 
    func_estado         = dbase.Column( dbase.Unicode(30), nullable=True )  

globales.carga_clase("db_migrado_funcionario_pqrs", DB_MIGRADO_FUNCIONARIO_PQRS)

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

    "carg_id": {
        "titulo"     : "Id del cargo",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "unid_id": {
        "titulo"     : "Id de la unidad",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "func_primernombre": {
        "titulo"     : "Tipo de identificación",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "func_primerapellido": {
        "titulo"     : "Tipo de identificación",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "func_estado": {
        "titulo"     : "Número de identificación",
        "tipo"       : "texto",
        "longitud"   : 50,
        "defecto"    : ""
    },   
}

#campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {}

#camposElastic = campos.copy()
#camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Funcionarios migrados PQRS",
    "clase"       : "db_migrado_funcionario_pqrs",
    "estructura"  : "funcionario_pqr",    
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
