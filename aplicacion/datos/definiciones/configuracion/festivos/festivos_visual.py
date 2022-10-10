import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .festivos import definicion

###############
# GRID BASICO #
###############
festivo  =  adaptadores_grid_forma.adaptador_columna_grid("festivo", definicion["campos"]["festivo"], {'ancho': None})
estado_  =  adaptadores_grid_forma.adaptador_columna_grid("estado_", definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    festivo,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Manejo de Festivos", 
    atributos_especificos={"crear": "Crear Festivo"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["festivos_grid"] = grid_basico 

################
# FORMA BASICA #
################
festivo =  adaptadores_grid_forma.adaptador_campo_forma("festivo",  definicion["campos"]["festivo"])
estado_ =  adaptadores_grid_forma.adaptador_campo_forma(
                "estado_", definicion["campos"]["estado_"], 
                {'tipoeditor': 'radio', "elementos": ["ACTIVO", "INACTIVO"]}
            )

campos = [
    festivo,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Festivos", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["festivos_forma"] = forma_basico