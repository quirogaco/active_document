#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

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

@_app.post( '/test_01' )
#async def test_01(datos: str = Form(...)):    
async def test_01():
   #datos     = rapidjson.loads( datos, datetime_mode=modoFecha )
   #id_tarea  = basicas.uuidTexto() 
   #resultado = datos
   resultado = {}

   return resultado