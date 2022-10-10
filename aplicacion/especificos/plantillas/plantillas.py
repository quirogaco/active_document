#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes      import indexar_datos
from aplicacion.comunes      import manejo_archivos

# PLANTILLA
def crear_plantilla(accion, datos={}, archivos=[], id_tarea=""):
    datos_plantilla = {
        "descripcion"   : datos["datos"]["descripcion"],
        "dependencia_id": datos["datos"].get("dependencia_id", None)
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("plantillas", datos_plantilla)
    manejo_archivos.manejo("plantillas", "insertar", {"id":resultado["id"]}, archivos, id_tarea, "anexos", "plantillas")

    indexar_datos.indexar_estructura("plantillas", resultado["id"])
    indexar_datos.indexar_estructura("plantillas", resultado["id"], 30)
    resultado["accion"] = accion    

    return resultado

def modificar_plantilla(accion, datos={}, archivos=[], id_tarea=""):
    plantilla_id    = datos["datos"]["id"]
    datos_plantilla = {
        "descripcion"   : datos["datos"]["descripcion"],
        "dependencia_id": datos["datos"].get("dependencia_id", None)
    }
    resultado = sqalchemy_modificar.modificar_un_registro("plantillas", plantilla_id, datos_plantilla)
    indexar_datos.indexar_estructura("plantillas", resultado["id"])
    indexar_datos.indexar_estructura("plantillas", resultado["id"], 30)
    resultado["accion"] = accion    
    
    return resultado

def borrar_plantilla(accion, datos={}, archivos=[], id_tarea=""):
    plantilla_id = datos["datos"]["id"]
    resultado    = sqalchemy_borrar.borrar_un_registro("plantillas", plantilla_id)
    # ARCHIVO WORD !!JCR, se pierde la conexion, pero el registro en SQL, Y el archivo MINIO se mantiene
    #manejo_archivos.manejo("plantillas", "eliminar", {"id":resultado["id"]}, archivos, id_tarea, "anexos", "plantillas")
    elastic_operaciones.eliminar_registro("plantillas", plantilla_id)
    resultado["accion"] = accion
    
    return resultado