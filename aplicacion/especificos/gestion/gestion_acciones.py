#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from aplicacion.comunes  import manejo_archivos

# ARCHIVOS 
def gestion_pdf_principal(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    resultado = {
        "pdf_informacion": ""
    }
    datos = datos['datos']
    archivos = manejo_archivos.buca_anexo_especifico_id(datos["origen_id"], "principal")   
    if len(archivos) > 0:
        resultado = {
            "pdf_informacion": archivos[0]
        }
    
    return resultado