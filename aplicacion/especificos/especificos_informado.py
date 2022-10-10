#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random  

from librerias.datos.sql     import sqalchemy_modificar
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes      import indexar_datos
from aplicacion.comunes      import manejo_archivos

def ocultar_informados(accion, datos={}, archivos=[], id_tarea=""):
    informacion = {
        "estado": "OCULTADO"
    }
    for copia_id in datos['ocultar']:        
        resultado   = sqalchemy_modificar.modificar_un_registro("copias", copia_id, informacion)    
        elastic_operaciones.indexar_registro("copias", copia_id)

    return resultado

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    resultado = ocultar_informados("", datos, archivos, id_tarea)
    
    return resultado