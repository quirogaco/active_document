#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime, uuid

import rapidjson
from rapidjson import DM_ISO8601, DM_SHIFT_TO_UTC

# Id unico
def uuidTexto(base=''):
   return str(uuid.uuid1()).lower()

# lee la fecha solo a�o, mes, dia, minutos, segundos, sin milisegundos
def fechaHora():
   ahora = datetime.datetime.now()
   ahoraParcial = datetime.datetime(ahora.year, ahora.month, ahora.day, ahora.hour, ahora.minute, ahora.second, 0)
   
   return ahoraParcial

def fecha():
   ahora = datetime.datetime.now()
   ahoraParcial = datetime.datetime(ahora.year, ahora.month, ahora.day, 0, 0, 0, 0)
   
   return ahoraParcial

def ano():
   ahora = datetime.datetime.now()
   
   return ahora.strftime("%Y")

# Json cargar datos 
def json_carga(datos_json):
   modoFecha = DM_ISO8601 | DM_SHIFT_TO_UTC
   datos = rapidjson.loads( datos_json, datetime_mode=modoFecha )

   return datos

# Json cargar datos de una archivo
def json_carga_archivo(nombre_archivo):
   modoFecha = DM_ISO8601 | DM_SHIFT_TO_UTC
   with open( nombre_archivo, 'r' ) as archivo_json: 
      datos = rapidjson.load( archivo_json, datetime_mode=modoFecha )

   return datos