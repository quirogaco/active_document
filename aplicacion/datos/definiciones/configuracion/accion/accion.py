#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from aplicacion.datos.clases.clases_base    import base_general_campos
from aplicacion.datos.definiciones._comunes import elementos_comunes

# Campos estructura
campos = {
    "codigo"  : elementos_comunes.codigo_obligatorio({}),
    "nombre"  : elementos_comunes.nombre_obligatorio({}),
    "_estado_": elementos_comunes.estado_obligatorio({}),
}
campos.update(base_general_campos.campos)

# Campos elastic
# Campos que no van en la tabla SQL.
camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Acciones",
    "clase"       : "base_general",
    "estructura"  : "accion",    
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