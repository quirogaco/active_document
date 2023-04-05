#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from pathlib import Path

from fastapi.responses        import FileResponse
from librerias.flujos         import flujos_leer_sql
from librerias.datos.archivos import leer_archivo

def archivo_pqrs(operacion, clase, descarga, encabezados, parametros, archivo_id):
    #archivo_nombre  = 'D:/Activiti_User_Guide.pdf'
   #archivo_nombre  = 'D:/A.docx'
   #ruta            = Path(archivo_nombre)
   #archivo         = ruta.open('rb')
   #archivo_tamano  = ruta.stat().st_size
   
   #datos           = leer_archivo.archivo(encabezados, archivo, descarga, archivo_tamano)    
   #return datos
   
   print("archivo_pqrs FileResponse-1:", archivo_id)
   pprint.pprint(parametros)
   ruta_base = "/mnt/repositorioCacIG/adjuntos/"
   ano        = str(parametros.get("fecha", ""))[0:4]
   idRadicado = str(parametros.get("idRadicado", ""))
   idArchivo  = str(parametros.get("id", ""))
   ruta_base = "/mnt/repositorioCacIG/adjuntos/" + ano + "/" + idRadicado + "/" + idArchivo
   print("rutabase:",  ruta_base)

   return FileResponse(ruta_base)


# Publica función de llamado
CONFIGURACION_GENERAL["manejo_archivo"]["pqrs"] = archivo_pqrs
