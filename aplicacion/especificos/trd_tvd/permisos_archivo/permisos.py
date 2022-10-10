#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes      import indexar_datos

def crear_permisos(accion, datos={}, archivos=[], id_tarea=""):
    pprint.pprint(datos)
    datos = {
        "descripcion": datos["datos"]["descripcion"],
        "datos" : {
            "usuarios"     : datos["datos"].get("usuarios", []),
            "grupos"       : datos["datos"].get("grupos", []),
            "territoriales": datos["datos"].get("territoriales", []),
            "dependencias" : datos["datos"].get("dependencias", []),
            "series"       : datos["datos"].get("series", []),
            "subseries"    : datos["datos"].get("subseries", [])
        } 
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("permisos_archivo", datos)
    indexar_datos.indexar_estructura("permisos_archivo", resultado["id"])
    resultado["accion"] = accion    
    
    return resultado

def modificar_permisos(accion, datos={}, archivos=[], id_tarea=""):
    permiso_id = datos["datos"]["id"]
    datos = {
        "descripcion": datos["datos"]["descripcion"],
        "datos" : {
            "usuarios"     : datos["datos"].get("usuarios", []),
            "grupos"       : datos["datos"].get("grupos", []),
            "territoriales": datos["datos"].get("territoriales", []),
            "dependencias" : datos["datos"].get("dependencias", []),
            "series"       : datos["datos"].get("series", []),
            "subseries"    : datos["datos"].get("subseries", [])
        } 
    }
    resultado = sqalchemy_modificar.modificar_un_registro("permisos_archivo", permiso_id, datos)    
    indexar_datos.indexar_estructura("permisos_archivo", resultado["id"])
    resultado["accion"] = accion    
    
    return resultado

def borrar_permisos(accion, datos={}, archivos=[], id_tarea=""):
    permiso_id= datos["datos"]["id"]
    resultado = sqalchemy_borrar.borrar_un_registro("permisos_archivo", permiso_id)
    elastic_operaciones.eliminar_registro("permisos_archivo", permiso_id)
    resultado["accion"] = accion
    
    return resultado