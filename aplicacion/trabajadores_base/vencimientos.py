#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, builtins, datetime

from librerias.datos.elastic import elastic_operaciones
from librerias.datos.sql import sqalchemy_leer
from librerias.datos.base import globales

from . import crea_celery_app

generales_app = crea_celery_app.aplicacion_celery('conversion_pdf', 'conversion_pdf')

# Convierte archivos pdf a Pdf/a y Ocr
from aplicacion.documentos.conversion import tarea_convertir
@generales_app.task(name='vencimientos')
def vencimiento_procesos(**parametros):
    conexion = globales.lee_conexion_elastic("base")
    print("")
    print("")
    print("------------------------------------------")
    print("INDEXAR PROCESOS", datetime.datetime.now())
    estructura = "peticiones"
    modelo = globales.lee_modelo_elastic(estructura)
    total = sqalchemy_leer.contar_registros("base", estructura)
    paso = 100
    for posicion in range(0, total, paso):
        print("")
        print("INDEXAR:", posicion, (posicion+paso), total, end=' - ')
        resultado = sqalchemy_leer.leer_rango(
            "base", 
            estructura, 
            desde=posicion, 
            hasta=(posicion+paso), 
            retornar="diccionario"
        )
        print("INDEXAR LEE:", posicion, (posicion+paso), total, end=' - ')
        bulk = elastic_operaciones.bulk_indexar(
            conexion, 
            modelo["modelo"], 
            modelo["indice"], 
            resultado
        )
        print("INDEXAR INDEXA:", posicion, (posicion+paso), total, end=' - ')

    print("")
    
    print("RESULTADO>>>" + estructura, total)    
    print("")
