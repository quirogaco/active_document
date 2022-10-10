#!/usr/bin/python
# -*- coding: utf-8 -*-

from librerias.datos.sql import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from .indexar_datos import indexar
from . import logs

def crea_registro(datos_serie, trd_id):
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_serie_trd", datos_serie)
    indexar("agn_serie_trd", resultado["id"], trd_id)

    return resultado

def crear_serie(accion, datos={}, archivo=[], id_tarea=""):
    trd_id  = datos["trd_id"]  
    datos_serie = {
        "tabla"               : "TRD", 
        "codigo"              : datos["datos"]["codigo"], 
        "nombre"              : datos["datos"]["nombre"],
        "gestion"             : datos["datos"].get("gestion", 0),
        "central"             : datos["datos"].get("central", 0),
        "eliminacion"         : datos["datos"].get("eliminacion", "NO"),
        "seleccion"           : datos["datos"].get("seleccion", "NO"),
        "conservacion"        : datos["datos"].get("conservacion", "NO"),
        "micro_digitalizacion": datos["datos"].get("micro_digitalizacion", "NO"),
        "dependencia_id"      : datos["padre_id"] 
    }    
    resultado = crea_registro(datos_serie, trd_id)
    logs.log_trd("agn_trd", trd_id, "CREACIÓN DE SERIE - " + datos["datos"]["nombre"], "CREACION", id_tarea) 
    resultado["accion"] = accion    

    return resultado

def modificar_serie(accion, datos={}, archivo=[], id_tarea=""):
    id      = datos["datos"]["id"]
    trd_id  = datos["trd_id"]  
    datos_serie = {
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
    resultado = sqalchemy_modificar.modificar_un_registro("agn_serie_trd", id, datos_serie)
    logs.log_trd("agn_trd", trd_id, "MODIFICACIÓN DE SERIE - " + datos["datos"]["nombre"], "CREACION", id_tarea) 
    indexar("agn_serie_trd", resultado["id"], trd_id)
    resultado["accion"] = accion    

    return resultado

def salvar_serie(accion, datos={}, archivo=[], id_tarea=""):
    dependencia_id = datos["datos"].get("id", "")
    if dependencia_id == "":
        resultado = crear_serie(accion, datos, archivo, id_tarea)
    else:
        resultado = modificar_serie(accion, datos, archivo, id_tarea)
    
    return resultado

def borrar_serie(accion, datos={}, archivo=[], id_tarea=""):
    id         = datos["datos"]["id"]
    trd_id     = datos["trd_id"]  
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_serie_trd", id)
    logs.log_trd("agn_trd", trd_id, "BORRADO DE SERIE - " + datos["datos"]["nombre"], "CREACION", id_tarea) 
    indexar("agn_serie_trd", resultado["id"], trd_id)
    resultado["accion"] = accion
    
    return resultado