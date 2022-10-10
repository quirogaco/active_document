#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general_campos
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes

campos = {
    "nombre": tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120}),  
}
campos.update(base_general_campos.campos)

definicion = {
    "descripcion" : "Tipos de ciudadanos",
    "clase"       : "global_base_general",
    "estructura"  : "tipo_ciudadano",
    "campos"      : campos,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}
camposIndexamiento = {}
camposElastic = campos
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# PROCESAMIENTO ESTRUCTURA
elementos_comunes.procesaBaseGeneral(definicion)