#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes

from . import tramite_campos

referencias = [
    # Formulario
    {
        "campoReferencia"    : "formulario_id",
        "atributosReferencia": [{
            "formulario_nombre": "nombre",
        }],
        "estructuraDestino": "formularios_dinamicos",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Tramites definición",
    "clase"       : "config_tramites",
    "estructura"  : "tramites",    
    "campos"      : tramite_campos.campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {},
    "reporte"     : "SI"
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

camposIndexamiento = {}
camposElastic      = tramite_campos.campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)