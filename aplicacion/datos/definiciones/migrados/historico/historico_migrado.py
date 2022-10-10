#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.utilidades import basicas  

# Definiciones sql
from librerias.datos.sql  import sqalchemy_declarativa_base as dbase
from librerias.datos.sql  import sqalchemy_tipo_campos as tipos

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general

from librerias.datos.base       import globales
from librerias.datos.validacion import valida 
from librerias.datos.elastic    import elastic_utilidades
from librerias.datos.elastic    import elastic_operaciones

#############################
#          CLASE            #
# MIGRADO ARCHIVO HISTORICO #
#############################
class DB_MIGRADO_ARCHIVO_HISTORICO(base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa([
        'id', 
        'un_administrativa', 
        'un_productora',
        'serie',
        'subserie',
        'asunto',
        'id_persona', 
        'ano',
        'fecha_inicial',
        'fecha_final',
        'carpeta',
        'periodo',
        'nombre',
        'apellido',
        'codigo_esap',  
        'archivo_pdf',     
        'archivo_ocr', 
        'texto_ocr'
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'id', 
        'un_administrativa',
        'un_productora,'
        'serie',
        'subserie',
        'asunto',
        'id_persona', 
        'ano',
        'fecha_inicial',
        'fecha_final',
        'carpeta',
        'periodo',
        'nombre',
        'apellido',
        'codigo_esap',
        'archivo_pdf',
        'archivo_ocr',
        'texto_ocr'
    ]
     
    id                = dbase.Column( dbase.Unicode(50),   default=basicas.uuidTexto, primary_key=True) 
    un_administrativa = dbase.Column( dbase.Unicode(256),  nullable=True, default="")
    un_productora     = dbase.Column( dbase.Unicode(256),  nullable=True, default="")
    serie             = dbase.Column( dbase.Unicode(256),  nullable=True, default="")
    subserie          = dbase.Column( dbase.Unicode(256),  nullable=True, default="")
    asunto            = dbase.Column( dbase.Unicode(1024), nullable=True, default="")
    id_persona        = dbase.Column( dbase.Unicode(64),   nullable=True, default="")
    ano               = dbase.Column( dbase.Unicode(64),   nullable=True, default="")
    fecha_inicial     = dbase.Column( dbase.Unicode(20),   nullable=True, default="")
    fecha_final       = dbase.Column( dbase.Unicode(20),   nullable=True, default="")
    carpeta           = dbase.Column( dbase.Unicode(128),  nullable=True, default="")
    periodo           = dbase.Column( dbase.Unicode(128),  nullable=True, default="")
    nombre            = dbase.Column( dbase.Unicode(256),  nullable=True, default="")
    apellido          = dbase.Column( dbase.Unicode(256),  nullable=True, default="")
    codigo_esap       = dbase.Column( dbase.Unicode(64),   nullable=True, default="")
    archivo_pdf       = dbase.Column( dbase.Unicode(1024), nullable=True, default="")
    archivo_ocr       = dbase.Column( dbase.Unicode(1024), nullable=True, default="")

    @property
    def texto_ocr(self):
        texto_ocr = []
        if (self.archivo_ocr != None) :
            #archivo_ocr = "d:/" + self.archivo_ocr
            archivo_ocr = self.archivo_ocr
            texto_ocr = basicas.json_carga_archivo(archivo_ocr)
            
        return texto_ocr

globales.carga_clase("db_migrado_archivo_historico", DB_MIGRADO_ARCHIVO_HISTORICO)


##################################
#           ESTRUCTURA           #
##################################

# OCR - > Texto por archivo
"""
paginas_texto_definicion = {
    'tipo'       : 'anidados',
    'propiedades': {
        'pagina_nro': {
            'tipoElastic': 'entero'
        }, 
        'pagina_texto': {
            'tipoElastic': 'texto_base'
        }
    }
}

"texto_ocr"        : tipos.lista_texto(propiedades={"titulo": "Ocr", "tipoElastic": paginas_texto_definicion})    
"""

campos = {
    "id"               : tipos.id(),       
    "un_administrativa": tipos.texto_obligatorio(propiedades={"titulo": "Unidad administrativa", "longitud": 256}),
    "un_productora"    : tipos.texto_obligatorio(propiedades={"titulo": "Unidad productor",      "longitud": 256}),    
    "serie"            : tipos.texto_obligatorio(propiedades={"titulo": "Serie",                 "longitud": 256}),        
    "subserie"         : tipos.texto_obligatorio(propiedades={"titulo": "SubSerie",              "longitud": 256}),        
    "asunto"           : tipos.texto_obligatorio(propiedades={"titulo": "Asunto",                "longitud": 1024}),   
    "id_persona"       : tipos.texto_obligatorio(propiedades={"titulo": "Identificaci�n"}),        
    "ano"              : tipos.texto_obligatorio(propiedades={"titulo": "A�o"}),  
    "fecha_inicial"    : tipos.texto_obligatorio(propiedades={"titulo": "Fecha inicial"}),  
    "fecha_final"      : tipos.texto_obligatorio(propiedades={"titulo": "Fecha final"}),     
    "carpeta"          : tipos.texto_obligatorio(propiedades={"titulo": "Carpeta",               "longitud": 256}),         
    "periodo"          : tipos.texto_obligatorio(propiedades={"titulo": "Periodo",               "longitud": 128}),         
    "nombre"           : tipos.texto_obligatorio(propiedades={"titulo": "Nombre",                "longitud": 256}),   
    "apellido"         : tipos.texto_obligatorio(propiedades={"titulo": "Apellido",              "longitud": 256}),        
    "codigo_esap"      : tipos.texto_obligatorio(propiedades={"titulo": "Codigo"}),        
    "archivo_pdf"      : tipos.clave_obligatorio(propiedades={"titulo": "Pdf",                   "longitud": 1024}),        
    "archivo_ocr"      : tipos.clave_obligatorio(propiedades={"titulo": "Ocr",                   "longitud": 1024}),      
    "texto_ocr"        : tipos.lista_texto(propiedades={"titulo": "Ocr"})    
}

# Campos elastic
camposIndexamiento = {}
camposElastic = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Archivos migrados",
    "clase"       : "db_migrado_archivo_historico",
    "estructura"  : "archivo_historico_migrado",    

    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,

    # Referencias a otras estructuras
    "referencias" : [],
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {
        'excluir': [
            "texto_ocr",
            #"texto_ocr.pagina_nro"
        ]
    }
}

# Publica definicion de estructura
globales.carga_definicion(definicion["estructura"], definicion)

##### VALIDACIÓN #######
# Genera modelo de validación
validador = valida.definirModelo(definicion["estructura"], definicion["campos"])
# Publica modelo de validacion
globales.carga_validador(definicion["estructura"], validador)

##### ELASTIC #######
# Genera modelo de elastic
elastic_modelo, runtime, querytime = elastic_utilidades.generaModelo(camposElastic, definicion["indexamiento"], definicion["estructura"])

# Registra modelo de elastic
elastic_utilidades.registraModelo(
    definicion["estructura"], 
    elastic_modelo, 
    definicion["indexamiento"], 
    definicion.get("campoIndice", "id") 
)
elastic_operaciones.creaIndice(definicion["estructura"], "base")