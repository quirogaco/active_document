#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import logging

import prefect
from prefect import Flow

logger = prefect.context.get("logger")
logger.setLevel(logging.CRITICAL)
#logger.setLevel(logging.DEBUG)

from librerias.utilidades        import basicas 
from librerias.datos.base        import globales 
from librerias.flujos            import flujos_utilidades
from librerias.datos.estructuras import estructura_tareas_sql

def crea_flujo(ruta="base", estructura="", datos={}, opciones={}, id_tarea=  None):
    flujo_data = {
        "parametros": {
            "ruta"      : ruta,
            "estructura": estructura,
            "datos"     : datos,
            "opciones"  : opciones,
            "id_tarea"  : id_tarea
        },
        "resultados": {
            "datos"  : None,
            "errores": None
        }
    }
    with Flow("indexar__elimina_registro_sql") as flujoGeneral:
        ultimo_resultado = estructura_tareas_sql.indexar_elimina_registro_SQL(flujo_data)
        
    return flujoGeneral, ultimo_resultado

def ejecutar(ruta="base", estructura="", datos={}, id_tarea=None): 
    flujoGeneral, ultimo_resultado = crea_flujo(ruta, estructura, datos, {}, id_tarea)

    flujo_estado = flujoGeneral.run()        
    resultado    = flujos_utilidades.estadoFlujo(flujoGeneral, flujo_estado, ultimo_resultado)
    
    return resultado