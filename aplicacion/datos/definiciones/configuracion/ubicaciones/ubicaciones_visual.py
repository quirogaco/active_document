#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .ubicaciones import definicion

###############
# GRID BASICO #
###############
codigo  = adaptadores_grid_forma.adaptador_columna_grid("codigo",  definicion["campos"]["codigo"], {'ancho': None})
nombre  = adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"], {'ancho': None})
correo  = adaptadores_grid_forma.adaptador_columna_grid("correo",  definicion["campos"]["correo"], {'ancho': None})
estado_ = adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    codigo,
    nombre,
    correo,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Ubicaciones (territoriales, dependencias)", 
    atributos_especificos={"crear": "Crear Ubicación"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["ubicaciones_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo  = adaptadores_grid_forma.adaptador_campo_forma("codigo",  definicion["campos"]["codigo"])
nombre  = adaptadores_grid_forma.adaptador_campo_forma("nombre",  definicion["campos"]["nombre"])
correo  = adaptadores_grid_forma.adaptador_campo_forma("correo",  definicion["campos"]["correo"], {"modo": "email"})
estado_ =  adaptadores_grid_forma.adaptador_campo_forma(
                "estado_", definicion["campos"]["estado_"], 
                {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]}
           )

campos = [
    codigo,
    nombre,
    correo,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Ubicaciones (Territoriales, Dependencias)", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["ubicaciones_forma"] = forma_basico