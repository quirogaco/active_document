#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import builtins, pprint
import redis

from librerias.datos.base    import globales 
from librerias.datos.sql     import sqalchemy_conectar
from librerias.datos.elastic import elastic_conectar
from librerias.datos.minio   import minio_conectar
from librerias.datos.redis   import redis_conectar

nsBase = 'ad/base/'

def crearClienteRedis(hosts):
    redisCliente = redis.Redis(host=hosts, port=6379, db=0, decode_responses=True)
    
    return redisCliente

def leerParametro(redisCliente, ruta):
    valor = redisCliente.get(nsBase+ruta)

    return valor

def leer_datos_sql(ipServicios):
    redisCliente = crearClienteRedis(ipServicios)
    datosSql     = {
        "sqlnombre" : leerParametro(redisCliente, "db/sqlname"),
        "direccion" : leerParametro(redisCliente, "db/adrress"),
        "nombre"    : leerParametro(redisCliente, "db/name"),
        "usuario"   : leerParametro(redisCliente, "db/user"),
        "clave"     : leerParametro(redisCliente, "db/password")
    }
    
    return datosSql

def leer_datos_elastic(ipServicios):
    redisCliente = crearClienteRedis(ipServicios)
    datosSql     = {
        "ip"     : leerParametro(redisCliente, "elastic/ip"),
        "port"   : leerParametro(redisCliente, "elastic/port"),
        "timeout": int(leerParametro(redisCliente, "elastic/timeout"))
    }
    
    return datosSql

def leer_datos_minio(ipServicios):
    redisCliente = crearClienteRedis(ipServicios)
    datosSql     = {
        "ip"        : leerParametro(redisCliente, "minio/ip"),
        "port"      : leerParametro(redisCliente, "minio/port"),
        "access_key": leerParametro(redisCliente, "minio/access_key"),
        "secret_key": leerParametro(redisCliente, "minio/secret_key"),
    }
    
    return datosSql

def leer_datos_redis(ipServicios):
    redisCliente = crearClienteRedis(ipServicios)
    datosRedis   = {
        "host": leerParametro(redisCliente, "redis/host"),
        "port": leerParametro(redisCliente, "redis/port"),
    }
    
    return datosRedis

def configuracion_general(ruta="base"):
    # Conexion SQL
    datosSql = leer_datos_sql(builtins._appServicios)
    globales.carga_configuracion_sql(ruta, datosSql)
    sqalchemy_conectar.conectarSql(ruta)

    # Conexion ELASTIC
    datosElastic = leer_datos_elastic(builtins._appServicios)
    globales.carga_configuracion_elastic(ruta, datosElastic)
    elastic_conectar.conectarElastic(ruta)

    # Conexión MINIO
    datosMinio = leer_datos_minio(builtins._appServicios)
    globales.carga_configuracion_minio(datosMinio)
    minio_conectar.conectarMinio()

    # Conexión REDIS
    datosRedis = leer_datos_redis(builtins._appServicios)
    globales.carga_configuracion_redis(datosRedis)
    redis_conectar.conectarRedis()
