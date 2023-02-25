#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint, datetime

from aplicacion.datos.definiciones._comunes import elementos_comunes

from . import unico_campos

# Campos elastic
camposElastic = unico_campos.campos.copy()
#camposIndexamiento = unico_campos.indexamiento.copy()
#camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion": "Radicados unificados",
    "clase": "gestor_radicados_unico",
    "estructura": "radicados_unico",    
    "mixta": "radicados_entrada,radicados_salida,radicados_interno",    
    "campos": unico_campos.campos,    
    "camposIndexamiento": [],
    "archivos": {},
    # Referencias a otras estructuras
    "referencias": [],
    "campoIndice": "id",
    "indexa": "si",
    "indexamiento": {}
}

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)