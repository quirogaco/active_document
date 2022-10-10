#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pprint, datetime, random 

from aplicacion.trabajadores_base import radicados_celery
from aplicacion.datos.redis       import redis_datos
from aplicacion.trabajadores      import utilidades

def log_trd(fuente, fuente_id, accion, datos, id_tarea):
    datos_tarea     = redis_datos.lee_tarea_ejecucion(id_tarea)
    accionante_tipo = "USUARIO"
    accionante_id   = datos_tarea['_usuario_']['id']
    detalle         = "OPERACIÓN : " + accion

    # Log del radicado
    datos_log = {
        "accionante_tipo"  : accionante_tipo,      
        "accionante_id"    : accionante_id,    
        "destinatario_tipo": "",      
        "destinatario_id"  : "",     
        "proceso"          : "TRD",
        "fuente"           : fuente,
        "fuente_id"        : fuente_id, 
        "accion"           : accion,  
        "detalle"          : detalle,
        "estado"           : "GENERADO",  
        "detalle_estado"   : detalle
    }
    
    radicados_celery.radicados_app_crea_log.apply_async(**utilidades.parametros(
        'radicados', 
        parametros={
            "datos": datos_log
        }
    ))