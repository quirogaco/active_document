#!/usr/bin/python
# -*- coding: UTF-8 -*-

import builtins, pprint

##############################################################
# SQL INFORMACIóN BASICA DE SQLALCHEMY                       #
# SQL         : Datos de acceso a la base de datos           #
# SQL_MOTORES : Sqlalchemy engines vincula a bases de datos  #
# SQL_SESIONES: Sqlalchemy creador de sesiones por motor     #
##############################################################

# CONFIGURACIóN: Ruta de configuración SQL
def carga_configuracion_sql(ruta="base", datos={}):
    CONFIGURACION_GENERAL["SQL"][ruta] = datos

def lee_configuracion_sql(ruta):
    configuracion = CONFIGURACION_GENERAL["SQL"][ruta]

    return configuracion

# MOTORES: Ruta de motores SQL
def carga_motor_sql(ruta="base", motorSql=None):
    CONFIGURACION_GENERAL["SQL_MOTORES"][ruta] = motorSql

def lee_motor_sql(ruta):
    motorSql = CONFIGURACION_GENERAL["SQL_MOTORES"][ruta]

    return motorSql

# SESIONES: Ruta de sesiones SQL
def carga_sesion_sql(ruta="base", motorSql=None):
    CONFIGURACION_GENERAL["SQL_SESIONES"][ruta] = motorSql

def lee_sesion_sql(ruta):
    sesion = CONFIGURACION_GENERAL["SQL_SESIONES"][ruta]

    return sesion

#################################################################
# SQL DEFINICIONES Y CLASES DE ESTRUCTURAS DE DATOS             #
# CLASES_SQL        : Sqlalchemy clases de tablas               #
# DEFINICIONES_SQL  : Diccionario de definicion de estructuras  #
# VALIDADOR DE DATOS: Validador de datos de la estructura       #
#################################################################

def carga_clase(nombre, CLASE):
    CONFIGURACION_GENERAL["CLASES_SQL"][nombre] = CLASE

def lee_clase(nombre):
    CLASE = CONFIGURACION_GENERAL["CLASES_SQL"][nombre]

    return CLASE

def carga_definicion(nombre, definicion):
    CONFIGURACION_GENERAL["DEFINICIONES_SQL"][nombre] = definicion

def lee_definicion(nombre):
    definicion = CONFIGURACION_GENERAL["DEFINICIONES_SQL"][nombre]

    return definicion

def carga_validador(nombre, validador):
    CONFIGURACION_GENERAL["VALIDADORES"][nombre] = validador

def lee_validador(nombre):
    validador = CONFIGURACION_GENERAL["VALIDADORES"][nombre]

    return validador

################################################## 
# ALMACENA FUNCIONES PARA PROCESAMIENTO DE DATOS #
# ASOCIADOS A ESTRUCTURAS                        #
##################################################

def carga_procesamiento(estructura, nombre, funcion):
    if CONFIGURACION_GENERAL["PROCESAMIENTO_ESTRUCTURAS"].get(estructura, False) == False:
        CONFIGURACION_GENERAL["PROCESAMIENTO_ESTRUCTURAS"][estructura] = {}

    CONFIGURACION_GENERAL["PROCESAMIENTO_ESTRUCTURAS"][estructura][nombre] = funcion

def lee_procesamiento(estructura, nombre):
    funcion = None    

    if CONFIGURACION_GENERAL["PROCESAMIENTO_ESTRUCTURAS"].get(estructura, None) != None:
        funcion = CONFIGURACION_GENERAL["PROCESAMIENTO_ESTRUCTURAS"][estructura].get(nombre, None)

    return funcion

############################################## 
# ALMACENA DEFINICIONES PARA MODELOS ELASTIC #
# ASOCIADOS A ESTRUCTURAS                    #
############################################## 

# CONFIGURACIóN: Ruta de configuración ELASTIC
def carga_configuracion_elastic(ruta="base", datos={}):
    CONFIGURACION_GENERAL["ELASTIC"][ruta] = datos

def lee_configuracion_elastic(ruta):
    configuracion = CONFIGURACION_GENERAL["ELASTIC"][ruta]

    return configuracion

def carga_modelo_elastic(estructura="", modelo={}, mapa={}, indexamiento={}, indice="", campoId=None, querytime={}):
    if CONFIGURACION_GENERAL["ELASTIC_MODELOS"].get(estructura, False) == False:
        CONFIGURACION_GENERAL["ELASTIC_MODELOS"][estructura] = {}
    
    datos = {
        "modelo"      : modelo,
        "mapa"        : mapa,
        "indexamiento": indexamiento,        
        "indice"      : indice,
        "campoId"     : campoId,
        "querytime"   : querytime
    }
    CONFIGURACION_GENERAL["ELASTIC_MODELOS"][estructura] = datos

def lee_modelo_elastic(estructura=""):
    modelo = CONFIGURACION_GENERAL["ELASTIC_MODELOS"][estructura]

    return modelo

def carga_modelo_querytime(estructura="", querytime={}):
    CONFIGURACION_GENERAL["ELASTIC_QUERYTIME"][estructura] = querytime

def lee_modelo_querytime(estructura=""):
    querytime = CONFIGURACION_GENERAL["ELASTIC_QUERYTIME"].get(estructura, {})

    return querytime

def carga_conexion_elastic(ruta, conexion):
    CONFIGURACION_GENERAL["ELASTIC_CONEXIONES"][ruta] = conexion

def lee_conexion_elastic(ruta):
    conexion = CONFIGURACION_GENERAL["ELASTIC_CONEXIONES"][ruta]

    return conexion

def carga_estructura_dinamica(estructura="", funcion=None):
    CONFIGURACION_GENERAL["ELASTIC_DINAMICAS"][estructura] = funcion

def lee_estructura_dinamica(estructura=""):
    funcion = CONFIGURACION_GENERAL["ELASTIC_DINAMICAS"].get(estructura)

    return funcion

def carga_estructura_especial(estructura="", funcion=None):
    CONFIGURACION_GENERAL["ESTRUCTURAS_ESPECIALES"][estructura] = funcion

def lee_estructura_especial(estructura=""):
    funcion = CONFIGURACION_GENERAL["ESTRUCTURAS_ESPECIALES"].get(estructura)

    return funcion

############################################## 
# ALMACENA DEFINICIONES PARA MODELOS MINIO  #
# ASOCIADOS A ESTRUCTURAS                    #
############################################## 

def carga_configuracion_minio(datos={}):
    CONFIGURACION_GENERAL["MINIO"] = datos

def lee_configuracion_minio():
    configuracion = CONFIGURACION_GENERAL["MINIO"]

    return configuracion

def carga_conexion_minio(conexion):
    CONFIGURACION_GENERAL["MINIO_CONEXIONES"] = conexion

def lee_conexion_minio():
    conexion = CONFIGURACION_GENERAL["MINIO_CONEXIONES"]

    return conexion

####################### 
# INFOMACION DE REDIS #
####################### 

def carga_configuracion_redis(datos={}):
    CONFIGURACION_GENERAL["REDIS"] = datos

def lee_configuracion_redis():
    configuracion = CONFIGURACION_GENERAL["REDIS"]

    return configuracion

def carga_conexion_redis(conexion):
    CONFIGURACION_GENERAL["REDIS_CONEXIONES"] = conexion

def lee_conexion_redis():
    conexion = CONFIGURACION_GENERAL["REDIS_CONEXIONES"]

    return conexion

#################################################################
# DEFINICIONES VISUALES PARA COMPONENTES EN NAVEGADOR           #
#################################################################

def carga_definicion_visual(estructura="", nombre="", definicion={}):
    if CONFIGURACION_GENERAL["DEFINICIONES_VISUALES"].get(estructura, False) == False:
        CONFIGURACION_GENERAL["DEFINICIONES_VISUALES"][estructura] = {}

    CONFIGURACION_GENERAL["DEFINICIONES_VISUALES"][estructura][nombre] = definicion

def lee_definicion_visual(estructura="", nombre=""):
    definicion =CONFIGURACION_GENERAL["DEFINICIONES_VISUALES"][estructura][nombre]

    return definicion