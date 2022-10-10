#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from parent_import import parentdir

# Clases
globales     = parentdir.parentdir.librerias.datos.base.globales

# Base general con atributos basicos
base_general = parentdir.parentdir.aplicacion.datos.clases_base.base_general

# Definición de clases de BD
sqa_clases   = parentdir.parentdir.librerias.datos.sql.sqa_clases

# Responsable de gestión
GESTION_RESPONSABLE_DEFINICION = {
    'clase'   : 'GESTION_RESPONSABLE',
    'tipo'    : 'general',
    'columnas': {
        'instancia_id': {
            'titulo'       : 'Instancia id',
            'tipo'         : 'unicode',
            'longitud'     : 50,
            'defecto'      : 'uuid',
            'indice'       : 'SI',
            'elastic'      : 'uuid'
        },

        'tarea_id': {
            'titulo'       : 'Tarea id',
            'tipo'         : 'unicode',
            'longitud'     : 50,
            'defecto'      : 'uuid',
            'indice'       : 'SI',
            'elastic'      : 'uuid'
        },

        'dependencia_id': {
            'titulo'       : 'Dependencia id',
            'tipo'         : 'unicode',
            'longitud'     : 50,
            'defecto'      : 'uuid',
            'indice'       : 'SI',
            'elastic'      : 'uuid'
        },

        'responsable_id': {
            'titulo'       : 'Responsable id',
            'tipo'         : 'unicode',
            'longitud'     : 50,
            'defecto'      : 'uuid',
            'indice'       : 'SI',
            'elastic'      : 'uuid'
        },

        'evento_id': {
            'titulo'       : 'Evento id',
            'tipo'         : 'unicode',
            'longitud'     : 50,
            'defecto'      : 'uuid',
            'indice'       : 'SI',
            'elastic'      : 'uuid'
        },

        'atributos': {
            'titulo'       : 'Atributos',
            'tipo'         : 'json',
            'elastic'      : 'json'
        }
    }
}


CLASE = sqa_clases.registra_db(GESTION_RESPONSABLE_DEFINICION)

print("Responsable:", CLASE)



"""

# Declaracion de base sqlalchemy
class GESTION_RESPONSABLE(base_general.DB_BASE_GENERAL, globales.CLASE_BASE_SQL):
    origen = sqa_columnas.crea_columna(
        'origen', 
        {
            'titulo'  : 'Origen',
            'tipo'    : 'unicode',
            'longitud': 50,
            'defecto' : 'UNICO',
            'nulo'    : 'SI',
            'indice'  : 'SI',
            'elastic' : 'clave'
        }
    ) 


import builtins
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy import Column, Integer, String, Unicode, ForeignKey, \
                       DateTime, Date, Index, asc, desc, event, PickleType
from sqlalchemy.dialects.oracle import NVARCHAR, NVARCHAR2

from sqlalchemy_utils.types import json

from sqlalchemy.orm import sessionmaker, relationship, backref

import uuid

from acappella.data  import fulltext, pyes_base, sql_globals
    
#/* Clase de entidad publica */
class ENTIDAD_PUBLICA(Base):
    __tablename__  = 'm10_entidades_publicas'
    __titulo__     = 'Entidades Publicas'
    __id__         = 'id'
        
    # origen 'BASE'= TABLAS DE ADMINISTRACIO, 'RADICADO'= asociado a un radicado    
    origen             = Column( Unicode(50),  index=True, nullable=True, default=u'BASE')
    
    nit                = Column( Unicode(50),  index=True, nullable=True, default=u'')
    razonSocial        = Column( Unicode(512), index=True, nullable=True, default=u'') # obligatorio en captura
        
    direccion          = Column( Unicode(512), nullable=True, default=u'')
    codigoPostal       = Column( Unicode(20),  nullable=True, default=u'')
    correoElectronico  = Column( Unicode(512), nullable=True, default=u'')
    telefonoFijo       = Column( Unicode(100), nullable=True, default=u'')
    fax                = Column( Unicode(100), nullable=True, default=u'')    
    ciudad_id          = Column( Unicode(50),  ForeignKey('m10_ciudades.id'), nullable=True, default=u'')
    control            = Column( Unicode(20), nullable=True, default=u'')
    parametros         = Column( json.JSONType, default={} ) 
    
    # valores de control  
    id                    = Column( Unicode(50), default=utils.UuidStr, primary_key=True)
    _estado_              = Column( Unicode(10),  default=u'ACTIVO', index=True, nullable=False)
    _creado_en_           = Column( DateTime, nullable=False, default=utils.getOnlyDateTime)
    _actualizado_en_      = Column( DateTime, nullable=False, default=utils.getOnlyDateTime, onupdate=utils.getOnlyDateTime)
    _codigo_unidad_       = Column( Unicode(20), index=True, nullable=False, default=u'*')
    _codigo_organizacion_ = Column( Unicode(20), index=True, nullable=False, default=organization_default)
"""