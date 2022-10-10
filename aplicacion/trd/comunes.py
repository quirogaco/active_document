#!/usr/bin/python
# -*- coding: UTF-8 -*-

from librerias.datos.sql   import sqalchemy_filtrar 

# Recuperar accesos
def recuperar_accesos(elemento_tipo, elemento_id):
    accesos_datos = {}
    filtros       = [ [ "elemento_tipo", "=", elemento_tipo ], [ "elemento_id", "=", elemento_id ] ]
    accesos       = sqalchemy_filtrar.filtrarOrdena(estructura="agn_accesos_trd", filtros=filtros, ordenamientos=[])
    for acceso in accesos:
        accesos_datos["autorizacion"] = acceso["autorizacion"]
        accesos_datos["autorizados"]  = acceso["autorizados"]

    return accesos_datos