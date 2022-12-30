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

def rangoArchivo(
      archivo: IO[bytes],
      inicio : int = 0,
      final : int = None,
      bloque_tamano: int = 65536,
) -> Generator[bytes, None, None]:
   global total_leidos, total_tamano, contador

   consumido = 0
   archivo.seek(inicio)
   while True:
      contador += 1
      datos_longitud = min(bloque_tamano, final - inicio - consumido) if final else bloque_tamano
      total_leidos += datos_longitud
      if datos_longitud <= 0:
            break

      datos = archivo.read(datos_longitud)
      if not datos:
            break

      consumido += datos_longitud

      yield datos

   if hasattr(archivo, 'close'):
      archivo.close()

total_leidos = 0
total_tamano = 0
contador     = 0            
def archivo_pdf_visor(encabezados_peticion, archivo, descarga, archivo_tamano):
   global total_leidos, total_tamano, contador

   print("<<<<<<<<<<<<<<<<<<< ARCHIVO >>>>>>>>>>>>>>>>>>>>>>>")
   contenido_rango       = encabezados_peticion.get('range')
   contenido_longitud    = archivo_tamano
   total_tamano          = archivo_tamano
   estado_codigo         = 200
   encabezados_respuesta = {}
   estado_codigo         = 206

   #if descarga != "si":
   # Envio a visor
   if contenido_rango is not None:
      contenido_rango               = contenido_rango.strip().lower()
      contenido_rango               = contenido_rango.split('=')[-1]
      rango_inicio, rango_final, *_ = map(str.strip, (contenido_rango + '-').split('-'))
      rango_inicio                  = max(0, int(rango_inicio)) if rango_inicio else 0
      rango_final                   = min(contenido_longitud - 1, int(rango_final)) if rango_final else contenido_longitud - 1
      contenido_longitud            = (rango_final - rango_inicio) + 1
      archivo_datos                 = rangoArchivo(archivo, inicio = rango_inicio, final = rango_final + 1)      
      encabezados_respuesta['Content-Range'] = f'bytes {rango_inicio}-{rango_final}/{contenido_longitud}'  
      total_leidos += contenido_longitud 
      print("LEIDO RANGO>>>:", total_tamano, total_leidos, contenido_longitud)
   else:
      rango_inicio       = 0
      rango_final        = 65536
      rango_final        = min(contenido_longitud - 1, rango_final) if rango_final else contenido_longitud - 1
      print("LEIDO noo --> RANGO>>>:", rango_final)
      #contenido_longitud = (rango_final - rango_inicio) + 1
      archivo_datos      = rangoArchivo(archivo, inicio = rango_inicio, final = rango_final + 1)
      #encabezados_respuesta['Content-Range'] = f'bytes {rango_inicio}-{rango_final}/{contenido_longitud}'          

   response = StreamingResponse(          
      archivo_datos,
      media_type = 'application/pdf',
      status_code = estado_codigo,
   )

   response.headers.update({
      'Accept-Ranges': 'bytes',
      'Content-Length': str(contenido_longitud),
      **encabezados_respuesta,
   })      
      
   return response

def descarga_archivo(ruta):
   media_type = mimetypes.guess_type(ruta)[0]
   def iterar_archivo():  
      with open(ruta, mode="rb") as archivo:  
         yield from archivo  

   return StreamingResponse(iterar_archivo(), media_type=media_type)

def leer_buffer_minio(archivo_id):
   registro_archivo  = sqalchemy_leer.leer_un_registro("archivos_anexos", archivo_id)
   #"""
   print("")
   print("----------------------------------")
   pprint.pprint(registro_archivo)
   print("----------------------------------")
   print("")
   #"""
   media_type         = mimetypes.guess_type(registro_archivo["nombre"])[0]
   buffer             = io.BytesIO()
   contenido_longitud = minio_acciones.leer_objeto_buffer(registro_archivo["cubeta"], registro_archivo["nombre"], buffer)   
   buffer.seek(0)

   return media_type, contenido_longitud, buffer, registro_archivo

def salva_archivo_minio_ruta(archivo_id, ruta_destino=""):
   media_type, contenido_longitud, buffer, registro_archivo = leer_buffer_minio(archivo_id)
   if ruta_destino == "":
      ruta_destino = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + "." + registro_archivo["tipo_archivo"]
   
   print("")
   print("----------ruta_destino  ----------")
   pprint.pprint(ruta_destino)
   print("----------------------------------")
   print("")
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