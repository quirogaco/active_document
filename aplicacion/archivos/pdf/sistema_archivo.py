#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from typing import List
from fastapi           import Request
from fastapi.responses import StreamingResponse

from librerias.utilidades import basicas  


total_leidos = 0
total_tamano = 0
contador     = 0
def pdfVisorLocal(encabezados_peticion, parametros, archivo_nombre):
   global total_leidos, total_tamano, contador

   ruta                  = Path(archivo_nombre)
   archivo               = ruta.open('rb')
   archivo_tamano        = ruta.stat().st_size
   contenido_rango       = encabezados_peticion.get('range')
   contenido_longitud    = archivo_tamano
   total_tamano          = archivo_tamano
   estado_codigo         = 200
   encabezados_respuesta = {}
   estado_codigo         = 206

   if contenido_rango is not None:
      contenido_rango               = contenido_rango.strip().lower()
      contenido_rango               = contenido_rango.split('=')[-1]
      rango_inicio, rango_final, *_ = map(str.strip, (contenido_rango + '-').split('-'))
      rango_inicio                  = max(0, int(rango_inicio)) if rango_inicio else 0
      rango_final                   = min(contenido_longitud - 1, int(rango_final)) if rango_final else contenido_longitud - 1
      contenido_longitud            = (rango_final - rango_inicio) + 1
      archivo                       = rangoArchivo(archivo, inicio = rango_inicio, final = rango_final + 1)      
      encabezados_respuesta['Content-Range'] = f'bytes {rango_inicio}-{rango_final}/{contenido_longitud}'    

   else:
      rango_inicio       = 0
      rango_final        = 65536
      rango_final        = min(contenido_longitud - 1, rango_final) if rango_final else contenido_longitud - 1
      #contenido_longitud = (rango_final - rango_inicio) + 1
      archivo            = rangoArchivo(archivo, inicio = rango_inicio, final = rango_final + 1)
      #encabezados_respuesta['Content-Range'] = f'bytes {rango_inicio}-{rango_final}/{contenido_longitud}'    

   response = StreamingResponse \
   (
      archivo,
      media_type = 'application/pdf',
      status_code = estado_codigo,
   )

   response.headers.update \
   ({
      'Accept-Ranges': 'bytes',
      'Content-Length': str(contenido_longitud),
      **encabezados_respuesta,
   })

   return response



from librerias.flujos     import flujos_leer_sql


print("PFDS ...... CARGA")