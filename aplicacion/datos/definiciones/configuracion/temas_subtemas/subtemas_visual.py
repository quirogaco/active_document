#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .subtemas import definicion

###############
# GRID BASICO #
###############
codigo      = adaptadores_grid_forma.adaptador_columna_grid("codigo",      definicion["campos"]["codigo"], {'ancho': None})
nombre      = adaptadores_grid_forma.adaptador_columna_grid("nombre",      definicion["campos"]["nombre"], {'ancho': None})
tema_nombre = adaptadores_grid_forma.adaptador_columna_grid("tema_nombre", definicion["campos"]["tema_nombre"], {'ancho': None})
estado_     = adaptadores_grid_forma.adaptador_columna_grid("estado_",     definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    codigo,
    nombre,
    tema_nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Subtemas por tema", 
    atributos_especificos={"crear": "Crear Subtema"}
)
CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["subtemas_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo         = adaptadores_grid_forma.adaptador_campo_forma("codigo",             definicion["campos"]["codigo"])
nombre         = adaptadores_grid_forma.adaptador_campo_forma("nombre",             definicion["campos"]["nombre"])
tema_id = adaptadores_grid_forma.adaptador_campo_forma(
    "tema_id", 
    definicion["campos"]["tema_id"], 
    {
        'tipoeditor': 'select', 
        "fuente"    : "temas",
        "filtros"   : [["estado_", "=", "activo"]]
    }
)
estado_ =  adaptadores_grid_forma.adaptador_campo_forma(
    "estado_", definicion["campos"]["estado_"], 
    {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]}
)

campos = [
    codigo,
    nombre,
    tema_id,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Subtemas por Tema", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["subtemas_forma"] = forma_basico