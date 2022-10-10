#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from aplicacion.especificos.configuracion_general import configuracion_general

from librerias.datos.sql  import sqalchemy_filtrar

# LISTADO DE PLANTILLA PARA RECORRIDOS 
def listado_plantillas_recorrido(accion, datos={}, archivos=[], id_tarea=""):
    datos = []
    # Si se radico via pagina WEB
    configuracion = configuracion_general.leer_registro_configuracion("radicacion_canales")
    if configuracion != None:
        # Lee canal de comunicaci�n        
        canales    = configuracion["datos"]     
        plantillas = canales.get("plantillas_recorridos", [])
        for plantilla_id in plantillas:
            filtros   = [ [ "id", "=", plantilla_id ] ]
            registros = sqalchemy_filtrar.filtrarOrdena(estructura="plantillas", filtros=filtros, ordenamientos=[])
            for registro in registros:
                datos.append({
                    "id"         : registro["id"],
                    "descripcion": registro["descripcion"]
                })



    resultado = {
        "plantillas": datos
    }    

    return resultado

def genera_recorrido(accion, datos={}, archivos=[], id_tarea=""):
    plantilla_datos = datos["datos"]
    print("genera_recorrido:")
    pprint.pprint(plantilla_datos)

    resultado = {
        "plantillas": {}
    }    

    return resultado