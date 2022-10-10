#!/usr/bin/python
# -*- coding: UTF-8 -*-
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


# Arbol de TRD
def trd_arbol(_r):
    arbol = []

    DEPENDENCIA_CLASE = globales.lee_clase("agn_dependencia_trd")
    sesion            = sqalchemy_comunes.nuevaSesion("base") 
    filtros           = and_(DEPENDENCIA_CLASE.trd_id == _r.id, DEPENDENCIA_CLASE.tabla == "TRD")
    dependencias      = sesion.query(DEPENDENCIA_CLASE).filter( filtros ).all()
    for dependencia in dependencias:
        dato = {
            "id"    : dependencia.id,
            "codigo": dependencia.codigo,  
            "nombre": dependencia.nombre,            
            "tipo"  : "dependencia"              
        }  
        if dependencia.dependencia_padre_id in ["", None]:           
            # Raiz  
            arbol.append(dato) 
        else:
            # Si esta bajo otra dependencia
            dato["padre_id"] = dependencia.dependencia_padre_id
            arbol.append(dato)     

        #  Series
        arbol.extend(dependencia.dependencia_arbol)

    sesion.close()

    #pprint.pprint(arbol)

    return arbol

campos = {
    "fondo_id"     : tipos.clave_obligatorio(propiedades={"titulo": "Fondo id", "longitud": 60}),
    "fondo_nombre" : tipos.texto(propiedades={"columna": "no", "titulo": "Fondo documental", "longitud": 250}),   
    "sigla"        : tipos.clave_obligatorio(propiedades={"titulo": "Sigla fondo", "longitud": 60}),  
    "nombre"       : tipos.texto_obligatorio(propiedades={"titulo": "Nombre fondo", "longitud": 250}),  
    "fecha_version": tipos.fecha_obligatorio(propiedades={"titulo": "Fecha versión"}),
    "version"      : tipos.clave_obligatorio(propiedades={"titulo": "Versión", "longitud": 20}),    
    "territorial_codigo": tipos.clave_obligatorio(propiedades={"titulo": "Codigo Territorial/Sede", "longitud": 20}),    
    "territorial_nombre": tipos.clave_obligatorio(propiedades={"titulo": "Nombre Territorial/Sede", "longitud": 200}),    
    
    # TRD COMPLETA
    "trd_arbol"     : tipos.texto(propiedades={"columna": "no", "tipoElastic": "objeto", "titulo": "Trd completa", "propiedad": trd_arbol}),   
}

referencias = [
    # Fondo
    {
        "campoReferencia"    : "fondo_id",
        "atributosReferencia": [{
            "fondo_nombre": "nombre",
        }],
        "estructuraDestino": "agn_fondo_documental",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Tabla de Retención",
    "clase"       : "agn_trd",
    "estructura"  : "agn_trd",    
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