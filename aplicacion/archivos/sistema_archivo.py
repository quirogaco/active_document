#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from librerias.datos.archivos import leer_archivo

def sistema_archivo(operacion, clase, descarga, encabezados, parametros, archivo_id, id_tarea):
   print("")
   print("-------------------")
   print("sistema_archivo:", operacion, clase, descarga, archivo_id)
   print("-------------------")
   print("")

   return leer_archivo.descarga_archivo_minio(operacion, clase, descarga, archivo_id)

# Publica función de llamado
CONFIGURACION_GENERAL["manejo_archivo"]["sistema"] = sistema_archivo