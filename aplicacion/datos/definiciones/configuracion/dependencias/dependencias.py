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
    return ( r_.nombre + " [ " + str(r_.ubicacion_nombre) + " ]" )

campos = {
    "codigo"            : tipos.texto_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60, "reporte": "SI"}),     
    "nombre"            : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120, "reporte": "SI"}),  
    "ubicacion_id"      : tipos.clave_obligatorio(propiedades={"titulo": "Ubicación geografica", "longitud": 60}),  
    "jefe_id"           : tipos.clave(propiedades={"titulo": "Jefe", "longitud": 60}),  
    "archivo_id"        : tipos.clave(propiedades={"titulo": "Encargado del archivo", "longitud": 60}),
    "correspondencia_id": tipos.clave(propiedades={"titulo": "Encargado de la Correspodencia", "longitud": 60}),
    "pqrs_id"           : tipos.clave(propiedades={"titulo": "Encargado dePRQS y Tramites", "longitud": 60}),        
    "padre_id"          : tipos.clave(propiedades={"titulo": "Dependencia Superior", "longitud": 60}),

    # Propiedades
    "nombre_completo"   : tipos.texto(propiedades={"columna": "no", "titulo": "Nombre completo", "longitud": 250, "propiedad": nombre_completo, "reporte": "SI"}),    
    "coordinadores_ids" : tipos.clave(
        propiedades= {
            "columna"  : "no",
            "titulo"   : "Coordinadores", 
            "validador": "clave_lista", 
        }
    ),  
    "coordinadores_nombres" : tipos.texto(propiedades={"columna": "no", "titulo": "Coordinadores", "longitud": 1000, "validador": "clave_lista", "reporte": "SI"}), 
    "ubicacion_nombre"      : tipos.texto(propiedades={"columna": "no", "titulo": "Territorial/Sede", "longitud": 250, "reporte": "SI"}), 
    "jefe_nombre"           : tipos.texto(propiedades={"columna": "no", "titulo": "Jefe Dependencia", "longitud": 250, "reporte": "SI"}), 
    "archivo_nombre"        : tipos.texto(propiedades={"columna": "no", "titulo": "Encargado de archivo", "longitud": 250, "reporte": "SI"}), 
    "correspondencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Encargado de correspondencia", "longitud": 250, "reporte": "SI"}), 
    "pqrs_nombre"           : tipos.texto(propiedades={"columna": "no", "titulo": "Encargado de PQRS", "longitud": 250, "reporte": "SI"}),     
    "padre_nombre"          : tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia superior gestión", "longitud": 250, "reporte": "SI"}), 
}

referencias = [
    # Territorial
    {
        "campoReferencia"    : "ubicacion_id",
        "atributosReferencia": [{
            "ubicacion_nombre"   : "nombre",
        }],
        "estructuraDestino": "ubicaciones",
        "campoDestino"     : "id",            
    },

    # JEFE DE LA DEPENDENCIA  
    {
        "campoReferencia"    : "jefe_id",
        "atributosReferencia": [{
            "jefe_nombre"   : "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    },

    # ENCARGADO DE ARCHIVO 
    {
        "campoReferencia"    : "archivo_id",
        "atributosReferencia": [{
            "archivo_nombre"   : "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    },

    # ENCARGADO DE CORRESPONDENCIA
    {
        "campoReferencia"    : "correspondencia_id",
        "atributosReferencia": [{
            "correspondencia_nombre"   : "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    },

    # ENCARGADO PQRS
    {
        "campoReferencia"    : "pqrs_id",
        "atributosReferencia": [{
            "pqrs_nombre"   : "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    },

    # COORDINADORES
    {
        # Campos de donde salen los datos de la referencia
        "campoReferencia"    : "coordinadores_ids", 
        "atributosReferencia": [{
            "coordinadores_nombres": "nombre",
            "coordinadores_ids"    : "id",
        }],            
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",  
        "modo"             : "multiple",
        "externa"          : {
            "tipo_relacion": "COORDINADORES DEPENDENCIA"            
        }          
    },

    # DEPENDENCIA PADRE
    {
        "campoReferencia"    : "padre_id",
        "atributosReferencia": [{
            "padre_nombre"   : "nombre",
        }],
        "estructuraDestino": "dependencias",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Dependencia",
    "clase"       : "config_dependencias",
    "estructura"  : "dependencias",    
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