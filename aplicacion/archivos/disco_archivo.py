#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pprint, base64
from pathlib import Path

from fastapi.responses        import FileResponse

def disco_archivo(operacion, clase, descarga, encabezados, parametros, archivo_id, id_tarea):
    # Texto Base 64 a byte
    archivo_nombre_byte   = bytes(archivo_id, 'utf8')
    # Base 64 a texto original
    decodificado          = base64.b64decode( archivo_nombre_byte + b'==')    
    # Byte a texto
    archivo_nombre        = str( decodificado, 'utf-8')

    print("archivo_nombre-0", archivo_nombre)    
    
    return FileResponse(archivo_nombre)

# Publica función de llamado
CONFIGURACION_GENERAL["manejo_archivo"]["disco_archivo"] = disco_archivo