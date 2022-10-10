#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random 

from librerias.datos.sql         import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic     import elastic_operaciones
from librerias.flujos            import flujos_insertar_sql
from librerias.utilidades        import basicas  
from librerias.datos.estructuras import estructura_operaciones

from aplicacion.especificos.trd_tvd.permisos_archivo import permisos

acciones_funcion = {    
    # CONFIGURACION PERMISOS
    "crear_permisos"   : permisos.crear_permisos,    
    "modifica_permisos": permisos.modificar_permisos,
}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]

    print("")
    print("")
    print("------------------------------------------------")
    print('/ESPECIFICOS ARCHIVO --> acciones_ejecuta:', id_tarea) 
    print('datos:')
    pprint.pprint(datos)   
    print('archivos:', archivos)
    
    resultado = datos
    funcion   = acciones_funcion[accion]
    resultado = funcion(accion, datos, archivos, id_tarea)
    print("------------------------------------------------")
    print("")
    print("")

    retorna = datos
    retorna["datos"] = resultado

    return retorna