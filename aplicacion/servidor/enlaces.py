#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, os, shutil, tempfile
import builtins

from typing import List
import rapidjson
from rapidjson import DM_ISO8601, DM_SHIFT_TO_UTC, DM_NAIVE_IS_UTC, DM_IGNORE_TZ
from fastapi.responses import ORJSONResponse
from fastapi           import Form, Request
from fastapi           import File, UploadFile
from fastapi.responses import FileResponse

from librerias.utilidades import basicas 
from librerias.datos.base import globales 

from .comunes import *

from servicios import servicios
@_app.get( '/servicios/{servicio}', response_class=ORJSONResponse )
async def servicio(servicio:str, requerimiento: Request ):
   parametros = requerimiento.query_params._dict
   resultado  = servicios.ejecutar(servicio, parametros)
   
   return resultado

from servicios import estructuras

modoFecha = DM_ISO8601 | DM_SHIFT_TO_UTC | DM_NAIVE_IS_UTC | DM_IGNORE_TZ
@_app.post( '/estructuras/comandos/{estructura}' )
async def estructuras_comandos(estructura:str, archivos: List[UploadFile] = File, datos: str = Form(...)):    
   datos    = rapidjson.loads( datos, datetime_mode=modoFecha )
   archivos = prepara_archivos(archivos)
   # Datos generales de la tarea
   id_tarea = basicas.uuidTexto() 
   publica_tarea(id_tarea, datos)
   #"""
   print("")
   print("")
   print("------------------------------------------------")
   print('/estructuras/comandos/{estructura}:', estructura) 
   print('datos:')
   pprint.pprint(datos)   
   print('archivos:', archivos)
   print("------------------------------------------------")
   print("")
   print("")
   #"""
   resultado = estructuras.ejecutar(estructura, datos, archivos, id_tarea=id_tarea)   
   resultado["peticion"] = {
      "estructura": estructura, 
      "parametros": datos
   }
   
   return resultado

from servicios import consultas
@_app.post( '/estructuras/consulta/{estructura}' )
async def estructuras_consulta(estructura:str, requerimiento: Request ):
   forma      =  await requerimiento.body()
   """
   print("")
   print('/estructuras/consulta/{estructura}:', estructura)  
   pprint.pprint(forma)
   """
   parametros = rapidjson.loads( forma, datetime_mode=rapidjson.DM_ISO8601)
   # Datos generaes de la tarea
   id_tarea = basicas.uuidTexto() 
   publica_tarea(id_tarea, parametros)
   
   #"""
   print('parametros-2:')
   pprint.pprint(parametros)
   print("")
   print("")
   print("")
   #"""
   data       = consultas.ejecutar(estructura, parametros, id_tarea)
   
   resultado  = {
      "data"   : data, 
      "error"  : "no",
      "mensaje": ""
   }
   """
   print("")
   print("")
   print("RESULTADO--->")
   pprint.pprint(resultado)
   """
   
   return resultado

@_app.get( '/manejo_pdf/{operacion}/{clase}/{descarga}/{pdf_id}' )
async def manejo_pdf(operacion:str, clase:str, descarga:str, pdf_id:str, requerimiento: Request ):
   global total_leidos, contador

   encabezados    = dict(requerimiento.headers)
   parametros     = requerimiento.query_params
   
   id_tarea = basicas.uuidTexto() 
   funcion = CONFIGURACION_GENERAL["manejo_pdf"].get(operacion, None)
   print("manejo_pdf:", funcion)
   
   return funcion(operacion, clase, descarga, encabezados, parametros, pdf_id, id_tarea)

@_app.get( '/manejo_archivo/{operacion}/{clase}/{descarga}/{archivo_id}' )
async def manejo_archivo(operacion:str, clase:str, descarga:str, archivo_id:str, requerimiento: Request):
   global total_leidos, contador

   encabezados    = dict(requerimiento.headers)
   #body           =  await requerimiento.body()
   #parametros     = rapidjson.loads( body, datetime_mode=modoFecha )
   #parametros.update( requerimiento.query_params )
   parametros     = requerimiento.query_params
   id_tarea       = basicas.uuidTexto() 
   
   funcion        = CONFIGURACION_GENERAL["manejo_archivo"].get(operacion, None)
   #print("manejo_archivo------>>>>>", operacion, parametros, " - funcion:", funcion)

   return funcion(operacion, clase, descarga, encabezados, parametros, archivo_id, id_tarea)

@_app.get( '/definiciones_visuales/{clase}/{tipo}' )
async def definiciones(clase:str, tipo:str, requerimiento: Request ):
      parametros = requerimiento.query_params._dict
   
      definicion = CONFIGURACION_GENERAL["definiciones_visuales"][clase].get(tipo, None)
   
      resultado = {
         "datos": definicion
      }
      
      return resultado

@_app.get( '/logo_ingreso' )
async def logo_ingreso():
   ruta_archivo = builtins.rutaBase + "/aplicacion/servidor/logo_ingreso.jpg"
   print('/logo_ingreso>', ruta_archivo)
    
   return FileResponse(ruta_archivo)

#############################################
# TOCA MOVERLO CADA UNO A SU PROPIO ESPACIO #
#############################################

from .especificos import * 
from .radicados   import * 
from .test        import * 