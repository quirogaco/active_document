#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from aplicacion.datos.clases.clases_base    import base_general_campos
from aplicacion.datos.definiciones._comunes import elementos_comunes


# Campos estructura
campos = {
    "codigo"         : elementos_comunes.codigo_obligatorio({}),
    "nombre"         : elementos_comunes.nombre_obligatorio({}),
    "departamento_id": elementos_comunes.id_obligatorio({"titulo": "Departamento"}),
    "_estado_"       : elementos_comunes.estado_obligatorio({})
}
campos.update(base_general_campos.campos)

# Campos elastic
# Campos que no van en la tabla SQL.
camposIndexamiento = {
    "continente_nombre"  : elementos_comunes.elastic_texto,
    "pais_nombre"        : elementos_comunes.elastic_texto,
    "departamento_nombre": elementos_comunes.elastic_texto
}
camposElastic = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Ciudad",
    "clase"       : "base_general",
    "estructura"  : "ciudad",    
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,
    # Referencias a otras estructuras
    "referencias" : [
        {
            "campoReferencia"    : "departamento_id",
            "atributosReferencia": [{
                "departamento_nombre": "nombre",
                "pais_nombre"        : "pais_nombre",
                "continente_nombre"  : "continente_nombre",
            }],
            "estructuraDestino": "departamento",
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