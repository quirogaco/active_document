#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, base64, builtins
from pathlib import Path

from librerias.flujos         import flujos_leer_sql
from librerias.datos.archivos import leer_archivo

def manuales_pdf(operacion, clase, descarga, encabezados, parametros, pdf_id, id_tarea):
    print("manuales_pdf:", pdf_id)
    # Texto Base 64 a byte
    archivo_nombre = pdf_id
    base = builtins.rutaBase + "manuales/"
    ruta = Path(base + archivo_nombre) 
    if descarga == "no":
        archivo         = ruta.open('rb')
        archivo_tamano  = ruta.stat().st_size
        datos = leer_archivo.archivo_pdf_visor(encabezados, archivo, descarga, archivo_tamano) 
    else:
        datos = leer_archivo.descarga_archivo(ruta)
    
    return datos

# Publica función de llamado
CONFIGURACION_GENERAL["manejo_pdf"]["manuales_pdf"] = manuales_pdf
