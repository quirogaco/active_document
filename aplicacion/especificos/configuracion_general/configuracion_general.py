#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar, sqalchemy_filtrar 
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes      import indexar_datos
from aplicacion.comunes      import manejo_archivos

######################### 
# CONFIGURACIoN GENERAL #
#########################

# LEER REGISTRO DE CONFIGURACIoN
def leer_registro_configuracion(codigo):
    datos = None
    filtros = [ [ "codigo", "=", codigo ] ]
    configuraciones = sqalchemy_filtrar.filtrarOrdena(estructura="configuracion_general", filtros=filtros, ordenamientos=[])
    if len(configuraciones) > 0:
        return configuraciones[0]
    
    return datos

# CREAR REGISTRO DE CONFIGURACIoN
def crear_registro_configuracion(codigo, datos):
    datos_configuracion = {
        "codigo": codigo,
        "datos" : datos["datos"]
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("configuracion_general", datos_configuracion)

    return resultado

# MODIFICAR REGISTRO DE CONFIGURACIoN
def modificar_registro_configuracion(registro_id, datos):
    pprint.pprint(datos)
    datos_configuracion = {
        "datos" : datos["datos"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("configuracion_general", registro_id, datos_configuracion)
    
    return resultado

def salvar_configuracion(codigo, datos={}):
    resultado = leer_registro_configuracion(codigo)
    if resultado != None:
        resultado = modificar_registro_configuracion(resultado["id"], datos)
    else:
        resultado = crear_registro_configuracion(codigo, datos)

    return resultado

#########################
# RADICACIoN PLANTILLAS #
#########################
def leer_radicacion_canales(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    codigo = datos["datos"]["_tipo_"]
    resultado = leer_registro_configuracion(codigo)

    return resultado

def salvar_radicacion_canales(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    datos = datos["datos"]
    codigo = datos["_tipo_"]
    datos_plantilla = {
        "datos": datos
    }    
    resultado = salvar_configuracion(codigo, datos_plantilla)
    
    return resultado