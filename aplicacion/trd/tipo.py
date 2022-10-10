#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint
from librerias.datos.sql  import sqalchemy_leer, sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from .indexar_datos       import indexar
from . import logs


def crea_registro(datos_tipo, trd_id):
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_tipo_documental_trd", datos_tipo)
    indexar("agn_tipo_documental_trd", resultado["id"], trd_id)

    return resultado

# TIPO
def crear_tipo(accion, datos={}, archivo=[], id_tarea=""):
    print("crear_tipo:", datos)
    padre_id   = datos["padre_id"] 
    padre_tipo = datos["padre_tipo"] 
    trd_id     = datos["trd_id"]  
    datos_tipo = {
        "tabla"      : "TRD", 
        "nombre"     : datos["datos"]["nombre"],
        "papel"      : datos["datos"]["papel"],
        "electronico": datos["datos"]["electronico"],
        "indice": datos["datos"].get("indice", 0)
    }

    if (padre_tipo == "serie"):
        datos_tipo["serie_id"]    = padre_id
        datos_tipo["subserie_id"] = None
    else:        
        subserie                  = sqalchemy_leer.leer_un_registro("agn_subserie_trd", padre_id)
        datos_tipo["serie_id"]    = subserie["serie_id"]
        datos_tipo["subserie_id"] = padre_id

    resultado = crea_registro(datos_tipo, trd_id)
    logs.log_trd("agn_trd", trd_id, "CREACIÓN DE TIPO - " + datos["datos"]["nombre"], "CREACION", id_tarea) 
    resultado["accion"] = accion    

    return resultado

def modificar_tipo(accion, datos={}, archivo=[], id_tarea=""):
    id      = datos["datos"]["id"]
    trd_id  = datos["trd_id"]  
    datos_tipo = {
        "nombre"     : datos["datos"]["nombre"],
        "papel"      : datos["datos"]["papel"],
        "electronico": datos["datos"]["electronico"],
        "indice": datos["datos"].get("indice", 0)
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_tipo_documental_trd", id, datos_tipo)
    indexar("agn_tipo_documental_trd", resultado["id"], trd_id)
    logs.log_trd("agn_trd", trd_id, "MODIFICACIÓN DE TIPO - " + datos["datos"]["nombre"], "CREACION", id_tarea) 
    resultado["accion"] = accion    

    return resultado

def salvar_tipo(accion, datos={}, archivo=[], id_tarea=""):
    dependencia_id = datos["datos"].get("id", "")
    if dependencia_id == "":
        resultado = crear_tipo(accion, datos, archivo, id_tarea)
    else:
        resultado = modificar_tipo(accion, datos, archivo, id_tarea)
    
    return resultado

def borrar_tipo(accion, datos={}, archivo=[], id_tarea=""):
    id         = datos["datos"]["id"]
    trd_id     = datos["trd_id"]  
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_tipo_documental_trd", id)
    indexar("agn_tipo_documental_trd", resultado["id"], trd_id)
    logs.log_trd("agn_trd", trd_id, "BORRADO DE TIPO - " + datos["datos"]["nombre"], "CREACION", id_tarea) 
    resultado["accion"] = accion
    
    return resultado