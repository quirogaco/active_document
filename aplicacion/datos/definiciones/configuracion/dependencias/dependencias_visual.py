#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .dependencias import definicion

###############
# GRID BASICO #
###############
codigo           = adaptadores_grid_forma.adaptador_columna_grid("codigo",  definicion["campos"]["codigo"], {'ancho': None})
ubicacion_nombre = adaptadores_grid_forma.adaptador_columna_grid("ubicacion_nombre",  definicion["campos"]["ubicacion_nombre"], {'ancho': None})
nombre           = adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"], {'ancho': None})

estado_ = adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    codigo,
    nombre,
    ubicacion_nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Dependencias, areas, oficinas", 
    atributos_especificos={"crear": "Crear Dependencia"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["dependencias_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo       = adaptadores_grid_forma.adaptador_campo_forma("codigo",  definicion["campos"]["codigo"])
nombre       = adaptadores_grid_forma.adaptador_campo_forma("nombre",  definicion["campos"]["nombre"], {'longitud':100})
ubicacion_id = adaptadores_grid_forma.adaptador_campo_forma(
    "ubicacion_id", 
    definicion["campos"]["ubicacion_id"], 
    {
        'tipoeditor': 'select', 
        "fuente"    : "ubicaciones",
        "filtros"   : [["estado_", "=", "activo"]]
    }
)
jefe_id      = adaptadores_grid_forma.adaptador_campo_forma(
    "jefe_id", 
    definicion["campos"]["jefe_id"], 
    {
        'tipoeditor': 'select', 
        "fuente"    : "usuarios",
        "filtros"   : [["estado_", "=", "activo"]]
    }
)
correspondencia_id = adaptadores_grid_forma.adaptador_campo_forma(
    "correspondencia_id", 
    definicion["campos"]["correspondencia_id"], 
    {
        'tipoeditor': 'select', 
        "fuente"    : "usuarios",
        "filtros"   : [["estado_", "=", "activo"]]
    }
)
archivo_id   = adaptadores_grid_forma.adaptador_campo_forma(
    "archivo_id", 
    definicion["campos"]["archivo_id"], 
    {
        'tipoeditor': 'select', 
        "fuente"    : "usuarios",
        "filtros"   : [["estado_", "=", "activo"]]
    }
)
pqrs_id = adaptadores_grid_forma.adaptador_campo_forma(
    "pqrs_id", 
    definicion["campos"]["pqrs_id"], 
    {
        'tipoeditor': 'select', 
        "fuente"    : "usuarios",
        "filtros"   : [["estado_", "=", "activo"]]
    }
)
coordinadores_ids = adaptadores_grid_forma.adaptador_campo_forma(
    "coordinadores_ids", 
    definicion["campos"]["coordinadores_ids"], 
    {
        'tipoeditor': 'tag', 
        "fuente"    : "usuarios",
        "filtros"   : [["estado_", "=", "activo"]]
    }
)
padre_id = adaptadores_grid_forma.adaptador_campo_forma(
    "padre_id", 
    definicion["campos"]["padre_id"], 
    {
        'tipoeditor'        : 'select', 
        "fuente"            : "dependencias",
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",
        "filtros"           : [["estado_", "=", "activo"]]
    }
)
dependencias_ids = adaptadores_grid_forma.adaptador_campo_forma(
    "dependencias_ids", 
    definicion["campos"]["dependencias_ids"], 
    {
        'tipoeditor': 'tag', 
        "fuente"    : "dependencias",
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
    ubicacion_id,
    jefe_id,
    correspondencia_id,
    archivo_id,
    pqrs_id,
    coordinadores_ids,
    padre_id,
    dependencias_ids,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Dependencias (Areas, Oficinas, Grupos de trabajo)", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["dependencias_forma"] = forma_basico