#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

from sqlalchemy import and_

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes
from librerias.datos.sql                    import sqalchemy_comunes

# Arbol de DEPENDENCIA
def tvd_dependencia(_r):
    arbol = []

    # Caga Series
    SERIE_CLASE = globales.lee_clase("agn_serie_tvd")
    sesion      = sqalchemy_comunes.nuevaSesion("base") 
    filtros     = and_( SERIE_CLASE.dependencia_id == _r.id, SERIE_CLASE.tabla == "TVD")
    series      = sesion.query(SERIE_CLASE).filter( filtros ).all()
    for serie in series:
        datos = {
            "id"      : serie.id,
            "codigo"  : serie.codigo,
            "nombre"  : serie.nombre,
            "padre_id": _r.id,
            "tipo"    : "serie"          
        }
        arbol.append(datos)

        arbol.extend(serie.serie_arbol)

    sesion.close()

    return arbol

campos = {
    # TRD/TVD
    "tabla"              : tipos.clave(propiedades={"titulo": "TRD/TVD", "longitud": 60}),
    
    # Tvd Información
    "tvd_id"       : tipos.clave_obligatorio(propiedades={"titulo": "Tvd id", "longitud": 60}),
    "tvd_nombre"   : tipos.texto(propiedades={"columna": "no", "titulo": "Tvd descripción", "longitud": 250}),   
    "tvd_version"  : tipos.texto(propiedades={"columna": "no", "titulo": "Tvd Versión", "longitud": 250}),   
    "tvd_estado"   : tipos.texto(propiedades={"columna": "no", "titulo": "Tvd Estado", "longitud": 250}),  
    
    # Dependencia padre
    "dependencia_padre_id"    : tipos.clave(propiedades={"titulo": "Dependencia padre id", "longitud": 60}),
    "dependencia_padre_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia nombre", "longitud": 250}),   

    "codigo"       : tipos.clave_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60}),  
    "nombre"       : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 250}),
    "dependencia_arbol": tipos.texto(propiedades={"columna": "no", "tipoElastic": "objeto", "titulo": "Tvd dependencia", "propiedad": tvd_dependencia}),  
}

referencias = [
    # Tvd
    {
        "campoReferencia"    : "tvd_id",
        "atributosReferencia": [{
            "tvd_nombre" : "nombre",
            "tvd_version": "version",
            "tvd_activa" : "estado_",
        }],
        "estructuraDestino": "agn_tvd",
        "campoDestino"     : "id",            
    },

    # Dependencia Trd
    {
        "campoReferencia"    : "dependencia_padre_id",
        "atributosReferencia": [{
            "dependencia_padre_nombre": "nombre",
        }],
        "estructuraDestino": "agn_dependencia_tvd",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Dependencia Tabla de Valoración",
    "clase"       : "agn_dependencia_tvd",
    "estructura"  : "agn_dependencia_tvd",    
    "campos"      : campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

# Campos elastic
camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)