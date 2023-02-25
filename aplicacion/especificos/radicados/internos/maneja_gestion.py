#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, datetime, random

from aplicacion.datos.redis  import redis_datos
from librerias.datos.sql     import (
    sqalchemy_modificar, 
    sqalchemy_leer, 
    sqalchemy_filtrar, 
    sqalchemy_insertar
)
from librerias.datos.elastic import elastic_operaciones

from aplicacion.comunes import indexar_datos
from aplicacion.logs import crea_logs

# Modifica registro de gestión 
def modifica_peticion(gestion, peticion_id, datos):
    sqalchemy_modificar.modificar_un_registro("peticiones", peticion_id, datos)
    elastic_operaciones.indexar_registro("peticiones", peticion_id)

def actualiza(radicado_datos, peticion_id, id_tarea):
    # Información de la tarea
    datos_tarea = redis_datos.lee_tarea_ejecucion(id_tarea)
    # Trae petición
    gestion = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)
    
    # Actualiza petición
    atributos_               = gestion["atributos_"]
    atributos_["finalizado"] = {
        "fecha_respuesta": datetime.datetime.now(),        
        "finalizado_comentario": (
            "RADICADO CON # [" + radicado_datos["nro_radicado"] + "] "
        ),
        "finalizado_en"        : datetime.datetime.now(),        
        "fecha_respuesta"      : datetime.datetime.now()
    }
    datos_modificados         = {
        "atributos_": atributos_
    }
    modifica_peticion(gestion, peticion_id, datos_modificados)
    
    """
    # INTERNO -> Log del radicado 
    accionante_id   = datos_tarea['_usuario_']['id']
    datos_log = {
        "accionante_tipo"  : "USUARIO",      
        "accionante_id"    : accionante_id,    
        "destinatario_tipo": "",      
        "destinatario_id"  : "",     
        "proceso"          : "GESTION",
        "fuente"           : "radicados_interno",
        "fuente_id"        : radicado_datos["id"], 
        "accion"           : "RESPONDER",  
        "detalle"          : ( "RESPONDE DE RADICADO CON #: " + radicado["nro_radicado"]),
        "estado"           : "FINALIZADO",  
        "detalle_estado"   : "FINALIZADO CON RADICACIÓN DE SALIDA",  
    }
    crea_logs.crea_log(datos_log)
    """

    return {} 