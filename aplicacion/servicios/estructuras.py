#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.estructuras import estructura_operaciones

def ejecutar(estructura, parametros, archivos, id_tarea):   
   resultado = {}
   accion    = parametros.get('__accion__', '')
   datos     = parametros.get('datos', {})
   if accion == 'insertar':
      resultado = estructura_operaciones.insertarEstructura(estructura, datos, archivos, id_tarea)

   elif accion == 'modificar':
      resultado = estructura_operaciones.modificarEstructura(estructura, datos, archivos, id_tarea)

   elif accion == 'eliminar':
      resultado = estructura_operaciones.eliminarEstructura(estructura, datos, archivos, id_tarea)

   elif accion == 'leerRegistro':
      resultado = estructura_operaciones.leerRegistroEstructura(estructura, datos, archivos, id_tarea)

   else:
      funcion   = CONFIGURACION_GENERAL["FUNCIONES_TAREAS"][accion]
      resultado = funcion(estructura, accion, parametros, {}, archivos, id_tarea)

   return resultado