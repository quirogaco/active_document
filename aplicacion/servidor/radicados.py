#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, os, shutil, tempfile

from typing import List
import rapidjson
from rapidjson import DM_ISO8601, DM_SHIFT_TO_UTC, DM_NAIVE_IS_UTC, DM_IGNORE_TZ
from fastapi.responses import ORJSONResponse
from fastapi           import Form, Request
from fastapi           import File, UploadFile

from librerias.datos.sql  import sqalchemy_filtrar 
from librerias.utilidades import basicas 
from librerias.datos.base import globales 

#############################################
# TOCA MOVERLO CADA UNO A SU PROPIO ESPACIO #
#############################################
import datetime
from sqlalchemy.sql.expression import and_
from librerias.datos.base import globales

from .comunes import *

modoFecha = DM_ISO8601 | DM_SHIFT_TO_UTC | DM_NAIVE_IS_UTC | DM_IGNORE_TZ

from aplicacion.especificos import especificos_radicado
@_app.post( '/radicados_acciones' )
async def radicados_acciones(
   archivos: List[UploadFile] = File, 
   datos: str = Form(...)
):    
   datos = rapidjson.loads( datos, datetime_mode=modoFecha )
   archivos = prepara_archivos(archivos)
   # Datos generales de la tarea
   id_tarea = basicas.uuidTexto() 
   publica_tarea(id_tarea, datos)
   # Accion de gestion
   print("radicados_acciones:", id_tarea)
   resultado = especificos_radicado.acciones_ejecuta(datos, archivos, id_tarea)

   """
   print("")
   print("")
   print("########### RESULTADO ##############")
   print(resultado)
   print("#########################")
   print("")
   print("")
   """
   
   return resultado