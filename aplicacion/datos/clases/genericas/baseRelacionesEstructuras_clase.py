#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Definiciones sql
from librerias.datos.sql                 import sqalchemy_declarativa_base as dbase

# Clases
from librerias.datos.base                import globales 

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general

# Clase de datos, basica
class GLOBAL_ESTRUCTURAS_RELACION(base_general.DB_BASE_GENERAL, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa_base([
        'detalle',
        'tipo_relacion', 
        'cardinalidad', 
        'origen', 
        'origen_id', 
        'origen_role',
        'destino', 
        'destino_id', 
        'destino_role'
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'detalle'
        'tipo_relacion', 
        'cardinalidad', 
        'origen', 
        'origen_id', 
        'origen_role',
        'destino', 
        'destino_id', 
        'destino_role'
    ]

    detalle       = dbase.Column( dbase.Unicode(512), nullable=True)

    # Información de la relación
    tipo_relacion = dbase.Column( dbase.Unicode(128), index=True, nullable=False)
    cardinalidad  = dbase.Column( dbase.Unicode(30),  index=True, default="UNO")
    
    # ORIGEN
    origen        = dbase.Column( dbase.Unicode(128), index=True, default="")
    origen_id     = dbase.Column( dbase.Unicode(64),  index=True, default="")
    origen_role   = dbase.Column( dbase.Unicode(64),  index=True, default="")

    # DESTINO
    destino       = dbase.Column( dbase.Unicode(128), index=True, default="")
    destino_id    = dbase.Column( dbase.Unicode(64),  index=True, default="")
    destino_role  = dbase.Column( dbase.Unicode(64),  index=True, default="")

    atributos_   = dbase.Column( dbase.json.JSONType, default={} )    

globales.carga_clase("global_base_relacion_estructura", GLOBAL_ESTRUCTURAS_RELACION)