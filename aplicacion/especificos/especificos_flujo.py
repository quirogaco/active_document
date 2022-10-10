#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random  

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes      import indexar_datos

def carga_datos(datos, modo=""):
    datos_flujo = {
        "nombre"            : datos["datos"]["nombre"],
        "detalle"           : datos["datos"].get("detalle", ""), 
        "total_tiempo"      : datos["datos"].get("total_tiempo", 0), 
        "alertar_tiempo"    : datos["datos"].get("alertar_tiempo", ""), 
        "alertar_porcentaje": datos["datos"].get("alertar_porcentaje", ""), 
        "horas_dias"        : datos["datos"].get("horas_dias", "DIAS"), 
        "tipo_tiempo"       : datos["datos"].get("tipo_tiempo", "HABILES"), 
        "formulario_id"     : datos["datos"].get("formulario_id", ""), 
        "flujo"             : datos["datos"].get("flujo", {})
    }

    return datos_flujo

def crear_flujo(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    datos_flujo = carga_datos(datos, "crear")
    resultado   = sqalchemy_insertar.insertar_registro_estructura("tramites", datos_flujo)
    indexar_datos.indexar_estructura("tramites", resultado["id"])      

    return resultado

def modificar_flujo(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    flujo_id    = datos["datos"]["id"]
    datos_flujo = carga_datos(datos, "modificar")
    resultado   = sqalchemy_modificar.modificar_un_registro("tramites", flujo_id, datos_flujo)    
    indexar_datos.indexar_estructura("tramites", resultado["id"])
    
    return resultado

def borrar_flujo(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    flujo_id  = datos["datos"]["id"]
    resultado = sqalchemy_borrar.borrar_un_registro("tramites", flujo_id)
    elastic_operaciones.eliminar_registro("tramites", flujo_id)
    
    return resultado

acciones_funcion = {  
    "crear"    : crear_flujo,
    "modificar": modificar_flujo,
    "borrar"   : borrar_flujo
}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]
    funcion   = acciones_funcion[accion]
    resultado = funcion(accion, datos, archivos, id_tarea)
    resultado["accion"] = accion  
    
    return resultado