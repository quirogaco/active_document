#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, builtins
from librerias.datos.base     import globales
from aplicacion.trabajadores  import utilidades


def llamar_celery(ubicacion, funcion_nombre, funcion, parametros, atributos, retardo=0):
    try:
        resultado = utilidades.llamar_celery(
            funcion, 
            'generales', 
            parametros,
            retardo=retardo
        )
    except Exception as e:
        resultado = None
        error = str(e)
        print("Error secuencia ejecución celery: [ubicacion:" + ubicacion + "] - [Función:" + funcion_nombre + "] " + error)

    return resultado

def llamar_normal(ubicacion, funcion_nombre, funcion, parametros, atributos):
    try:
        resultado   = funcion(**parametros)
    except Exception as e:
        error = str(e)
        print("Error secuencia ejecución: [ubicacion:" + ubicacion + "] - [Función:" + funcion_nombre + "] " + error)

    return resultado

def llamar_funcion(ubicacion, funcion_nombre, funcion, parametros, atributos, tipo="normal", retardo=0):
    error = None
    if tipo == "celery":
        resultado = llamar_celery(ubicacion, funcion_nombre, funcion, parametros, atributos, retardo=retardo)
    else:
        resultado = llamar_normal(ubicacion, funcion_nombre, funcion, parametros, atributos)

    return resultado


def ejecutar_secuencia(secuencia=[], ubicacion="general", tipo="normal", retardo=0):
    # Resultados de la ejecución
    parametros_siguiente_ejecucion = {} 
    resultados                     = []
    for comando in secuencia:        
        funcion_nombre = comando["funcion"]
        definicion     = globales.lee_funcion_general(funcion_nombre)
        if definicion != None:
            funcion     = definicion["funcion"]
            atributos   = definicion.get("atributos", {})       
            tipo        = atributos.get("tipo", "normal")      
            # Mezclar con parametros siguente ejecución
            parametros  = comando.get("parametros", {})         
            
            # Ejecutar función   
            resultado = llamar_funcion(ubicacion, funcion_nombre, funcion, parametros, atributos, tipo, retardo=retardo)
            
            parametros_siguiente_ejecucion = {} # Parameros secuencia
            error = None

            # Falta validar errores de ejecución
            datos       = {
                "funcion"  : funcion_nombre,
                "resultado": resultado,
                "error"    : error
            }
            resultados.append(datos)

    return resultados