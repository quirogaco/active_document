#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from parent_import import parentdir
from box import Box

configuracion   = parentdir.parentdir.aplicacion.inicio.configuracion
globales        = parentdir.parentdir.librerias.datos.base.globales
base_general    = parentdir.parentdir.aplicacion.datos.clases_base.base_general
sqlalchemy_conectar = parentdir.parentdir.librerias.datos.sql.sqlalchemy_conectar
sqa_operaciones     = parentdir.parentdir.librerias.datos.sql.sqa_operaciones


import datos_db
globales.carga_configuracion_sql("test", datos_db.datos)
pprint.pprint(globales.CONFIGURACION_GENERAL.SQL)

conexionSql = sqlalchemy_conectar.conexionSql("test")
print("conexionSql:", conexionSql)
motorSql    = sqlalchemy_conectar.motorSql(conexionSql)
print("motorSql:", motorSql)
#print("CLASE_BASE_SQL:", globales.CLASE_BASE_SQL)
print("conectado:", sqlalchemy_conectar.conectarSql("test"))

print("GLOBALES sql:", globales.CONFIGURACION_GENERAL.SQL,  globales.CONFIGURACION_GENERAL.SQL_MOTORES, globales.CONFIGURACION_GENERAL.SQL_SESIONES)

print("CLASE_BASE_SQL, base_general:", globales.CLASE_BASE_SQL, base_general.DB_BASE_GENERAL)

sesion = sqa_operaciones.nuevaSesion("test")
print(sesion)

"""
baseGeneral = parentdir.parentdir.aplicacion.datos.genericas.baseGeneral

sqa_operaciones.creaTablas("test")
"""