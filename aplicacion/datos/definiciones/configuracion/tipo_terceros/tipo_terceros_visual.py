#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .tipo_terceros import definicion

###############
# GRID BASICO #
###############
nombre  = adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"],  {'ancho': None})
tipo    = adaptadores_grid_forma.adaptador_columna_grid("tipo",    definicion["campos"]["tipo"],    {'ancho': None})
estado_ = adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    nombre,
    tipo,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Tipos de Tercero", 
    atributos_especificos={"crear": "Crear Tipo de Tercero"}
)
CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["tipo_terceros_grid"] = grid_basico 

################
# FORMA BASICA #
################
nombre  = adaptadores_grid_forma.adaptador_campo_forma("nombre", definicion["campos"]["nombre"])
tipo    =  adaptadores_grid_forma.adaptador_campo_forma(
    "tipo", definicion["campos"]["tipo"], 
    {'tipoeditor': 'radio', "elementos": ["JURIDICA", "NATURAL"]}
)
estado_ =  adaptadores_grid_forma.adaptador_campo_forma(
    "estado_", definicion["campos"]["estado_"], 
    {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]}
)

campos = [
    nombre,
    tipo,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Tipos de Terceross", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["tipo_terceros_forma"] = forma_basico