#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.visuales   import adaptadores_grid_forma

from .rango_edad import definicion

###############
# GRID BASICO #
###############
codigo  =  adaptadores_grid_forma.adaptador_columna_grid("codigo",  definicion["campos"]["codigo"], {'ancho': None})
nombre  =  adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"], {'ancho': None})

columnas = [
    codigo,
    nombre
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Manejo de Rangos de Edad", 
    atributos_especificos={"crear": "Crear rango de edad"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["rango_edad_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo     =  adaptadores_grid_forma.adaptador_campo_forma("codigo",  definicion["campos"]["codigo"])
nombre     =  adaptadores_grid_forma.adaptador_campo_forma("nombre",  definicion["campos"]["nombre"])

campos = [
    codigo,
    nombre
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Rangos de Edad", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["rango_edad_forma"] = forma_basico