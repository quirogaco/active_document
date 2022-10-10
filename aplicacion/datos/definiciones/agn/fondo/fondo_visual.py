#!/usr/bin/python
# -*- coding: utf-8 -*-
from librerias.visuales   import adaptadores_grid_forma
from .fondo import definicion

###############
# GRID BASICO #
###############
sigla   = adaptadores_grid_forma.adaptador_columna_grid("sigla",   definicion["campos"]["sigla"],   {'ancho': None})
nombre  = adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"],  {'ancho': None})
estado_ = adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    sigla,
    nombre,    
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Fondos Documentales", 
    atributos_especificos={"crear": "Crear Fondo"}
)
CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["agn_fondo_documental_grid"] = grid_basico 

################
# FORMA BASICA #
################
sigla   = adaptadores_grid_forma.adaptador_campo_forma("sigla",  definicion["campos"]["sigla"])
nombre  = adaptadores_grid_forma.adaptador_campo_forma("nombre", definicion["campos"]["nombre"])
estado_ =  adaptadores_grid_forma.adaptador_campo_forma(
    "estado_", definicion["campos"]["estado_"], 
    {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]}
)

campos = [
    sigla,
    nombre,    
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Fondos documentales", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["agn_fondo_documental_forma"] = forma_basico