#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

import configuracion_base

from librerias.datos.elastic import elastic_operaciones
from librerias.datos.sql import (
    sqalchemy_leer,
    sqalchemy_modificar
)
from librerias.datos.base import globales

conexion = globales.lee_conexion_elastic("base")

def actualizar():
    radicados = sqalchemy_leer.leer_todos(
        "base", 
        "radicados_entrada", 
        desde=0, 
        hasta=10000
    )
    #pprint.pprint(radicados[0])
    print("")

    for radicado in radicados:
        atributos_ = radicado["atributos_"]
        if atributos_["clase_radicado"] in ["VENTANILLA", "PQRDS"]:
            print("CAMBIA-->")
            pprint.pprint(radicado)
            atributos_["clase_radicado"] = "PQRSD"
            nuevos_datos = {
                "atributos_": atributos_
            }
            sqalchemy_modificar.modificar_un_registro(
                "radicados_entrada", 
                radicado["id"], 
                nuevos_datos
            )

actualizar()