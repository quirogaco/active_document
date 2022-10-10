#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Definiciones sql
from librerias.datos.sql                 import sqalchemy_declarativa_base as dbase

# Clases
from librerias.datos.base                import globales 

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general

# Clase de datos, basica
class GLOBAL_ARCHIVOS_RELACION(base_general.DB_BASE_GENERAL, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa_base([
        'tipo_relacion', 
        'cardinalidad', 
        'origen', 
        'origen_id', 
        'origen_role',
        'archivo_id'
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'tipo_relacion', 
        'cardinalidad', 
        'origen', 
        'origen_id', 
        'origen_role',
        'archivo_id'
    ]

    # Estructura de datos asociada
    tipo_relacion = dbase.Column( dbase.Unicode(64), index=True, nullable=False, default="ANEXOS")
    cardinalidad  = dbase.Column( dbase.Unicode(64), index=True, nullable=False, default="multiple")
    
    # ORIGEN
    origen        = dbase.Column( dbase.Unicode(128), index=True, nullable=False)
    origen_id     = dbase.Column( dbase.Unicode(64),  index=True, nullable=False)
    origen_role   = dbase.Column( dbase.Unicode(64),  index=True, nullable=False, default="PADRE")

    # ARCHIVO
    archivo_id    = dbase.Column( dbase.Unicode(64),  index=True, nullable=False)

globales.carga_clase("global_base_relacion_archivo", GLOBAL_ARCHIVOS_RELACION)