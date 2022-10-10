#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random

from . import datos_comunes

##################
# BASICOS SALIDA #
##################
campos_basicos_interno = [
    'radicado_en',
    'radicado_por',
    'nro_radicado',
    'fecha_radicado',
    'asunto',
    'dependencia_envia_id',
    'funcionario_envia_id',    
    'dependencia_recibe_id',
    'funcionario_recibe_id',
]

# DATOS BASICOS DEL INTERNO (DEL REGISTRO FISICO)
def datos_basicos(datos, tarea_id):    
    radicado_por, radicado_en = datos_comunes.datos_radicador(datos, tarea_id)
    radicado                  = "I-2021-" + str(random.randint(0, 10000))
    tipo_firma                = ",".join(datos['tipo_firma'])
    medio_notificacion        = ",".join(datos['medio_notificacion'])
    datos_especificos = {
        'radicado_en'            : radicado_en,
        'radicado_por'           : radicado_por,
        'nro_radicado'           : radicado,
        'fecha_radicado'         : datetime.datetime.now(),
        'asunto'                 : datos['asunto'],
        'dependencia_envia_id'   : datos['dependencia_envia_id'],
        'funcionario_envia_id'   : datos['funcionario_envia_id'],
        'dependencia_recibe_id'  : datos['dependencia_recibe_id'],
        'funcionario_recibe_id'  : datos['funcionario_recibe_id'],        
    }
    
    return datos_especificos


# DATOS EXTENDIDOS DE LA SALIDA (atributos_)
def datos_extendidos(datos, tarea_id):    
    extendidos = {}
    for campo, valor in datos.items():
        if (campo not in campos_basicos_interno):
            extendidos[campo] = valor
    
    extendidos = datos_comunes.limpiar_datos(extendidos, ['archivos', 'id'])

    return extendidos