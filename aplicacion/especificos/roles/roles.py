#!/usr/bin/python
# -*- coding: utf-8 -*-

from librerias.datos.sql import (
    sqalchemy_modificar, 
    sqalchemy_insertar, 
    sqalchemy_borrar
)
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes import indexar_datos
from aplicacion.comunes import manejo_archivos

# ROLES
def crear_role(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    datos_role = {
        "nombre": datos["datos"]["nombre"],
        "datos": {
            "opciones": datos["datos"].get("opciones_id", [])
        } 
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura(
        "roles", 
        datos_role
    )
    indexar_datos.indexar_estructura("roles", resultado["id"])
    resultado["accion"] = accion    

    return resultado

def modificar_role(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    role_id = datos["datos"]["id"]
    datos_role = {
        "nombre": datos["datos"]["nombre"],
        "datos": {
            "opciones": datos["datos"].get("opciones_id", [])
        }    
    }
    resultado = sqalchemy_modificar.modificar_un_registro(
        "roles", 
        role_id, 
        datos_role
    )    
    indexar_datos.indexar_estructura("roles", resultado["id"])
    resultado["accion"] = accion    
    
    return resultado

def borrar_role(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    role_id = datos["datos"]["id"]
    resultado = sqalchemy_borrar.borrar_un_registro("roles", role_id)
    elastic_operaciones.eliminar_registro("roles", role_id)
    resultado["accion"] = accion
    
    return resultado