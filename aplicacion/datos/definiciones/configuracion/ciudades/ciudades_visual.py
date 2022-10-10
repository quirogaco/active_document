#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .ciudades import definicion

###############
# GRID BASICO #
###############
codigo              = adaptadores_grid_forma.adaptador_columna_grid("codigo",              definicion["campos"]["codigo"], {'ancho': None})
nombre              = adaptadores_grid_forma.adaptador_columna_grid("nombre",              definicion["campos"]["nombre"], {'ancho': None})
nombre_completo     = adaptadores_grid_forma.adaptador_columna_grid("nombre_completo",     definicion["campos"]["nombre_completo"], {'ancho': None})
departamento_nombre = adaptadores_grid_forma.adaptador_columna_grid("departamento_nombre", definicion["campos"]["departamento_nombre"], {'ancho': None})
pais_nombre         = adaptadores_grid_forma.adaptador_columna_grid("pais_nombre",         definicion["campos"]["pais_nombre"], {'ancho': None})
continente_nombre   = adaptadores_grid_forma.adaptador_columna_grid("continente_nombre",   definicion["campos"]["continente_nombre"], {'ancho': None})
estado_             = adaptadores_grid_forma.adaptador_columna_grid("estado_",             definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    codigo,
    nombre,
    nombre_completo,
    departamento_nombre,
    pais_nombre,
    continente_nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Manejo de Ciudades", 
    atributos_especificos={"crear": "Crear Ciudad"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["ciudades_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo          = adaptadores_grid_forma.adaptador_campo_forma("codigo",  definicion["campos"]["codigo"])
nombre          = adaptadores_grid_forma.adaptador_campo_forma("nombre",  definicion["campos"]["nombre"])
departamento_id = adaptadores_grid_forma.adaptador_campo_forma(
                    "departamento_id", 
                    definicion["campos"]["departamento_id"], 
                    {
                        'tipoeditor': 'select', 
                        "fuente"    : "departamentos",
                        "filtros"   : [["estado_", "=", "activo"]]
                    }
                )
estado_    =  adaptadores_grid_forma.adaptador_campo_forma(
                "estado_", definicion["campos"]["estado_"], 
                {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]}
              )

campos = [
    codigo,
    nombre,
    departamento_id,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Ciudades", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["ciudades_forma"] = forma_basico