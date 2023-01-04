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
from aplicacion.archivos                    import archivo_indexa

def archivo_procesamiento(_r):
    if getattr(_r, "_archivos", None) is None:
        archivos = archivo_indexa.indexa_archivos("correos", _r.id)
        setattr(_r, "_archivos", archivos)
    else:    
        archivos = _r._archivos    
    
    return archivos

campos = {
    "correo_entidad": tipos.clave(propiedades={"titulo": "Correo entidad", "longitud": 256}), 
    "correo_origen": tipos.clave(propiedades={"titulo": "Correo origen", "longitud": 256}),       
    "asunto"       : tipos.texto(propiedades={"titulo": "Asunto", "longitud": 1024}),    
    "fecha_correo" : tipos.fecha(propiedades={"titulo": "Fecha correo"}),  
    "estado"       : tipos.clave(propiedades={"titulo": "Estado", "longitud": 60}),
    "radicado"     : tipos.clave(propiedades={"titulo": "Radicado", "longitud": 60}),
    "archivos"     : tipos.clave(propiedades={"columna": "no", "titulo": "Archivos","propiedad": archivo_procesamiento}),
}

referencias = []

definicion = {
    "descripcion" : "Correos descargados",
    "clase"       : "global_correos_descargados",
    "estructura"  : "correos_descargados",    
    "campos"      : campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
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