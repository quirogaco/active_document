#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

"""
basicas         = parentdir.parentdir.librerias.utilidades.basicas
configuracion   = parentdir.parentdir.aplicacion.inicio.configuracion
globales        = parentdir.parentdir.librerias.datos.base.globales
base_general    = parentdir.parentdir.aplicacion.datos.clases.clases_base.base_general
sqalchemy_conectar    = parentdir.parentdir.librerias.datos.sql.sqalchemy_conectar
sqalchemy_operaciones      = parentdir.parentdir.librerias.datos.sql.sqalchemy_operaciones
elastic_conectar           = parentdir.parentdir.librerias.datos.elastic.elastic_conectar
flujos_insertar_sql        = parentdir.parentdir.librerias.flujos.flujos_insertar_sql
flujos_indexar_sql         = parentdir.parentdir.librerias.flujos.flujos_indexar_sql
estructura_operaciones_sql = parentdir.parentdir.librerias.datos.estructuras.estructura_operaciones_sql

# Tabla base general
baseGeneral_clase = parentdir.parentdir.aplicacion.datos.clases.genericas.baseGeneral_clase

# Conexión SQL
import datos_db
globales.carga_configuracion_sql("base", datos_db.datos)
sqalchemy_conectar.conectarSql("base")

# Conexión ELASTIC
import datos_es
print("--->", datos_es)
globales.carga_configuracion_elastic("base", datos_es.datos)
print("globales.ELASTIC_CONEXIONES:", globales.CONFIGURACION_GENERAL.ELASTIC_CONEXIONES)
elastic_conectar.conectarElastic("base")

# Estructura 
pais                   = parentdir.parentdir.aplicacion.datos.definiciones.pais.pais
"""

# indexar
"""
resultado = flujos_indexar_sql.ejecutar("base", "pais", {"registroId": "333333", "flush": True})
print("resultado:", resultado)
resultado = flujos_indexar_sql.ejecutar("base", "pais", {"registroId": "6666", "flush": True})
print("resultado:", resultado)
resultado = flujos_indexar_sql.ejecutar("base", "pais", {"registroId": "7777", "flush": True})
print("resultado:", resultado)
resultado = flujos_indexar_sql.ejecutar("base", "pais", {"registroId": "8888", "flush": True})
print("resultado:", resultado)
resultado = flujos_indexar_sql.ejecutar("base", "pais", {"registroId": "XXXXX", "flush": True})
print("resultado:", resultado)
resultado = flujos_indexar_sql.ejecutar("base", "pais", {"registroId": "ZZZZZZ", "flush": True})
print("resultado:", resultado)
resultado = flujos_indexar_sql.ejecutar("base", "pais", {"registroId": "yyyyyy", "flush": True})
print("resultado:", resultado)
"""


from librerias.utilidades import basicas  
from librerias.flujos     import flujos_insertar_sql

uuid = basicas.uuidTexto()
print("id:", uuid)
datos = {
    #"id"        : uuid,
    "codigo"    : "0002",
    "nombre"    : "0002->EUROPA",
    #"_creado_en_"    : datetime.datetime.now(),
    #"_creado_en_"     : datetime.datetime(year=2010, month=3,  day=20),
    #"_actualizado_en_": datetime.datetime(year=2011, month=2, day=1)
}
resultado = flujos_insertar_sql.ejecutar("base", "continente", datos)

print("")
print("")
print("resultado:")
pprint.pprint(resultado)
