#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from aplicacion.datos.clases.clases_base    import base_general_campos
from aplicacion.datos.definiciones._comunes import elementos_comunes

campos = {
    "codigo"  : elementos_comunes.codigo_obligatorio({}),
    "nombre"  : elementos_comunes.nombre_obligatorio({}),
    "_estado_": elementos_comunes.estado_obligatorio({}),
    "pais_id" : elementos_comunes.id_obligatorio({"titulo": "Pais"}),   
}
campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {
    "continente_nombre": elementos_comunes.elastic_texto,
    "pais_nombre"      : elementos_comunes.elastic_texto
}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Departamento",
    "clase"       : "base_general",
    "estructura"  : "departamento",    
    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,
    # Referencias a otras estructuras
    "referencias" : [
        {
            "campoReferencia"    : "pais_id",
            "atributosReferencia": [{
                "pais_nombre"      : "nombre",
                "continente_nombre": "continente_nombre",
            }],
            "estructuraDestino": "pais",
            "campoDestino"     : "id",            
        },
    ],

    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# PROCESAMIENTO ESTRUCTURA
elementos_comunes.procesaBaseGeneral(definicion)