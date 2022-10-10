#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random  

from .tramites import acciones_tramites

acciones_funcion = {  
    """  
    # CONFIGURACION GENERAL
    "leer_radicacion_canales"  : configuracion_general.leer_radicacion_canales,
    "salvar_radicacion_canales": configuracion_general.salvar_radicacion_canales,    

    # PLANTILLA
    "crear_plantilla"    : plantillas.crear_plantilla,
    "modificar_plantilla": plantillas.modificar_plantilla,
    "borrar_plantilla"   : plantillas.borrar_plantilla
    """
}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]

    print("")
    print("")
    print("------------------------------------------------")
    print('/ESPECIFICOS TRAMITE -> acciones_ejecuta:', id_tarea) 
    print('datos:')
    pprint.pprint(datos)   
    print('archivos:', archivos)
    print("id tarea-AA", id_tarea)
    
    resultado  = {}
    #funcion   = acciones_funcion[accion]
    #resultado = funcion(accion, datos, archivos, id_tarea)
    print("------------------------------------------------")
    print("")
    print("")

    return resultado