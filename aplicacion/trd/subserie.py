#!/usr/bin/python
# -*- coding: utf-8 -*-

from librerias.datos.sql import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from .indexar_datos import indexar
from . import logs


def crea_registro(datos_subserie, trd_id):
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_subserie_trd", datos_subserie)
    indexar("agn_subserie_trd", resultado["id"], trd_id)

    return resultado

def crear_subserie(accion, datos={}, archivo=[], id_tarea=""):
    trd_id = datos["trd_id"]  
    datos_subserie = {
        "tabla"               : "TRD", 
        "codigo"              : datos["datos"]["codigo"], 
        "nombre"              : datos["datos"]["nombre"],
        "gestion"             : datos["datos"].get("gestion", 0),
        "central"             : datos["datos"].get("central", 0),
        "eliminacion"         : datos["datos"].get("eliminacion", "NO"),
        "seleccion"           : datos["datos"].get("seleccion", "NO"),
        "conservacion"        : datos["datos"].get("conservacion", "NO"),
        "micro_digitalizacion": datos["datos"].get("micro_digitalizacion", "NO"),
        "serie_id"            : datos["padre_id"]
    }
    resultado = crea_registro(datos_subserie, trd_id)
    logs.log_trd("agn_trd", trd_id, "CREACIÓN DE SUBSERIE - " + datos["datos"]["nombre"], "CREACION", id_tarea) 
    resultado["accion"] = accion    

    return resultado

def modificar_subserie(accion, datos={}, archivo=[], id_tarea=""):
    id     = datos["datos"]["id"]
    trd_id = datos["trd_id"]   
    datos_subserie = {
        "codigo"              : datos["datos"]["codigo"], 
        "nombre"              : datos["datos"]["nombre"],
        "gestion"             : datos["datos"].get("gestion", 0),
        "central"             : datos["datos"].get("central", 0),
        "eliminacion"         : datos["datos"].get("eliminacion", "NO"),
        "seleccion"           : datos["datos"].get("seleccion", "NO"),
        "conservacion"        : datos["datos"].get("conservacion", "NO"),
        "micro_digitalizacion": datos["datos"].get("micro_digitalizacion", "NO"),
        "estado_"             : datos["datos"]["estado_"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_subserie_trd", id, datos_subserie)
    indexar("agn_subserie_trd", resultado["id"], trd_id)
    logs.log_trd("agn_trd", trd_id, "MODIFICACIÓN DE SUBSERIE - " + datos["datos"]["nombre"], "CREACION", id_tarea) 
    resultado["accion"] = accion    

    return resultado

def salvar_subserie(accion, datos={}, archivo=[], id_tarea=""):
    dependencia_id = datos["datos"].get("id", "")
    if dependencia_id == "":
        resultado = crear_subserie(accion, datos, archivo, id_tarea)
    else:
        resultado = modificar_subserie(accion, datos, archivo, id_tarea)
    
    return resultado

def borrar_subserie(accion, datos={}, archivo=[], id_tarea=""):
    id         = datos["datos"]["id"]
    trd_id     = datos["trd_id"]  
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_subserie_trd", id)
    indexar("agn_subserie_trd", resultado["id"], trd_id)
    logs.log_trd("agn_trd", trd_id, "BORRADO DE SUBSERIE - " + datos["datos"]["nombre"], "CREACION", id_tarea) 
    resultado["accion"] = accion
    
    return resultado