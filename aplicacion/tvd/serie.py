#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones
from .indexar_datos          import indexar

def crear_serie(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    tvd_id  = datos["tvd_id"]  
    datos_serie = {
        "tabla"               : "TVD", 
        "codigo"              : datos["datos"]["codigo"], 
        "nombre"              : datos["datos"]["nombre"],
        "central"             : datos["datos"]["central"],
        "eliminacion"         : datos["datos"]["eliminacion"],
        "seleccion"           : datos["datos"]["seleccion"],
        "conservacion"        : datos["datos"]["conservacion"],
        "micro_digitalizacion": datos["datos"]["micro_digitalizacion"],
        "dependencia_id"      : datos["padre_id"] 
    }    
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_serie_trd", datos_serie)
    indexar("agn_serie_trd", resultado["id"], tvd_id)
    elastic_operaciones.indexar_registro("agn_tvd", tvd_id)
    resultado["accion"] = accion    

    return resultado

def modificar_serie(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    id      = datos["datos"]["id"]
    tvd_id  = datos["tvd_id"]  
    datos_serie = {
        "codigo"              : datos["datos"]["codigo"], 
        "nombre"              : datos["datos"]["nombre"],
        "central"             : datos["datos"]["central"],
        "eliminacion"         : datos["datos"]["eliminacion"],
        "seleccion"           : datos["datos"]["seleccion"],
        "conservacion"        : datos["datos"]["conservacion"],
        "micro_digitalizacion": datos["datos"]["micro_digitalizacion"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_serie_trd", id, datos_serie)
    indexar("agn_serie_trd", resultado["id"], tvd_id)
    elastic_operaciones.indexar_registro("agn_tvd", tvd_id)
    resultado["accion"] = accion    

    return resultado

def salvar_serie(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["datos"].get("id", "")
    if dependencia_id == "":
        resultado = crear_serie(accion, datos, archivo, acciones, id_tarea)
    else:
        resultado = modificar_serie(accion, datos, archivo, acciones, id_tarea)
    
    return resultado

def borrar_serie(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    id         = datos["datos"]["id"]
    tvd_id     = datos["tvd_id"]  
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_serie_trd", id)
    indexar("agn_serie_trd", resultado["id"], tvd_id)
    elastic_operaciones.indexar_registro("agn_tvd", tvd_id)
    resultado["accion"] = accion
    
    return resultado