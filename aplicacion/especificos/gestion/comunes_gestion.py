#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, datetime, builtins, base64

from librerias.datos.sql import sqalchemy_modificar, sqalchemy_leer
from librerias.datos.elastic import elastic_operaciones

from aplicacion.comunes import indexar_datos
from aplicacion.especificos.archivos_acciones import acciones

# Modifica registro de gestión 
def modifica_peticion(peticion_id, datos):
    sqalchemy_modificar.modificar_un_registro("peticiones", peticion_id, datos)
    elastic_operaciones.indexar_registro("peticiones", peticion_id)

    gestion = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)
    if gestion["origen_tipo"] == "ENTRADA":
        indexar_datos.indexar_estructura(
            "radicados_entrada", 
            gestion["origen_id"], 
            retardo=120
        )


def peticion_real(peticion_id):
    peticion = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)  
    if (peticion["colaborativa"] not in ["", None]):
        peticion_id = peticion["colaborativa"]

    return peticion_id

def anexar_gestion(accion, datos={}, archivo=[], id_tarea=""):
    peticiones_id = datos["peticiones"]  
    peticion_id   = peticion_real(peticiones_id[0])  
    datos_archivo = {
        "datos": {
            "estructura": "peticiones",
            "origen_id" : peticion_id,
            "relacion"  : "anexos"
        }
    }
    acciones.salvar_archivo("insertar", datos_archivo, archivo, id_tarea)

    return {}