#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes      import indexar_datos
from aplicacion.comunes      import manejo_archivos

def leer_fuentes(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    fuentes = []
    for indice, valor in CONFIGURACION_GENERAL["DEFINICIONES_SQL"].items():        
        if valor.get("reporte", "NO") == "SI":
            dato = {
                "id"        : indice,
                "estructura": valor["estructura"],
                "nombre"    : valor["descripcion"]
            }
            fuentes.append(dato)

    fuentes = sorted(fuentes, key = lambda item: item['nombre'])

    resultado = {
        "datos": fuentes
    }
    
    return resultado

def leer_campos_fuente(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    fuente        = datos["datos"]["fuente"]
    campos_fuente = []
    for indice, valor in CONFIGURACION_GENERAL["DEFINICIONES_SQL"][fuente]["campos"].items():
        if valor.get("reporte", "NO") == "SI": # JCR "NO", POR DEFAULT
            dato = {
                "id"    : indice,
                "nombre": valor["titulo"],
                "datos" : valor
            }
            campos_fuente.append(dato)   

    campos_fuente = sorted(campos_fuente, key = lambda item: item['nombre'])     

    resultado = {
        "datos": campos_fuente
    }
    
    return resultado

# ROLES
def crear_reporte(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    fuentes  = datos["datos"]["fuentes"]
    columnas = datos["datos"]["columnas_reporte"]
    diseno        = {
        "fuente"  : fuentes,
        "columnas": columnas
    }
    datos_reporte = {
        "codigo": datos["datos"]["codigo"],        
        "nombre": datos["datos"]["nombre"],
        "diseno" : {
            "diseno": diseno
        } 
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("reportes_dinamicos", datos_reporte)
    indexar_datos.indexar_estructura("reportes_dinamicos", resultado["id"])
    resultado["accion"] = accion    

    return resultado

def modificar_reporte(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    reporte_id = datos["datos"]["id"]
    fuentes    = datos["datos"]["fuentes"]
    columnas   = datos["datos"]["columnas_reporte"]
    diseno        = {
        "fuente"  : fuentes,
        "columnas": columnas
    }
    datos_reporte = {
        "codigo": datos["datos"]["codigo"],        
        "nombre": datos["datos"]["nombre"],
        "diseno" : {
            "diseno": diseno
        } 
    }
    pprint.pprint(datos_reporte)
    resultado = sqalchemy_modificar.modificar_un_registro("reportes_dinamicos", reporte_id, datos_reporte)    
    indexar_datos.indexar_estructura("reportes_dinamicos", resultado["id"])
    resultado["accion"] = accion    
    
    return resultado

def borrar_reporte(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    reporte_id = datos["datos"]["id"]
    resultado  = sqalchemy_borrar.borrar_un_registro("reportes_dinamicos", reporte_id)
    elastic_operaciones.eliminar_registro("reportes_dinamicos", reporte_id)
    resultado["accion"] = accion
    
    return resultado