
import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .paises import definicion

###############
# GRID BASICO #
###############
codigo            = adaptadores_grid_forma.adaptador_columna_grid("codigo",            definicion["campos"]["codigo"], {'ancho': None})
nombre            = adaptadores_grid_forma.adaptador_columna_grid("nombre",            definicion["campos"]["nombre"], {'ancho': None})
continente_nombre = adaptadores_grid_forma.adaptador_columna_grid("continente_nombre", definicion["campos"]["continente_nombre"], {'ancho': None})
estado_           = adaptadores_grid_forma.adaptador_columna_grid("estado_",           definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    codigo,
    nombre,
    continente_nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Manejo de Paises", 
    atributos_especificos={"crear": "Crear Pais"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["paises_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo        = adaptadores_grid_forma.adaptador_campo_forma("codigo",  definicion["campos"]["codigo"])
nombre        = adaptadores_grid_forma.adaptador_campo_forma("nombre",  definicion["campos"]["nombre"])
continente_id = adaptadores_grid_forma.adaptador_campo_forma(
                    "continente_id", 
                    definicion["campos"]["continente_id"], 
                    {
                        'tipoeditor': 'select', 
                        "fuente"    : "continentes",
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
    continente_id,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Paises", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["paises_forma"] = forma_basico