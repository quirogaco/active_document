#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from datetime import datetime
import pprint

from librerias.datos.base import globales

def ejecutar(parametros):
   resultado = {
      "datos"     : {},
      "estructura": "",
      "definicion": ""
   }
   accion    = parametros["__accion__"]
   if accion == "leer":
      estructura = parametros["estructura"]
      definicion = parametros["definicion"]
      resultado["datos"] = globales.lee_definicion_visual(estructura, definicion)
      resultado["estructura"] = estructura
      resultado["definicion"] = definicion

   return resultado