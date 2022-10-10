#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pprint
from pathlib import Path

from fastapi.responses        import FileResponse
from librerias.flujos         import flujos_leer_sql
from librerias.datos.archivos import leer_archivo

def archivo_pqrs(operacion, clase, descarga, encabezados, parametros, archivo_id, id_tarea):
    radicado_id, fecha, archivo_id = archivo_id.split('_')
    archivo_nombre =  '/mnt/repositorioCacIG/adjuntos/' + fecha[0:4] + "/" + radicado_id + "/" + archivo_id
    
    return FileResponse(archivo_nombre)


# Publica funci�n de llamado
CONFIGURACION_GENERAL["manejo_archivo"]["pqrs"] = archivo_pqrs
