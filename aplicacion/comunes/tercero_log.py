#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime, random 

from aplicacion.trabajadores_base import radicados_celery
from aplicacion.datos.redis       import redis_datos
from aplicacion.trabajadores      import utilidades

###############
# ACCIONANTES #
###############
def accionante_salida(accion, datos, datos_tarea):
    accionante_tipo = "usuario"
    accionante_id   = datos_tarea['_usuario_']['id']

    return accionante_tipo, accionante_id

def accionante_lee(radicado_tipo, radicado_clase, accion, datos, datos_tarea):
    accionante_tipo = ""
    accionante_id   = ""
    if radicado_tipo == "SALIDA":
        accionante_tipo, accionante_id = accionante_salida(accion, datos, datos_tarea)

    return accionante_tipo, accionante_id

#################
# DESTINATARIOS #
#################
def destinatario_salida(accion, datos, datos_tarea):
    destinatario_tipo = "tercero"
    ## TERCERO ID DEBE ESTAR CREADO DE ANTEMANO PARA QUE ESTO FUNCIONE
    ## SI NO LOS SABEMOS LO FORZAMOS A CREAR CON ID PREDEFINIDO
    destinatario_id   = datos['tercero_id']

    return destinatario_tipo, destinatario_id

def destinatario_lee(radicado_tipo, radicado_clase, accion, datos, datos_tarea):
    destinatario_tipo = ""
    destinatario_id   = ""
    if radicado_tipo == "SALIDA":
        destinatario_tipo, destinatario_id = destinatario_salida(accion, datos, datos_tarea)
        
    return destinatario_tipo, destinatario_id

####################
# ACCIONES DETALLE #
####################
from aplicacion.especificos.radicados.comunes import acciones_detalle_salida

def acciones_salida(accion, atributo, datos, datos_tarea):
    resultado = acciones_detalle_salida.acciones_salida[accion][atributo]

    return resultado

def acciones_lee(radicado_tipo, radicado_clase, accion, atributo, datos, datos_tarea):
    resultado = ""
    if radicado_tipo == "SALIDA":
        resultado = acciones_salida(accion, atributo, datos, datos_tarea)

    return resultado

##########
# FUENTE #
##########
def fuente_lee(radicado_tipo, radicado_clase):
    resultado = "radicados_entrada"

    if radicado_tipo == "SALIDA":
        resultado = "radicados_salida"
    
    if radicado_tipo == "INTERNO":
        resultado = "radicados_interno"

    return resultado

def log_radicado(radicado_tipo, radicado_clase, accion, datos, id_tarea):
    datos_tarea = redis_datos.lee_tarea_ejecucion(id_tarea)

    print("LOG RADICADO datos tarea:", radicado_tipo, radicado_clase)
#pprint.pprint(datos_tarea)

    accionante_tipo, accionante_id     = accionante_lee(radicado_tipo, radicado_clase, accion, datos, datos_tarea)
    destinatario_tipo, destinatario_id = destinatario_lee(radicado_tipo, radicado_clase, accion, datos, datos_tarea)
    proceso   = acciones_lee(radicado_tipo, radicado_clase, accion, "PROCESO", datos, datos_tarea)
    fuente    = fuente_lee(radicado_tipo, radicado_clase)
    accion_   = acciones_lee(radicado_tipo, radicado_clase, accion, "ACCION", datos, datos_tarea)
    estado    = acciones_lee(radicado_tipo, radicado_clase, accion, "ESTADO", datos, datos_tarea)
    destalle_ = acciones_lee(radicado_tipo, radicado_clase, accion, "MENSAJE_ESTADO", datos, datos_tarea)

    # Log del radicado
    datos_log = {
        "accionante_tipo"  : accionante_tipo,      
        "accionante_id"    : accionante_id,    
        "destinatario_tipo": destinatario_tipo,      
        "destinatario_id"  : destinatario_id,     
        "proceso"          : proceso,
        "fuente"           : fuente,
        "fuente_id"        : datos.get('id', "222"), 
        "accion"           : accion_,  
        "detalle"          : ( "RADICACI�N CON #: " + datos.get("nro_radicado", "333")),
        "estado"           : estado,  
        "detalle_estado"   : destalle_
    }

    """
    print("")
    print("")
    print("DATOS LOG")    
    pprint.pprint(datos_log)
    print("")
    print("")
    """

    #""" 
    radicados_celery.crea_log.apply_async(**utilidades.parametros(
        'radicados', 
        parametros={
            "datos": datos_log
        }
    ))
    #"""