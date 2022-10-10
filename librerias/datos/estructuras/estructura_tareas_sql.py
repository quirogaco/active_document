#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import typing,pprint
from prefect import task
from prefect.triggers import all_successful

from . import estructura_operaciones_sql, estructura_operaciones
from librerias.datos.base import globales 
from librerias.datos.sql  import sqalchemy_operaciones 

##############
# TAREAS SQL #
##############
# Insertar registro SQL
@task(name="estructura insertar registro SQL", trigger=all_successful)
def insertar_registro_SQL(flujo_data):    
    # Parametros
    estructura = flujo_data["parametros"]["estructura"]
    datos      = flujo_data["parametros"]["datos"]
    ruta       = flujo_data["parametros"]["ruta"]
    id_tarea   = flujo_data["parametros"]["id_tarea"]

    #############
    # Funciones #
    #############
    definicion = globales.lee_definicion(estructura)
    CLASE      = globales.lee_clase(definicion["clase"])
    datos      = estructura_operaciones.preprocesa_estructura_datos(estructura, "insertar", datos, id_tarea)
    registro   = sqalchemy_operaciones.insertar_registro(ruta, CLASE, datos, "diccionario")
    registro   = estructura_operaciones.postprocesa_estructura_datos(estructura, "insertar", registro, id_tarea)
    
    # Que pasa con errores ???
    flujo_data["resultados"]["datos"] = registro

    return flujo_data

# Mofidicar registro SQL
@task(name="estructura modificar registro SQL", trigger=all_successful)
def modificar_registro_SQL(flujo_data):   
    # Parametros
    estructura = flujo_data["parametros"]["estructura"]
    datos      = flujo_data["parametros"]["datos"]
    ruta       = flujo_data["parametros"]["ruta"]
    id_tarea   = flujo_data["parametros"]["id_tarea"]

    #############
    # Funciones #
    #############
    definicion = globales.lee_definicion(estructura)
    CLASE      = globales.lee_clase(definicion["clase"])
    datos      = estructura_operaciones.preprocesa_estructura_datos(estructura, "modificar", datos, id_tarea)
    registro   = sqalchemy_operaciones.modificar_registro(ruta, CLASE, datos, "diccionario")
    registro   = estructura_operaciones.postprocesa_estructura_datos(estructura, "modificar", registro, id_tarea)
    
    # Que pasa con errores ???
    flujo_data["resultados"]["datos"] = registro

    return flujo_data

# Eliminar registro SQL
@task(name="estructura eliminar registro SQL", trigger=all_successful)
def eliminar_registro_SQL(flujo_data):    
    # Parametros
    estructura = flujo_data["parametros"]["estructura"]
    datos      = flujo_data["parametros"]["datos"]
    ruta       = flujo_data["parametros"]["ruta"]
    id_tarea   = flujo_data["parametros"]["id_tarea"]

    #############
    # Funciones #
    #############
    definicion = globales.lee_definicion(estructura)
    CLASE      = globales.lee_clase(definicion["clase"])
    datos      = estructura_operaciones.preprocesa_estructura_datos(estructura, "eliminar", datos, id_tarea)
    registro   = sqalchemy_operaciones.eliminar_registro(ruta, CLASE, datos, "diccionario")
    registro   = estructura_operaciones.postprocesa_estructura_datos(estructura, "eliminar", registro, id_tarea)
    
    # Que pasa con errores ???
    flujo_data["resultados"]["datos"] = registro

    return flujo_data

##################
# TAREAS ELASTIC #
##################
# Indexar registro SQL
@task(name="estructura indexar registro SQL", trigger=all_successful)
def indexar_registro_SQL(flujo_data):    
    # Parametros
    estructura = flujo_data["parametros"]["estructura"]
    ruta       = flujo_data["parametros"]["ruta"]
    registroId = flujo_data["parametros"]["datos"]["registroId"]
    flush      = flujo_data["parametros"]["datos"].get("flush", True)
    id_tarea   = flujo_data["parametros"]["id_tarea"]

    #############
    # Funciones #
    #############
    resultado = estructura_operaciones_sql.indexar_registro_SQL(ruta, estructura, registroId, flush, id_tarea)

    # Errores
    sale    = {
        "datos"  : None,
        "errores": None
    }
    if type(resultado) == str:
        sale["errores"] = resultado
    else:
        sale["datos"] = resultado
    flujo_data["resultados"] = sale

    if sale["errores"] != None:
        raise ValueError(sale["errores"])    
    
    return flujo_data

# Indexar eliminar registro SQL
@task(name="estructura indexar elimina registro SQL", trigger=all_successful)
def indexar_elimina_registro_SQL(flujo_data):    
    # Parametros
    estructura = flujo_data["parametros"]["estructura"]
    ruta       = flujo_data["parametros"]["ruta"]
    registroId = flujo_data["parametros"]["datos"]["registroId"]
    flush      = flujo_data["parametros"]["datos"].get("flush", True)
    id_tarea   = flujo_data["parametros"]["id_tarea"]

    #############
    # Funciones #
    #############
    resultado = estructura_operaciones_sql.indexar_elimina_registro_SQL(ruta, estructura, registroId, flush, id_tarea)  

    # Errores
    sale    = {
        "datos"  : None,
        "errores": None
    }
    if type(resultado) == str:
        sale["errores"] = resultado
    else:
        sale["datos"] = resultado
    flujo_data["resultados"] = sale

    if sale["errores"] != None:
        raise ValueError(sale["errores"])    
    
    return flujo_data

# Indexar leer registro SQL
@task(name="estructura leer registro SQL", trigger=all_successful)
def indexar_leer_registro_SQL(flujo_data):    
    # Parametros
    estructura = flujo_data["parametros"]["estructura"]
    ruta       = flujo_data["parametros"]["ruta"]
    registroId = flujo_data["parametros"]["datos"]["id"]
    id_tarea   = flujo_data["parametros"]["id_tarea"]

    #############
    # Funciones #
    #############
    resultado = estructura_operaciones_sql.indexar_leer_registro_SQL(ruta, estructura, registroId, id_tarea)   

    # Errores
    sale    = {
        "datos"  : None,
        "errores": None
    }
    if type(resultado) == str:
        sale["errores"] = resultado
    else:
        sale["datos"] = resultado
    flujo_data["resultados"] = sale

    if sale["errores"] != None:
        raise ValueError(sale["errores"])    
    
    return flujo_data