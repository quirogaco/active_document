#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, base64
from pathlib import Path

from librerias.flujos         import flujos_leer_sql
from librerias.datos.archivos import leer_archivo

def pdf_disco(operacion, clase, descarga, encabezados, parametros, pdf_id, id_tarea):
    # Texto Base 64 a byte
    archivo_nombre_byte   = bytes(pdf_id, 'utf8')
    # Base 64 a texto original
    decodificado          = base64.b64decode( archivo_nombre_byte + b'==')    
    # Byte a texto
    archivo_nombre        = str( decodificado, 'utf-8')

    ruta                = Path(archivo_nombre) 
    if descarga == "no":
        archivo         = ruta.open('rb')
        archivo_tamano  = ruta.stat().st_size
        datos = leer_archivo.archivo_pdf_visor(encabezados, archivo, descarga, archivo_tamano) 
    else:
        datos = leer_archivo.descarga_archivo(ruta)
    
    return datos

# Publica función de llamado
CONFIGURACION_GENERAL["manejo_pdf"]["pdf_disco"] = pdf_disco
