#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.sql  import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from .indexar_datos       import indexar_acceso

def crear_acceso(accion, datos={}, archivo=[], acciones={}, id_tarea=""):    
    autorizados = {
        "usuarios": datos["datos"].get("usuarios", []),
        "grupos"  : datos["datos"].get("grupos", [])   
    }
    datos_acceso =  {
        "elemento_tipo": datos["datos"]["padre_tipo"],
        "elemento_id"  : datos["datos"]["padre_id"],
        "autorizacion" : datos["datos"]["autorizacion"],
        "autorizados"  : autorizados
    }
    
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_accesos_tvd", datos_acceso)
    indexar_acceso(datos["datos"]["padre_tipo"], datos["datos"]["padre_id"], resultado["id"])
    resultado["accion"] = accion  
    
    return resultado

def modificar_acceso(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    id     = datos["datos"]["id"]
    tvd_id = datos["tvd_id"]   
    datos_subserie = {
        "codigo"              : datos["datos"]["codigo"], 
        "nombre"              : datos["datos"]["nombre"],
        "gestion"             : datos["datos"]["gestion"],
        "central"             : datos["datos"]["central"],
        "eliminacion"         : datos["datos"]["eliminacion"],
        "seleccion"           : datos["datos"]["seleccion"],
        "conservacion"        : datos["datos"]["conservacion"],
        "micro_digitalizacion": datos["datos"]["micro_digitalizacion"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_subserie_tvd", id, datos_subserie)
    indexar("agn_subserie_tvd", resultado["id"], tvd_id)
    resultado["accion"] = accion    

    return resultado

def salvar_acceso(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["datos"].get("id", "")
    if dependencia_id == "":
        resultado = crear_acceso(accion, datos, archivo, acciones, id_tarea)
    else:
        resultado = modificar_acceso(accion, datos, archivo, acciones, id_tarea)
    
    return resultado

def borrar_acceso(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    id         = datos["datos"]["id"]
    tvd_id     = datos["tvd_id"]  
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_subserie_tvd", id)
    indexar("agn_subserie_tvd", resultado["id"], tvd_id)
    resultado["accion"] = accion
    
    return resultado