#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, os, shutil, tempfile

from typing import List
import rapidjson
from rapidjson import DM_ISO8601, DM_SHIFT_TO_UTC, DM_NAIVE_IS_UTC, DM_IGNORE_TZ
from fastapi.responses import ORJSONResponse
from fastapi import Form, Request
from fastapi import File, UploadFile

from librerias.datos.sql  import sqalchemy_filtrar 
from librerias.utilidades import errores, basicas, directorio_activo
from librerias.datos.base import globales 

#############################################
# TOCA MOVERLO CADA UNO A SU PROPIO ESPACIO #
#############################################
import datetime
from sqlalchemy.sql.expression import and_
from librerias.datos.base import globales
from servicios import opciones_usuario
from librerias.datos.sql import sqalchemy_comunes

from .comunes import *

modoFecha = DM_ISO8601 | DM_SHIFT_TO_UTC | DM_NAIVE_IS_UTC | DM_IGNORE_TZ

from aplicacion.comunes import log_ingreso
from . import login

def prepara_post_data(datos, archivos):
   datos      = rapidjson.loads( datos, datetime_mode=modoFecha )
   archivos   = prepara_archivos(archivos)
   # Datos generaes de la tarea
   id_tarea   = basicas.uuidTexto() 
   publica_tarea(id_tarea, datos)

   return datos, archivos, id_tarea

def ejecuta_acciones(modulo, datos, archivos, id_tarea):
   try:
        respuesta = modulo.acciones_ejecuta(datos, archivos, id_tarea)
        
   except Exception as e:
      texto_error, ruta_error = errores.busca_error()


      print("")
      print("")    
      print("******** ERROR REQUEST *****************")
      print(ruta_error)
      print("****************************************")
      print("")
      print("")

      respuesta = ORJSONResponse(
         status_code = 500,
         headers = {
               "Access-Control-Allow-Origin" : "*",
               "Access-Control-Allow-Methods": "POST, PUT, GET, OPTIONS, DELETE",
               "Access-Control-Max-Age"      : "86400"
         },
         content = {
               "error": ruta_error
         }
      )

   return respuesta

from aplicacion.especificos.gestion import acciones_gestion
@_app.post( '/gestion_acciones' )
async def gestion_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):    
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = acciones_gestion.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

from aplicacion.especificos import especificos_archivo
@_app.post( '/gestion_archivo' )
async def gestion_archivo(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):    
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = especificos_archivo.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

from aplicacion.envios import acciones_envios
@_app.post( '/envio_acciones' )
async def envio_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):   
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = acciones_envios.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

from aplicacion.masivos import masivos_salidas
@_app.post( '/masivos_salidas' )
async def masivos_salidas_rest(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):    
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = masivos_salidas.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

#########################
# ESPECIFICOS GENERALES #
#########################
from aplicacion.especificos import especificos_manejo
@_app.post( '/especifico_acciones' )
async def especifico_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):    
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = especificos_manejo.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

##########
# FLUJOS #
##########
from aplicacion.especificos import especificos_flujo
@_app.post( '/flujo_acciones' )
async def flujo_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):       
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = especificos_flujo.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

############
# TRAMITES #
############
from aplicacion.especificos import especificos_tramite
@_app.post( '/tramite_acciones' )
async def tramite_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):       
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = especificos_tramite.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

############
# REPORTES #
############
from aplicacion.reportes import reportes_manejo
@_app.post( '/reportes_acciones' )
async def reportes_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):    
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = reportes_manejo.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

#########################
# FORMULARIOS DINAMICOS #
#########################
from aplicacion.especificos import especificos_formularios_dinamicos
@_app.post( '/formularios_dinamicos' )
async def formularios_dinamicos(
   archivos: List[UploadFile] = File,
   datos: str = Form(...)
):       
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = especificos_formularios_dinamicos.acciones_ejecuta(
      datos, 
      archivos, 
      id_tarea
   )
      
   return resultado

###############################
# DATOS FORMULARIOS DINAMICOS #
###############################
from aplicacion.especificos import especificos_datos_dinamicos
@_app.post( '/datos_dinamicos' )
async def datos_dinamicos(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):       
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = especificos_datos_dinamicos.acciones_ejecuta(
      datos, 
      archivos, 
      id_tarea
   )
      
   return resultado

####################
# MANEJO DE COPIAS #
####################
from aplicacion.especificos import especificos_informado
@_app.post( '/oculta_informados' )
async def oculta_informados(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):       
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = especificos_informado.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

###########
# ARCHIVO #
###########

#######
# TRD #
#######
from aplicacion.trd import trd_manejo
@_app.post( '/trd_acciones' )
async def trd_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):    
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = trd_manejo.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

from aplicacion.expedientes import expedientes_manejo

"""
@_app.get( '/expediente_acciones' )
async def expediente_acciones(requerimiento: Request): 
   #pprint.pprint(dir(requerimiento.query_params))  
   #parametros     = rapidjson.loads( requerimiento.query_params["datos"], datetime_mode=modoFecha )
   print("")
   print("")
   print("PARAMETROS get:")   
   print(requerimiento.query_params)
   #pprint.pprint(parametros)

   return {} 

"""

@_app.post( '/expediente_acciones' )
async def expediente_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):    
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = expedientes_manejo.acciones_ejecuta(datos, archivos, id_tarea)
   
   return resultado


#######
# TVD #
#######
from aplicacion.tvd import tvd_manejo
@_app.post( '/tvd_acciones' )
async def tvd_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):    
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   resultado = tvd_manejo.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado

from aplicacion.tvd_expedientes import tvd_expedientes_manejo
@_app.post( '/tvd_expediente_acciones' )
async def tvd_expediente_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):    
   datos, archivos, id_tarea = prepara_post_data(datos, archivos)
   expedientes_manejo.acciones_ejecuta(datos, archivos, id_tarea)
      
   return resultado