#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from prefect.triggers import all_successful
from prefect import task

from . import valida
from librerias.datos.base import globales 

# Valida datos tarea prefect
@task(name="valida datos", trigger=all_successful)
def valida_datos_tarea(flujo_data):
    # Parametros
    estructura = flujo_data["parametros"]["estructura"]
    datos      = flujo_data["parametros"]["datos"]
    #############
    # Funciones #
    #############
    validador = globales.lee_validador(estructura)
    sale      = valida.valida_datos(datos, validador)    
    # Genera datos y errores
    flujo_data["resultados"] = sale

    # Genera error 
    if sale["errores"] != None:
        mensaje = ""
        for error in sale["errores"]:
            mensaje += " ," + error["campo"] + " -> " + error["mensaje"]
        raise ValueError(mensaje)
    
    return flujo_data