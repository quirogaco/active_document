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
    "codigo"     : tipos.texto_obligatorio(propiedades={"titulo": "Codigo",             "longitud": 60,  "unico": "si"}),     
    "nombre"     : tipos.texto_obligatorio(propiedades={"titulo": "Nombre",             "longitud": 120, "unico": "si"}),  
    "correo"     : tipos.texto_obligatorio(propiedades={"titulo": "Correo electrónico", "longitud": 256}),  
    "estado_"    : tipos.texto_obligatorio(propiedades={"titulo": "Estado"}) 
}
campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {}
camposElastic      = campos
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Ubicación geografica",
    "clase"       : "global_base_general",
    "estructura"  : "ubicaciones",
    "campos"      : campos,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

camposElastic = campos
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# PROCESAMIENTO ESTRUCTURA
elementos_comunes.procesaBaseGeneral(definicion)