#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import datetime

from librerias.datos.sql import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar

from aplicacion.trd       import logs
from .indexar_datos       import indexar_prestamo

def crear_prestamo(accion, datos={}, archivo=[], id_tarea=""):  
    usuario_id     = datos["_usuario_"]["id"]  
    expedientes_id = datos["datos"].get("expedientes_id", [])
    for expediente_id in expedientes_id:
        datos_prestamo = {
            "usuario_id"    : usuario_id,
            "expediente_id" : expediente_id,
            "motivo"        : datos["datos"]["motivo"],
            "archivo_etapa" : "GESTION",
            "estado"        : "SOLICITADO",
            "archivo_origen": "TRD",
            "fecha_peticion": datetime.datetime.now(),
            "vencido"       : "NO",
            "anotacion"     : "",
            "renovaciones"  : 0,
        }
        resultado = sqalchemy_insertar.insertar_registro_estructura("agn_prestamos_trd", datos_prestamo)
        indexar_prestamo(expediente_id, resultado["id"])
        logs.log_trd("agn_expedientes_trd", expediente_id, "SOLICITUD PRESTAMO", "SOLICITUD", id_tarea) 

    resultado["accion"] = accion  
    
    return resultado

def accion_prestamo(accion, datos={}, archivo=[], id_tarea=""):  
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

        prestamo = sqalchemy_leer.leer_un_registro("agn_prestamos_trd", prestamo_id)
        modificado = sqalchemy_modificar.modificar_un_registro("agn_prestamos_trd", prestamo_id, datos_prestamo)
        indexar_prestamo(prestamo["expediente_id"], prestamo_id)
        logs.log_trd("agn_expedientes_trd", prestamo["expediente_id"], ("PRESTAMO " + datos_prestamo["estado"]), datos_prestamo["estado"], id_tarea) 

    resultado["accion"] = accion  
    
    return resultado