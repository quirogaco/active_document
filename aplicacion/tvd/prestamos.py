#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import datetime

from librerias.datos.sql import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from .indexar_datos      import indexar_prestamo

"""
def modificar_acceso(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    id     = datos["datos"]["id"]
    tvd_id = datos["tvd_id"]   
    datos_subserie = {
        "codigo"              : datos["datos"]["codigo"], 
        "nombre"              : datos["datos"]["nombre"],
        "gestion"             : datos["datos"]["gestion"],
        "central"             : datos["datos"]["central"],
        "eliminacion"         : datos["datos"]["eliminacion"],
        "seleccion"           : datos["datos"]["seleccion"],
        "conservacion"        : datos["datos"]["conservacion"],
        "micro_digitalizacion": datos["datos"]["micro_digitalizacion"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_subserie_tvd", id, datos_subserie)
    indexar("agn_subserie_tvd", resultado["id"], tvd_id)
    resultado["accion"] = accion    

    return resultado

def salvar_acceso(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["datos"].get("id", "")
    if dependencia_id == "":
        resultado = crear_acceso(accion, datos, archivo, acciones, id_tarea)
    else:
        resultado = modificar_acceso(accion, datos, archivo, acciones, id_tarea)
    
    return resultado

def borrar_acceso(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    id         = datos["datos"]["id"]
    tvd_id     = datos["tvd_id"]  
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_subserie_tvd", id)
    indexar("agn_subserie_tvd", resultado["id"], tvd_id)
    resultado["accion"] = accion
    
    return resultado
"""

def crear_prestamo(accion, datos={}, archivo=[], acciones={}, id_tarea=""):  
    usuario_id     = datos["_usuario_"]["id"]  
    expedientes_id = datos["datos"].get("expedientes_id", [])
    for expediente_id in expedientes_id:
        datos_prestamo = {
            "usuario_id"    : usuario_id,
            "expediente_id" : expediente_id,
            "motivo"        : datos["datos"]["motivo"],
            "archivo_etapa" : "CENTRAL",
            "estado"        : "SOLICITADO",
            "archivo_origen": "TVD",
            "fecha_peticion": datetime.datetime.now(),
            "vencido"       : "NO",
            "anotacion"     : "",
            "renovaciones"  : 0,
        }
        resultado = sqalchemy_insertar.insertar_registro_estructura("agn_prestamos_tvd", datos_prestamo)
        indexar_prestamo(expediente_id, resultado["id"])
    resultado["accion"] = accion  
    
    return resultado

def accion_prestamo(accion, datos={}, archivo=[], acciones={}, id_tarea=""):  
    prestamos_id = datos["datos"].get("prestamos_id", [])
    resultado    = {}
    for prestamo_id in prestamos_id:
        datos_prestamo = {
            "anotacion": datos["datos"]["anotacion"]
        }

        if (accion == "negar_prestamo"):
            datos_prestamo["estado"] = "NEGADO"

        if (accion == "entregar_prestamo"):
            datos_prestamo["estado"]            = "ENTREGADO"
            datos_prestamo["fecha_entrega"]     = datetime.datetime.now()

        if (accion == "recibir_prestamo"):
            datos_prestamo["estado"]           = "DEVUELTO"
            datos_prestamo["fecha_devolucion"] = datetime.datetime.now()

        prestamo   = sqalchemy_leer.leer_un_registro("agn_prestamos_tvd", prestamo_id)
        modificado = sqalchemy_modificar.modificar_un_registro("agn_prestamos_tvd", prestamo_id, datos_prestamo)
        indexar_prestamo(prestamo["expediente_id"], prestamo_id)

    resultado["accion"] = accion  
    
    return resultado