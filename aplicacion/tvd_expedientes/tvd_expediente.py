#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random 

from librerias.datos.sql         import sqalchemy_modificar, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic     import elastic_operaciones
from librerias.flujos            import flujos_insertar_sql
from librerias.utilidades        import basicas  
from librerias.datos.estructuras import estructura_operaciones

# TVD
def crear_expediente(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    datos_expediente = {
        "tabla"      : "TVD", 
        "serie_id"   : datos["datos"]["serie_id"], 
        "subserie_id": datos["datos"]["subserie_id"], 
        "nombre"     : datos["datos"]["nombre"]        
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_expedientes_trd", datos_expediente)
    elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])
    resultado["accion"] = accion    

    return resultado

def modificar_expediente(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    expediente_id = datos["datos"]["id"]
    datos_expediente = {
        "serie_id"          : datos["datos"]["serie_id"], 
        "subserie_id"       : datos["datos"]["subserie_id"], 
        "nombre"            : datos["datos"]["nombre"]
    }
    resultado = sqalchemy_modificar.modificar_un_registro("agn_expedientes_trd", expediente_id, datos_expediente)
    elastic_operaciones.indexar_registro("agn_expedientes_trd", resultado["id"])
    resultado["accion"] = accion    

    return resultado

def borrar_expediente(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    expediente_id = datos["datos"]["id"]
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_expedientes_trd", expediente_id)
    elastic_operaciones.eliminar_registro("agn_expedientes_trd", expediente_id)
    resultado["accion"] = accion
    
    return resultado