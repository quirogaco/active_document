#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from datetime import datetime

from librerias.datos.base    import globales
from librerias.datos.elastic import elastic_busquedas

# Si tiene filtros y estructuras espeficicas
def estructuras_dinamicas(estructura, parametros):   
   funcion = globales.lee_estructura_dinamica(estructura)
   if funcion != None:
      estructura, parametros = funcion(estructura, parametros)

   return estructura, parametros

# Si es estructura que no esta en elastic, ej: lista o dicionario del sistema
def estructura_especial(estructura, parametros):
   resultado = None
   funcion   = globales.lee_estructura_especial(estructura)
   if funcion != None:
      resultado = funcion(estructura, parametros)     

   return resultado


# Ejecuta la consulta sobre ELASTIC, los datos viene en texto.
def ejecutar(estructura, parametros, id_tarea):
   resultado = estructura_especial(estructura, parametros)
   if resultado is None:
      estructura, parametros = estructuras_dinamicas(estructura, parametros)
      definicion = globales.lee_definicion(estructura)
      resultado  = elastic_busquedas.ejecutar(estructura, parametros, definicion, id_tarea)

   return resultado