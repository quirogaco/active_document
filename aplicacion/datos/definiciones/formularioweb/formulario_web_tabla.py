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

####################
#      CLASE       #
# FORMULARIOS WEB  #
####################

class DB_RADICADOS_FORMULARIO_WEB(base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa([
        'id', 
        'tipo_radicado',
        'nro_radicado',
        'fecha_radicado',
        'tipo_entidad_id',
        'nombre_entidad',
        'tipo_identificacion_id',
        'nro_identificacion',
        'nombres',
        'apellidos'
        'medio_notificacion',
        'correo',
        'direccion',
        'ciudad_id',
        'genero_id',
        'detalle',
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        '_estructura_', 
        'id', 
        'tipo_radicado',        
        'nro_radicado',
        'fecha_radicado',
        'tipo_entidad_id',
        'nombre_entidad',
        'tipo_identificacion_id',
        'nro_identificacion',
        'nombres',
        'apellidos',
        'medio_notificacion',
        'correo',
        'direccion',
        'ciudad_id',
        'genero_id',
        'detalle',
    ]

    id                  = dbase.Column( dbase.Unicode(50),  default=basicas.uuidTexto, primary_key=True)

    # OPCIONAL VER COMO BORRAR
    _estructura_       = dbase.Column( dbase.Unicode(60),  index=True, default="" )
    _estado_           = dbase.Column( dbase.Unicode(60),  index=True, default="" )
    _atributos_        = dbase.Column( dbase.json.JSONType, default={} )
    archivo            = dbase.Column( dbase.json.JSONType, default={} )   

    ### Datos basicos
    # "JURIDICA, NATURAL, ANONIMO" 
    tipo_radicado       = dbase.Column( dbase.Unicode(60),  index=True )
    nro_radicado        = dbase.Column( dbase.Unicode(60),  index=True )
    fecha_radicado      = dbase.Column( dbase.DateTime,     nullable=False, default=basicas.fechaHora)

    ### Datos identidad
    # JURIDICA
    tipo_entidad_id     = dbase.Column( dbase.Unicode(60),   index=True, default="" )
    nombre_entidad      = dbase.Column( dbase.Unicode(256),  index=True, default="" )

    # Tipo de identificación
    # NATURAL    
    tipo_identificacion_id = dbase.Column( dbase.Unicode(60),   index=True, default="" )
    # JURIDICA, NATURAL
    # Nit, Cedula
    nro_identificacion   = dbase.Column( dbase.Unicode(128),  index=True, default="" )
    # JURIDICA, NATURAL
    nombres             = dbase.Column( dbase.Unicode(256),  index=True, default="" )
    apellidos           = dbase.Column( dbase.Unicode(256),  index=True, default="" )

    ### Ubicación
    medio_notificacion  = dbase.Column( dbase.Unicode(60),   index=True, default="" ) 
    correo              = dbase.Column( dbase.Unicode(256),  index=True, default="" )
    direccion           = dbase.Column( dbase.Unicode(256),  index=True, default="" )
    ciudad_id           = dbase.Column( dbase.Unicode(60),   index=True, default="" )

    # Genero
    # NATURAL    
    genero_id           = dbase.Column( dbase.Unicode(60),   index=True, default="" )

    # Detalles
    detalle             = dbase.Column( dbase.Text, default="" )

globales.carga_clase("db_formulario_web", DB_RADICADOS_FORMULARIO_WEB)