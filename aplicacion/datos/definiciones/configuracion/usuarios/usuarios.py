#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint

# Definiciones sql
from librerias.datos.base import globales
from librerias.datos.sql import sqalchemy_leer

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general
from librerias.datos.sql import sqalchemy_tipo_campos as tipos
from librerias.datos.sql import sqalchemy_clase_dinamica
from librerias.datos.base import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes

def roles_especificos(r_):
    roles = []

    dependencia = None
    if r_.dependencia_id not in ["", None]:
        dependencia = sqalchemy_leer.leer_un_registro(
            "dependencias", 
            r_.dependencia_id
        )
        coordinadores_ids = dependencia["coordinadores_ids"]
        if (r_.id in coordinadores_ids):
            roles.append("COORDINADOR")
        
    if (r_.id == r_.jefe_id):
        roles.append("JEFE")

    if (r_.id == r_.archivo_id):
        roles.append("ARCHIVO")

    if (r_.id == r_.correspondencia_id):
        roles.append("CORRESPONDENCIA")

    if (r_.id == r_.pqrs_id):
        roles.append("PQRSD")

    # if roles:
    #    print("roles_especificos:", r_.codigo, r_.nombre, roles)

    return roles

def nombre_completo(r_):
    return ( r_.nombre + " - " + str(r_.dependencia_nombre_completo) )

campos = {
    "codigo": tipos.texto_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60, "reporte": "SI"}),     
    "nombre": tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120, "reporte": "SI"}),  
    "clave": tipos.texto(propiedades={"titulo": "Clave",  "longitud": 20}),  
    "correo": tipos.texto(propiedades={"titulo": "Correo", "longitud": 128, "reporte": "SI"}),  
    "dependencia_id": tipos.clave(propiedades={"titulo": "Dependencia/oficina",  "longitud": 60}),
    "reemplaza_id": tipos.clave(propiedades={"titulo": "Reemplaza/Encargo", "longitud": 60}),
    "estado_": tipos.texto_obligatorio(propiedades={"titulo": "Estado"}), 

    # Propiedades
    "roles_especificos": tipos.clave(
        propiedades={
            "columna": "no", 
            "titulo": "Roles especificos", 
            "propiedad": roles_especificos, 
            "reporte": "SI",
            "validador": "clave_lista"
        }
    ), 
    "nombre_completo": tipos.texto(propiedades={"columna": "no", "titulo": "Nombre completo", "longitud": 250, "propiedad": nombre_completo, "reporte": "SI"}),  
    "roles_ids": tipos.clave(
        propiedades= {
            "columna": "no",
            "titulo": "Roles del usuario", 
            "validador": "clave_lista", 
        }
    ),

    "ubicacion_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Ubicación (Territorial/Dependencia)", "longitud": 250, "reporte": "SI"}), 
    "ubicacion_id": tipos.texto(propiedades={"columna": "no", "titulo": "Ubicación id (Territorial/Dependencia)", "longitud": 64}), 
    "dependencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia (Area/Grupo)", "longitud": 250, "reporte": "SI"}), 
    "dependencia_nombre_completo": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia nombre completo (Area/Grupo)", "longitud": 250, "reporte": "SI"}), 
    "reemplaza_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Reemplaza", "longitud": 250, "reporte": "SI"}), 
}
"""
JCR // FALTA FECHA DE SALIDA A VACACIONES Y OTROS DATOS
"""

referencias = [
    {
        "campoReferencia": "dependencia_id",
        "atributosReferencia": [{
            "dependencia_nombre": "nombre",
            "dependencia_nombre_completo": "nombre_completo",
            "ubicacion_id": "ubicacion_id",
            "ubicacion_nombre": "ubicacion_nombre",
            "jefe_id": "jefe_id",
            "archivo_id": "archivo_id",
            "correspondencia_id": "correspondencia_id",
            "pqrs_id": "pqrs_id",
            "coordinadores_ids": "coordinadores_ids"
        }],
        "estructuraDestino": "dependencias",
        "campoDestino": "id"         
    },
    
    {
        "campoReferencia": "reemplaza_id",
        "atributosReferencia": [{
            "reemplaza_nombre": "nombre",
        }],
        "estructuraDestino": "usuarios",
        "campoDestino": "id"            
    },

    # ROLES
    {
        "campoReferencia": "roles_ids", 
        "atributosReferencia": [{
            "roles_nombres": "nombre",
            "roles_ids": "id",
        }],            
        "estructuraDestino": "roles",
        "campoDestino": "id",  
        "modo": "multiple",
        "externa": {
            "tipo_relacion": "ROLES DEL USUARIO"              
        }          
    }
]

definicion = {
    "descripcion": "Usuarios",
    "clase": "config_usuarios",
    "estructura": "usuarios",    
    "campos": campos,
    "referencias": referencias, 
    "campoIndice": "id",
    "indexa": "si",
    "indexamiento": {},
    "reporte": "SI" # Fuente de datos para REPORTES
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)