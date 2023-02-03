#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

from . import definiciones_visuales
from . import opciones_usuario

"""
servicios_diccionario = {
   "definicion"      : definiciones_visuales.ejecutar,
   "opciones_usuario": opciones_usuario.ejecutar
}

def ejecutar(servicio, parametros):
   resultado = {}
   funcion = servicios_diccionario.get(servicio, None)
   if funcion != None:
      resultado = funcion(parametros)
   else:
      pass # JCR !!! REVISAR ERRORES   

   return resultado
"""