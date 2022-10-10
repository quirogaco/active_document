#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .usuarios import definicion

###############
# GRID BASICO #
###############
codigo             = adaptadores_grid_forma.adaptador_columna_grid("codigo",  definicion["campos"]["codigo"], {'ancho': None})
nombre             = adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"], {'ancho': None})
dependencia_nombre = adaptadores_grid_forma.adaptador_columna_grid("dependencia_nombre",  definicion["campos"]["dependencia_nombre"], {'ancho': None})
ubicacion_nombre   = adaptadores_grid_forma.adaptador_columna_grid("ubicacion_nombre",    definicion["campos"]["ubicacion_nombre"], {'ancho': None})
estado_            = adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    codigo,
    nombre,
    dependencia_nombre,
    ubicacion_nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Usuarios", 
    atributos_especificos={"crear": "Crear Usuario"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["usuarios_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo = adaptadores_grid_forma.adaptador_campo_forma("codigo",  definicion["campos"]["codigo"])
nombre = adaptadores_grid_forma.adaptador_campo_forma("nombre",  definicion["campos"]["nombre"])
correo = adaptadores_grid_forma.adaptador_campo_forma("correo",  definicion["campos"]["correo"], {"modo": "email"})
clave  = adaptadores_grid_forma.adaptador_campo_forma("clave",   definicion["campos"]["clave"], {"modo": "password"})

dependencia_id = adaptadores_grid_forma.adaptador_campo_forma(
    "dependencia_id", 
    definicion["campos"]["dependencia_id"], 
    {
        'tipoeditor'        : 'select', 
        "fuente"            : "dependencias",
        "busqueda_expresion": "nombre_completo",
        "muestra_expresion" : "nombre_completo",
        "filtros"           : [["estado_", "=", "activo"]]
    }
)
reemplaza_id = adaptadores_grid_forma.adaptador_campo_forma(
    "reemplaza_id", 
    definicion["campos"]["reemplaza_id"], 
    {
        'tipoeditor': 'select', 
        "fuente"    : "usuarios",
        "filtros"   : [["estado_", "=", "activo"]]
    }
)
roles_ids = adaptadores_grid_forma.adaptador_campo_forma(
    "roles_ids", 
    definicion["campos"]["roles_ids"], 
    {
        'tipoeditor': 'tag', 
        "fuente"    : "roles",
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
    clave,
    correo,
    dependencia_id,
    reemplaza_id,
    roles_ids,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Usuarios", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["usuarios_forma"] = forma_basico