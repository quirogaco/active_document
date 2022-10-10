#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from pathlib import Path

from fastapi.responses        import FileResponse
from librerias.flujos         import flujos_leer_sql
from librerias.datos.archivos import leer_archivo

def ventanilla_entrada(operacion, clase, descarga, encabezados, parametros, archivo_id):
    print("ventanilla_entrada ARCHIVO:", archivo_id)
    pprint.pprint(parametros)
    ruta_base = parametros['path'][3:]

    print("ruta_base-0", ruta_base)
    ruta_base = ("/BACKUP/16-03-2021/" + ruta_base).replace("\\", "/")
    print("ruta_base-1", ruta_base)    
    
    return FileResponse(ruta_base)

# Publica función de llamado
CONFIGURACION_GENERAL["manejo_archivo"]["ventanilla_entrada"] = ventanilla_entrada
