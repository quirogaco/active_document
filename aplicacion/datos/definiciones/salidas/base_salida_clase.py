#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definiciones sql
from librerias.datos.sql  import sqalchemy_declarativa_base as dbase
from librerias.utilidades import basicas  
# Clases
from librerias.datos.base import globales 

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general

class GESTOR_RADICADOS_SALIDA(base_general.DB_BASE_GENERAL, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa_base([
        'radicado_en',
        'radicado_por',    
        'nro_radicado',
        'fecha_radicado',
        'fecha_documento',
        'asunto',
        'medio_notificacion',
        'respuesta_tipo',
        'dependencia_responde_id',
        'funcionario_responde_id',
        'tipo_firma',
        'gestion_id',
        'atributos_'
    ])
    
    # Campos fijos de la tabla
    __basicos__ = [        
        'radicado_en',
        'radicado_por',
        'nro_radicado',
        'fecha_radicado',
        'fecha_documento',
        'asunto',
        'medio_notificacion',
        'respuesta_tipo',
        'dependencia_responde_id',
        'funcionario_responde_id',
        'tipo_firma',
        'gestion_id',
        'atributos_'
    ]

    # ESTRUCTURA
    estructura_    = dbase.Column( dbase.Unicode(64), index=True, nullable=False, default="*")

    # SITIO DE RADICACI�N
    radicado_en    = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="*")
    
    # RADICADOR
    radicado_por   = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="*")
    
    # Nombre del archivo, objeto para MINIO
    nro_radicado   = dbase.Column( dbase.Unicode(64), index=True, nullable=False)

    # Fecha radicado
    fecha_radicado = dbase.Column( dbase.DateTime, nullable=False, default=basicas.fechaHora)

    # Fecha documento
    fecha_documento = dbase.Column( dbase.DateTime, nullable=False, default=basicas.fechaHora)

    # Asunto
    asunto         = dbase.Column( dbase.Unicode(2048), index=True, nullable=False)

    # Medio de notificaci�n
    medio_notificacion = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="DIRECCION FISICA")  

    # Tipo respuesta
    respuesta_tipo    = dbase.Column( dbase.Unicode(64), index=True, nullable=False, default="FINAL")

    # Dependencia remitente
    dependencia_responde_id = dbase.Column( dbase.Unicode(64), index=True, nullable=False, default="") 

    # Funcionario remitente
    funcionario_responde_id = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="*") 

    # Tipo firma
    tipo_firma              = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="FISICA")

    # GESTION ID ORIGEN
    gestion_id    = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="*") 

    # Atrbutos especificos del RADICADO
    atributos_     = dbase.Column( dbase.json.JSONType, default={} )    
    
globales.carga_clase("gestor_radicados_salida", GESTOR_RADICADOS_SALIDA)