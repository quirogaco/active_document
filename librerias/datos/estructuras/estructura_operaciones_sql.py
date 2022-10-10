#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from . import estructura_operaciones
from librerias.datos.base    import globales 
from librerias.datos.sql     import sqalchemy_leer
from librerias.datos.elastic import elastic_operaciones 

#############################
# OPERACIONES DE INDEXACION #
#############################

# INDEXAR REGISTRO
def indexar_registro_SQL(ruta, estructura, registroId, flush=True, id_tarea=""):
    definicion = globales.lee_definicion(estructura)
    CLASE      = globales.lee_clase(definicion["clase"])
    modelo     = globales.lee_modelo_elastic(estructura)
    campoId    = modelo["campoId"]    

    # Lee registro extendido
    datos      = sqalchemy_leer.leer_registroId(ruta, estructura, definicion, CLASE, registroId, campoId, True)
    # Normaliza sin modificar datos orignales, ya sale normalizado de leer_registroId, exendido                                            
    datos      = estructura_operaciones.normaliza_estructura_datos(estructura, datos, False) 
    datos      = elastic_operaciones.indexar_documento(ruta, estructura, datos, flush) 
    
    return datos

# INDEXAR ELIMINA REGISTRO
def indexar_elimina_registro_SQL(ruta, estructura, registroId, flush=True, id_tarea=None):    
    datos = elastic_operaciones.indexar_elimina_documento(ruta, estructura, registroId, flush)

    return datos

# INDEXAR LEE REGISTRO
def indexar_leer_registro_SQL(ruta, estructura, registroId, id_tarea=""):  
    datos = elastic_operaciones.indexar_leer_documento(ruta, estructura, registroId)
    
    return datos["_source"]