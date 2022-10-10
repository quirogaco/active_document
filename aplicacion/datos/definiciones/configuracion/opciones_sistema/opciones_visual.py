#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .opciones_sistema import definicion

###############
# GRID BASICO #
###############
clase      =  adaptadores_grid_forma.adaptador_columna_grid("clase",      definicion["campos"]["clase"],      {'ancho': 150})
#codigo     =  adaptadores_grid_forma.adaptador_columna_grid("codigo",     definicion["campos"]["codigo"],     {'ancho': 180})
titulo     =  adaptadores_grid_forma.adaptador_columna_grid("titulo",     definicion["campos"]["titulo"],     {'ancho': 400})
ruta       =  adaptadores_grid_forma.adaptador_columna_grid("ruta",       definicion["campos"]["ruta"],       {'ancho': 180})
componente =  adaptadores_grid_forma.adaptador_columna_grid("componente", definicion["campos"]["componente"], {'ancho': 180})
padre      =  adaptadores_grid_forma.adaptador_columna_grid("padre",      definicion["campos"]["padre"],      {'ancho': 180})
entidad    =  adaptadores_grid_forma.adaptador_columna_grid("entidad",    definicion["campos"]["entidad"],    {'ancho': 180})

columnas = [
    clase,
    #codigo,
    titulo,
    ruta,
    componente,
    padre,
    entidad
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Manejo de opciones del Menu", 
    atributos_especificos={"crear": "Crear Opción"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["opciones_sistema_grid"] = grid_basico 

################
# FORMA BASICA #
################
clase      =  adaptadores_grid_forma.adaptador_campo_forma("clase",      definicion["campos"]["clase"], {'tipoeditor': 'radio', "elementos": ["GRID", "FORMA"]})
#codigo     =  adaptadores_grid_forma.adaptador_campo_forma("codigo",     definicion["campos"]["codigo"])
titulo     =  adaptadores_grid_forma.adaptador_campo_forma("titulo",     definicion["campos"]["titulo"])
ruta       =  adaptadores_grid_forma.adaptador_campo_forma("ruta",       definicion["campos"]["ruta"])
componente =  adaptadores_grid_forma.adaptador_campo_forma("componente", definicion["campos"]["componente"])
icono      =  adaptadores_grid_forma.adaptador_campo_forma("icono",      definicion["campos"]["icono"])
tipo       =  adaptadores_grid_forma.adaptador_campo_forma("tipo",       definicion["campos"]["tipo"],    {'tipoeditor': 'radio', "elementos": ["IMPORTAR", "REMOTO"]})
navegar    =  adaptadores_grid_forma.adaptador_campo_forma("navegar",    definicion["campos"]["navegar"], {'tipoeditor': 'radio', "elementos": ["SI", "NO"]})
padre      =  adaptadores_grid_forma.adaptador_campo_forma("padre",      definicion["campos"]["padre"])
entidad    =  adaptadores_grid_forma.adaptador_campo_forma("entidad",    definicion["campos"]["entidad"])

campos = [
    clase,
    #codigo,
    titulo,
    ruta,
    componente,
    icono,
    tipo,
    navegar,
    padre,
    entidad
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de opciones del Menu", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["opciones_sistema_forma"] = forma_basico