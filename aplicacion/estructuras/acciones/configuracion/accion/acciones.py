#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

from librerias.datos.base import globales

def pre_procesa(estructura, accion, datos):
    """
    print("")
    print("")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("PRE_PROCESA:", estructura, accion)
    pprint.pprint(datos)    
    """

    return datos

def post_procesa(estructura, accion, datos):
    """
    print("")
    print("")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("POST_PROCESA:", estructura, accion)
    pprint.pprint(datos)   
    """ 
    
    return datos

globales.carga_procesamiento("accion", "pre_estructura",  pre_procesa)
globales.carga_procesamiento("accion", "post_estructura", post_procesa)