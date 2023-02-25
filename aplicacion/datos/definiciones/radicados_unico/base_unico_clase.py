#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definiciones sql
from librerias.datos.sql  import sqalchemy_declarativa_base as dbase
from librerias.utilidades import basicas  
# Clases
from librerias.datos.base import globales 

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general

class GESTOR_RADICADOS_UNICO(base_general.DB_BASE_GENERAL, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa_base([
        'radicado_en',
        'radicado_por',    
        'nro_radicado',
        'fecha_radicado',
        'fecha_documento',
        'asunto'
    ])
    
    # Campos fijos de la tabla
    __basicos__ = [     
        'radicado_en',
        'radicado_por',
        'nro_radicado',
        'fecha_radicado',
        'fecha_documento',
        'asunto'
    ]    
globales.carga_clase("gestor_radicados_unico", GESTOR_RADICADOS_UNICO)