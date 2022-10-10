#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random 

from . import tvd_expediente
from . import tvd_archivo_base

acciones_funcion = {
    # EXPEDIENTES
    "crear_expediente"    : tvd_expediente.crear_expediente,
    "modificar_expediente": tvd_expediente.modificar_expediente,
    "borrar_expediente"   : tvd_expediente.borrar_expediente,
    
    # ARCHIVOS
    "salvar_archivo_base" : tvd_archivo_base.salvar_archivo,
}

import time
def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]

    print("")
    print("")
    print("------------------------------------------------")
    print('EXPEDIENTES MANEJO TVD --- -> acciones_ejecuta:', id_tarea) 
    print('datos:')
    pprint.pprint(datos)   
    print('archivos:', archivos)
    
    resultado = datos
    funcion   = acciones_funcion[accion]
    resultado = funcion(accion, datos, archivos, id_tarea)
    print("------------------------------------------------")
    print("")
    print("")

    retorna = datos
    retorna["datos"] = resultado

    return retorna
