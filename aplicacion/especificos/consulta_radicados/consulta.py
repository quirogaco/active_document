#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.sql      import sqalchemy_filtrar

def consultar_entrada(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    print("ENTRADA - >consultar_radicado:", accion)
    pprint.pprint(datos)
    nro_radicado = datos["datos"]["nro_radicado"]
    filtros      = [ [ "nro_radicado", "=", nro_radicado ] ]
    print("filtros:", filtros)
    radicados    = sqalchemy_filtrar.filtrarOrdena(estructura="radicados_entrada", filtros=filtros, ordenamientos=[])

    #pprint.pprint(radicados)

    mensaje = ""
    datos   = {}
    if len(radicados) == 0:
        mensaje = "NUMERO DE RADICADO INVALIDO"
    else:
        datos = radicados[0]
        if datos["gestion_estado"] == None:
            datos["gestion_estado"] = "PENDIENTE POR ASIGNAR"

    resultado =  {
        "accion" : accion,
        "mensaje": mensaje,
        "datos"  : datos
    }
    
    return resultado