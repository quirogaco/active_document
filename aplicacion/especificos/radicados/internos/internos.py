#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, datetime, random

from librerias.datos.sql import sqalchemy_insertar, sqalchemy_leer
from aplicacion.comunes import pdf_notifica
from aplicacion.comunes import indexar_datos

from aplicacion.especificos.radicados.comunes import datos_radicados
from aplicacion.especificos.radicados.comunes import radicado_global

def crear_radicado(datos_basicos, datos):
    resultado = sqalchemy_insertar.insertar_registro_estructura(
        "radicados_interno", 
        datos_basicos
    )
   
    return resultado

from . import maneja_gestion
from aplicacion.especificos.radicados.gestion import gestion

def radicar(accion, datos={}, archivos=[], id_tarea=""):
    datos_radicado = datos["datos"]
    #"""
    print("")
    print("...............")    
    print("INTERNO- > RADICAR:", accion, id_tarea)
    pprint.pprint(datos)
    print("INTERNO - > RADICAR ARCHIVOS:")
    pprint.pprint(archivos)
    #"""

    # Datos de operacion
    datos_basicos = datos_radicados.datos_basicos(
        "INTERNO", 
        "INTERNO", 
        datos_radicado, 
        id_tarea
    )
    datos_extendidos = datos_radicados.datos_extendidos(
        "INTERNO", 
        "INTERNO", 
        datos_radicado, 
        id_tarea
    )
    datos_copia = datos_radicados.datos_copia(datos_radicado)

    # Creación del radicado
    datos_basicos["fecha_radicado"] = datetime.datetime.now()
    datos_basicos["atributos_"]  = datos_extendidos
    radicado = crear_radicado(datos_basicos, datos)
    radicado_id = radicado["id"]
    datos_radicado["id"] = radicado_id
    datos_cola = {
        "tarea_id": id_tarea,
        "radicado_tipo": "INTERNO",
        "radicado_id": radicado_id,
        "archivos": archivos,
        "radicado": radicado
    }
    radicado_global.invoca_tercero_log_anexos_copias(datos_cola)

    # Genera pdf y notifica
    # Datos del radicado, todavia no se a indexado
    # 
    datos_completos = {}
    datos_completos.update(radicado)
    datos_completos.update(datos_basicos)
    datos_completos.update(datos_extendidos)

    # Lee información gestión
    gestion_id = datos_radicado.get("gestion_id", None)
    if gestion_id != None:
        peticion = sqalchemy_leer.leer_un_registro("peticiones", gestion_id) 
        datos_completos["borrador_id"] = peticion["borrador_id"]

    # Correo destinatario notificacion
    destinatario = sqalchemy_leer.leer_un_registro(
        "usuarios", 
        datos_radicado['funcionario_recibe_id']
    ) 
    datos_completos["correo_electronico"] = destinatario["correo"]
    pdf_notifica.pdf_notificacion("INTERNO", datos_completos, id_tarea)

    # Actualiza gestión del borrador
    if gestion_id not in ["", None]:
        maneja_gestion.actualiza(radicado, gestion_id, id_tarea)

    # Crea gestion para destinatario
    gestion.asigna_interno(accion, datos_radicado, archivos, id_tarea)
    
    # Indexa de ultimo
    indexar_datos.indexar_estructura(
        "radicados_interno", 
        radicado_id, 
        retardo=60
    )

    # Con copia a eventos de RADICACIóN
    #copia_radicados.copia_radicado("SALIDA", "SALIDA", radicado_id, copia_usuarios, copia_grupos, copia_terceros)    
        
    resultado =  {
        "accion" : accion,
        "estado" : "",
        "mensaje": "",
        "datos"  : radicado
    }
    
    return resultado