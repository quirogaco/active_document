#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .acciones import definicion

###############
# GRID BASICO #
###############
codigo  =  adaptadores_grid_forma.adaptador_columna_grid("codigo",  definicion["campos"]["codigo"],  {'ancho': 180})
nombre  =  adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"],  {'ancho': 600})
estado_ =  adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': 180})

columnas = [
    codigo,
    nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Manejo de Acciones del Sistema", 
    atributos_especificos={"crear": "Crear Acción"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["acciones_sistema_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo     =  adaptadores_grid_forma.adaptador_campo_forma("codigo",  definicion["campos"]["codigo"])
nombre     =  adaptadores_grid_forma.adaptador_campo_forma("nombre",  definicion["campos"]["nombre"])
estado_    =  adaptadores_grid_forma.adaptador_campo_forma("estado_", definicion["campos"]["estado_"], {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]})

campos = [
    codigo,
    nombre,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Acciones del Sistema", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["acciones_sistema_forma"] = forma_basico