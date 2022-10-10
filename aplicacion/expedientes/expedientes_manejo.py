#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, datetime, random 

from librerias.datos.sql         import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic     import elastic_operaciones
from librerias.flujos            import flujos_insertar_sql
from librerias.utilidades        import basicas  
from librerias.datos.estructuras import estructura_operaciones

from aplicacion.trd import exportar_log
from . import expediente
from . import archivo_base
from . import transferencias
from . import fuid
from . import hoja_control
from . import indice_electronico_excel

acciones_funcion = {
    # EXPEDIENTES
    "crear_expediente"    : expediente.crear_expediente,
    "modificar_expediente": expediente.modificar_expediente,
    "borrar_expediente"   : expediente.borrar_expediente,
    "cerrar_expediente"   : expediente.cerrar_expediente,
    "abrir_expediente"    : expediente.abrir_expediente,    
    "consulta_expediente" : expediente.consulta_expediente,    
    "expediente_indice"   : expediente.expediente_indice,
    "indice_electronico_excel": indice_electronico_excel.imprimir_indice,
    "exportar_expediente_log" : exportar_log.exportar_log,
    "actualiza_caja_anotacion": expediente.actualiza_caja_anotacion,
    "permite_eliminar": expediente.permite_eliminar,
    "no_permite_eliminar": expediente.no_permite_eliminar,
    "disposicion_final": expediente.disposicion_final,
    "imprimir_control"        : hoja_control.imprimir_control,
    "test"                : expediente.test,

    # ARCHIVOS
    "salvar_archivo"   : archivo_base.salvar_archivo,
    "modificar_archivo": archivo_base.modificar_archivo,
    "borrar_archivo": archivo_base.borrar_archivo,

    # TRANSFERENCIAS
    "crear_transferencia"     : transferencias.crear_transferencia,
    "modificar_transferencia" : transferencias.modificar_transferencia,
    "borrar_transferencia"    : transferencias.borrar_transferencia,
    "recibir_transferencia"   : transferencias.recibir_transferencia,
    "devolver_transferencia"  : transferencias.devolver_transferencia,
    "comentario_transferencia": transferencias.comentario_transferencia, 
    "exportar_transferencia_log": exportar_log.exportar_log,

    # FUID
    "imprimir_fuid" : fuid.imprimir_fuid,
}

import time
def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]

    print("")
    print("")
    print("------------------------------------------------")
    print('EXPEDIENTES MANEJO -> acciones_ejecuta:', id_tarea) 
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
