#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random

from aplicacion.datos.redis import redis_datos

campos_tercero = [
    "busca_remitente",
    "tercero_clase",  
    "tercero_tercero_tipo_id",
    "tercero_tipo_identificacion_id",          
    "tercero_nro_identificacion",
    "tercero_razon_social",
    "tercero_cargo",
    "tercero_nombres",
    "tercero_apellidos",
    "tercero_correo_electronico",
    "tercero_direccion", 
    "tercero_codigo_postal",
    "tercero_telefono",
    "tercero_telefono_movil", 
    "tercero_fax", 
    "tercero_ciudad_id"
]

def limpiar_datos(datos_limpiar={}, atributos=[]):
    for atributo in atributos:
        try:
            del datos_limpiar[atributo]
        except:
            pass

    return datos_limpiar

def datos_radicador(datos, tarea_id):
    datos_tarea  = redis_datos.lee_tarea_ejecucion(tarea_id)
    _usuario     = datos_tarea.get('_usuario_', {})
    radicado_por = _usuario .get('id')
    radicado_en  = _usuario .get('ubicacion_id')

    return radicado_por, radicado_en