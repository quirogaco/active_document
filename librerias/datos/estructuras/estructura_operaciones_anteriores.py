#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from librerias.datos.base import globales 
from librerias.utilidades import errores 

#################################
# Operaciones posteriores       #
# a insertar, modificar, borrar #
# en estructuras                #
#################################
def operaciones(estructura, accion, archivos, id_tarea, datos):
      try:
            # Funciones de tareas especifica 
            definicion        = globales.lee_definicion(estructura)
            tareas_anteriores = definicion.get("pre_tareas", [])
            for elemento in tareas_anteriores:
                  tarea      = elemento.get("tarea", None)
                  parametros = elemento.get("parametros", {}),            
                  funcion = CONFIGURACION_GENERAL["TAREAS_ESPECIFICAS"].get(tarea, None)
                  if funcion != None:
                        funcion(estructura, accion, datos, parametros, archivos, id_tarea)
      except:
            errores.mostrar_errores()

      return datos