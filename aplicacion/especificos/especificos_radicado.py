#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, datetime, random 

from librerias.datos.sql import (
    sqalchemy_modificar, 
    sqalchemy_leer, 
    sqalchemy_insertar, 
    sqalchemy_borrar
)
from librerias.datos.elastic import elastic_operaciones
from librerias.flujos import flujos_insertar_sql
from librerias.utilidades import basicas  
from librerias.datos.estructuras import estructura_operaciones

from .radicados.entradas import entradas
from .radicados.internos import internos
from .radicados.salidas import salidas
from .radicados.gestion import gestion

acciones_funcion = {    
    # INTERNOS
    "radicar_interno": internos.radicar,

    # SALIDAS
    "radicar_salida": salidas.radicar,

    # FORMULARIOS WEB
    "radicar_entrada": entradas.radicar,

    # ENTRADAS
    "radicar_ventanilla": entradas.radicar_ventanilla,

    # PQRS
    "radicar_pqrs": entradas.radicar_peticion,

    # GESTIÓN
    "asigna_pqrs": gestion.asigna_pqrs,
    "asigna_ventanilla": gestion.asigna_ventanilla
}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]

    #"""
    # print("")
    # print("")
    # print("------------------------------------------------")
    # print('/ESPECIFICOS RADICADOS -> acciones_ejecuta:', id_tarea) 
    # print('datos:')
    # pprint.pprint(datos)   
    # print('archivos:', archivos)
    #"""

    resultado = datos
    funcion   = acciones_funcion[accion]
    resultado = funcion(accion, datos, archivos, id_tarea)
    #print("------------------------------------------------")
    #print("")
    #print("")

    retorna = datos
    retorna["datos"] = resultado

    return retorna