#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from aplicacion.archivos   import archivo_operaciones

registro = archivo_operaciones.crear_archivo_relacion(   
    "radicado_web_juridica",    # estructura
    "radicado_web_juridica_01", # estructura_id
    "d:/FP0000000004.pdf",      # nombre_archivo_fuente
    "e-2021-82.pdf",            # nombre_objeto
    "datos.test"                # cubeta
)

"""
   #estructura,                # Estructura
   #estructura_id,             # Id de la estructura
   #nombre_archivo_fuente,     # Archivo en disco
   #nombre_objeto,             # Nombre del objeto MINIO
   #cubeta          = None,    # Bucket MINIO
   tipo_archivo    = None,    
   temporal        = False, 
   borrar_temporal = True
"""

#"d:/FP0000000004.pdf", "e-2021-82.pdf", "datos.test"

print("reshgitro:", registro)