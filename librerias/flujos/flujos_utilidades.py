#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from prefect.engine.results import LocalResult

def manejador_de_estado(obj, old_state, new_state):
    #return new_state
    return False

# El flujo fue exitoso
def exitoso(resultado):
    return resultado.is_successful()

# El flujo fue fallido
def fallido(resultado):
    return resultado.is_failed()

import pprint
# Mensaje error flujo
def mensajeError(flujo, resultado):    
    mensaje = {}
    for clave, resultado in resultado.result.items():
        if (resultado.is_failed()==True) and (str(resultado.result.args[0]).find('Trigger was "all_successful"') == -1):
            mensaje = resultado.result.args[0]
    
    return mensaje

# Resultado de tarea
def resultado_flujo(flujo, resultado, tarea_nombre):
    tarea           = flujo.get_tasks(tarea_nombre)[0]
    resultado_tarea = resultado.result[tarea].result
            
    return resultado_tarea

def estadoFlujoTareaNombre(flujo, estado, tarea_nombre):
    resultado = {
        "error": "no",
        "datos": None
    }

    if exitoso(estado):        
        resultado["datos"] = resultado_flujo(flujo, estado, tarea_nombre)
        
    if fallido(estado):
        resultado["error"] = "si"
        resultado["datos"] = mensajeError(flujo, estado)

    return resultado

def estadoFlujo(flujo, flujo_estado, ultimo_resultado,):
    resultado = {
        "error": "no",
        "datos": None
    }

    if exitoso(flujo_estado):        
        resultado["datos"] = flujo_estado.result[ultimo_resultado].result
        
    if fallido(flujo_estado):      
        resultado["error"] = "si"
        resultado["datos"] = mensajeError(flujo, flujo_estado)

    return resultado