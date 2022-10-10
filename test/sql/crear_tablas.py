#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from parent_import import parentdir
from box import Box

configuracion   = parentdir.parentdir.aplicacion.inicio.configuracion
globales        = parentdir.parentdir.librerias.datos.base.globales
base_general    = parentdir.parentdir.aplicacion.datos.clases.clases_base.base_general
sqlalchemy_conectar    = parentdir.parentdir.librerias.datos.sql.sqlalchemy_conectar
sqlalchemy_operaciones = parentdir.parentdir.librerias.datos.sql.sqlalchemy_operaciones


import datos_db
globales.carga_configuracion_sql("base", datos_db.datos)
pprint.pprint(globales.CONFIGURACION_GENERAL.SQL)
print("conectado:", sqlalchemy_conectar.conectarSql("base"))

# Tabla base general
baseGeneral_clase = parentdir.parentdir.aplicacion.datos.clases.genericas.baseGeneral_clase

sqlalchemy_operaciones.creaTablas("base")