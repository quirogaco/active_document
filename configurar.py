#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#########################
# Configuracion general #
#########################
import os

# Argumentos
import argparse
# Argumentos esperados
parser     = argparse.ArgumentParser()
parser.add_argument('-services', type=str, default="0.0.0.0", help='Ip de los servicio docker del sistema')
argumentos = parser.parse_args()

# Ip generica de conexion a servicios externos dockers
ipGeneral = argumentos.services # convierte a byte

import redis

def crearParametro(redisClient, ruta, valor):
  print("crearParametro:", ruta, valor)
  redisClient.set(ruta, valor)
    
# Cliente redis
redisClient = redis.Redis(host=ipGeneral, port=6379, db=0)
print("redis:", redisClient)

# Active documento nombre de espacios base
nsBase = 'ad/base/'
# Ip de servicios basica del sistema
crearParametro(redisClient, (nsBase + "ip/servicios"), ipGeneral)

# Ruta basica del sistema en DISCO, path
ruta_basica = (os.getcwd() + os.sep).replace('\\', '/')
print("ruta_basica:", ruta_basica)
crearParametro(redisClient, (nsBase+"ruta/basica"), ruta_basica)   

# Redis direccion
crearParametro(redisClient, (nsBase+"redis/direccion"), (ipGeneral+":6379"))
crearParametro(redisClient, (nsBase+"redis/host"), ipGeneral)
crearParametro(redisClient, (nsBase+"redis/port"), "6379")

# Arangodb direccion
crearParametro(redisClient, (nsBase+"arango/host"), ipGeneral)
crearParametro(redisClient, (nsBase+"arango/port"), "8529")

# Amqp direccion y usuario
crearParametro(redisClient, (nsBase+"amqp/direccion"), (ipGeneral+":5672"))
crearParametro(redisClient, (nsBase+"amqp/usuario"),   "guest")

# Configuracion global
crearParametro(redisClient, (nsBase+"globals/organizacion"), "esap")
crearParametro(redisClient, (nsBase+"globals/unidad"), "NACIONAL")
crearParametro(redisClient, (nsBase+"globals/detalle"), "Esap")
crearParametro(redisClient, (nsBase+"globals/sigla"), "esap")

# Configuracion modo login
crearParametro(redisClient, (nsBase+"login/modo"), "database")

# Elastic search
crearParametro(redisClient, (nsBase+"elastic/ip"), "http://"+ipGeneral)
crearParametro(redisClient, (nsBase+"elastic/port"), "9200")
crearParametro(redisClient, (nsBase+"elastic/timeout"), "2400")

# Tika
crearParametro(redisClient, (nsBase+"tika/ip"), "http://"+ipGeneral)
crearParametro(redisClient, (nsBase+"tika/port"), "2181")

# Minio
crearParametro(redisClient, (nsBase+"minio/ip"), ipGeneral)
crearParametro(redisClient, (nsBase+"minio/port"), "9000")
crearParametro(redisClient, (nsBase+"minio/access_key"), "minio")
crearParametro(redisClient, (nsBase+"minio/secret_key"), "minio123")

# Base de datos
crearParametro(redisClient, (nsBase+"db/sqlname"), "oracle")
crearParametro(redisClient, (nsBase+"db/adrress"), "127.0.0.1:1521/XE")
crearParametro(redisClient, (nsBase+"db/name"), "")
crearParametro(redisClient, (nsBase+"db/user"), "GESTOR_360")
crearParametro(redisClient, (nsBase+"db/password"), "12345678")

""" LOCAL
crearParametro(redisClient, (nsBase+"db/sqlname"), "oracle")
crearParametro(redisClient, (nsBase+"db/adrress"), "XE")
crearParametro(redisClient, (nsBase+"db/name"), "")
crearParametro(redisClient, (nsBase+"db/user"), "GESTIONDOC_AC")
crearParametro(redisClient, (nsBase+"db/password"), "12345678")
"""

""" SERVIDOR
crearParametro(redisClient, (nsBase+"db/sqlname"), "oracle")
crearParametro(redisClient, (nsBase+"db/adrress"), "XE_SERVIDOR")
crearParametro(redisClient, (nsBase+"db/name"), "")
crearParametro(redisClient, (nsBase+"db/user"), "GESTIONDOC_AC")
crearParametro(redisClient, (nsBase+"db/password"), "123456789")

# Servidor ESAP
crearParametro(redisClient, (nsBase+"db/sqlname"), "oracle")
crearParametro(redisClient, (nsBase+"db/adrress"), "ESAP_SCAN")
crearParametro(redisClient, (nsBase+"db/name"), "")
crearParametro(redisClient, (nsBase+"db/user"), "activedoc")
crearParametro(redisClient, (nsBase+"db/password"), "Act1v32020")
"""