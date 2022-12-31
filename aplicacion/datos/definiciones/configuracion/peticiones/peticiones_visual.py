#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .peticiones import definicion

###############
# GRID BASICO #
###############
codigo          = adaptadores_grid_forma.adaptador_columna_grid("codigo",          definicion["campos"]["codigo"],          {'ancho': 100})
nombre          = adaptadores_grid_forma.adaptador_columna_grid("nombre",          definicion["campos"]["nombre"],          {'ancho': 350})
horas_dias      = adaptadores_grid_forma.adaptador_columna_grid("horas_dias",      definicion["campos"]["horas_dias"],      {'ancho': 150})
tipo_tiempo     = adaptadores_grid_forma.adaptador_columna_grid("tipo_tiempo",     definicion["campos"]["tipo_tiempo"],     {'ancho': 150})
modifica_tiempo = adaptadores_grid_forma.adaptador_columna_grid("modifica_tiempo", definicion["campos"]["modifica_tiempo"], {'ancho': None})
pqrs            = adaptadores_grid_forma.adaptador_columna_grid("pqrs",            definicion["campos"]["pqrs"],            {'titulo': 'Tipo', 'ancho': None})
estado_ = adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    codigo,
    nombre,
    horas_dias,
    tipo_tiempo,
    modifica_tiempo,
    pqrs,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Tipos de Petición", 
    atributos_especificos={"crear": "Crear Tipo de Petición"}
)
CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["tipo_peticiones_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo             = adaptadores_grid_forma.adaptador_campo_forma("codigo",             definicion["campos"]["codigo"])
nombre             = adaptadores_grid_forma.adaptador_campo_forma("nombre",             definicion["campos"]["nombre"])
total_tiempo       = adaptadores_grid_forma.adaptador_campo_forma("total_tiempo",       definicion["campos"]["total_tiempo"],   {'tipoeditor': 'entero'})
alertar_tiempo     = adaptadores_grid_forma.adaptador_campo_forma("alertar_tiempo",     definicion["campos"]["alertar_tiempo"]    )
alertar_porcentaje = adaptadores_grid_forma.adaptador_campo_forma("alertar_porcentaje", definicion["campos"]["alertar_porcentaje"])
bloquear           = adaptadores_grid_forma.adaptador_campo_forma("bloquear",           definicion["campos"]["bloquear"],       {'tipoeditor': 'entero'})
horas_dias         =  adaptadores_grid_forma.adaptador_campo_forma(
    "horas_dias", definicion["campos"]["horas_dias"], 
    {'tipoeditor': 'radio', "elementos": ["HORAS", "DIAS"]}
)
tipo_tiempo      =  adaptadores_grid_forma.adaptador_campo_forma(
    "tipo_tiempo", definicion["campos"]["tipo_tiempo"], 
    {'tipoeditor': 'radio', "elementos": ["HABILES", "CALENDARIO"]}
)
modifica_tiempo =  adaptadores_grid_forma.adaptador_campo_forma(
    "modifica_tiempo", definicion["campos"]["modifica_tiempo"], 
    {'tipoeditor': 'radio', "elementos": ["SI", "NO"]}
)
pqrs               =  adaptadores_grid_forma.adaptador_campo_forma(
    "pqrs", definicion["campos"]["pqrs"], 
    {'tipoeditor': 'radio', "elementos": ["PQRSD", "TRAMITE", "DOCUMENTO"]}
)
dependencias_ids = adaptadores_grid_forma.adaptador_campo_forma(
    "dependencias_ids", 
    definicion["campos"]["dependencias_ids"], 
    {
        "tipoeditor"        : 'tag', 
        "fuente"            : "dependencias",
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
    total_tiempo,
    alertar_tiempo,
    alertar_porcentaje,
    bloquear,
    horas_dias,
    tipo_tiempo,
    modifica_tiempo,
    pqrs,
    dependencias_ids,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Tipos de Peticiones", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["tipo_peticiones_forma"] = forma_basico