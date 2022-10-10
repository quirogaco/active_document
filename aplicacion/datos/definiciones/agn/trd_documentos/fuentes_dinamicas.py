#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales

from .usuarios import definicion

# Falta definirlo bien, no se usa todavia
def filtros_expediente(estructura, parametros):
    filtros = parametros["params"]["filtros"]
    usuario = parametros["params"]["_usuario_"]
    filtro  = [ "dependencia_id", "=", usuario["dependencia_id"] ]
    filtros.append(filtro) 
    
    # Vuelve a la estructura original
    estructura = definicion["estructura"]
    
    return estructura, parametros

globales.carga_estructura_dinamica("expedientes_documentos", filtros_expediente)