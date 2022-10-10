#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
import io
import os
import mimetypes
import tempfile

from fastapi.responses     import StreamingResponse
from typing                import IO, Generator
from librerias.datos.minio import minio_acciones
from librerias.datos.sql   import sqalchemy_leer
from librerias.utilidades  import basicas  

def leer_buffer_minio(archivo_id):
   registro_archivo  = sqalchemy_leer.leer_un_registro("archivos_anexos", archivo_id)
   """
   print("") 
   print("----------------------------------")
   pprint.pprint(registro_archivo)
   print("----------------------------------")
   print("")
   """
   media_type         = mimetypes.guess_type(registro_archivo["nombre"])[0]
   buffer             = io.BytesIO()
   contenido_longitud = minio_acciones.leer_objeto_buffer(registro_archivo["cubeta"], registro_archivo["nombre"], buffer)   
   buffer.seek(0)

   return media_type, contenido_longitud, buffer, registro_archivo

def salva_archivo_minio_ruta(archivo_id, ruta_destino=""):
   media_type, contenido_longitud, buffer, registro_archivo = leer_buffer_minio(archivo_id)
   if ruta_destino == "":
      ruta_destino = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + "." + registro_archivo["tipo_archivo"]
      
   with open(ruta_destino, 'wb') as archivo:
      archivo.write(buffer.getbuffer())

   return ruta_destino

def salva_archivo_minio(archivo_id):
   nombre_archivo = salva_archivo_minio_ruta(archivo_id, ruta_destino="")

   return nombre_archivo

def descarga_archivo_minio(operacion, clase, descarga, archivo_id):
   media_type, contenido_longitud, buffer, registro_archivo = leer_buffer_minio(archivo_id)
   encabezados_respuesta = {}
   response = StreamingResponse(          
      buffer,
      media_type  = media_type
   )
   response.headers.update({
      'Content-Length': str(contenido_longitud),
      **encabezados_respuesta,
   })
      
   return response