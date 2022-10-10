#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .grupo_usuarios import definicion

###############
# GRID BASICO #
###############
nombre  = adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"],  {'ancho': None})
estado_ = adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Grupos de usuarios", 
    atributos_especificos={"crear": "Crear Grupo"}
)
CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["grupo_usuarios_grid"] = grid_basico 

################
# FORMA BASICA #
################
nombre  = adaptadores_grid_forma.adaptador_campo_forma("nombre", definicion["campos"]["nombre"])
estado_ =  adaptadores_grid_forma.adaptador_campo_forma(
    "estado_", definicion["campos"]["estado_"], 
    {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]}
)

campos = [
    nombre,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Grupos de usuarios", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["grupo_usuarios_forma"] = forma_basico