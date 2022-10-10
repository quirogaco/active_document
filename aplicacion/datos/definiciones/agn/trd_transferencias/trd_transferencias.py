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
    "usuario_id"        : tipos.clave_obligatorio(propiedades={"titulo": "Usuario id", "longitud": 60}), 
    "usuario_nombre"    : tipos.texto(propiedades={"columna": "no", "titulo": "Nombre usuario", "longitud": 256}),  
    "dependencia_id"    : tipos.clave_obligatorio(propiedades={"titulo": "Dependencia id", "longitud": 60}), 
    "dependencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia nombre", "longitud": 256}),    
    "estado"            : tipos.clave_obligatorio(propiedades={"titulo": "Estado", "longitud": 60, "defecto": "PENDIENTE"}), # PENDIENTE
    "detalle"           : tipos.texto(propiedades={ "titulo": "Detalle", "longitud": 256}),  
    
    "fecha_transferencia": tipos.fecha(propiedades={"titulo": "Fecha transferencia"}), 
    "fecha_creacion"     : tipos.fecha(propiedades={"titulo": "Fecha creación"}), 
    "fecha_envio"        : tipos.fecha(propiedades={"titulo": "Fecha envio"}), 
    "fecha_aprobacion"   : tipos.fecha(propiedades={"titulo": "Fecha aprobación"}), 
    "fecha_devolucion"   : tipos.fecha(propiedades={"titulo": "Fecha devolución"}), 
}

referencias = [
    # Usuario peticionario
    {
        "campoReferencia"    : "usuario_id",
        "atributosReferencia": [{
            "usuario_nombre": "nombre"
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    },

    # Dependencia peticionario
    {
        "campoReferencia"    : "dependencia_id",
        "atributosReferencia": [{
            "dependencia_nombre": "nombre"
        }],
        "estructuraDestino": "dependencias",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Transferencias primarias",
    "clase"       : "agn_transferencias_trd",
    "estructura"  : "agn_transferencias_trd",    
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