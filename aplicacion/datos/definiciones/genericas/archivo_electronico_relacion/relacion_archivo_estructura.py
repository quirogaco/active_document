#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general_campos
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from aplicacion.datos.definiciones._comunes import elementos_comunes

campos = {
    # Define el tipo de relación ej. "anexos,adicionales, etc", 
    "tipo_relacion": tipos.clave_obligatorio(propiedades={"titulo": "Tipo relación", "longitud": 64}),  
    
    # Cardinalidad de la relacion:
    # "uno"   : uno a uno
    # "varios": varios 
    "cardinalidad": tipos.clave(propiedades={"titulo": "Cardinalidad de la relación", "longitud": 64}),  

    # ORIGEN
    # Estructura origen de la relación
    "origen"     : tipos.clave_obligatorio(propiedades={"titulo": "Estructura origen", "longitud": 128}), 
    # ID de la Estructura origen de la relación
    "origen_id"  : tipos.clave_obligatorio(propiedades={"titulo": "ID de la Estructura origen", "longitud": 64}),         
    # ROLE de la Estructura origen de la relación
    "origen_role": tipos.clave_obligatorio(propiedades={"titulo": "Role de la Estructura origen", "longitud": 64}), 

    # ARCHIVO
    "archivo_id" : tipos.clave_obligatorio(propiedades={"titulo": "ID del archivo asociado", "longitud": 64}), 
}
campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {}
camposElastic = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Relación a archivos",
    "clase"       : "global_base_relacion_archivo",
    "estructura"  : "archivos_relacion",    
    "campos"      : campos,
    "referencias" : [],
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)