    #!/usr/bin/python
# -*- coding: UTF-8 -*-

import pprint

from inspect import isfunction

from . import elastic_tiposCampos
from librerias.datos.base    import globales
from librerias.datos.elastic import elastic_operaciones
from .                       import elastic_campos_script

"""
        "settings" : {
            "index.mapping.nested_objects.limit": 100000,
            #"index.max_result_window": 1000000,            
            "analysis" : {                
                "analyzer":{
                    "no_accent": {
                    "tokenizer": "standard",
                    "filter"   : [ "lowercase", "asciifolding" ]
                    }
                },

                "normalizer":{
                    "normalizado": {
                        "type"       : "custom",
                        "char_filter": [],
                        "filter"     : ["lowercase", "asciifolding"]
                    }
                }
            }
        },  
"""
# Crea mapa elastic
def generaMapa(modelo, runtime, opciones):    
    mapa = {
        "settings" : {
            "index.mapping.nested_objects.limit": 100000,
            "index.max_result_window": 1000000,            
            "analysis" : {                
                "analyzer":{
                    "no_accent": {
                        "tokenizer": "standard",
                        "filter"   : [ "lowercase", "asciifolding" ]
                    }
                },

                "normalizer":{
                    "normalizado": {
                        "type"       : "custom",
                        "char_filter": [],
                        "filter"     : ["lowercase", "asciifolding"]
                    }
                }
            }
        },  

        'mappings': {
            #'dynamic'   : 'runtime',
            'properties': modelo,
            # Es solo descriptivo se usa para generar 
            # campo al momento del query, elastic_busquedas
            'runtime'   : runtime
        },
    }

    return mapa

# Registra modelo elastic
def registraModelo(
    estructura="", 
    modelo={}, 
    indexamiento={}, 
    campoId="id", 
    runtime={}, 
    querytime={}
):
    mapa = generaMapa(modelo, runtime, indexamiento)
    globales.carga_modelo_elastic(
        estructura, 
        modelo, 
        mapa, 
        indexamiento, 
        "", 
        campoId
    )
    globales.carga_modelo_querytime(estructura, querytime)
    
diccionario_tipos = {
    "texto"             : elastic_tiposCampos.texto,
    "texto_ordenado"    : elastic_tiposCampos.texto_ordenado,
    "texto_base"        : elastic_tiposCampos.texto_base,

    "clave"             : elastic_tiposCampos.clave,
    "clave_ordenado"    : elastic_tiposCampos.clave_ordenado,

    "fechaHora"         : elastic_tiposCampos.fechaHora,
    "fechaHora_ordenado": elastic_tiposCampos.fechaHora_ordenado,
    "fecha"             : elastic_tiposCampos.fecha,
    "fecha_ordenado"    : elastic_tiposCampos.fecha_ordenado,

    "entero"            : elastic_tiposCampos.entero,
    "entero_ordenado"   : elastic_tiposCampos.entero_ordenado,

    "decimal"           : elastic_tiposCampos.decimal,
    "decimal_ordenado"  : elastic_tiposCampos.decimal_ordenado,

    "largo"             : elastic_tiposCampos.largo,
    "largo_ordenado"    : elastic_tiposCampos.largo_ordenado,

    "anidados"          : elastic_tiposCampos.anidados,

    "lista"             : elastic_tiposCampos.lista,
    "objeto"            : elastic_tiposCampos.objeto,
    "lista_texto"       : elastic_tiposCampos.lista_texto,
    
    "coma"              : elastic_tiposCampos.coma
}

# Retorna tipos propiedades elastic
def tiposPropiedades(propiedades): 
    tipos = {}
    for campo, propiedad in propiedades.items():  
        tipoElastic = propiedad["tipoElastic"]
        if isinstance(tipoElastic, str):
            tipoElastic = diccionario_tipos[ propiedad["tipoElastic"] ]    
        tipos[campo] = tipoElastic        
    
    return tipos

tabla  = ""
campog = ""
def propiedades_anidadas(parametros):
    global tabla, campog

    propiedades = {}
    for etiqueta, valor in parametros.items():
        tipoElastic = valor.get("tipoElastic", None)
        if tipoElastic != None:  
            if isinstance(tipoElastic, dict): 
                define_tipo = diccionario_tipos[tipoElastic['tipo']]
                valores = propiedades_anidadas(tipoElastic['propiedades'])     
                propiedades[etiqueta] = define_tipo(valores)        
            else:
                propiedades[etiqueta] = diccionario_tipos[tipoElastic]

    return propiedades

# Retorna tipo elastic
def tipoFullText(tipo):     
    propiedades = None
    if isinstance(tipo, dict): 
        define_tipo = diccionario_tipos[tipo['tipo']]
        propiedades = propiedades_anidadas(tipo['propiedades'])
        resultado = define_tipo(propiedades)               
    else:
        resultado =  diccionario_tipos[tipo]

    return resultado

# Crea modelo elastic, basado en campos y atributos
def generaModelo(campos={}, opciones={}, estructura=""):
    global tabla, campog
    
    tabla     = estructura
    modelo    = {}
    runtime   = {}
    querytime = {}
    for campo, valores in campos.items(): 
        campog = campo  
        tipoElastic = valores.get("tipoElastic", None)
        formato = valores.get("formato", None)
        if tipoElastic != None:
            modelo[campo] = tipoFullText(tipoElastic)
            if formato != None:   
                querytime[formato["nombre"]] = \
                    elastic_campos_script.campo_guion(campo, formato["tipo"])   

    return modelo, runtime, querytime

# Crea modelo elastic, basado en campos y atributos
def generaRegistraModelo(campos={}, definicion={}):
    if len(campos.keys()) > 0:
        elastic_modelo, elastic_runtime, elastic_querytime = generaModelo(
            campos, 
            definicion["indexamiento"], 
            definicion["estructura"]
        )

        # Registra modelo de elastic
        registraModelo(
            definicion["estructura"], 
            elastic_modelo,             
            definicion["indexamiento"], 
            definicion.get("campoIndice", "id"),
            elastic_runtime,
            elastic_querytime
        )
        elastic_operaciones.creaIndice(definicion["estructura"], "base")