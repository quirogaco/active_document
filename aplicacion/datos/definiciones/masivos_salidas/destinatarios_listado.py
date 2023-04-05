#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes

from . import destinatarios_listado_campos
from . import destinatarios_listado_referencias

definicion = {
    "descripcion" : "Listado de destinatarios",
    "clase"       : "ventanilla_destinatarios_lista",
    "estructura"  : "destinatarios_listado",    
    "campos"      : destinatarios_listado_campos.campos,
    "referencias" : destinatarios_listado_referencias.referencias,
    "campoIndice" : "id",
    "indexa"      : "no",
    "indexamiento": {}
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

# Campos elastic
camposIndexamiento = destinatarios_listado_campos.indexamiento.copy()
camposElastic      = destinatarios_listado_campos.campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)