#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from aplicacion.datos.clases.clases_base    import base_general_campos
from aplicacion.datos.definiciones._comunes import elementos_comunes

campos = {
    "nombre"     : elementos_comunes.nombre_obligatorio(),
    "consecutivo": elementos_comunes.entero_obligatorio({"titulo": "Valor del consecutivo"}),
    "_estado_"   : elementos_comunes.estado_obligatorio(),    
}
campos.update(base_general_campos.campos)

# Campos elastic
# Campos que no van en la tabla SQL.
camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Consecutivo",
    "clase"       : "base_general",
    "estructura"  : "consecutivo",
    
    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# PROCESAMIENTO ESTRUCTURA
elementos_comunes.procesaBaseGeneral(definicion)