#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.sql import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_filtrar 
from .indexar_datos      import indexar_acceso

def crear_acceso(accion, datos={}, archivo=[], acciones={}, id_tarea=""):  
    elemento_tipo = datos["datos"]["padre_tipo"]  
    elemento_id   = datos["datos"]["padre_id"]
    autorizados = {
        "usuarios": datos["datos"].get("usuarios", []),
        "grupos"  : datos["datos"].get("grupos", [])   
    }
    datos_acceso =  {
        "elemento_tipo": elemento_tipo,
        "elemento_id"  : elemento_id,
        "autorizacion" : datos["datos"]["autorizacion"],
        "autorizados"  : autorizados
    }

    filtros       = [ [ "elemento_tipo", "=", elemento_tipo ], [ "elemento_id", "=", elemento_id ] ]
    accesos       = sqalchemy_filtrar.filtrarOrdena(estructura="agn_accesos_trd", filtros=filtros, ordenamientos=[])
    if len(accesos) == 0:
        resultado = sqalchemy_insertar.insertar_registro_estructura("agn_accesos_trd", datos_acceso)
    else:
        resultado = sqalchemy_modificar.modificar_un_registro("agn_accesos_trd", accesos[0]["id"], datos_acceso)
    
    indexar_acceso(datos["datos"]["padre_tipo"], datos["datos"]["padre_id"], resultado["id"])
    resultado["accion"] = accion  
    
    return resultado

def salvar_acceso(accion, datos={}, archivo=[], id_tarea=""):
    resultado = crear_acceso(accion, datos, archivo, id_tarea)
    
    return resultado