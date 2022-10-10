#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from minio import Minio

from librerias.datos.base  import globales

def conectarMinio():
    configuracion = globales.lee_configuracion_minio()
    url           = configuracion["ip"] + ':' + configuracion["port"] 
    conexion      = Minio(    
        url,
        access_key = configuracion["access_key"],
        secret_key = configuracion["secret_key"],
        secure     = False,
    )
    conexion      = conexion
    globales.carga_conexion_minio(conexion)

    return conexion