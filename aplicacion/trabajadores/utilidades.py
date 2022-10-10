#!/usr/bin/env python3
# -*- coding: ISO-8859-15 -*-  

def parametros(cola, parametros={}, opciones={}, retardo=0):
    retardo_segundo = 0
    if retardo > 0:
        retardo_segundo = retardo

    datos = {
        'kwargs'    : parametros,
        'retry'     : True,
        'serializer': 'json',
        'timeout'   : 360,
        'queue'     : cola,
        'countdown' : retardo_segundo
    }

    return datos

def llamar_celery(funcion, cola, parametros_llamado={}, retardo=0):   
    funcion.apply_async(**parametros(
        cola, 
        parametros = parametros_llamado,     
        retardo    = retardo
    ))