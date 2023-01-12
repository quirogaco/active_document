#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from aplicacion.especificos.gestion.acciones import acciones_detalle
from aplicacion.trabajadores_base import radicados_celery
from aplicacion.datos.redis       import redis_datos
from aplicacion.trabajadores      import utilidades
from aplicacion.logs              import crea_logs

def log_radicado_entrada(datos={}, id_tarea=""):
    datos_tarea = redis_datos.lee_tarea_ejecucion(id_tarea)
    # Log del radicado
    datos_log = {
        "accionante_tipo": "usuario",
        "accionante_id": datos_tarea['_usuario_']['id'],
        "destinatario_tipo": "dependencia",          
        "destinatario_id": datos['destinatario_id'],          
        "proceso": datos["proceso"],
        "fuente": "radicados_entrada",
        "fuente_id": datos['id'], 
        "accion": datos["accion"],  
        "detalle": datos['detalle'],
        "estado": datos["estado"],  
        "detalle_estado": datos["detalle"]
    }

    radicados_celery.radicados_app_crea_log.apply_async(**utilidades.parametros(
        'radicados', 
        parametros={
            "datos": datos_log
        }
    ))
    
def log_gestion(datos={}, id_tarea="", encolar=True, retardo=0):
    datos_tarea = redis_datos.lee_tarea_ejecucion(id_tarea)
    accion = datos["accion"]
    # Log del radicado
    datos_log = {
        "accionante_tipo": "usuario",
        "accionante_id": datos_tarea['_usuario_']['id'], 
        "destinatario_tipo": "usuario",         
        "destinatario_id": datos['destinatario_id'],     
        "proceso": acciones_detalle.acciones_entrada[accion]["PROCESO"],
        "fuente": "peticiones",
        "fuente_id": datos['id'], 
        "accion": acciones_detalle.acciones_entrada[accion]["ACCION"],  
        "detalle": datos['detalle'],
        "estado": acciones_detalle.acciones_entrada[accion]["ESTADO"],  
        "detalle_estado": acciones_detalle.acciones_entrada[accion]["MENSAJE_ESTADO"]
    }

    if encolar == True:
        radicados_celery.radicados_app_crea_log.apply_async(
            **utilidades.parametros(
                'radicados', 
                parametros={
                    "datos": datos_log
                },
                retardo=retardo
            )
        )
    else:
        crea_logs.crea_log(datos=datos_log)