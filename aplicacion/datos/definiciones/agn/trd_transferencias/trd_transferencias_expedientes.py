#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes
from librerias.datos.sql                    import sqalchemy_comunes

campos = {
    "transferencia_id"     : tipos.clave_obligatorio(propiedades={"titulo": "Transferencia id", "longitud": 60}), 
    "expediente_id"        : tipos.clave_obligatorio(propiedades={"titulo": "Expediente id", "longitud": 60}), 
    "expediente_nombre"    : tipos.texto(propiedades={"columna": "no", "titulo": "Nombre expediente", "longitud": 256}),
    "transferencia_detalle": tipos.texto(propiedades={"columna": "no", "titulo": "Transferencia", "longitud": 256})
}

referencias = [
    # TRANSFERENCIA
    {
        "campoReferencia"    : "transferencia_id",
        "atributosReferencia": [{
            "transferencia_detalle": "detalle"
        }],
        "estructuraDestino": "agn_transferencias_trd",
        "campoDestino"     : "id",            
    },

    # EXPEDIENTE
    {
        "campoReferencia"    : "expediente_id",
        "atributosReferencia": [{
            "expediente_nombre": "nombre"
        }],
        "estructuraDestino": "agn_expedientes_trd",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Transferencias primarias",
    "clase"       : "agn_transferencias_exp_trd",
    "estructura"  : "agn_transferencias_exp_trd",    
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