#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pprint, datetime, random 

import pandas as pd

from . import valida_data
from . import crea_data

from librerias.datos.sql         import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic     import elastic_operaciones
from librerias.flujos            import flujos_insertar_sql
from librerias.utilidades        import basicas  
from librerias.datos.estructuras import estructura_operaciones
from . import logs

def preparacion_inicial(df):
    mensajes = valida_data.validar(df)

    return mensajes

# TRD
def crear_trd(accion, datos={}, archivo=[], id_tarea=""): 
    _datos = {
        "ubicaciones_gestion": datos["datos"]["ubicaciones_gestion"],
    }

    # crear TRD 
    datos_trd = {
        "fondo_id": datos["datos"]["fondo_id"], 
        "nombre": datos["datos"]["nombre"],   
        "sigla": datos["datos"]["sigla"],        
        "version": datos["datos"]["version"],
        "version": datos["datos"]["version"],
        "territorial_codigo": datos["datos"]["territorial_codigo"],
        "datos": _datos,        
        "estado_": datos["datos"]["estado_"]
    }    
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_trd", datos_trd)

    # importar TRD
    if (len(archivo) > 0):
        df = pd.read_excel(archivo[0]["nombre_completo"])
        mensajes = preparacion_inicial(df)
        print(df.to_string())
        estructura = crea_data.prepare_estructura(df)
        crea_data.salvar_data(estructura, resultado["id"])

    # indexar y logs
    elastic_operaciones.indexar_registro("agn_trd", resultado["id"])    
    logs.log_trd("agn_trd", resultado["id"], "CREACIÓN DE TRD", "CREACION", id_tarea)     

    #resultado = {}
    resultado["accion"] = accion   

    return resultado

def modificar_trd(accion, datos={}, archivo=[], id_tarea=""):
    print("MODIFICAR:")
    pprint.pprint(datos)
    trd_id = datos["datos"]["id"]
    _datos = {
        "ubicaciones_gestion": datos["datos"]["ubicaciones_gestion"]
    }
    datos_trd = {
        "fondo_id": datos["datos"]["fondo_id"], 
        "nombre": datos["datos"]["nombre"],   
        "sigla": datos["datos"]["sigla"],        
        "version": datos["datos"]["version"],
        "territorial_codigo": datos["datos"]["territorial_codigo"],
        "territorial_nombre": datos["datos"]["territorial_nombre"],
        "datos": _datos,
        "estado_": datos["datos"]["estado_"]
    }
    print("MODIFICAR datos_trd:")
    pprint.pprint(datos_trd)
    resultado = sqalchemy_modificar.modificar_un_registro(
        "agn_trd", 
        trd_id, 
        datos_trd
    )
    elastic_operaciones.indexar_registro("agn_trd", resultado["id"])
    logs.log_trd(
        "agn_trd", 
        resultado["id"], 
        "MODIFICACIÓN DE TRD", 
        "MODIFICACION", 
        id_tarea
    ) 
    
    resultado["accion"] = accion   
    #resultado = {}

    return resultado

def borrar_trd(accion, datos={}, archivo=[], id_tarea=""):
    trd_id = datos["datos"]["id"]
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_trd", trd_id)
    elastic_operaciones.eliminar_registro("agn_trd", trd_id)
    logs.log_trd("agn_trd", resultado["id"], "ELIMINACIÓN DE TRD", "BORRADO", id_tarea)

    resultado["accion"] = accion
    
    return resultado