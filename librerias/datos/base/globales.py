#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import builtins, pprint

from librerias.datos.sql import sqalchemy_declarativa_base

# Clase base para operaciones SQL, debe existir para definir tablas
# Carga declarativa genera base CLASE_BASE
CLASE_BASE_SQL = sqalchemy_declarativa_base.crea_base()

# Configuración general
if getattr(builtins, "CONFIGURACION_GENERAL", None) == None:
    builtins.CONFIGURACION_GENERAL = {}

    # Configuración SQL
    CONFIGURACION_GENERAL["SQL"]          = {}
    CONFIGURACION_GENERAL["SQL_MOTORES"]  = {} 
    CONFIGURACION_GENERAL["SQL_SESIONES"] = {} 

    # Relaciones SQL a generar
    CONFIGURACION_GENERAL["RELACIONES_SQL"] = {}   

    # Registro de clases de Bases de datos
    CONFIGURACION_GENERAL["CLASES_SQL"] = {} 

    # Registro de clases de Bases de datos
    CONFIGURACION_GENERAL["DEFINICIONES_SQL"] = {}

    # Registro de validadores de estructuras
    CONFIGURACION_GENERAL["VALIDADORES"] = {}

    # Funciones de procesamiento
    CONFIGURACION_GENERAL["PROCESAMIENTO_ESTRUCTURAS"]      = {} 
    # Configuración ELASTIC
    CONFIGURACION_GENERAL["ELASTIC"]            = {}
    # Modelos de elasticsearch
    CONFIGURACION_GENERAL["ELASTIC_MODELOS"]    = {} 
    # Campos de query en tiempo de ejecución
    CONFIGURACION_GENERAL["ELASTIC_QUERYTIME"]    = {} 
    # Conexiones a elasticsearch
    CONFIGURACION_GENERAL["ELASTIC_CONEXIONES"] = {}
    # Estructuras dinamicas, basadas en estructuras normales, con filtros especificos
    CONFIGURACION_GENERAL["ELASTIC_DINAMICAS"] = {}
    # Estructuras que no estan en elastic, ej: lista o dicionario del sistema
    CONFIGURACION_GENERAL["ESTRUCTURAS_ESPECIALES"] = {}

    # Definiciones
    CONFIGURACION_GENERAL["DEFINICIONES_VISUALES"] = {}

    # Funciones python por tipo de servicio
    CONFIGURACION_GENERAL["FUNCIONES_TAREAS"] = {}

    # Funcion de referencia para leer información asociada al registro
    CONFIGURACION_GENERAL["FUNCIONES_REFERENCIA"] = {}

    # Enviar pdf para visores y descargar
    CONFIGURACION_GENERAL["manejo_pdf"]          = {}

    # Enviar archivos para visores y descargar
    CONFIGURACION_GENERAL["manejo_archivo"]          = {}

    # Definiciones visuales de grid y formas
    CONFIGURACION_GENERAL["definiciones_visuales"]   = {}
    CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]  = {}
    CONFIGURACION_GENERAL["definiciones_visuales"]["forma"] = {}

    # Tareas especificas para registros
    CONFIGURACION_GENERAL["TAREAS_ESPECIFICAS"] = {}

    # Funciones generales a ejecutar
    CONFIGURACION_GENERAL["FUNCIONES_GENERALES"] = {}


from .basicas import *

#####################################################
# DEFINICIONES RUTINA LLAMADAS POR TIPO DE SERVICIO #
#####################################################

def carga_funcion_servicio(estructura="", nombre="", definicion={}):
    if CONFIGURACION_GENERAL["FUNCIONES_SERVICIO"].get(estructura, False) == False:
        CONFIGURACION_GENERAL["FUNCIONES_SERVICIO"][estructura] = {}

    CONFIGURACION_GENERAL["FUNCIONES_SERVICIO"][estructura][nombre] = definicion

def leer_funcion_servicio(estructura="", nombre=""):
    definicion =CONFIGURACION_GENERAL["FUNCIONES_SERVICIO"][estructura][nombre]

    return definicion


##################################################
# DEFINICIONES FUNCIONES PROCESOS POR REFERENCIA #
##################################################

def carga_funcion_referencia(estructura="", nombre="", funcion=None):
    if CONFIGURACION_GENERAL["FUNCIONES_REFERENCIA"].get(estructura, False) == False:
        CONFIGURACION_GENERAL["FUNCIONES_REFERENCIA"][estructura] = {}

    CONFIGURACION_GENERAL["FUNCIONES_REFERENCIA"][estructura][nombre] =  funcion

def lee_funcion_referencia(estructura="", nombre=""):
    funcion = CONFIGURACION_GENERAL["FUNCIONES_REFERENCIA"][estructura][nombre]

    return funcion

#########################
# TAREAS POR ESTRUCTURA #
#########################

def carga_tarea(idtarea="", definicion=None):
    if CONFIGURACION_GENERAL["TAREAS_ESPECIFICAS"].get(idtarea, False) == False:
        CONFIGURACION_GENERAL["TAREAS_ESPECIFICAS"][idtarea] = []

    CONFIGURACION_GENERAL["TAREAS_ESPECIFICAS"][idtarea].append(definicion)

def lee_tarea(idtarea=""):
    tarea = CONFIGURACION_GENERAL["TAREAS_ESPECIFICAS"].get(idtarea, None) 
    
    return tarea

#########################
# LLAMADO DE FUNCIONES #
#########################
def carga_funcion_general(nombre, funcion, atributos={}):
    CONFIGURACION_GENERAL["FUNCIONES_GENERALES"][nombre] = {
        "funcion"  : funcion,
        "atributos": atributos 
    }

def lee_funcion_general(nombre=""):
    atributos = CONFIGURACION_GENERAL["FUNCIONES_GENERALES"].get(nombre, None) 
    
    return atributos