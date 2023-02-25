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
from librerias.utilidades import directorio_activo

#############################################
# TOCA MOVERLO CADA UNO A SU PROPIO ESPACIO #
#############################################
import datetime
from sqlalchemy.sql.expression import and_
from librerias.datos.base import globales
from servicios import opciones_usuario
from librerias.datos.sql  import sqalchemy_comunes

from .comunes import *

modoFecha = DM_ISO8601 | DM_SHIFT_TO_UTC | DM_NAIVE_IS_UTC | DM_IGNORE_TZ

def ingreso_local(codigo, clave):
   registro_usuario = None
   codigo   = codigo.replace("*", "")
   clave    = clave.upper()
   filtros  = [ [ "codigo", "=", codigo ], [ "clave", "=", clave ] ]
   usuarios = sqalchemy_filtrar.filtrarOrdena(estructura="usuarios", filtros=filtros, ordenamientos=[])   
   if len(usuarios) > 0:
      registro_usuario = usuarios[0]
   
   return registro_usuario

def ingreso_directorio(codigo, clave):
   registro_usuario = None
   #codigo   = codigo.upper()
   #clave    = clave.upper()
   filtros  = [ [ "codigo", "=", codigo ] ]
   usuarios = sqalchemy_filtrar.filtrarOrdena(
      estructura="usuarios", 
      filtros=filtros, 
      ordenamientos=[]
   )     
   print("usuarios:", usuarios)
   if len(usuarios) > 0:
      registro_usuario = usuarios[0]
   
   return registro_usuario

def datos_usuario(registro_usuario):
   datos             = {}
   datos["opciones"] = opciones_usuario.leer_opciones(registro_usuario)
   datos["usuario"]  = {
      "id"                : registro_usuario["id"],
      "codigo"            : registro_usuario["codigo"],
      "nombre"            : registro_usuario["nombre"],
      "correo"            : registro_usuario["correo"],
      "dependencia_id"    : registro_usuario["dependencia_id"],
      "dependencia_nombre": registro_usuario["dependencia_nombre"],
      "ubicacion_id"      : registro_usuario["ubicacion_id"],
      "ubicacion_nombre"  : registro_usuario["ubicacion_nombre"],         
      "reemplaza_id"      : registro_usuario["reemplaza_id"],   
      "roles_especificos" : registro_usuario["roles_especificos"],          
   }
   datos["sesion"]  = {
      "id"          : "xxx-1-2",
      "fecha"       : datetime.datetime.now(),
      "peticiones"  : 0,         
   }

   return datos

from aplicacion.comunes import log_ingreso

@_app.get( '/ingreso_sistema' )
async def ingreso_sistema(requerimiento: Request):   
   parametros  = requerimiento.query_params._dict
   ldap_ip     = "172.16.1.20"
   ldap_puerto = "389"
   
   # Valores iniciales
   registro_usuario = None
   mensaje = "Usuario invalido"     
   resultado = {
      "datos"  : {},
      "error"  : "si",
      "mensaje": mensaje   
   }   

   # Parametros de login
   estado = "INGRESADO"
   ip_peticion = requerimiento.client.host  
   codigo = parametros["codigo"]
   clave = parametros["clave"]
   print('/ingreso_sistema', codigo, clave)

   if codigo.find("*") > -1:
      # Usuario sistema
      registro_usuario = ingreso_local(codigo, clave)
      if (registro_usuario == None):
         mensaje = "Usuario NO registrado en la APLICACION"
         estado = "NEGADO"   
   else:
      # Usuario directorio activo
      da = directorio_activo.validar_usuario(
         codigo, 
         clave, 
         ldap_ip, 
         ldap_puerto
      )
      print("DAAAA:", da)
      if (da in  ["", None]):
         registro_usuario = ingreso_directorio(codigo, clave)
         if (registro_usuario == None):
            mensaje = "Usuario NO registrado en la APLICACION"
            estado = "NEGADO"   
      else:
         mensaje = "Usuario NO registrado en la ENTIDAD"
         estado = "NEGADO"   

   if (registro_usuario != None):   
      if (len(registro_usuario["roles_ids"]) > 0): 
         mensaje = ""   
         datos = datos_usuario(registro_usuario)
         resultado["error"] = "no" 
         resultado["datos"] = datos
      else:
         if codigo not in ["JEFE*", "ENLACE*", "PROFESIONAL*"]:
            mensaje = "Usuario NO tiene ROLES asignados"
            estado = "NEGADO" 
            resultado["mensaje"] = mensaje
         else:
            mensaje = ""   
            datos = datos_usuario(registro_usuario)
            resultado["error"] = "no" 
            resultado["datos"] = datos
   else:
      resultado["mensaje"] = mensaje    

   log_ingreso.crea_log("INGRESAR", codigo, ip_peticion, estado )

   resultado["mensaje"] = mensaje

   pprint.pprint(registro_usuario)

   return resultado