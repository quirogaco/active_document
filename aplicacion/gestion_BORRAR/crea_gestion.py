#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.estructuras import estructura_operaciones_sql
from .                           import crea_gestion_base

##########################
#  RUTINAS DE VENTANILLA #
##########################    
def ventanilla_gestion(datos={}, archivos=[], id_tarea=""):
    pqrs        = datos.get("pqrs", "NO")
    radicado_id = datos["id"]
    if pqrs == "NO":
        crea_gestion_base.crea_registro_gestion(datos, archivos, id_tarea)
    else:
        crea_gestion_base.actualiza_radicado(radicado_id, "PQRS", id_tarea)

    # Indexar radicado de nuevo
    estructura_operaciones_sql.indexar_registro_SQL("base", "radicados_entrada", radicado_id, True)

####################
#  RUTINAS DE PQRS #
####################4
def pqrs_gestion(estructura, accion, datos, tarea, archivos, id_tarea):    
    resultado   = {}
    datos       = datos["datos"]  
    radicado_id = datos["id"]
    ventanilla  = datos.get("ventanilla", "NO")
    if ventanilla == "NO":
        crea_gestion_base.crea_registro_gestion(datos, archivos, id_tarea)
    else:
        crea_gestion_base.actualiza_radicado(radicado_id, "VENTANILLA", id_tarea)

    # Indexar radicado de nuevo
    estructura_operaciones_sql.indexar_registro_SQL("base", "radicados_entrada", radicado_id, True)

    return resultado

# Publica funcion para llamado
CONFIGURACION_GENERAL["FUNCIONES_TAREAS"]["pqrs_gestion"] = pqrs_gestion