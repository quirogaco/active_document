#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#from sqlalchemy.inspection import inspect

#from sqlalchemy.ext.declarative import declarative_base, as_declarative
from sqlathanor import declarative_base, AttributeConfiguration

# Se invocan por otro modulos, es necesario
from sqlalchemy import Column, Unicode, DateTime, Integer, Text
#from sqlalchemy_utils.types import json
from . import json_tipo as json

"""
@as_declarative()
class Base:
   def _asdict(self):
      print("SELG:", self)
      pprint.pprint( dir(self) )
      for c in inspect(self).mapper.column_attrs:
         key = c.key
         print(key)
         print(getattr(self, key))
      
      #return {c.key: getattr(self, c.key)
      #         for c in inspect(self).mapper.column_attrs}
      return {}
"""

# Declaracion de base sqlalchemy
def crea_base():
   base = declarative_base()
   #base  =  Base

   return base


def nada(item):
   return item

# Serializa valores de sqlalchemy
def serializa(campos=[]):
   atributos = []
   for campo in campos:
      atributo = {
         "name"          : campo,
         "supports_csv"  : True,
         "csv_sequence"  : 1,
         "supports_json" : True,
         "supports_yaml" : True,
         "supports_dict" : True,
         "on_serialize"  : nada,
         "on_deserialize": nada
      }
      atributos.append( AttributeConfiguration(**atributo) )

   return atributos

# Serializa valores de sqlalchemy, mas datos base
def serializa_base(campos=[]):
   campos.extend([
      'id', 
      'estado_', 
      'creado_en_', 
      'actualizado_en_', 
      'codigo_unidad_', 
      'codigo_organizacion_' 
   ])
   atributos = []
   for campo in campos:
      atributo = {
         "name"          : campo,
         "supports_csv"  : True,
         "csv_sequence"  : 1,
         "supports_json" : True,
         "supports_yaml" : True,
         "supports_dict" : True,
         "on_serialize"  : nada,
         "on_deserialize": nada
      }
      atributos.append( AttributeConfiguration(**atributo) )

   return atributos
