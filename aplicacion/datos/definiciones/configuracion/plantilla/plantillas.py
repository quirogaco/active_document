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
from aplicacion.archivos                    import archivo_indexa

def tipo_archivo(_r):
    archivos = _r.archivos
    tipo     = ""
    if len(archivos) > 0:
        tipo = archivos[0]["tipo_archivo"]
        
    return tipo

def archivo_procesamiento(_r):
    if getattr(_r, "_archivos", None) is None:
        archivos = archivo_indexa.indexa_archivos("plantillas", _r.id)
        setattr(_r, "_archivos", archivos)
    else:    
        archivos = _r._archivos    
    
    return archivos

campos = {
    "descripcion"       : tipos.texto_obligatorio(propiedades={"titulo": "Descripción", "longitud": 256, "reporte": "SI"}),     
    "dependencia_id"    : tipos.clave(propiedades={"titulo": "dependencia_id", "longitud": 60}),  
    "dependencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia nombre", "longitud": 250}),    
    "archivos"          : tipos.clave(propiedades={"columna": "no", "titulo": "Archivos","propiedad": archivo_procesamiento}),
    "tipo_archivo"      : tipos.texto(propiedades={"columna": "no", "titulo": "Tipo Archivo", "propiedad": tipo_archivo}), 
}

referencias = [
    # Dependencia
    {
        "campoReferencia"    : "dependencia_id",
        "atributosReferencia": [{
            "dependencia_nombre"   : "nombre_completo",
        }],
        "estructuraDestino": "dependencias",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Plantillas",
    "clase"       : "config_plantillas",
    "estructura"  : "plantillas",    
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

############
# Archivos #
############    
from aplicacion.datos.comunes.elastic import archivos
# Campos adicionales de indexamiento
indexamiento = {
    "archivos": archivos.archivos_estructura
}

# Campos elastic
camposIndexamiento = indexamiento.copy()
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)