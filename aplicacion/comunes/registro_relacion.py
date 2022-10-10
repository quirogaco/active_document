#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, pathlib, pprint

from librerias.datos.sql   import sqalchemy_insertar

#####################################
# Crea registro de relacion ARCHIVO #
#####################################
def crear_registro_relacion(   
   origen,        # Estructura origen
   origen_id,     # Id de la estructura origen
   origen_role,   # Role registro origen
   destino,       # Estructura destino
   destino_id,    # Id de la estructura destino
   destino_role,  # Role registro destino
   tipo_relacion, # Tipo de relación origen-destino
   cardinalidad   # Cardinalida simple, multiple
):
   ############################
   # Crea registro de archivo #
   ############################
   data_relacion = {
      'origen'       : origen,
      'origen_id'    : origen_id,
      'origen_role'  : origen_role,
      'destino'      : destino,
      'destino_id'   : destino_id,
      'destino_role' : destino_role,
      'tipo_relacion': tipo_relacion,
      'cardinalidad' : cardinalidad
   }
   resultado = sqalchemy_insertar.insertar_registro_estructura("estructura_relacion", data_relacion)
   
   return resultado