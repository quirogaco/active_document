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


# Usuarios autorizados
def usuarios(_r):
    datos    = []
    #permisos = _r.datos.get("permisos", {})
    #datos    = permisos.datos.get("usuarios", [])
    datos    = _r.datos.get("usuarios", [])

    return datos

# Grupos autorizados
def grupos(_r):
    datos    = []
    #permisos = _r.datos.get("permisos", {})
    #datos    = permisos.datos.get("grupos", [])
    datos    = _r.datos.get("grupos", [])

    return datos

# Territoriales
def territoriales(_r):
    datos    = []
    #permisos = _r.datos.get("permisos", {})
    #datos    = permisos.datos.get("territoriales", [])
    datos    = _r.datos.get("territoriales", [])

    return datos

# Dependencias
def dependencias(_r):
    datos    = []
    #permisos = _r.datos.get("permisos", {})
    #datos    = permisos.datos.get("dependencias", [])
    datos    = _r.datos.get("dependencias", [])

    return datos

# Series
def series(_r):
    datos    = []
    #permisos = _r.datos.get("permisos", {})
    #datos    = permisos.datos.get("series", [])
    datos    = _r.datos.get("series", [])

    return datos

# SubSeries
def subseries(_r):
    datos    = []
    #permisos = _r.datos.get("permisos", {})
    #datos    = permisos.datos.get("subseries", [])
    datos    = _r.datos.get("subseries", [])

    return datos

campos = {
    "descripcion"  : tipos.clave_obligatorio(propiedades={"titulo": "Codigo", "longitud": 120}),         
    "datos"        : tipos.json(propiedades={"titulo": "Datos permisos", "defecto": 'json'}), 
    "usuarios"     : tipos.texto(propiedades={"columna": "no", "titulo": "Usuarios autorizados", "propiedad": usuarios}),
    "grupos"       : tipos.texto(propiedades={"columna": "no", "titulo": "Grupos autorizados",   "propiedad": grupos}),
    "territoriales": tipos.texto(propiedades={"columna": "no", "titulo": "Usuarios autorizados", "propiedad": territoriales}),
    "dependencias" : tipos.texto(propiedades={"columna": "no", "titulo": "Usuarios autorizados", "propiedad": dependencias}),
    "series"       : tipos.texto(propiedades={"columna": "no", "titulo": "Usuarios autorizados", "propiedad": series}),
    "subseries"    : tipos.texto(propiedades={"columna": "no", "titulo": "Usuarios autorizados", "propiedad": subseries})
}

referencias = []

definicion = {
    "descripcion" : "Permisos archivo",
    "clase"       : "config_permisos_archivo",
    "estructura"  : "permisos_archivo",    
    "campos"      : campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {},
    #"reporte"     : "SI" # Fuente de datos para REPORTES
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)