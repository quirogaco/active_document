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

campos = {
    # Elemento de permisos
    "elemento_tipo": tipos.clave_obligatorio(propiedades={"titulo": "Elemento tipo", "longitud": 60}),
    "elemento_id"  : tipos.clave_obligatorio(propiedades={"titulo": "Elemento id", "longitud": 60}),    
    "autorizacion" : tipos.texto_obligatorio(propiedades={"titulo": "Autorización", "longitud": 60}),   
    "autorizados"  : tipos.json(propiedades={"titulo": "Usuarios autorizados", "defecto": 'json'}), 
}

definicion = {
    "descripcion" : "Autorizaciones de acceso (Tabla de acceso TVD)",
    "clase"       : "agn_accesos_tvd",
    "estructura"  : "agn_accesos_tvd",    
    "campos"      : campos,
    "referencias" : [],
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

# Campos elastic
camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)