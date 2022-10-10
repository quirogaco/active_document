#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import rapidjson
from rapidjson import DM_ISO8601, DM_SHIFT_TO_UTC, DM_NAIVE_IS_UTC, DM_IGNORE_TZ
modoFecha = DM_ISO8601 | DM_SHIFT_TO_UTC | DM_NAIVE_IS_UTC | DM_IGNORE_TZ

from librerias.datos.base  import globales

#######################
# TAREAS EN EJECUCION #
######################
def carga_tarea_ejecucion(idtarea="", datos={}):    
    conexion = globales.lee_conexion_redis()
    datos    = rapidjson.dumps( datos, datetime_mode=modoFecha )
    conexion.set( idtarea, rapidjson.dumps( datos, datetime_mode=modoFecha ) )
    
def lee_tarea_ejecucion(idtarea=""):
    conexion = globales.lee_conexion_redis()
    datos    = conexion.get( idtarea )
    objeto   = rapidjson.loads( rapidjson.loads( datos, datetime_mode=modoFecha ), datetime_mode=modoFecha )

    return objeto