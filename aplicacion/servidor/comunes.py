#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, os, shutil, tempfile

# Publica información de tareas ejecutandose
from aplicacion.datos.redis import redis_datos

def publica_tarea(id_tarea, datos):
   datos_tarea = {
      '_usuario_': datos.get("_usuario_", {}),
      'accion'   : datos.get("accion", {}),
      'datos'    : datos.get("datos", {})
   }
   redis_datos.carga_tarea_ejecucion(id_tarea, datos_tarea)
  
def prepara_archivos(archivos):   
   lista_archivos = []
   if type(archivos) is list:
      for archivo in archivos:
         nombre_archivo = tempfile.gettempdir() + os.sep + archivo.filename
         with open(nombre_archivo, 'wb') as buffer:
            shutil.copyfileobj(archivo.file, buffer) 
            data = {
               "nombre_completo": nombre_archivo,
               "nombre"         : archivo.filename
            }
            lista_archivos.append(data)

   return lista_archivos