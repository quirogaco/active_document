#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime, random 

from aplicacion.trabajadores_base import radicados_celery
from aplicacion.datos.redis       import redis_datos
from aplicacion.trabajadores      import utilidades

#################
# DESTINATARIOS #
#################
def destinatario_salida(accion, datos, datos_tarea):
    destinatario_tipo = "tercero"
    ## TERCERO ID DEBE ESTAR CREADO DE ANTEMANO PARA QUE ESTO FUNCIONE
    ## SI NO LOS SABEMOS LO FORZAMOS A CREAR CON ID PREDEFINIDO
    destinatario_id   = datos.get('tercero_id')

    return destinatario_tipo, destinatario_id

def destinatario_lee(radicado_tipo, radicado_clase, accion, datos, datos_tarea):
    destinatario_tipo = ""
    destinatario_id   = ""
    if radicado_tipo == "SALIDA":
        destinatario_tipo, destinatario_id = destinatario_salida(accion, datos, datos_tarea)
        
    return destinatario_tipo, destinatario_id

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

def copia_usuarios(fuente, radicado_tipo, radicado_id, copias):
    for destino_id in copias:
        dato_copia = {
            "radicado_tipo"    : radicado_tipo,  
            "radicado_id"      : radicado_id,  
            "destinatario_tipo": "usuario",  
            "destinatario_id"  : destino_id,  
            "estado"           : "ASIGNADO",
            "fuente"           : fuente            
        }

        radicados_celery.crea_copia.apply_async(**utilidades.parametros(
            'copias', 
            parametros={
                "datos": dato_copia
            }
        ))

def copia_radicado(radicado_tipo, radicado_clase, radicado_id, copia_usuarios, copia_grupos, copia_terceros):
    fuente = "radicados_entrada"
    if radicado_tipo == "salida":
        fuente = "radicados_salida"          
    if radicado_tipo == "interno":
        fuente = "radicados_interno"  
        
    copia_usuarios(fuente, radicado_tipo, radicado_id, copia_usuarios)