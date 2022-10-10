#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random 

from librerias.datos.sql         import sqalchemy_borrar
from librerias.datos.elastic     import elastic_operaciones

# Definición
from . import tvd
from . import dependencia
from . import serie
from . import subserie

# Accesos
from . import accesos

# Prestamos
from . import prestamos

def borrar_tvd(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    tvd_id = datos["datos"]["id"]
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_tvd", tvd_id)
    elastic_operaciones.eliminar_registro("agn_tvd", tvd_id)
    resultado["accion"] = accion
    
    return resultado

acciones_funcion = {
    # tvd
    "crear_tvd"         : tvd.crear_tvd,
    "modificar_tvd"     : tvd.modificar_tvd,
    "borrar_tvd"        : tvd.borrar_tvd,

    # DEPENDENCIA
    "salvar_dependencia"   : dependencia.salvar_dependencia,
    "modificar_dependencia": dependencia.salvar_dependencia,
    "borrar_dependencia"   : dependencia.borrar_dependencia,

    # SERIE
    "salvar_serie"   : serie.salvar_serie,
    "modificar_serie": serie.salvar_serie,
    "borrar_serie"   : serie.borrar_serie,

    # SUBSERIE
    "salvar_subserie"   : subserie.salvar_subserie,
    "modificar_subserie": subserie.salvar_subserie,
    "borrar_subserie"   : subserie.borrar_subserie,

    # ACCESOS
    "salvar_acceso"   : accesos.salvar_acceso,
    "modificar_acceso": accesos.salvar_acceso,
    "borrar_acceso"   : accesos.borrar_acceso,

    # PRSESTAMOS
    "crear_prestamo"   : prestamos.crear_prestamo,
    "negar_prestamo"   : prestamos.accion_prestamo,
    "entregar_prestamo": prestamos.accion_prestamo,
    "recibir_prestamo" : prestamos.accion_prestamo
}

import time
def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]

    print("")
    print("")
    print("------------------------------------------------")
    print('/tvd MANEJO -> acciones_ejecuta:', id_tarea) 
    print('datos:')
    pprint.pprint(datos)   
    print('archivos:', archivos)
    
    resultado = datos
    funcion   = acciones_funcion[accion]
    resultado = funcion(accion, datos, archivos, id_tarea)
    print("------------------------------------------------")
    print("")
    print("")

    retorna = datos
    retorna["datos"] = resultado

    return retorna
