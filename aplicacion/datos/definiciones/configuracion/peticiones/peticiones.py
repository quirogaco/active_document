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
    "total_tiempo"      : tipos.entero(propiedades={"titulo": "Tiempo total", "reporte": "SI"}), 
    "alertar_tiempo"    : tipos.texto(propiedades={"titulo": "Tiempo para alertar ", "reporte": "SI"}),      
    "alertar_porcentaje": tipos.texto(propiedades={"titulo": "Porcentaje para alertar", "reporte": "SI"}),       
    "horas_dias"        : tipos.texto_obligatorio(propiedades={"titulo": "Horas ó dias", "longitud": 32, "reporte": "SI"}),       
    "tipo_tiempo"       : tipos.texto_obligatorio(propiedades={"titulo": "Calculo de tiempo en", "longitud": 32, "reporte": "SI"}),  
    "modifica_tiempo"   : tipos.texto_obligatorio(propiedades={"titulo": "Modifica tiempo", "longitud": 10, "reporte": "SI"}),          
    "pqrs"              : tipos.texto_obligatorio(propiedades={"titulo": "Es PQRS", "longitud": 10, "reporte": "SI"}), 
    "bloquear"          : tipos.entero(propiedades={"titulo": "Bloquear traslado (dias)", "reporte": "SI"}),      
    "estado_"           : tipos.texto_obligatorio(propiedades={"titulo": "Estado", "reporte": "SI"}),

    "dependencias_ids"    : tipos.clave(propiedades={"titulo": "Dependencias", "columna": "no", "validador": "clave_lista"}),   
    "dependencias_nombres": tipos.texto(propiedades={"titulo": "Dependencias", "columna": "no", "validador": "clave_lista"})
}

referencias = [
    {
        "campoReferencia"    : "dependencias_ids", 
        "atributosReferencia": [{
            "dependencias_nombres": "nombre",
            "dependencias_ids"    : "id",
        }],            
        "estructuraDestino": "dependencias",
        "campoDestino"     : "id",  
        "modo"             : "multiple",
        "externa"          : {
            "tipo_relacion": "DEPENDENCIAS POR PETICION"              
        }                  
    },        
]

definicion = {
    "descripcion" : "Tipo de Peticiones",
    "clase"       : "config_tipo_peticiones",
    "estructura"  : "tipo_peticiones",    
    "campos"      : campos,
    "referencias" : referencias,
    #"referencias" : [],
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