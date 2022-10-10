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

def crea_flujo(ruta="base", estructura="", datos={}, opciones={}):
    flujo_data = {
        "parametros": {
            "ruta"      : ruta,
            "estructura": estructura,
            "datos"     : datos,
            "opciones"  : opciones,
            "id_tarea"  : basicas.uuidTexto()
        },
        "resultados": {
            "datos"  : None,
            "errores": None
        }
    }
    with Flow("indexar_registro_sql") as flujoGeneral:
        ultimo_resultado = estructura_tareas_sql.indexar_registro_SQL(flujo_data)
        
    return flujoGeneral, ultimo_resultado

def ejecutar(ruta="base", estructura="", datos={}):    
    flujoGeneral, ultimo_resultado = crea_flujo(ruta, estructura, datos)

    flujo_estado = flujoGeneral.run()        
    resultado    = flujos_utilidades.estadoFlujo(flujoGeneral, flujo_estado, ultimo_resultado)
    
    return resultado