#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from librerias.datos.base import globales 

def cadenaConexion(ruta):
    configuracion = globales.lee_configuracion_sql(ruta)

    sqlnombre = configuracion["sqlnombre"]
    usuario   = configuracion["usuario"]
    clave     = configuracion["clave"]
    direccion = configuracion["direccion"]
    nombre    = configuracion["nombre"]

    conexion = sqlnombre + "://" + usuario + ":" + clave + "@" + direccion # + "/" + nombre

    #print("conexion:", conexion)

    return conexion

def motorSql(cadena_conexion):
    motor = sqlalchemy.create_engine(
        cadena_conexion, 
        #echo=False, 
        #echo= True, 
        #coerce_to_unicode= True,        
        pool_pre_ping=True,
        poolclass=NullPool
    )

    return motor

def conexionSql(ruta):
    cadena_conexion = cadenaConexion(ruta)
    
    return cadena_conexion

def sesionesSql(ruta, motor):
    sesion = sessionmaker(bind=motor, autoflush=False)
        
    return sesion

import pprint

def conectarSql(ruta):
    cadena_conexion = conexionSql(ruta)
    
    # Motor sql
    motor = motorSql(cadena_conexion)
    globales.carga_motor_sql(ruta, motor)
    
    # Sesiones SQL
    sesion = sesionesSql(ruta, motor)
    globales.carga_sesion_sql(ruta, sesion)

    return motor