#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random  

from aplicacion.especificos.gestion import gestion_acciones
from .plantillas            import plantillas
from .roles                 import roles
from .configuracion_general import configuracion_general
from .consulta_radicados    import consulta
from .archivos_acciones     import acciones
from .reportes              import reportes
from .recorridos            import recorridos

acciones_funcion = {    
    # CONFIGURACION GENERAL
    "leer_radicacion_canales"  : configuracion_general.leer_radicacion_canales,
    "salvar_radicacion_canales": configuracion_general.salvar_radicacion_canales,    

    # PLANTILLA
    "crear_plantilla"    : plantillas.crear_plantilla,
    "modificar_plantilla": plantillas.modificar_plantilla,
    "borrar_plantilla"   : plantillas.borrar_plantilla,

    # ROLES
    "crear_role"    : roles.crear_role,
    "modificar_role": roles.modificar_role, 
    "borrar_role"   : roles.borrar_role,

    # CONSULTA RADICADOS
    "consultar_radicado"  : consulta.consultar_entrada,

    # ARCHIVOS ACCIONES
    "salvar_archivo": acciones.salvar_archivo,

    # ACCIONES DE GESTÓN
    "gestion_pdf_principal": gestion_acciones.gestion_pdf_principal,

    # REPORTES
    "crear_reporte"     : reportes.crear_reporte,
    "modificar_reporte" : reportes.modificar_reporte,
    "borrar_reporte"    : reportes.borrar_reporte,
    "leer_fuentes"      : reportes.leer_fuentes,
    "leer_campos_fuente": reportes.leer_campos_fuente,

    # RECORRIDOS
    "listado_plantillas_recorrido": recorridos.listado_plantillas_recorrido,
    "genera_recorrido"            : recorridos.genera_recorrido,
}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]

    print("")
    print("")
    print("------------------------------------------------")
    print('/ESPECIFICOS MANEJO -> acciones_ejecuta:', id_tarea) 
    print('datos:')
    pprint.pprint(datos)   
    print('archivos:', archivos)
    print("id tarea-AA", id_tarea)
    
    resultado = datos
    funcion   = acciones_funcion[accion]
    resultado = funcion(accion, datos, archivos, id_tarea)
    print("------------------------------------------------")
    print("")
    print("")

    retorna = datos
    retorna["datos"] = resultado

    return retorna