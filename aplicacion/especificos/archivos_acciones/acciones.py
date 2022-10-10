#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from aplicacion.comunes      import indexar_datos
from aplicacion.comunes      import manejo_archivos

# ARCHIVOS 
def salvar_archivo(accion, datos={}, archivos=[], id_tarea=""):
    manejo_archivos.manejo(datos["datos"]["estructura"], "insertar", {"id":datos["datos"]["origen_id"]}, archivos, id_tarea, tipo_relacion = datos["datos"]["relacion"])
    indexar_datos.indexar_estructura(datos["datos"]["estructura"], datos["datos"]["origen_id"], 60)
    
    return {}