
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random 

from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones

from . import indexar_datos

# ARCHIVOS
def salvar_archivo(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    expediente_id  = datos['expediente_id']
    soporte        = datos["datos"]['soporte']    
    datos_archivos = {
        "tabla"         : "TVD", 
        "expediente_id" : expediente_id, 
        "detalle"       : datos["datos"]["detalle"], 
        "fecha_creacion": datos["datos"]["fecha_creacion"], 
        "fecha_funcion" : "RSA-MD5",
        "soporte"       : soporte
    }
    # Atributos por soporte
    datos_archivos["folios_fisicos"] = 0
    if soporte in ["DIGITALIZADO", "FISICO"]:
        datos_archivos["folios_fisicos"] = datos["datos"]["folios_fisicos"] 
    resultado = sqalchemy_insertar.insertar_registro_estructura("agn_documentos_trd", datos_archivos)
    # Indexa registros y anexos, falta indexar expediente
    indexar_datos.salvar_anexos("insertar", {"id":resultado["id"]}, archivos, id_tarea)
    indexar_datos.indexar("agn_documentos_trd", resultado["id"], expediente_id)    
    
    resultado["accion"] = accion    

    return resultado

def modificar_expediente(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
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

def borrar_expediente(accion, datos={}, archivos=[], acciones={}, id_tarea=""):
    expediente_id = datos["datos"]["id"]
    resultado  = sqalchemy_borrar.borrar_un_registro("agn_expedientes_trd", expediente_id)
    elastic_operaciones.eliminar_registro("agn_expedientes_trd", expediente_id)
    resultado["accion"] = accion
    
    return resultado