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
    "codigo"        : tipos.texto_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60}),     
    "nombre"        : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120}),     
    "estado_"       : tipos.texto_obligatorio(propiedades={"titulo": "Estado"})    
}
campos.update(base_general_campos.campos)

definicion = {
    "descripcion" : "Grupos",
    "clase"       : "global_base_general",
    "estructura"  : "grupos",
    "campos"      : campos,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Campos elastic
camposIndexamiento = {}
camposElastic      = campos
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# PROCESAMIENTO ESTRUCTURA
elementos_comunes.procesaBaseGeneral(definicion)
