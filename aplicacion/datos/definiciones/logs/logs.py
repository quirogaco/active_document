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

from . import logs_campos

referencias = [
    # Creador
    {
        "campoReferencia"    : "accionante_id",
        "atributosReferencia": [{
            "accionante_nombre": "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    },

    # Responsable 
    {
        "campoReferencia"    : "destinatario_id",
        "atributosReferencia": [{
            "destinatario_nombre"   : "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    },
]

definicion = {
    "descripcion" : "Log de acciones",
    "clase"       : "global_log_acciones",
    "estructura"  : "logs",    
    "campos"      : logs_campos.campos,
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
camposElastic      = logs_campos.campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)