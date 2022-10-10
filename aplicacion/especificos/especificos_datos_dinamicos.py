#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random  

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes      import indexar_datos
from aplicacion.comunes      import manejo_archivos

def carga_datos(datos, modo=""):
    """
    "formulario_id"    
    "versiones"      
    "actuales"      
    "historico"    
    """
    datos_formularios_dinamicos = {
        "formulario_id"    : datos["datos"]["formulario_id"],
        "actuales"         : datos["datos"].get("actuales", {}),         
    }

    return datos_formularios_dinamicos

def crear_formularios_dinamicos(accion, datos={}, archivos=[], id_tarea=""):
    datos_formularios_dinamicos = carga_datos(datos, "crear")
    resultado = sqalchemy_insertar.insertar_registro_estructura("datos_formularios_dinamicos", datos_formularios_dinamicos)
    manejo_archivos.manejo("datos_formularios_dinamicos", "insertar", {"id":resultado["id"]}, archivos, id_tarea, "anexos", "dinamicos")
    indexar_datos.indexar_estructura("datos_formularios_dinamicos", resultado["id"])   

    return resultado

def modificar_formularios_dinamicos(accion, datos={}, archivos=[], id_tarea=""):
    flujo_id    = datos["datos"]["id"]
    datos_formularios_dinamicos = carga_datos(datos, "modificar")
    resultado   = sqalchemy_modificar.modificar_un_registro("datos_formularios_dinamicos", flujo_id, datos_formularios_dinamicos)    
    indexar_datos.indexar_estructura("datos_formularios_dinamicos", resultado["id"])
    
    return resultado

def borrar_formularios_dinamicos(accion, datos={}, archivos=[], id_tarea=""):
    flujo_id  = datos["datos"]["id"]
    resultado = sqalchemy_borrar.borrar_un_registro("datos_formularios_dinamicos", flujo_id)
    elastic_operaciones.eliminar_registro("datos_formularios_dinamicos", flujo_id)
    
    return resultado

acciones_funcion = {  
    "crear"    : crear_formularios_dinamicos,
    "modificar": modificar_formularios_dinamicos,
    "borrar"   : borrar_formularios_dinamicos
}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    print("")
    print("")    
    print("acciones_ejecuta->>>id_tarea:", id_tarea)
    pprint.pprint(datos)
    print(archivos)
    accion = datos["accion"]
    print("")
    print("")
    
    funcion   = acciones_funcion[accion]
    resultado = funcion(accion, datos, archivos, id_tarea)
    resultado["accion"] = accion  
    #resultado = {}
    
    return resultado