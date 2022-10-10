#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

from sqlalchemy import and_

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes
from librerias.datos.sql                    import sqalchemy_comunes

# Arbol de SUBSERIE
def tvd_subserie(_r):
    arbol = []

    return arbol

campos = {
    # TRD/TVD
    "tabla"              : tipos.clave(propiedades={"titulo": "TRD/TVD", "longitud": 60}),
    
    # Serie padre
    "serie_id"    : tipos.clave_obligatorio(propiedades={"titulo": "Dependencia padre id", "longitud": 60}),
    "serie_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia descripción", "longitud": 250}),
    "version"     : tipos.texto(propiedades={"columna": "no", "titulo": "Tvd versión", "longitud": 250}),   
    "activa"      : tipos.texto(propiedades={"columna": "no", "titulo": "Tvd activa", "longitud": 250}),      

    "codigo"            : tipos.clave_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60}),  
    "nombre"            : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 250}), 

    # Retención
    "central"           : tipos.entero(propiedades={"titulo": "Años en archivo central"}), 

    # Disposición
    "eliminacion"         : tipos.texto(propiedades={"titulo": "Eliminación", "defecto": "NO"}),    
    "seleccion"           : tipos.texto(propiedades={"titulo": "Selección", "defecto": "NO"}),  
    "conservacion"        : tipos.texto(propiedades={"titulo": "Conservación", "defecto": "NO"}),  
    "micro_digitalizacion": tipos.texto(propiedades={"titulo": "Micro digitalización", "defecto": "NO"}),
    "subserie_arbol"      : tipos.texto(propiedades={"columna": "no", "tipoElastic": "objeto", "titulo": "Tvd serie", "propiedad": tvd_subserie})
}

referencias = [
    # Serie Tvd
    {
        "campoReferencia"    : "serie_id",
        "atributosReferencia": [{
            "serie_nombre": "nombre",
            "periodo"     : "periodo",
            "activa"      : "estado",
        }],
        "estructuraDestino": "agn_serie_tvd",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "SubSerie Tabla de Valoración",
    "clase"       : "agn_subserie_tvd",
    "estructura"  : "agn_subserie_tvd",    
    "campos"      : campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

# Campos elastic
camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)