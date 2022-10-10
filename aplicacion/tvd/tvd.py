#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random 

from librerias.datos.sql         import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic     import elastic_operaciones

# TVD
def crear_tvd(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    datos_tvd = {
        "fondo_id"          : datos["datos"]["fondo_id"], 
        "nombre"            : datos["datos"]["nombre"],   
        "sigla"             : datos["datos"]["sigla"],        
        "periodo"           : datos["datos"]["periodo"],
        "territorial_codigo": datos["datos"]["territorial_codigo"],
        "territorial_nombre": datos["datos"]["territorial_nombre"],
        "fecha_periodo"     : datos["datos"]["fecha_periodo"]
        #"estado_"           : datos["datos"]["estado_"]
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_tvd", datos_tvd)
    elastic_operaciones.indexar_registro("agn_tvd", resultado["id"])
    resultado["accion"] = accion    

    return resultado

def modificar_tvd(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    tvd_id = datos["datos"]["id"]
    datos_tvd = {
        "fondo_id"          : datos["datos"]["fondo_id"], 
        "nombre"            : datos["datos"]["nombre"],   
        "sigla"             : datos["datos"]["sigla"],        
        "periodo"           : datos["datos"]["periodo"],
        "territorial_codigo": datos["datos"]["territorial_codigo"],
        "territorial_nombre": datos["datos"]["territorial_nombre"],
        #"estado_"           : datos["datos"]["estado_"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_tvd", tvd_id, datos_tvd)
    elastic_operaciones.indexar_registro("agn_tvd", resultado["id"])
    resultado["accion"] = accion    

    return resultado

def borrar_tvd(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    tvd_id = datos["datos"]["id"]
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_tvd", tvd_id)
    elastic_operaciones.eliminar_registro("agn_tvd", tvd_id)
    resultado["accion"] = accion
    
    return resultado