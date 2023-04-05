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

# Arbol de DEPENDENCIA
def trd_dependencia(_r):
    arbol = []

    # Caga Series
    SERIE_CLASE = globales.lee_clase("agn_serie_trd")
    sesion = sqalchemy_comunes.nuevaSesion("base") 
    series = sesion.query(SERIE_CLASE).filter( SERIE_CLASE.dependencia_id == _r.id ).all()
    for serie in series:
        datos = {
            "id": serie.id,
            "codigo": serie.codigo,
            "nombre": serie.nombre,
            "padre_id": _r.id,
            "tipo": "serie"          
        }
        arbol.append(datos)

        arbol.extend(serie.serie_arbol)

    sesion.close()

    return arbol

def nombre_largo(_r):
    TRD_CLASE = globales.lee_clase("agn_trd")
    sesion = sqalchemy_comunes.nuevaSesion("base") 
    trd = sesion.query(TRD_CLASE).filter( TRD_CLASE.id == _r.trd_id ).first()
    nombre = _r.nombre + " - " + str(trd.territorial_nombre)
    sesion.close()

    return nombre


# Acceso
def acceso(_r):
    acceso = comunes_trd.recuperar_accesos("dependencia", _r.id) 

    return acceso


def dependencias_gestion(r_):
    datos = r_.datos.get("dependencias_gestion", "")
    
    return datos

campos = {
    # TRD/TVD
    "tabla": tipos.clave(propiedades={"titulo": "TRD/TVD", "longitud": 60}),

    # Trd Informaciósn
    "trd_id": tipos.clave_obligatorio(propiedades={"titulo": "Trd id", "longitud": 60}),
    "trd_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Trd descripción", "longitud": 250}),   
    "trd_version": tipos.texto(propiedades={"columna": "no", "titulo": "Trd Versión", "longitud": 250}),   
    "trd_estado": tipos.texto(propiedades={"columna": "no", "titulo": "Trd Estao", "longitud": 250}),  
    
    # Dependencia padre
    "dependencia_padre_id": tipos.clave(propiedades={"titulo": "Dependencia padre id", "longitud": 60}),
    "dependencia_padre_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Trd descripción", "longitud": 250}),   

    "codigo": tipos.clave_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60}),  
    "nombre": tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 250}),
    "nombre_largo" : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 250, "propiedad": nombre_largo}),
    "dependencia_arbol": tipos.texto(propiedades={"columna": "no", "tipoElastic": "objeto", "titulo": "Trd dependencia", "propiedad": trd_dependencia}),  
    "ubicaciones_gestion": tipos.texto(propiedades={"columna": "no", "titulo": "Ubicaciones gestion"}),
    "dependencias_gestion": tipos.clave(propiedades={"columna": "no", "titulo": "Dependencias gestion", "propiedad": dependencias_gestion}),
    "datos": tipos.json(propiedades={"titulo": "Datos adicionales", "defecto": 'json'}), 
    # Acceso
    "acceso": tipos.json(propiedades={"columna": "no", "tipoElastic": "objeto", "titulo": "Trd serie", "propiedad": acceso})
}

referencias = [
    # Aqui toca revisarlo cuando es TVD LA DEPENDENCIA
    # Trd
    {
        "campoReferencia"    : "trd_id",
        "atributosReferencia": [{
            "trd_nombre" : "nombre",
            "trd_version": "version",
            "trd_activa" : "estado_",
            "ubicaciones_gestion": "ubicaciones_gestion"
        }],
        "estructuraDestino": "agn_trd",
        "campoDestino"     : "id",            
    },

    # Dependencia Trd
    {
        "campoReferencia"    : "dependencia_padre_id",
        "atributosReferencia": [{
            "dependencia_padre_nombre": "nombre",
        }],
        "estructuraDestino": "agn_dependencia_trd",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Dependencia Tabla de Retención",
    "clase"       : "agn_dependencia_trd",
    "estructura"  : "agn_dependencia_trd",    
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