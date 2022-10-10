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
from aplicacion.datos.comunes.referencias   import archivos

campos = {
    "formulario_id"    : tipos.clave_obligatorio(propiedades={"titulo": "Codigo", "longitud": 120}),        
    "formulario_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Formulario  nombre", "longitud": 250, "reporte": "SI"}), 
    "versiones"        : tipos.entero(propiedades={"titulo": "Versiones", "defecto":0}),
    "actuales"         : tipos.json(propiedades={"titulo": "Datos dinamicos actuales", "defecto": 'json'}), 
    "historico"        : tipos.json(propiedades={"titulo": "Datos dinamicos historicos", "defecto": 'json'}),
    "archivos"         : tipos.clave(propiedades={"columna": "no", "titulo": "Archivos"}),
}

referencias = [
    # Formulario
    {
        "campoReferencia"    : "formulario_id",
        "atributosReferencia": [{
            "formulario_nombre": "nombre",
        }],
        "estructuraDestino": "formularios_dinamicos",
        "campoDestino"     : "id",            
    },
    archivos.referencia_archivo,
]

definicion = {
    "descripcion" : "Datos de Formularios Dinamicos",
    "clase"       : "datos_formularios_dinamicos",
    "estructura"  : "datos_formularios_dinamicos",    
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