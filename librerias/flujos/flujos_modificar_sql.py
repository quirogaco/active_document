#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint
import logging

import prefect
from prefect import Flow

logger = prefect.context.get("logger")
#logger.setLevel(logging.CRITICAL)
logger.setLevel(logging.DEBUG)

from librerias.utilidades        import basicas 
from librerias.datos.validacion  import valida_tareas
from librerias.flujos            import flujos_utilidades
from librerias.datos.estructuras import estructura_tareas
from librerias.datos.estructuras import estructura_tareas_sql

def crea_flujo(ruta="base", estructura="", datos={}, opciones={}, id_tarea=None):
    flujo_data = {
        "parametros": {
            "ruta"      : ruta,
            "estructura": estructura,
            "datos"     : datos,
            "opciones"  : opciones,
            "accion"    : 'modificar',
            "id_tarea"  : id_tarea
        },
        "resultados": {
            "datos"  : None,
            "errores": None
        }
    }
    with Flow("modificar_registro_sql") as flujoGeneral:
        flujo_data       = estructura_tareas.unifica_datos(flujo_data)
        flujo_data       = valida_tareas.valida_datos_tarea(flujo_data)   
        flujo_data       = estructura_tareas.validas_duplicados_tarea(flujo_data)     
        # Deberia existir una que elmine todos los datos valiados que no esten en los modificados
        flujo_data       = estructura_tareas.prepara_operaciones(flujo_data)
        flujo_data       = estructura_tareas.armar_estructura_tarea(flujo_data)
        ultimo_resultado = estructura_tareas_sql.modificar_registro_SQL(flujo_data) 
        
    return flujoGeneral, ultimo_resultado

def ejecutar(ruta="base", estructura="", datos={}, id_tarea=None): 
    flujoGeneral, ultimo_resultado = crea_flujo(ruta, estructura, datos, id_tarea=id_tarea)

    flujo_estado = flujoGeneral.run()        
    resultado    = flujos_utilidades.estadoFlujo(flujoGeneral, flujo_estado, ultimo_resultado)
    
    return resultado