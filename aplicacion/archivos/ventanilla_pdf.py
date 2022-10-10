#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from pathlib import Path

from fastapi.responses        import FileResponse
from librerias.flujos         import flujos_leer_sql
from librerias.datos.archivos import leer_archivo

def ventanilla_entrada(operacion, clase, descarga, encabezados, parametros, archivo_id):
   ruta_base  = "/mnt/repositorioCacIG/adjuntos/"
   ano        = str(parametros.get("fecha", ""))[0:4]
   idRadicado = str(parametros.get("idRadicado", ""))
   idArchivo  = str(parametros.get("id", ""))
   ruta_base  = "/mnt/repositorioCacIG/adjuntos/" + ano + "/" + idRadicado + "/" + idArchivo
   
   return FileResponse(ruta_base)

# Publica funcion de llamado
CONFIGURACION_GENERAL["manejo_pdf"]["ventanilla_entrada"] = ventanilla_entrada
