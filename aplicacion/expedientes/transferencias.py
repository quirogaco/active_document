#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pprint, datetime, random, base64

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar, sqalchemy_filtrar 
from librerias.datos.elastic import elastic_operaciones
from librerias.datos.base    import globales
from librerias.datos.sql     import sqalchemy_comunes
from librerias.utilidades    import basicas 
from aplicacion.trd          import logs

# TRD
def crear_transferencia(accion, datos={}, archivo=[], id_tarea=""):
    datos_transferencia = {
        "fecha_creacion"     : datetime.datetime.now(),
        "usuario_id"         : datos["_usuario_"]["id"],
        "dependencia_id"     : datos["datos"]["dependencia_id"], 
        "fecha_transferencia": datos["datos"]["fecha_transferencia"]
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_transferencias_trd", datos_transferencia)
    elastic_operaciones.indexar_registro("agn_transferencias_trd", resultado["id"])
    logs.log_trd("agn_transferencias_trd", resultado["id"], "CREACION", "CREACIÓN DE TRANSFERENCIA", id_tarea) 
    resultado["accion"] = accion    

    return resultado

def modificar_transferencia(accion, datos={}, archivo=[], id_tarea=""):
    transferencia_id = datos["datos"]["id"]
    datos_transferencia = {
        "fecha_creacion"     : datetime.datetime.now(),
        "usuario_id"         : datos["_usuario_"]["id"],
        "dependencia_id"     : datos["datos"]["dependencia_id"], 
        "fecha_transferencia": datos["datos"]["fecha_transferencia"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_transferencias_trd", transferencia_id, datos_transferencia)
    elastic_operaciones.indexar_registro("agn_transferencias_trd", resultado["id"])
    logs.log_trd("agn_transferencias_trd", resultado["id"], "MODIFICACION", "MODIFICACIÓN DE TRANSFERENCIA", id_tarea) 
    resultado["accion"] = accion    

    return resultado

def borrar_transferencia(accion, datos={}, archivo=[], id_tarea=""):
    transferencia_id = datos["datos"]["id"]
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_transferencias_trd", transferencia_id)
    elastic_operaciones.eliminar_registro("agn_transferencias_trd", transferencia_id)
    resultado["accion"] = accion
    
    return resultado

from . import fuid
def recibir_transferencia(accion, datos={}, archivo=[], id_tarea=""):
    transferencia_id = datos["datos"]["transferencia_id"][0]
    datos_transferencia = {
        "estado": "RECIBIDO" 
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_transferencias_trd", transferencia_id, datos_transferencia)
    logs.log_trd("agn_transferencias_trd", resultado["id"], "RECIBIR", "RECIBIR TRANSFERENCIA", id_tarea) 
    elastic_operaciones.indexar_registro("agn_transferencias_trd", resultado["id"])

    # TRANSFERIR EXPEDIENTE
    EXPEDIENTE_CLASE    = globales.lee_clase("agn_expedientes_trd")
    sesion              = sqalchemy_comunes.nuevaSesion("base") 
    filtros             = (EXPEDIENTE_CLASE.estado == "CERRADO")
    expedientes         = sesion.query(EXPEDIENTE_CLASE).filter( filtros ).all()
    for expediente in expedientes:
        datos = {
            "transferencia_id": transferencia_id,
            "expediente_id"   : expediente.id
        }
        transferencia = sqalchemy_insertar.insertar_registro_estructura("agn_transferencias_exp_trd", datos)        
        elastic_operaciones.indexar_registro("agn_transferencias_exp_trd", transferencia["id"])
        elastic_operaciones.indexar_registro("agn_expedientes_trd", expediente.id)
        logs.log_trd("agn_expedientes_trd", expediente.id, "TRANSFERENCIA", "TRANSFERENCIA PRIMARIA", id_tarea) 

    sesion.close()

    # Imprime fuid
    ordenar         = [ [ "descendente", "creado_en_" ] ]
    filtros         = [ [ "estado", "=", "CERRADO"] ]
    expedientes     = sqalchemy_filtrar.filtrarOrdena(estructura="agn_expedientes_trd", filtros=filtros, ordenamientos=ordenar)
    nombre_archivo  = fuid.genera_excel(expedientes)
    nombre_byte     = nombre_archivo.encode('ascii')
    nombre_64       = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')
    
    resultado["accion"]         = accion  
    resultado["nombre_archivo"] = nombre_64_texto

    sale = {
        "nombre_archivo": nombre_64_texto
    }

    # Mueve expediente
    for expediente in expedientes:
        actualiza = {
            "etapa"    : "CENTRAL",
            "ubicacion": "CENTRAL",
            #"estado"   : "ABIERTO"
        }
        resultado = sqalchemy_modificar.modificar_un_registro("agn_expedientes_trd", expediente["id"], actualiza)
        elastic_operaciones.indexar_registro("agn_expedientes_trd", expediente["id"])

    print("SALE:", sale)

    return sale

def devolver_transferencia(accion, datos={}, archivo=[], id_tarea=""):
    transferencia_id = datos["datos"]["transferencia_id"][0]
    datos_transferencia = {
        "estado": "DEVUELTO" 
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_transferencias_trd", transferencia_id, datos_transferencia)
    logs.log_trd("agn_transferencias_trd", transferencia_id, "DEVOLVER", "DEVOLVER TRANSFERENCIA", id_tarea) 
    elastic_operaciones.indexar_registro("agn_transferencias_trd", resultado["id"])
    resultado["accion"] = accion    

    return resultado

def comentario_transferencia(accion, datos={}, archivo=[], id_tarea=""):
    datos            = datos["datos"]
    transferencia_id = datos["transferencia_id"]
    actualiza        = {
        "detalle": datos["detalle"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_transferencias_trd", transferencia_id, actualiza)
    logs.log_trd("agn_transferencias_trd", transferencia_id, "ANOTAR", ("ANOTACION:" + datos["detalle"]), id_tarea) 
    elastic_operaciones.indexar_registro("agn_transferencias_trd", resultado["id"])
    
    resultado["accion"] = accion

    return resultado