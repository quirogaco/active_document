#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import sys, builtins
import redis

# Nombre de espacio  para configuración Redis
nsBase = 'ad/base/'

def crearClienteRedis(hosts):
  redisClient = redis.Redis(host=hosts, port=6379, db=0, decode_responses=True)
  #print("redisclient:", redisClient)
  
  return redisClient

def leerParametro(redisClient, ruta):
  valor = redisClient.get(nsBase+ruta)

  return str(valor)

# Rutas globales para importación de librerias
def publicaRutas(ipServicios):
    redisClient       = crearClienteRedis(ipServicios)
    builtins.rutaBase = leerParametro(redisClient, "ruta/basica")
    sys.path.append(builtins.rutaBase + 'aplicacion')
    sys.path.append(builtins.rutaBase + 'librerias')