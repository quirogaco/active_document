#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Definiciones sql
from librerias.datos.sql                 import sqalchemy_declarativa_base as dbase

# Clases
from librerias.datos.base                import globales 

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general

# Clase de datos, basica
class GLOBAL_BASE_GENERAL(base_general.DB_BASE_GENERAL, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa_base([
        'estructura_', 
        'codigo', 
        'nombre', 
        'detalle', 
        'atributos_',        
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'estructura_', 
        'codigo', 
        'nombre', 
        'detalle', 
    ]

    # Estructura de datos asociada
    estructura_  = dbase.Column( dbase.Unicode(50),   index=True, nullable=False)
    codigo       = dbase.Column( dbase.Unicode(120),  index=True, nullable=True, default="")
    nombre       = dbase.Column( dbase.Unicode(512),  index=True, nullable=True, default="")
    detalle      = dbase.Column( dbase.Unicode(1024), nullable=True, default="")
    atributos_   = dbase.Column( dbase.json.JSONType, default={} )    

globales.carga_clase("global_base_general", GLOBAL_BASE_GENERAL)