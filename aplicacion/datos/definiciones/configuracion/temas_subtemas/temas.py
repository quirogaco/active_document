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


campos = {
    "codigo"            : tipos.texto_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60, "reporte": "SI"}),     
    "nombre"            : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120, "reporte": "SI"}),       
    "dependencia_id"    : tipos.clave(propiedades={"titulo": "Dependencia", "longitud": 60}),   
    "dependencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia", "longitud": 250, "reporte": "SI"}), 
    "tramite_id"        : tipos.clave(propiedades={"titulo": "Tramite", "longitud": 60}),   
    "tramite_nombre"    : tipos.texto(propiedades={"columna": "no", "titulo": "Tramite", "longitud": 250, "reporte": "SI"}), 
}

referencias = [
    {
        "campoReferencia"    : "dependencia_id", 
        "atributosReferencia": [{
            "dependencia_nombre": "nombre",
        }],            
        "estructuraDestino": "dependencias",
        "campoDestino"     : "id",  
        "modo"             : "simple",
    },   
    {
        "campoReferencia"    : "tramite_id", 
        "atributosReferencia": [{
            "tramite_nombre": "nombre",
        }],            
        "estructuraDestino": "tramites",
        "campoDestino"     : "id",  
        "modo"             : "simple",
    },        
]

definicion = {
    "descripcion" : "Temas por dependencia",
    "clase"       : "config_temas",
    "estructura"  : "temas",    
    "campos"      : campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {},
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