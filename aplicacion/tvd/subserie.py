#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones
from .indexar_datos          import indexar

def crear_subserie(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    tvd_id = datos["tvd_id"]  
    datos_subserie = {
        "tabla"               : "TVD", 
        "codigo"              : datos["datos"]["codigo"], 
        "nombre"              : datos["datos"]["nombre"],
        "central"             : datos["datos"]["central"],
        "eliminacion"         : datos["datos"]["eliminacion"],
        "seleccion"           : datos["datos"]["seleccion"],
        "conservacion"        : datos["datos"]["conservacion"],
        "micro_digitalizacion": datos["datos"]["micro_digitalizacion"],
        "serie_id"            : datos["padre_id"] 
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_subserie_trd", datos_subserie)
    indexar("agn_subserie_trd", resultado["id"], tvd_id)
    elastic_operaciones.indexar_registro("agn_tvd", tvd_id)
    resultado["accion"] = accion    

    return resultado

def modificar_subserie(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    id     = datos["datos"]["id"]
    tvd_id = datos["tvd_id"]   
    datos_subserie = {
        "codigo"              : datos["datos"]["codigo"], 
        "nombre"              : datos["datos"]["nombre"],
        "central"             : datos["datos"]["central"],
        "eliminacion"         : datos["datos"]["eliminacion"],
        "seleccion"           : datos["datos"]["seleccion"],
        "conservacion"        : datos["datos"]["conservacion"],
        "micro_digitalizacion": datos["datos"]["micro_digitalizacion"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_subserie_trd", id, datos_subserie)
    indexar("agn_subserie_trd", resultado["id"], tvd_id)
    elastic_operaciones.indexar_registro("agn_tvd", tvd_id)
    resultado["accion"] = accion    

    return resultado

def salvar_subserie(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["datos"].get("id", "")
    if dependencia_id == "":
        resultado = crear_subserie(accion, datos, archivo, acciones, id_tarea)
    else:
        resultado = modificar_subserie(accion, datos, archivo, acciones, id_tarea)
    
    return resultado

def borrar_subserie(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    id         = datos["datos"]["id"]
    tvd_id     = datos["tvd_id"]  
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_subserie_trd", id)
    indexar("agn_subserie_trd", resultado["id"], tvd_id)
    elastic_operaciones.indexar_registro("agn_tvd", tvd_id)
    resultado["accion"] = accion
    
    return resultado