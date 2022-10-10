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
            # Tareas de relaciones EXTERNAS
            tareas = globales.lee_tarea(id_tarea)
            if tareas != None:
                  for tarea in tareas:  
                        tipo_operacion = tarea.get("tipo", None)   

                        if  tipo_operacion == "relacion":             
                              ################################################
                              # RELACION A REGISTROS EXTERNOS QUE YA EXISTEN #
                              # ##############################################              
                              funcion = CONFIGURACION_GENERAL["FUNCIONES_TAREAS"].get('relaciones_externas', None)
                              if funcion != None:
                                    funcion(estructura, accion, datos, tarea, archivos, id_tarea)
                              
                        elif tipo_operacion == "archivos":             
                              #######################
                              # RELACION A ARCHIVOS #
                              # #####################              
                              funcion = CONFIGURACION_GENERAL["FUNCIONES_TAREAS"].get('archivos', None)
                              if funcion != None:
                                    funcion(estructura, accion, datos, tarea, archivos, id_tarea) 
                                    
                        else:
                              funcion = CONFIGURACION_GENERAL["TAREAS_ESPECIFICAS"].get(tipo_operacion, None)
                              if funcion != None:
                                    funcion(estructura, accion, datos, tarea, archivos, id_tarea)

            # Funciones ultimas de procesamiento
            funcion = globales.lee_procesamiento(estructura, "ultima_estructura")
            if funcion != None:
                  funcion(estructura, accion, datos, tarea, archivos, id_tarea)
      except:
            errores.mostrar_errores()

      return datos