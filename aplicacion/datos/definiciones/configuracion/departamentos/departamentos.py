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
    "codigo"           : tipos.texto_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60, "reporte": "SI"}),     
    "nombre"           : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120, "reporte": "SI"}),  
    "pais_id"          : tipos.clave_obligatorio(propiedades={"titulo": "Pais"}),          
    "pais_nombre"      : tipos.texto(propiedades={"columna": "no", "titulo": "Pais", "longitud": 250, "reporte": "SI"}), 
    "continente_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Continente", "longitud": 250, "reporte": "SI"}), 
    "estado_"          : tipos.texto_obligatorio(propiedades={"titulo": "Estado"})    
}

definicion = {
    "descripcion" : "Departamento",
    "clase"       : "config_departamentos",
    "estructura"  : "departamentos",    
    "campos"      : campos,
    "referencias" : [
        {
            "campoReferencia"    : "pais_id",
            "atributosReferencia": [{
                "pais_nombre"      : "nombre",
                "continente_nombre": "continente_nombre",
            }],
            "estructuraDestino": "paises",
            "campoDestino"     : "id",            
        },
    ],

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