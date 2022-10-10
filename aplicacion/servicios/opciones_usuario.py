#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales
from librerias.datos.sql  import sqalchemy_filtrar 

from . import opciones_dinamicos
from . import opciones_envios
from . import opciones_generales_cfg
from . import opciones_gestion
from . import opciones_migracion
from . import opciones_radicacion
from . import opciones_radicacion_cfg
from . import opciones_trd
from . import opciones_tvd
from . import opciones_archivo_cfg

opciones_usuario = []
opciones_usuario.extend(opciones_radicacion_cfg.opciones)
opciones_usuario.extend(opciones_generales_cfg.opciones)
opciones_usuario.extend(opciones_archivo_cfg.opciones)
opciones_usuario.extend(opciones_migracion.opciones)
opciones_usuario.extend(opciones_radicacion.opciones)
opciones_usuario.extend(opciones_gestion.opciones)
opciones_usuario.extend(opciones_envios.opciones)
opciones_usuario.extend(opciones_trd.opciones)
opciones_usuario.extend(opciones_tvd.opciones)
opciones_usuario.extend(opciones_dinamicos.opciones)

def leer_opciones(usuario):
   roles_id    = usuario["roles_ids"]
   opciones_id = []
   for role_id in roles_id:
      filtros  = [ [ "id", "=", role_id ] ]
      roles    = sqalchemy_filtrar.filtrarOrdena(estructura="roles", filtros=filtros, ordenamientos=[]) 
      if len(roles) > 0:
         role = roles[0]
         opciones = role["opciones_id"]
         opciones_id.extend(opciones)

   # Filtra los datos especificos
   listado = []
   for opcion in opciones_usuario:
      definicion = opcion.get("definicion") 
      if definicion != None:
         if (definicion.get("id") in opciones_id) or (len(opciones_id) == 0):
            adicionales = opcion.get("adicionales", []) 
            forma       = opcion.get("forma") 
            grid        = opcion.get("grid")            
            # Datos de menu
            if forma != None:
               listado.append(forma)

            if grid != None:
               listado.append(grid)
            
            for adicional in adicionales:
               listado.append(adicional)

   """
   print("")
   print("")
   print("")
   print("OPCIONES:")
   pprint.pprint(opciones_id)
   pprint.pprint(listado)
   print("")
   print("")
   print("")
   """
   
   return listado

def opciones_sistema_estructura(estructura, parametros):
   # Filtra los datos especificos
   listado = []
   for opcion in opciones_usuario:
      definicion = opcion.get("definicion") 
      if definicion != None:
         listado.append(definicion)

   listado = sorted(listado, key = lambda item: item['nombre'])
   
   resultado = None
   if len(listado) > 0:
      resultado = {
         "total": len(listado),
         "items": listado
      }
   
   return resultado

globales.carga_estructura_especial("opciones_sistema", opciones_sistema_estructura)