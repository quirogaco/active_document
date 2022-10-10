#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .temas import definicion

###############
# GRID BASICO #
###############
codigo             = adaptadores_grid_forma.adaptador_columna_grid("codigo",  definicion["campos"]["codigo"], {'ancho': None})
nombre             = adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"], {'ancho': None})
dependencia_nombre = adaptadores_grid_forma.adaptador_columna_grid("dependencia_nombre",  definicion["campos"]["dependencia_nombre"], {'ancho': None})
tramite_nombre     = adaptadores_grid_forma.adaptador_columna_grid("tramite_nombre", definicion["campos"]["tramite_nombre"], {'ancho': None})
estado_            = adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    codigo,
    nombre,
    dependencia_nombre,
    tramite_nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Temas por dependencia", 
    atributos_especificos={"crear": "Crear Tema"}
)
CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["temas_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo         = adaptadores_grid_forma.adaptador_campo_forma("codigo",             definicion["campos"]["codigo"])
nombre         = adaptadores_grid_forma.adaptador_campo_forma("nombre",             definicion["campos"]["nombre"])
dependencia_id = adaptadores_grid_forma.adaptador_campo_forma(
    "dependencia_id", 
    definicion["campos"]["dependencia_id"], 
    {
        'tipoeditor': 'select', 
        "fuente"    : "dependencias",
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",
        "filtros"   : [["estado_", "=", "activo"]]
    }
)
tramite_id = adaptadores_grid_forma.adaptador_campo_forma(
    "tramite_id", 
    definicion["campos"]["tramite_id"], 
    {
        'tipoeditor': 'select', 
        "fuente"    : "tramites",
        "busqueda_expresion": "nombre",
        "muestra_expresion" : "nombre",
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
    dependencia_id,
    tramite_id,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Temas por Dependencia", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["temas_forma"] = forma_basico