#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random

from . import datos_comunes

##################
# BASICOS SALIDA #
##################
campos_basicos_salida = [
    'radicado_en',
    'radicado_por',
    'nro_radicado',
    'fecha_radicado',
    'fecha_documento',
    'asunto',
    'medio_notificacion',
    'respuesta_tipo',
    'dependencia_responde_id',
    'funcionario_responde_id',
    'tipo_firma',
    'gestion_id'
]

# DATOS BASICOS DE LA ALIDA (DEL REGISTRO FISICO)
def datos_basicos(datos, tarea_id):    
    radicado_por, radicado_en = datos_comunes.datos_radicador(datos, tarea_id)
    radicado                  = "S-2021-" + str(random.randint(0, 10000))
    tipo_firma                = ",".join(datos['tipo_firma'])
    medio_notificacion        = ",".join(datos['medio_notificacion'])
    datos_especificos = {
        'radicado_en'            : radicado_en,
        'radicado_por'           : radicado_por,
        'nro_radicado'           : radicado,
        'fecha_radicado'         : datetime.datetime.now(),
        'fecha_documento'        : datos['fecha_documento'],
        'asunto'                 : datos['asunto'],
        'medio_notificacion'     : medio_notificacion,
        'respuesta_tipo'         : datos['respuesta_tipo'],
        'dependencia_responde_id': datos['dependencia_responde_id'],
        'funcionario_responde_id': datos['funcionario_responde_id'],
        'tipo_firma'             : tipo_firma,
        'gestion_id'             : ""
    }
    
    return datos_especificos


# DATOS EXTENDIDOS DE LA SALIDA (atributos_)
def datos_extendidos(datos, tarea_id):    
    extendidos = {}
    for campo, valor in datos.items():
        if (campo not in campos_basicos_salida) and (campo not in datos_comunes.campos_tercero):
            extendidos[campo] = valor
    
    extendidos = datos_comunes.limpiar_datos(extendidos, ['archivos', 'id'])

    return extendidos