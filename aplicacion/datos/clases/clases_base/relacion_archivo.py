#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Unicode, DateTime

from librerias.utilidades import basicas  

class DB_BASE_GENERAL(object):
   # Base de definición
   @declared_attr
   def __base__(cls):
      return 'base_general'

   # Nombre de la tabla
   @declared_attr
   def __tablename__(cls):
      return cls.__name__.lower()

   # Campo de id unico
   @declared_attr
   def __id__(cls):
      return 'id'

   # Id unico
   id                    = Column( Unicode(50), default=basicas.uuidTexto, primary_key=True)

   # Estado del registro
   _estado_              = Column( Unicode(10),  default=u'ACTIVO', index=True, nullable=False)

   # Fecha de creación
   _creado_en_           = Column( DateTime, nullable=False, default=basicas.fechaHora)

   # Fecha de actualización
   _actualizado_en_      = Column( DateTime, nullable=False, default=basicas.fechaHora, onupdate=basicas.fechaHora)

   # Unidad especifica
   _codigo_unidad_       = Column( Unicode(20), index=True, nullable=False, default=u'*')

   # Organizacion general
   _codigo_organizacion_ = Column( Unicode(20), index=True, nullable=False, default="*")

class DB_BASE_SIMPLE(object):
   # Base de definición
   @declared_attr
   def __base__(cls):
      return 'base_simple'

   # Nombre de la tabla
   @declared_attr
   def __tablename__(cls):
      return cls.__name__.lower()

   # Campo de id unico
   @declared_attr
   def __id__(cls):
      return 'id'