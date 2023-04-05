#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .roles import definicion

###############
# GRID BASICO #
###############
codigo             = adaptadores_grid_forma.adaptador_columna_grid("codigo",  definicion["campos"]["codigo"], {'ancho': None})
nombre             = adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"], {'ancho': None})
estado_            = adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    codigo,
    nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Roles", 
    atributos_especificos={"crear": "Crear Role"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["roles_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo       = adaptadores_grid_forma.adaptador_campo_forma("codigo",  definicion["campos"]["codigo"])
nombre       = adaptadores_grid_forma.adaptador_campo_forma("nombre",  definicion["campos"]["nombre"])
opciones_ids = adaptadores_grid_forma.adaptador_campo_forma(
    "opciones_ids", 
    definicion["campos"]["opciones_ids"], 
    {
        "tipoeditor"        : 'tag', 
        "fuente"            : "opciones_sistema",
        "busqueda_expresion": "titulo",
        "muestra_expresion" : "titulo",
        #"filtros"   : [["estado_", "=", "activo"]]
    }
)
acciones_ids = adaptadores_grid_forma.adaptador_campo_forma(
    "acciones_ids", 
    definicion["campos"]["acciones_ids"], 
    {
        'tipoeditor': 'tag', 
        "fuente"    : "acciones_sistema",
        #"filtros"   : [["estado_", "=", "activo"]]
    }
)
estado_ =  adaptadores_grid_forma.adaptador_campo_forma(
    "estado_", definicion["campos"]["estado_"], 
    {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]}
)

campos = [
    codigo,
    nombre,
    opciones_ids,
    acciones_ids,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Roles", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["roles_forma"] = forma_basico