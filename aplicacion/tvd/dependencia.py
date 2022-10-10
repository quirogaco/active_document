#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from datetime import datetime

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones
from .indexar_datos          import indexar

def crear_dependencia(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    padre_id   = datos["datos"]["padre_id"] 
    tvd_id     = datos["tvd_id"]  
    datos_dependencia = {
        "tabla" : "TVD", 
        "codigo": datos["datos"]["codigo"], 
        "nombre": datos["datos"]["nombre"],
        "trd_id": tvd_id 
    }
    # Hija de otra dependencia
    if padre_id != "":
        datos_dependencia["dependencia_padre_id"] = padre_id

    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_dependencia_trd", datos_dependencia)
    indexar("agn_dependencia_trd", resultado["id"], tvd_id)
    elastic_operaciones.indexar_registro("agn_tvd", tvd_id)
    resultado["accion"] = accion    

    return resultado

def modificar_dependencia(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["datos"]["id"]
    tvd_id         = datos["tvd_id"]  
    datos_dependencia = {
        "codigo": datos["datos"]["codigo"], 
        "nombre": datos["datos"]["nombre"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_dependencia_trd", dependencia_id, datos_dependencia)
    indexar("agn_dependencia_trd", resultado["id"], tvd_id)
    elastic_operaciones.indexar_registro("agn_tvd", tvd_id)
    resultado["accion"] = accion    

    return resultado

def salvar_dependencia(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["datos"].get("id", "")
    if dependencia_id == "":
        resultado = crear_dependencia(accion, datos, archivo, acciones, id_tarea)
    else:
        resultado = modificar_dependencia(accion, datos, archivo, acciones, id_tarea)
    
    return resultado

def borrar_dependencia(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    id     = datos["datos"]["id"]
    tvd_id = datos["tvd_id"]  
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_dependencia_trd", id)
    indexar("agn_dependencia_trd", resultado["id"], tvd_id)
    elastic_operaciones.indexar_registro("agn_tvd", tvd_id)
    
    resultado["accion"] = accion
    
    return resultado