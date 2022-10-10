#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from elasticsearch import Elasticsearch

from librerias.datos.base  import globales

def conectarElastic(ruta):
    configuracion = globales.lee_configuracion_elastic(ruta)
    url           = configuracion["ip"] + ':' + configuracion["port"]
    conexion      = Elasticsearch(hosts=url, timeout=int(configuracion["timeout"]))
    globales.carga_conexion_elastic(ruta, conexion)

    # Cuando no existen indices genera error
    conexion.indices.put_settings(
        index            = '_all',
        allow_no_indices = True,
        body             = {          
            'max_result_window': 500000
        }
    )

    return conexion