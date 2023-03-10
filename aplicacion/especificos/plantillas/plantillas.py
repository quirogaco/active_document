#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

from librerias.datos.sql import (
    sqalchemy_modificar, 
    sqalchemy_insertar, 
    sqalchemy_borrar
)
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes      import indexar_datos
from aplicacion.comunes      import manejo_archivos

# PLANTILLA
def crear_plantilla(accion, datos={}, archivos=[], id_tarea=""):
    print("crear_plantilla:", archivos)
    pprint.pprint(datos["datos"])
    datos_plantilla = {
        "descripcion": datos["datos"]["descripcion"],
        "dependencia_id": datos["datos"].get("dependencia_id", None),
        "datos": {
            "tipo_plantilla": datos["datos"].get("tipo_plantilla", ""),
            "territoriales_id": datos["datos"].get("territoriales_id", []),
            "dependencias_id": datos["datos"].get("dependencias_id", [])
        } 
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura(
        "plantillas", 
        datos_plantilla
    )
    print("crear_plantilla-0")
    manejo_archivos.manejo(
        "plantillas", 
        "insertar", 
        {"id": resultado["id"]}, 
        archivos, 
        id_tarea, 
        "anexos", 
        "plantillas"
    )
    print("crear_plantilla-1")
    indexar_datos.indexar_estructura("plantillas", resultado["id"])
    indexar_datos.indexar_estructura("plantillas", resultado["id"], 120)
    resultado["accion"] = accion    
    print("crear_plantilla-2")
    return resultado

def modificar_plantilla(accion, datos={}, archivos=[], id_tarea=""):
    plantilla_id = datos["datos"]["id"]
    datos_plantilla = {
        "descripcion": datos["datos"]["descripcion"],
        "dependencia_id": datos["datos"].get("dependencia_id", None),
        "datos": {
            "tipo_plantilla": datos["datos"].get("tipo_plantilla", ""),
            "territoriales_id": datos["datos"].get("territoriales_id", []),
            "dependencias_id": datos["datos"].get("dependencias_id", [])
        } 
    }
    resultado = sqalchemy_modificar.modificar_un_registro(
        "plantillas", 
        plantilla_id, 
        datos_plantilla
    )
    indexar_datos.indexar_estructura("plantillas", resultado["id"])
    indexar_datos.indexar_estructura("plantillas", resultado["id"], 120)
    resultado["accion"] = accion    
    
    return resultado

def borrar_plantilla(accion, datos={}, archivos=[], id_tarea=""):
    plantilla_id = datos["datos"]["id"]
    resultado = sqalchemy_borrar.borrar_un_registro("plantillas", plantilla_id)
    # ARCHIVO WORD !!JCR, se pierde la conexion, pero el registro en SQL, 
    # y el archivo MINIO se mantiene
    # manejo_archivos.manejo("plantillas", "eliminar", {"id":resultado["id"]}, archivos, id_tarea, "anexos", "plantillas")
    elastic_operaciones.eliminar_registro("plantillas", plantilla_id)
    resultado["accion"] = accion
    
    return resultado