#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes

def opciones_id(r_):
    opciones = r_.datos.get("opciones", [])
    
    return opciones

campos = {
    "nombre"     : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120, "reporte": "SI"}),   
    "datos"      : tipos.json(propiedades={"titulo": "Datos especificos", "defecto": 'json'}),   
    "opciones_id": tipos.clave(propiedades={"columna": "no", "titulo": "Opciones id", "propiedad": opciones_id}),     
}

definicion = {
    "descripcion" : "Roles",
    "clase"       : "config_roles",
    "estructura"  : "roles",    
    "campos"      : campos,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {},
    "referencias" : [],
    "reporte"     : "SI" # Fuente de datos para REPORTES
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)