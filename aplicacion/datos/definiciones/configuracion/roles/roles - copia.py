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
    "codigo" : tipos.texto_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60}),     
    "nombre" : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120}),        
    "estado_":  tipos.texto_obligatorio(propiedades={"titulo": "Estado"}),

    "opciones_ids"    : tipos.clave(propiedades={"titulo": "Opciones del role", "columna": "no", "validador": "clave_lista"}),   
    "opciones_titulos": tipos.texto(propiedades={"titulo": "Opciones", "columna": "no", "validador": "clave_lista"}),    
    "acciones_ids"    : tipos.clave(propiedades={"titulo": "Acciones del role", "columna": "no", "validador": "clave_lista"}),   
    "acciones_nombres": tipos.texto(propiedades={"titulo": "Acciones", "columna": "no", "validador": "clave_lista"})
}
# Referencias a otras estructuras
referencias = [
    # OPCIONES
    {
        "campoReferencia"    : "opciones_ids",
        "atributosReferencia": [{
            "opciones_titulos": "titulo",
            "opciones_ids"    : "id",
        }],            
        "estructuraDestino": "opciones_sistema",
        "campoDestino"     : "id",  
        "modo"             : "multiple",
        "externa"          : {
            "tipo_relacion": "OPCIONES DEL ROLE"              
        }  
    },

    # ACCIONES
    {
        "campoReferencia"    : "acciones_ids",
        "atributosReferencia": [{
            "acciones_nombres": "nombre",
            "acciones_ids"    : "id",
        }],            
        "estructuraDestino": "acciones_sistema",
        "campoDestino"     : "id",  
        "modo"             : "multiple",
        "externa"          : {
            "tipo_relacion": "ACCIONES DEL ROLE"              
        }  
    }
]

definicion = {
    "descripcion" : "Roles",
    "clase"       : "config_roles",
    "estructura"  : "roles",    
    "campos"      : campos,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {},
    "referencias" : referencias
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)