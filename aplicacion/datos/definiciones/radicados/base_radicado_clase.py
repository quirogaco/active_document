#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definiciones sql
from librerias.datos.sql  import sqalchemy_declarativa_base as dbase
from librerias.utilidades import basicas  
# Clases
from librerias.datos.base import globales 

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general

class GESTOR_RADICADOS_ENTRADA(base_general.DB_BASE_GENERAL, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa_base([
        'radicado_en',
        'radicado_por',        
        'nro_radicado',
        'fecha_radicado',
        'atributos_'
    ])
    
    # Campos fijos de la tabla
    __basicos__ = [
        'radicado_en',
        'radicado_por',
        'nro_radicado',
        'fecha_radicado',
        'atributos_'
    ]

    # ESTRUCTURA
    estructura_    = dbase.Column( dbase.Unicode(64), index=True, nullable=False, default="*")

    # SITIO DE RADICACIoN
    radicado_en    = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="*")
    
    # RADICADOR
    radicado_por   = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="*")
    
    # Nombre del archivo, objeto para MINIO
    nro_radicado   = dbase.Column( dbase.Unicode(64), index=True, nullable=False)
    
    # Fecha radicado
    fecha_radicado = dbase.Column( dbase.DateTime, nullable=False, default=basicas.fechaHora)

    # Atrbutos especificos del RADICADO
    atributos_     = dbase.Column( dbase.json.JSONType, default={} )    
    
globales.carga_clase("gestor_radicados_entrada", GESTOR_RADICADOS_ENTRADA)