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

def nombre_completo(r_):
    nombre_completo = ""
    """
    if (r_.clase is None):
        r_.clase = "ANONIMO"    
    """

    # Calcula nombre completo
    #if (r_.clase != "ANONIMO"):
    if (True):
        # Nombres
        nombre = ""
        if (r_.nombres not in ["", None]):
                nombre = str(r_.nombres)

        if (r_.apellidos not in ["", None]):
                nombre += " " + str(r_.apellidos)  
        nombre = nombre.strip()

        # Razon social
        razon_social = ""    
        if (r_.razon_social not in ["", None]):
            #r_.clase = "" 
            razon_social = r_.razon_social
        razon_social = razon_social.strip()
            
        # Nombre completo
        nombre_completo = razon_social
        if nombre_completo != "":
            if nombre != "":
                nombre_completo +=  " - " + nombre
        else:
            nombre_completo = nombre

    #if (r_.nombres in ["", None]) and (r_.apellidos in ["", None]) and (r_.razon_social in ["", None]):
    #    r_.clase = "ANONIMO" 

    nombre_completo += " [ " + str(r_.clase) + " ]"

    if (r_.tipo_tercero_nombre not in ["", None]):
        nombre_completo += " [ " + str(r_.tipo_tercero_nombre) + " ]"

    nombre_completo = nombre_completo.strip()

    return nombre_completo

def nombres_apellidos(r_):
    nombre = ""
    if (r_.nombres not in ["", None]):
        nombre = str(r_.nombres)

    if (r_.apellidos not in ["", None]):
        nombre += " " + str(r_.apellidos)  
    nombre = nombre.strip()

    return nombre

campos = {
    # JURIDICA, NATURAL, ANONIMO 
    "clase"                : tipos.texto(propiedades={"titulo": "Clase de tercero", "longitud": 60}),     

    # ORIGEN
    "radicado"            : tipos.texto(propiedades={"titulo": "Pertenece a radicado", "longitud": 60, "defecto": "NO"}),  

    # Ong, entidad control, publica, estudiante, profesional 
    "tipo_tercero_id"    : tipos.texto(propiedades={"titulo": "Tipo de tercero id", "longitud": 60}),    
    "tipo_tercero_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Tipo de tercero", "longitud": 250}),    

    # Identificación person natural
    "tipo_identificacion_id"    : tipos.clave(propiedades={"titulo": "Tipo identificación", "longitud": 60}),   
    "tipo_identificacion_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Tipo identificación", "longitud": 250}), 

    # Persona natural/juridica
    "nro_identificacion"   : tipos.texto(propiedades={"titulo": "Nit/Identificación", "longitud": 60}),    
    # Persona juridica
    "razon_social"         : tipos.texto(propiedades={"titulo": "Razon social", "longitud": 256}),
    "cargo"                : tipos.texto(propiedades={"titulo": "Cargo", "longitud": 128}),
    # Persona natural
    "nombres"              : tipos.texto(propiedades={"titulo": "Nombres", "longitud": 256}),
    "apellidos"            : tipos.texto(propiedades={"titulo": "Apellidos", "longitud": 256}),

    # Ubicación
    "correo_electronico"   : tipos.texto(propiedades={"titulo": "Correo electrónico", "longitud": 512}),
    "direccion"            : tipos.texto(propiedades={"titulo": "Dirección", "longitud": 128}),
    "codigo_postal"        : tipos.texto(propiedades={"titulo": "Codigo postal", "longitud": 128}),
    "telefono"             : tipos.texto(propiedades={"titulo": "Telefono", "longitud": 64}),
    "telefono_movil"       : tipos.texto(propiedades={"titulo": "Telefono movil", "longitud": 64}),
    "fax"                  : tipos.texto(propiedades={"titulo": "Fax", "longitud": 64}),

    "ciudad_id"            : tipos.clave(propiedades={"titulo": "Ciudad id", "longitud": 60}),   
    "ciudad_nombre"        : tipos.texto(propiedades={"columna": "no", "titulo": "Ciudad", "longitud": 250}),    

    # Propiedades
    "nombre_completo"   : tipos.texto(propiedades={"columna": "no", "titulo": "Nombre completo", "longitud": 250, "propiedad": nombre_completo}),
    "nombres_apellidos" : tipos.texto(propiedades={"columna": "no", "titulo": "Nombres y apellidos", "longitud": 250, "propiedad": nombres_apellidos})
}

referencias = [
    # Tipo tercero
    {
        "campoReferencia"    : "tipo_tercero_id",
        "atributosReferencia": [{
            "tipo_tercero_nombre": "nombre",
        }],
        "estructuraDestino": "tipo_terceros",
        "campoDestino"     : "id",            
    },

    # Identificación
    {
        "campoReferencia"    : "tipo_identificacion_id",
        "atributosReferencia": [{
            "tipo_identificacion_nombre": "nombre",
        }],
        "estructuraDestino": "tipo_identificaciones",
        "campoDestino"     : "id",            
    },

    # Ciudad
    {
        "campoReferencia"    : "ciudad_id",
        "atributosReferencia": [{
            "ciudad_nombre": "nombre_completo",
        }],
        "estructuraDestino": "ciudades",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Terceros",
    "clase"       : "config_terceros",
    "estructura"  : "terceros",    
    "campos"      : campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)