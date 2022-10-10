#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, datetime, random 

from librerias.datos.sql         import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic     import elastic_operaciones
from librerias.flujos            import flujos_insertar_sql
from librerias.utilidades        import basicas  
from librerias.datos.estructuras import estructura_operaciones

# Definición
from . import trd
from . import dependencia
from . import serie
from . import subserie
from . import tipo
from . import exportar
from . import exportar_log

# Accesos
from . import accesos

# Prestamos
from . import prestamos

def borrar_trd(accion, datos={}, archivo=[], id_tarea=""):
    trd_id = datos["datos"]["id"]
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_trd", trd_id)
    elastic_operaciones.eliminar_registro("agn_trd", trd_id)
    resultado["accion"] = accion
    
    return resultado

acciones_funcion = {
    # TRD
    "crear_trd"         : trd.crear_trd,
    "modificar_trd"     : trd.modificar_trd,
    "borrar_trd"        : trd.borrar_trd,
    "exportar_trd"      : exportar.exportar,
    "exportar_trd_log"  : exportar_log.exportar_log,

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

    # TIPO
    "salvar_tipo"   : tipo.salvar_tipo,
    "modificar_tipo": tipo.salvar_tipo,
    "borrar_tipo"   : tipo.borrar_tipo,

    # ACCESOS
    "salvar_acceso"   : accesos.salvar_acceso,

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
    print('/TRD MANEJO -> acciones_ejecuta:', id_tarea) 
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
