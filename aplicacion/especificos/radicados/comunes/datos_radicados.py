#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random

from aplicacion.datos.redis import redis_datos
from .                      import datos_radicado_salida, datos_radicado_entrada, datos_radicado_interno

#######################
# BASICOS, EXTENDIDOS #
#######################
# DATOS BASICOS DEL RADICADO (DEL REGISTRO FISICO)
def datos_basicos(radicado_tipo="", radicado_clase="", datos={}, tarea_id=""):
    datos_especificos = {}
    if radicado_tipo == "SALIDA":
        datos_especificos = datos_radicado_salida.datos_basicos(datos, tarea_id)

    if radicado_tipo == "ENTRADA":
        datos_especificos = datos_radicado_entrada.datos_basicos(datos, tarea_id)

    if radicado_tipo == "INTERNO":
        datos_especificos = datos_radicado_interno.datos_basicos(datos, tarea_id)

    return datos_especificos


# DATOS EXTENDIDOS DEL RADICADO (atributos_)
def datos_extendidos(radicado_tipo="", radicado_clase="", datos={}, tarea_id=""):
    datos_especificos = {}
    if radicado_tipo == "SALIDA":
        datos_especificos = datos_radicado_salida.datos_extendidos(datos, tarea_id)

    if radicado_tipo == "ENTRADA":
        datos_especificos = datos_radicado_entrada.datos_extendidos(datos, tarea_id)

    if radicado_tipo == "INTERNO":
        datos_especificos = datos_radicado_interno.datos_extendidos(datos, tarea_id)

    return datos_especificos


##########
# COPIAS #
##########
def datos_copia(datos):
    datos_especificos = {
        "copia_usuarios_id": datos.get("copia_usuarios_id", []),  
        "copia_grupos_id"  : datos.get("copia_grupos_id", []),  
        "copia_terceros_id": datos.get("copia_terceros_id", []),   
    }

    return datos_especificos

###########
# TERCERO #
###########
def datos_tercero(datos):
    datos_especificos = {
        "clase"                 : datos.get("tercero_clase", None),   
        "tipo_tercero_id"       : datos.get("tercero_tercero_tipo_id", None),   
        "tipo_identificacion_id": datos.get("tercero_tipo_identificacion_id", None),           
        "nro_identificacion"    : datos.get("tercero_nro_identificacion", ""),   
        "razon_social"          : datos.get("tercero_razon_social", ""),  
        "cargo"                 : datos.get("tercero_cargo", ""),   
        "nombres"               : datos.get("tercero_nombres", ""), 
        "apellidos"             : datos.get("tercero_apellidos", ""), 
        "correo_electronico"    : datos.get("tercero_correo_electronico", ""), 
        "direccion"             : datos.get("tercero_direccion", ""), 
        "codigo_postal"         : datos.get("tercero_codigo_postal", ""), 
        "telefono"              : datos.get("tercero_telefono", ""), 
        "telefono_movil"        : datos.get("tercero_telefono_movil", ""), 
        "fax"                   : datos.get("tercero_fax", ""), 
        "ciudad_id"             : datos.get("tercero_ciudad_id", "") 
    }

    return datos_especificos


def datos_tercero_tercero(datos):
    datos_especificos = {
        "tercero_clase": datos.get("clase", None),   
        "tercero_tercero_tipo_id": datos.get("tipo_tercero_id", None),   
        "tercero_tipo_identificacion_id": datos.get("tipo_identificacion_id", None),           
        "tercero_nro_identificacion": datos.get("nro_identificacion", ""),   
        "tercero_razon_social": datos.get("razon_social", ""),  
        "tercero_cargo": datos.get("cargo", ""),   
        "tercero_nombres": datos.get("nombres", ""), 
        "tercero_apellidos": datos.get("apellidos", ""), 
        "tercero_correo_electronico": datos.get("correo_electronico", ""),
        "correo_electronico": datos.get("correo_electronico", ""), 
        "tercero_direccion": datos.get("direccion", ""), 
        "tercero_codigo_postal": datos.get("codigo_postal", ""), 
        "tercero_telefono": datos.get("telefono", ""), 
        "tercero_telefono_movil": datos.get("telefono_movil", ""), 
        "tercero_fax": datos.get("fax", ""), 
        "tercero_ciudad_id": datos.get("ciudad_id", ""),
        "tercero_ciudad_nombre": datos.get("ciudad_nombre", "") 
    }

    return datos_especificos