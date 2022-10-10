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

def folios_electronicos(_r):    
    folios   = 0        
    archivos = _r.archivos
    if len(archivos) > 0:
        folios = archivos[0]["folios"]
    
    return folios

def tipo_archivo(_r):
    archivos = _r.archivos
    tipo     = ""
    if len(archivos) > 0:
        tipo = archivos[0]["tipo_archivo"]
        
    return tipo

def tamano(_r):
    archivos = _r.archivos
    tamano   = ""
    if len(archivos) > 0:
        tamano = archivos[0]["tamano"]
        
    return tamano

def archivo_procesamiento(_r):
    if getattr(_r, "_archivos", None) is None:
        archivos = archivo_indexa.indexa_archivos("agn_documentos_tvd", _r.id)
        setattr(_r, "_archivos", archivos)
    else:    
        archivos = _r._archivos        

    pprint.pprint(archivos)

    return archivos

def fecha_incorporado(_r):
    
    return _r.creado_en_

campos = {
    # TRD/TVD
    "tabla"              : tipos.clave(propiedades={"titulo": "TRD/TVD", "longitud": 60}),
    
    # Expediente 
    "expediente_id"      : tipos.clave(propiedades={"titulo": "Expediente id", "longitud": 60}),
    "expediente_nombre"  : tipos.texto(propiedades={"columna": "no", "titulo": "Expediente nombre", "longitud": 250}),  

    # Carpeta
    "carpeta_nro"        : tipos.clave(propiedades={"titulo": "Carpeta del expediente", "longitud": 64}),  

    "detalle"            : tipos.texto_obligatorio(propiedades={"titulo": "Descripcion", "longitud": 250}),      
    "fecha_creacion"     : tipos.fecha_obligatorio(propiedades={"titulo": "Fecha creaci�n"}),
    "fecha_incorporado"  : tipos.fecha_obligatorio(propiedades={"columna": "no", "titulo": "Fecha incorporado", "propiedad": fecha_incorporado}),      
    "soporte"            : tipos.clave(propiedades={"titulo": "Soporte", "longitud": 60}), # FISICO, ELECTRONICO, DIGITALIZADO 
    "folios_fisicos"     : tipos.entero(propiedades={"titulo": "Folios fisicos", "tipoElastic": "entero_ordenado"}),
    "folios_electronicos": tipos.entero(propiedades={"columna": "no", "titulo": "Folios electronicos", "tipoElastic": "entero_ordenado", "propiedad": folios_electronicos}),  
    "tipo_archivo"       : tipos.texto(propiedades={"columna": "no", "titulo": "Tipo Archivo", "propiedad": tipo_archivo}), 
    "tamano"             : tipos.entero(propiedades={"columna": "no", "titulo": "Tama�o", "tipoElastic": "entero_ordenado", "propiedad": tamano}), 

    # Fecha inicial/ final del EXPEDIENTE
    "fecha_funcion"      : tipos.clave(propiedades={"titulo": "Es documento final/inicial", "longitud": 64}),

    ############
    # archivos #
    ############
    "archivos"           : tipos.clave(propiedades={"columna": "no", "titulo": "Archivos","propiedad": archivo_procesamiento})
}

referencias = [
    # Expediente Tvd
    {
        "campoReferencia"    : "expediente_id",
        "atributosReferencia": [{
            "expediente_nombre": "nombre"
        }],
        "estructuraDestino": "agn_expedientes_tvd",
        "campoDestino"     : "id",            
    }
]

# Definici�n
definicion = {
    "descripcion" : "Documentos Tvd",
    "clase"       : "agn_documentos_tvd",
    "estructura"  : "agn_documentos_tvd",    
    "campos"      : campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

# la esructura de definicion["campos"], esta ampliada por  sqalchemy_clase_dinamica.crea_clase
# por eso elastic debe ir aqui depues de sqalchemy_clase_dinamica.crea_clase

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