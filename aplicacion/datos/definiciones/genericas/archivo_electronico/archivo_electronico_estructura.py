#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general_campos
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from aplicacion.datos.definiciones._comunes import elementos_comunes

campos = {
    # Bucket MINIO
    "cubeta"      : tipos.clave_obligatorio(propiedades={"titulo": "Cubeta de almacenamiento (bucket)", "longitud": 1024}),  
    # Nombre del objeto
    "nombre"      : tipos.clave_obligatorio(propiedades={"titulo": "Nombre del objeto", "longitud": 1024}),   
    # RUTA, ruta completa del archivo
    "ruta"        : tipos.clave(propiedades={"titulo": "Ruta completa del archivo", "longitud": 1024}), 
    # Tipo archivo
    "tipo_archivo": tipos.clave(propiedades={"titulo": "Tipo archivo", "longitud": 32}),
    # Longitu del archivo
    "tamano"      : tipos.entero(propiedades={"titulo": "Tamano"}),    
    # Longitu del archivo
    "folios"      : tipos.entero(propiedades={"titulo": "Folios"})   
}
campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {}
camposElastic = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Archivos electronicos",
    "clase"       : "global_base_archivo_electronico",
    "estructura"  : "archivos_electronicos",    
    "campos"      : campos,
    "referencias" : [],
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)