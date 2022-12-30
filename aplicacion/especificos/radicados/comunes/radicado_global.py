#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint

from aplicacion.trabajadores import utilidades
from aplicacion.trabajadores_base import radicados_celery

from aplicacion.comunes import indexar_datos
from aplicacion.comunes import manejo_archivos
from aplicacion.especificos.radicados.comunes import manejo_terceros
from aplicacion.especificos.radicados.comunes import copia_radicados
from . import log_radicados

# Invoca llamado celery
def invoca_tercero_log_anexos_copias(datos):
    print("")
    print("?????????????????????????")
    print("INVOCA crea_tercero_log_anexos_copias", datos["radicado_id"])
    print("")
    print("-------------------")
    radicados_celery.radicados_app_tercero_log_anexos_copias.apply_async(**utilidades.parametros(
        'radicados', 
        parametros={
            "datos": datos
        }
    ))

# Crea informacion de radicados en una sola tarea de cola
def crea_tercero_log_anexos_copias(datos={}):
    print("")
    print("******************************")
    print("crea_tercero_log_anexos_copias", datos["radicado_id"])
    print("")
    print("-------------------")
    # Id de la tarea
    tarea_id = datos["tarea_id"]    
    # Tipo de radicado
    radicado_tipo = datos["radicado_tipo"]
    # Id de radicado
    radicado_id = datos["radicado_id"]
    
    ######################
    # Manejo de archivos #
    ###################### 
    archivos = datos["archivos"]
    # Estructura
    if radicado_tipo == "SALIDA":
        estructura = "radicados_salida"
    elif radicado_tipo == "INTERNO":
        estructura = "radicados_interno"
    else:
        estructura = "radicados_entrada"
    manejo_archivos.manejo(
        estructura, 
        "insertar", 
        {"id": radicado_id}, 
        archivos, 
        tarea_id
    )

    ########################
    # Creación del tercero #
    ########################
    # se mueve al moemneto de radicar para poder generar plantilla con datos completos
    # if (radicado_tipo != "INTERNO"):
    #     tercero_datos = datos["tercero_datos"]
    #     tercero = manejo_terceros.crear_registro_tercero(
    # radicado_tipo, tercero_datos, radicado_id, tarea_id)

    ################################
    # Log de eventos de RADICACIóN #
    ################################
    radicado = datos["radicado"]
    # if (radicado_tipo != "INTERNO"):
    #     radicado["tercero_id"] = tercero["id"]
    # False al final es para que no invoque remoto, esta tarea ya es remota
    log_radicados.log_radicado(
        radicado_tipo, 
        radicado_tipo, 
        "RADICAR", 
        radicado, 
        tarea_id, 
        False
    )
    
    ###########################
    # Con copia de RADICACIóN #
    ###########################
    copia_grupos_id   = datos.get("copia_grupos_id", [])
    copia_usuarios_id = datos.get("copia_usuarios_id", [])
    if copia_grupos_id in ["", " ", None]:
        copia_grupos_id = []
    if copia_usuarios_id in ["", " ", None]:
        copia_usuarios_id = []                    
    copia_radicados.copia_radicado(
        radicado_tipo, 
        radicado_tipo, 
        radicado_id, 
        datos.get("nro_radicado", ""), 
        datos.get("asunto", []), 
        copia_usuarios_id, 
        copia_grupos_id, 
        []
    )
    
    ##############################
    # Indexa radicado de ultimo  #
    ##############################
    indexar_datos.indexar_estructura(estructura, radicado_id)