#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint 

# Definiciones sql
from librerias.datos.base import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general
from librerias.datos.sql import sqalchemy_tipo_campos as tipos
from librerias.datos.sql import sqalchemy_clase_dinamica
from librerias.datos.base import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes

from . import gestion_campos
from . import gestion_referencias
from . import gestion_atributos
   
definicion = {
    "descripcion" : "Gestión de peticiones",
    "clase": "gestor_peticiones",
    "estructura": "peticiones",    
    "campos": gestion_campos.campos,
    "referencias": gestion_referencias.referencias,
    "campoIndice": "id",
    "indexa": "si",
    "indexamiento": {}
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( 
    definicion, 
    (
        base_general.DB_BASE_SIMPLE, 
        globales.CLASE_BASE_SQL
    ) 
)
globales.carga_clase(definicion["clase"], CLASE)

# Campos elastic
camposIndexamiento = gestion_campos.indexamiento.copy()
camposElastic = gestion_campos.campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)

# Evento al cargar
CLASE = globales.lee_clase(definicion["clase"])

# Eventos de clase y objeto
# GENERA ERROR DE RECURSIVIDAD
# def al_cargar(target, context):
#     # Primero trae Id de gestión para logs
#     print("")
#     print("................")
#     print("CARGA GESTION")
#     gestion_atributos.carga_radicado(target)    

# sqalchemy_clase_dinamica.asigna_evento(CLASE, "load", al_cargar)