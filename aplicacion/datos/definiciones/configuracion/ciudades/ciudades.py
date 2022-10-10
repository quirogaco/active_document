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

def nombre_completo(r_):
    return ( r_.nombre + " " + str(r_.departamento_nombre) + " " + str(r_.pais_nombre) + " " + str(r_.continente_nombre) ) 

# Campos estructura
campos = {
    "codigo"             : tipos.texto_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60, "reporte": "SI"}),     
    "nombre"             : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120, "reporte": "SI"}),  
    "nombre_completo"    : tipos.texto(propiedades={"columna": "no", "titulo": "Nombre completo", "longitud": 250, "propiedad": nombre_completo, "reporte": "SI"}),          
    "departamento_id"    : tipos.clave_obligatorio(propiedades={"titulo": "Departamento"}), 
    "estado_"            : tipos.texto_obligatorio(propiedades={"titulo": "Estado"}),

    # Propiedades
    "departamento_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Departamento", "longitud": 250, "reporte": "SI"}),   
    "pais_nombre"        : tipos.texto(propiedades={"columna": "no", "titulo": "Pais", "longitud": 250, "reporte": "SI"}), 
    "continente_nombre"  : tipos.texto(propiedades={"columna": "no", "titulo": "Continente", "longitud": 250, "reporte": "SI"}),      
}

definicion = {
    "descripcion" : "Ciudad",
    "clase"       : "config_ciudades",
    "estructura"  : "ciudades",    
    "campos"      : campos,
    "referencias" : [
        {
            "campoReferencia"    : "departamento_id",
            "atributosReferencia": [{
                "departamento_nombre": "nombre",
                "pais_nombre"        : "pais_nombre",
                "continente_nombre"  : "continente_nombre",
            }],
            "estructuraDestino": "departamentos",
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