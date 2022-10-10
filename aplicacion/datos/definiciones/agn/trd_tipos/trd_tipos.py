#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pprint

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes

campos = {
    # TRD/TVD
    "tabla"      : tipos.clave(propiedades={"titulo": "TRD/TVD", "longitud": 60}),

    # Especificos
    "nombre"     : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 250}), 
    "papel"      : tipos.texto(propiedades={"titulo": "Soporte Papel", "defecto": "NO"}),    
    "electronico": tipos.texto(propiedades={"titulo": "Soporte Electronico", "defecto": "NO"}),  
    "formato"    : tipos.texto(propiedades={"titulo": "Micro digitalización"}),  
    
    # Serie padre
    "serie_id"    : tipos.clave(propiedades={"titulo": "Serie padre id", "longitud": 60}),
    "serie_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Serie descripción", "longitud": 250}),
    
    # SubSerie padre
    "subserie_id"    : tipos.clave(propiedades={"titulo": "Subserie padre id", "longitud": 60}),
    "subserie_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Subserie descripción", "longitud": 250}),

    "indice": tipos.entero(propiedades={"titulo": "Indice", "defecto": 0}),
}

referencias = [
    # Serie Trd
    {
        "campoReferencia"    : "serie_id",
        "atributosReferencia": [{
            "serie_nombre": "nombre",
        }],
        "estructuraDestino": "agn_serie_trd",
        "campoDestino"     : "id",            
    },

    # SubSerie Trd
    {
        "campoReferencia"    : "subserie_id",
        "atributosReferencia": [{
            "subserie_nombre": "nombre",
        }],
        "estructuraDestino": "agn_subserie_trd",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Tipo Documental Tabla de Retención",
    "clase"       : "agn_tipo_documental_trd",
    "estructura"  : "agn_tipo_documental_trd",    
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