#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

from librerias.datos.sql import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from .indexar_datos import indexar
from . import logs

def crea_datos(datos, trd_id):
    datos_dependencia = {
        "tabla" : "TRD", 
        "codigo": datos["codigo"], 
        "nombre": datos["nombre"],
        "trd_id": trd_id,
        "datos" : {
            "dependencias_gestion": datos.get("dependencias_gestion", [])
        }
    }

    return datos_dependencia

def crea_registro(datos_dependencia, trd_id):
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_dependencia_trd", datos_dependencia)
    indexar("agn_dependencia_trd", resultado["id"], trd_id)

    return resultado

def crear_dependencia(accion, datos={}, archivo=[], id_tarea=""):
    padre_id   = datos["datos"]["padre_id"] 
    trd_id     = datos["trd_id"]  
    datos_dependencia = crea_datos(datos["datos"], trd_id)
    # Hija de otra dependencia
    if padre_id != "":
        datos_dependencia["dependencia_padre_id"] = padre_id

    resultado = crea_registro(datos_dependencia, trd_id)
    logs.log_trd("agn_trd", trd_id, "CREACIÓN DE DEPENDENCIA - " + datos["datos"]["nombre"], "CREACION", id_tarea) 
    resultado["accion"] = accion    

    return resultado

def modificar_dependencia(accion, datos={}, archivo=[], id_tarea=""):
    dependencia_id = datos["datos"]["id"]
    trd_id         = datos["trd_id"]  
    datos_dependencia = crea_datos(datos["datos"], trd_id)
    resultado = sqalchemy_modificar.modificar_un_registro("agn_dependencia_trd", dependencia_id, datos_dependencia)
    indexar("agn_dependencia_trd", resultado["id"], trd_id)
    logs.log_trd("agn_trd", trd_id, "MODIFICACIÓN DE DEPENDENCIA - " + datos["datos"]["nombre"], "MODIFICACION", id_tarea) 
    resultado["accion"] = accion    

    return resultado

def salvar_dependencia(accion, datos={}, archivo=[], id_tarea=""):
    dependencia_id = datos["datos"].get("id", "")
    if dependencia_id == "":
        resultado = crear_dependencia(accion, datos, archivo, id_tarea)            
    else:
        resultado = modificar_dependencia(accion, datos, archivo, id_tarea)
    
    return resultado

def borrar_dependencia(accion, datos={}, archivo=[], id_tarea=""):
    id     = datos["datos"]["id"]
    trd_id = datos["trd_id"]  
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_dependencia_trd", id)
    indexar("agn_dependencia_trd", resultado["id"], trd_id)
    logs.log_trd("agn_trd", trd_id, "BORRADO DE DEPENDENCIA - " + datos["datos"]["nombre"], "BORRADO", id_tarea) 
    resultado["accion"] = accion
    
    return resultado