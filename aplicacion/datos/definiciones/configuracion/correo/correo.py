#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from aplicacion.datos.clases.clases_base    import base_general_campos
from aplicacion.datos.definiciones._comunes import elementos_comunes

campos = {
    "codigo"       : elementos_comunes.codigo_obligatorio({}),
    "correo"       : elementos_comunes.correo_obligatorio({"titulo":"Correo", "unico":"si"}),
    "url_enlace"   : elementos_comunes.texto_obligatorio( {"titulo":"Url de enlace"}),
    "puerto_enlace": elementos_comunes.texto_obligatorio( {"titulo":"Puerto Url de enlace", "longitud": 6}),
    "clave"        : elementos_comunes.texto_obligatorio( {"titulo":"Clave", "longitud": 10}),
    "tipo_servicio": elementos_comunes.texto_obligatorio( {"titulo":"Tipo (SMTP/IMAP)", "longitud": 30}),
    "_estado_"     : elementos_comunes.estado_obligatorio({}),
}
campos.update(base_general_campos.campos)

# Campos elastic
# Campos que no van en la tabla SQL.
camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Correo",
    "clase"       : "base_general",
    "estructura"  : "correo",    
    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,
    # Referencias a otras estructuras
    "referencias" : [],
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# PROCESAMIENTO ESTRUCTURA
elementos_comunes.procesaBaseGeneral(definicion)