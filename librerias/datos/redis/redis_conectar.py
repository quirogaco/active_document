#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
import redis

from librerias.datos.base  import globales

def conectarRedis():
    configuracion = globales.lee_configuracion_redis()
    conexion      = redis.Redis(host=configuracion["host"] , port=configuracion["port"] , db=0, decode_responses=True)
    globales.carga_conexion_redis(conexion)

    return conexion