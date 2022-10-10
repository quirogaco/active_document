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
    return ( r_.nombre + " - " + str(r_.dependencia_nombre_completo) )

campos = {
    "codigo"        : tipos.texto_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60, "reporte": "SI"}),     
    "nombre"        : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120, "reporte": "SI"}),  
    "clave"         : tipos.texto(propiedades={"titulo": "Clave",  "longitud": 20}),  
    "correo"        : tipos.texto(propiedades={"titulo": "Correo", "longitud": 128, "reporte": "SI"}),  
    "dependencia_id": tipos.clave(propiedades={"titulo": "Dependencia/oficina",  "longitud": 60}),
    "reemplaza_id"  : tipos.clave(propiedades={"titulo": "Reemplaza/Encargo", "longitud": 60}),
    "estado_"       : tipos.texto_obligatorio(propiedades={"titulo": "Estado"}), 

    # Propiedades
    # Propiedades
    "nombre_completo": tipos.texto(propiedades={"columna": "no", "titulo": "Nombre completo", "longitud": 250, "propiedad": nombre_completo, "reporte": "SI"}),  
    "roles_ids"  : tipos.clave(
        propiedades= {
            "columna"  : "no",
            "titulo"   : "Roles del usuario", 
            "validador": "clave_lista", 
        }
    ),

    "ubicacion_nombre"  : tipos.texto(propiedades={"columna": "no", "titulo": "Ubicación (Territorial/Dependencia)", "longitud": 250, "reporte": "SI"}), 
    "ubicacion_id"      : tipos.texto(propiedades={"columna": "no", "titulo": "Ubicación id (Territorial/Dependencia)", "longitud": 64}), 
    "dependencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia (Area/Grupo)", "longitud": 250, "reporte": "SI"}), 
    "dependencia_nombre_completo": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia nombre completo (Area/Grupo)", "longitud": 250, "reporte": "SI"}), 
    "reemplaza_nombre"  : tipos.texto(propiedades={"columna": "no", "titulo": "Reemplaza", "longitud": 250, "reporte": "SI"}), 
}
"""
JCR // FALTA FECHA DE SALIDA A VACACIONES Y OTROS DATOS
"""

referencias = [
    {
        "campoReferencia"    : "dependencia_id",
        "atributosReferencia": [{
            "dependencia_nombre"         : "nombre",
            "dependencia_nombre_completo": "nombre_completo",
            "ubicacion_id"               : "ubicacion_id",
            "ubicacion_nombre"           : "ubicacion_nombre"
        }],
        "estructuraDestino": "dependencias",
        "campoDestino"     : "id"         
    },
    
    {
        "campoReferencia"    : "reemplaza_id",
        "atributosReferencia": [{
            "reemplaza_nombre"   : "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id"            
    },

    # ROLES
    {
        "campoReferencia"    : "roles_ids", 
        "atributosReferencia": [{
            "roles_nombres": "nombre",
            "roles_ids"    : "id",
        }],            
        "estructuraDestino": "roles",
        "campoDestino"     : "id",  
        "modo"             : "multiple",
        "externa"          : {
            "tipo_relacion": "ROLES DEL USUARIO"              
        }          
    }
]

definicion = {
    "descripcion" : "Usuarios",
    "clase"       : "config_usuarios",
    "estructura"  : "usuarios",    
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