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
    print("FUENETS:")
    pprint.pprint(fuentes)
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