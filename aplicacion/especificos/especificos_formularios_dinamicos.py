#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random  

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes      import indexar_datos
from aplicacion.comunes      import manejo_archivos

def carga_datos(datos, modo=""):
    formularios_dinamicos = {
        "codigo": datos["datos"]["codigo"],
        "nombre": datos["datos"].get("nombre"), 
        "diseno": datos["datos"].get("diseno"),          
    }

    return formularios_dinamicos

def crear_formularios_dinamicos(accion, datos={}, archivos=[], id_tarea=""):
    formularios_dinamicos = carga_datos(datos, "crear")
    resultado = sqalchemy_insertar.insertar_registro_estructura("formularios_dinamicos", formularios_dinamicos)
    indexar_datos.indexar_estructura("formularios_dinamicos", resultado["id"])   

    return resultado

def modificar_formularios_dinamicos(accion, datos={}, archivos=[], id_tarea=""):
    flujo_id    = datos["datos"]["id"]
    formularios_dinamicos = carga_datos(datos, "modificar")
    resultado   = sqalchemy_modificar.modificar_un_registro("formularios_dinamicos", flujo_id, formularios_dinamicos)    
    indexar_datos.indexar_estructura("formularios_dinamicos", resultado["id"])
    
    return resultado

def borrar_formularios_dinamicos(accion, datos={}, archivos=[], id_tarea=""):
    flujo_id  = datos["datos"]["id"]
    resultado = sqalchemy_borrar.borrar_un_registro("formularios_dinamicos", flujo_id)
    elastic_operaciones.eliminar_registro("formularios_dinamicos", flujo_id)
    
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