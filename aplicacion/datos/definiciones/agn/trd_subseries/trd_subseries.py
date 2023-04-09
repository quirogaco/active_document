#!/usr/bin/python
# -*- coding: utf-8 -*-
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
from aplicacion.trd                         import comunes as comunes_trd

# Arbol de SUBSERIE
def trd_subserie(_r):
    arbol = []

    # Caga Tipos
    TIPO_CLASE = globales.lee_clase("agn_tipo_documental_trd")
    sesion     = sqalchemy_comunes.nuevaSesion("base") 
    tipos      = sesion.query(TIPO_CLASE).filter( TIPO_CLASE.subserie_id == _r.id ).all()
    for tipo in tipos:
        datos = {
            "id"      : tipo.id,
            "codigo"  : "",
            "nombre"  : tipo.nombre,
            "padre_id": _r.id,
            "tipo"    : "tipo"          
        }
        arbol.append(datos)
    sesion.close()

    return arbol

# Acceso
def acceso(_r):
    acceso = comunes_trd.recuperar_accesos("dependencia", _r.id) 

    return acceso

campos = {
    # TRD/TVD
    "tabla"              : tipos.clave(propiedades={"titulo": "TRD/TVD", "longitud": 60}),
    
    # Serie padre
    "serie_id"    : tipos.clave_obligatorio(propiedades={"titulo": "Dependencia padre id", "longitud": 60}),
    "serie_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia descripción", "longitud": 250}),
    "version"     : tipos.texto(propiedades={"columna": "no", "titulo": "Trd versión", "longitud": 250}),   
    "activa"      : tipos.texto(propiedades={"columna": "no", "titulo": "Trd activadescripción", "longitud": 250}),    
    "ubicaciones_gestion": tipos.texto(propiedades={"columna": "no", "titulo": "Ubicaciones gestion"}),
    "dependencias_gestion": tipos.clave(propiedades={"columna": "no", "titulo": "Dependencias gestion"}), 
    "dependencia_id": tipos.clave(propiedades={"columna": "no", "titulo": "Dependencia trd"}),   

    "codigo"            : tipos.clave_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60}),  
    "nombre"            : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 250}), 

    # Retención
    "gestion"           : tipos.entero(propiedades={"titulo": "Aóos en archivo de gestion"}), 
    "central"           : tipos.entero(propiedades={"titulo": "Aóos en archivo central"}), 

    # Disposición
    "eliminacion"         : tipos.texto(propiedades={"titulo": "Eliminación", "defecto": "NO"}),    
    "seleccion"           : tipos.texto(propiedades={"titulo": "Selección", "defecto": "NO"}),  
    "conservacion"        : tipos.texto(propiedades={"titulo": "Conservación", "defecto": "NO"}),  
    "micro_digitalizacion": tipos.texto(propiedades={"titulo": "Micro digitalización", "defecto": "NO"}),
    "subserie_arbol"      : tipos.texto(propiedades={"columna": "no", "tipoElastic": "objeto", "titulo": "Trd serie", "propiedad": trd_subserie}),

    # Acceso
    "acceso"              : tipos.json(propiedades={"columna": "no", "tipoElastic": "objeto", "titulo": "Trd serie", "propiedad": acceso})
}

referencias = [
    # Serie Trd
    {
        "campoReferencia"    : "serie_id",
        "atributosReferencia": [{
            "serie_nombre": "nombre",
            "ubicaciones_gestion": "ubicaciones_gestion",
            "dependencias_gestion": "dependencias_gestion",
            "dependencia_id": "dependencia_id",
            "version"     : "version",
            "activa"      : "estado",
        }],
        "estructuraDestino": "agn_serie_trd",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "SubSerie Tabla de Retención",
    "clase"       : "agn_subserie_trd",
    "estructura"  : "agn_subserie_trd",    
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