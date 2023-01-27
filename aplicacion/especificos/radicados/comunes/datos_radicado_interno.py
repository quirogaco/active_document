#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random

from . import datos_comunes
from librerias.utilidades import basicas
from librerias.datos.sql import (
    sqalchemy_filtrar,
    sqalchemy_modificar,
    sqalchemy_leer
) 

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
 
def radicado_consecutivo(tipo="INTERNOS"):
    filtros = [ [ "nombre", "=", tipo ] ]
    salida = sqalchemy_filtrar.filtrarOrdena(
        estructura="consecutivos", 
        filtros=filtros, 
        ordenamientos=[]
    )[0]
    consecutivo = salida["consecutivo"] + 1
    sqalchemy_modificar.modificar_un_registro(
        "consecutivos", 
        salida["id"],
        {"consecutivo": consecutivo}
    )

    return str(consecutivo).rjust(6,'0')

# DATOS BASICOS DEL INTERNO (DEL REGISTRO FISICO)
def datos_basicos(datos, tarea_id):    
    radicado_por, radicado_en = datos_comunes.datos_radicador(datos, tarea_id)
    consecutivo = radicado_consecutivo("INTERNOS")
    radicado = "I-" + basicas.ano() + "-" + consecutivo    
    tipo_firma = ",".join(datos['tipo_firma'])
    medio_notificacion = ",".join(datos['medio_notificacion'])
    datos_especificos = {
        'radicado_en': radicado_en,
        'radicado_por': radicado_por,
        'nro_radicado': radicado,
        'fecha_radicado': datetime.datetime.now(),
        'asunto': datos['asunto'],
        'dependencia_envia_id': datos['dependencia_envia_id'],
        'funcionario_envia_id': datos['funcionario_envia_id'],
        'dependencia_recibe_id': datos['dependencia_recibe_id'],
        'funcionario_recibe_id': datos['funcionario_recibe_id'], 
        'medio_notificacion': medio_notificacion,
        'tipo_firma': tipo_firma
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