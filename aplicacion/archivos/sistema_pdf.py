#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import pprint
from pathlib import Path

from librerias.datos.archivos import leer_archivo

def sistema_pdf(operacion, clase, descarga, encabezados, parametros, pdf_id, id_tarea):
   datos = leer_archivo.descarga_archivo_minio(operacion, clase, descarga, pdf_id)
   
   return datos


# Publica función de llamado
CONFIGURACION_GENERAL["manejo_pdf"]["sistema"] = sistema_pdf