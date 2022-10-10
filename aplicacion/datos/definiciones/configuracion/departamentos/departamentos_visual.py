
import pprint

from librerias.datos.base import globales
from librerias.visuales   import adaptadores_grid_forma

from .departamentos import definicion

###############
# GRID BASICO #
###############
codigo            = adaptadores_grid_forma.adaptador_columna_grid("codigo",            definicion["campos"]["codigo"], {'ancho': None})
nombre            = adaptadores_grid_forma.adaptador_columna_grid("nombre",            definicion["campos"]["nombre"], {'ancho': None})
pais_nombre       = adaptadores_grid_forma.adaptador_columna_grid("pais_nombre",       definicion["campos"]["pais_nombre"], {'ancho': None})
continente_nombre = adaptadores_grid_forma.adaptador_columna_grid("continente_nombre", definicion["campos"]["continente_nombre"], {'ancho': None})
estado_           = adaptadores_grid_forma.adaptador_columna_grid("estado_",           definicion["campos"]["estado_"], {'ancho': None})

columnas = [
    codigo,
    nombre,
    pais_nombre,
    continente_nombre,
    estado_
]

grid_basico = adaptadores_grid_forma.adaptador_grid(
    definicion["estructura"], 
    columnas, 
    "Manejo de Departamento", 
    atributos_especificos={"crear": "Crear Departamento"}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["grid"]["departamentos_grid"] = grid_basico 

################
# FORMA BASICA #
################
codigo     = adaptadores_grid_forma.adaptador_campo_forma("codigo",  definicion["campos"]["codigo"])
nombre     = adaptadores_grid_forma.adaptador_campo_forma("nombre",  definicion["campos"]["nombre"])
pais_id    = adaptadores_grid_forma.adaptador_campo_forma(
                    "pais_id", 
                    definicion["campos"]["pais_id"], 
                    {
                        'tipoeditor': 'select', 
                        "fuente"    : "paises",
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
    pais_id,
    estado_
]

forma_basico = adaptadores_grid_forma.adaptador_forma(
    definicion["estructura"], 
    campos, 
    "Manejo de Departamentos", 
    atributos_especificos={}
)

CONFIGURACION_GENERAL["definiciones_visuales"]["forma"]["departamentos_forma"] = forma_basico