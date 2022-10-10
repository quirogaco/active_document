#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.visuales   import adaptadores_grid_forma
from .tipo_identificacion import definicion

###############
# GRID BASICO #
###############
nombre  = adaptadores_grid_forma.adaptador_columna_grid("nombre",  definicion["campos"]["nombre"],  {'ancho': None})
estado_ = adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Tipos de Identificación", 
    atributos_especificos={"crear": "Crear Tipo de Identificación"}
)
CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["tipo_identificaciones_grid"] = grid_basico 

################
# FORMA BASICA #
################
nombre  = adaptadores_grid_forma.adaptador_campo_forma("nombre", definicion["campos"]["nombre"])
estado_ =  adaptadores_grid_forma.adaptador_campo_forma(
    "estado_", definicion["campos"]["estado_"], 
    {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]}
)

campos = [
    nombre,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Tipos de Identificación", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["tipo_identificaciones_forma"] = forma_basico

