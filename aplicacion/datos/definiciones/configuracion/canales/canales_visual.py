#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .canales import definicion

###############
# GRID BASICO #
###############
nombre           = adaptadores_grid_forma.adaptador_columna_grid("nombre",   definicion["campos"]["nombre"],   {'ancho': None})
plantilla_juridica_nombre = adaptadores_grid_forma.adaptador_columna_grid("plantilla_juridica_nombre", definicion["campos"]["plantilla_juridica_nombre"], {'ancho': None})
plantilla_natural_nombre  = adaptadores_grid_forma.adaptador_columna_grid("plantilla_natural_nombre", definicion["campos"]["plantilla_natural_nombre"], {'ancho': None})
plantilla_anonima_nombre  = adaptadores_grid_forma.adaptador_columna_grid("plantilla_anonima_nombre", definicion["campos"]["plantilla_anonima_nombre"], {'ancho': None})
estado_          = adaptadores_grid_forma.adaptador_columna_grid("estado_",  definicion["campos"]["estado_"],  {'ancho': None})

columnas = [
    nombre,  
    plantilla_juridica_nombre,  
    plantilla_natural_nombre,
    plantilla_anonima_nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Canales de comunicación", 
    atributos_especificos={"crear": "Crear Canal de comunicación"}
)
CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["canales_comunicacion_grid"] = grid_basico 

################
# FORMA BASICA #
################
nombre       = adaptadores_grid_forma.adaptador_campo_forma("nombre", definicion["campos"]["nombre"])

plantilla_juridica_id = adaptadores_grid_forma.adaptador_campo_forma(
                    "plantilla_juridica_id", 
                    definicion["campos"]["plantilla_juridica_id"], 
                    {
                        'tipoeditor'        : 'select', 
                        "busqueda_expresion": "descripcion",
                        "muestra_expresion" : "descripcion",
                        "fuente"            : "plantillas"
                    }
                )

plantilla_natural_id = adaptadores_grid_forma.adaptador_campo_forma(
                    "plantilla_natural_id", 
                    definicion["campos"]["plantilla_natural_id"], 
                    {
                        'tipoeditor'        : 'select', 
                        "busqueda_expresion": "descripcion",
                        "muestra_expresion" : "descripcion",
                        "fuente"            : "plantillas"
                    }
                )

plantilla_anonima_id = adaptadores_grid_forma.adaptador_campo_forma(
                    "plantilla_anonima_id", 
                    definicion["campos"]["plantilla_anonima_id"], 
                    {
                        'tipoeditor'        : 'select', 
                        "busqueda_expresion": "descripcion",
                        "muestra_expresion" : "descripcion",
                        "fuente"            : "plantillas"
                    }
                )

estado_      =  adaptadores_grid_forma.adaptador_campo_forma(
    "estado_", definicion["campos"]["estado_"], 
    {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]}
)

campos = [
    nombre,
    plantilla_juridica_id,    
    plantilla_natural_id,
    plantilla_anonima_id,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Canales de comunicación", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["canales_comunicacion_forma"] = forma_basico