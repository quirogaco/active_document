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

###############################
#              CLASE          #
# MIGRADO PQRS, Clase TERCERO #
###############################

class DB_MIGRADO_TERCERO_PQRS(base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa([
        'id', 
        'tipoidentificacion',
        'nroidentificacion',
        'primer_nombre',
        'segundo_nombre',
        'primer_apellido',
        'segundo_apellido',
        'nombres',
        'direccion',
        'correoelectronico',
        'telefonofijo',
        'telefonomovil',
        'peti_genero',
        'ciud_id',
        'pais_id',
        'depa_id',
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'id', 
        'tipoidentificacion',
        'nroidentificacion',
        'primer_nombre',
        'segundo_nombre',
        'primer_apellido',
        'segundo_apellido',
        'nombres',
        'direccion',
        'correoelectronico',
        'telefonofijo',
        'telefonomovil',
        'peti_genero',
        'ciud_id',
        'pais_id',
        'depa_id',
    ]
     
    id                  = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto, primary_key=True) 
    tipoidentificacion  = dbase.Column( dbase.Unicode(10),  index=True, nullable=True )
    nroidentificacion   = dbase.Column( dbase.Unicode(50),  index=True, nullable=True )
    primer_nombre       = dbase.Column( dbase.Unicode(128), nullable=True )
    segundo_nombre      = dbase.Column( dbase.Unicode(128), nullable=True )
    primer_apellido     = dbase.Column( dbase.Unicode(128), nullable=True )
    segundo_apellido    = dbase.Column( dbase.Unicode(128), nullable=True )
    nombres             = dbase.Column( dbase.Unicode(128), nullable=True )
    direccion           = dbase.Column( dbase.Unicode(128), nullable=True )
    correoelectronico   = dbase.Column( dbase.Unicode(128), nullable=True )
    telefonofijo        = dbase.Column( dbase.Unicode(128), nullable=True )
    telefonomovil       = dbase.Column( dbase.Unicode(128), nullable=True )
    peti_genero         = dbase.Column( dbase.Unicode(50),  nullable=True )
    ciud_id             = dbase.Column( dbase.Unicode(50),  nullable=True ) 
    pais_id             = dbase.Column( dbase.Unicode(50),  nullable=True ) 
    depa_id             = dbase.Column( dbase.Unicode(50),  nullable=True ) 

globales.carga_clase("db_migrado_tercero_pqrs", DB_MIGRADO_TERCERO_PQRS)

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

    "tipoidentificacion": {
        "titulo"     : "Tipo de identificación",
        "tipo"       : "texto",
        "longitud"   : 10,
        "defecto"    : ""
    },

    "nroidentificacion": {
        "titulo"     : "Número de identificación",
        "tipo"       : "texto",
        "longitud"   : 50,
        "defecto"    : ""
    },

    "primer_nombre": {
        "titulo"     : "Primer nombre",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "segundo_nombre": {
        "titulo"     : "Segundo nombre",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "primer_apellido": {
        "titulo"     : "Primer apellido",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "segundo_apellido": {
        "titulo"     : "Segundo apellido",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "nombres": {
        "titulo"     : "Nombres",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "direccion": {
        "titulo"     : "Direccion",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "correoelectronico": {
        "titulo"     : "Correo electronico",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "telefonofijo": {
        "titulo"     : "Telefono fijo",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "telefonomovil": {
        "titulo"     : "Telefono movil",
        "tipo"       : "texto",
        "longitud"   : 128,
        "defecto"    : ""
    },

    "peti_genero": {
        "titulo"     : "Genero",
        "tipo"       : "texto",
        "longitud"   : 30,
        "defecto"    : ""
    },

    "ciud_id": {
        "titulo"     : "Id ciudad",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "pais_id": {
        "titulo"     : "Id pais",
        "tipo"       : "texto",
        "longitud"   : 60,
        "defecto"    : ""
    },

    "depa_id": {
        "titulo"     : "Id departamento",
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
    "descripcion" : "Terceros migrados PQRS",
    "clase"       : "db_migrado_tercero_pqrs",
    "estructura"  : "tercero_pqr",    
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
