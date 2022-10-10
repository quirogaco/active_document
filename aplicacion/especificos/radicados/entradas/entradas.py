#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import pprint, datetime, random 

from librerias.datos.sql     import sqalchemy_insertar

from aplicacion.especificos.radicados.comunes import datos_radicados
from aplicacion.especificos.radicados.comunes import radicado_global
from aplicacion.comunes import pdf_notifica
from aplicacion.comunes import indexar_datos

def crear_radicado(datos_basicos, datos):
    resultado = sqalchemy_insertar.insertar_registro_estructura("radicados_entrada", datos_basicos)
    
    return resultado

# RADICACIóN 
def radicar(accion, datos={}, archivos=[], id_tarea=""):  
    datos_radicado = datos["datos"]
    
    # Datos de operacion
    radicado                       = "E-2022-" + str(random.randint(0, 10000))
    datos_radicado["nro_radicado"] = radicado    
    datos_basicos    = datos_radicados.datos_basicos("ENTRADA", "ENTRADA", datos_radicado, id_tarea)
    datos_extendidos = datos_radicados.datos_extendidos("ENTRADA", "ENTRADA", datos_radicado, id_tarea)
    datos_tercero    = datos_radicados.datos_tercero(datos_radicado)
    datos_copia      = datos_radicados.datos_copia(datos_radicado)

    # Creación del radicado
    datos_basicos["fecha_radicado"] = datetime.datetime.now()
    datos_basicos["atributos_"]     = datos_extendidos
    radicado    = crear_radicado(datos_basicos, datos)
    radicado_id = radicado["id"]

    # Genera pdf y notifica
    # Datos del radicado, todavia no se a indexado
    datos_completos = {}
    datos_completos.update(radicado)
    datos_completos.update(datos_basicos)
    datos_completos.update(datos_extendidos)
    datos_completos.update(datos_tercero)
    datos_completos.update(datos_copia)
    
    # Tarea celery general
    datos_cola = {
        "tarea_id"         : id_tarea,
        "radicado_tipo"    : "ENTRADA",
        "radicado_id"      : radicado_id,
        "radicado_id"      : radicado_id,
        "tercero_datos"    : datos_tercero,
        "archivos"         : archivos,
        "radicado"         : radicado,
        "nro_radicado"     : datos_radicado["nro_radicado"],
        "asunto"           : datos_radicado["asunto"],
        "copia_usuarios_id": datos_copia["copia_usuarios_id"],  
        "copia_grupos_id"  : datos_copia["copia_grupos_id"],  
        "copia_terceros_id": datos_copia["copia_terceros_id"],   
    }
    radicado_global.invoca_tercero_log_anexos_copias(datos_cola)

    pdf_notifica.pdf_notificacion("ENTRADA", datos_completos, id_tarea)

    # Indexa de ultimo
    indexar_datos.indexar_estructura("radicados_entrada", radicado_id, retardo=60)

    resultado =  {
        "accion" : accion,
        "estado" : "",
        "mensaje": "",
        "datos"  : radicado
    }

    return resultado 
 
# RADICACIóN Y PETICION 
from aplicacion.especificos.radicados.gestion import gestion

def radicar_peticion(accion, datos={}, archivos=[], id_tarea=""):
    # Radica documento
    radicado = radicar(accion, datos, archivos, id_tarea)
    datos["datos"]["id"] = radicado["datos"]["id"]
    datos["datos"]["radicado_id"] = radicado["datos"]["id"]

    # Es gestión o traslado a ventanilla
    archivos = []
    resuelto_inmediato = datos["datos"].get("resuelto_inmediato", "NO")
    repone_id          = datos["datos"].get("repone_id", None)
    if (resuelto_inmediato == "SI"):
        datos["datos"]["gestion_horas_dias"] = "DIAS"
        datos["datos"]["gestion_total_tiempo"] = 0
        datos["datos"]["atributos_"] = {}
        datos["datos"]["atributos_"]["finalizado"] = {
            "finalizado_por_id"    : datos['_usuario_']['id'],
            "finalizado_por_nombre": datos['_usuario_']['nombre'],
            "finalizado_en"        : datetime.datetime.now(),
            "finalizado_comentario": "RESUELTO EN PRIMER CONTACTO, " + datos["datos"].get("comentario_traslado", "")
        } 

    if repone_id in ["", None]:
        gestion.asigna_pqrs(accion, datos, archivos, id_tarea)
    else:
        gestion.asigna_reposicion(accion, radicado["datos"], repone_id, id_tarea)

    return radicado

def radicar_ventanilla(accion, datos={}, archivos=[], id_tarea=""):        
    # Radica documento
    radicado = radicar(accion, datos, archivos, id_tarea)
    datos["datos"]["id"] = radicado["datos"]["id"]
    datos["datos"]["radicado_id"] = radicado["datos"]["id"]

    # Es gestión o traslado a pqrs
    archivos = []
    gestion.asigna_ventanilla(accion, datos, archivos, id_tarea)

    return radicado