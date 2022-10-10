#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Definiciones sql
from librerias.datos.sql  import sqalchemy_declarativa_base as dbase
from librerias.utilidades import basicas  
# Clases
from librerias.datos.base import globales 

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general

class GESTOR_RADICADOS_INTERNO(base_general.DB_BASE_GENERAL, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa_base([
        'radicado_en',
        'radicado_por',    
        'nro_radicado',
        'fecha_radicado',
        'asunto',
        'dependencia_envia_id',
        'funcionario_envia_id',
        'dependencia_recibe_id',
        'funcionario_recibe_id',
        'tipo_firma',
        'atributos_'
    ])
    
    # Campos fijos de la tabla
    __basicos__ = [        
        'radicado_en',
        'radicado_por',
        'nro_radicado',
        'fecha_radicado',
        'asunto',
        'dependencia_envia_id',
        'funcionario_envia_id',
        'dependencia_recibe_id',
        'funcionario_recibe_id',
        'tipo_firma',
        'atributos_'
    ]

    # ESTRUCTURA
    estructura_    = dbase.Column( dbase.Unicode(64), index=True, nullable=False, default="*")

    # SITIO DE RADICACIÓN
    radicado_en    = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="*")
    
    # RADICADOR
    radicado_por   = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="*")
    
    # Nombre del archivo, objeto para MINIO
    nro_radicado   = dbase.Column( dbase.Unicode(64), index=True, nullable=False)

    # Fecha radicado
    fecha_radicado = dbase.Column( dbase.DateTime, nullable=False, default=basicas.fechaHora)

    # Asunto
    asunto         = dbase.Column( dbase.Unicode(2048), index=True, nullable=False)

    # Dependencia remitente
    dependencia_envia_id = dbase.Column( dbase.Unicode(64), index=True, nullable=False, default="") 

    # Funcionario remitente
    funcionario_envia_id = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="*") 

    # Dependencia recibe
    dependencia_recibe_id = dbase.Column( dbase.Unicode(64), index=True, nullable=False, default="") 

    # Funcionario recibe
    funcionario_recibe_id = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="*") 

    # Tipo firma
    tipo_firma              = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="FISICA")

    # Atrbutos especificos del RADICADO
    atributos_     = dbase.Column( dbase.json.JSONType, default={} )    
    
globales.carga_clase("gestor_radicados_interno", GESTOR_RADICADOS_INTERNO)