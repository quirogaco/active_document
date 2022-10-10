#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.utilidades import basicas  

#########
# TEXTO #
#########
def texto(propiedades={}):
    campo = {
        "titulo"     : "",
        "tipo"       : "texto",
        "defecto"    : "texto",
        "indexado"   : "no",
        "obligatorio": "no",
        "longitud"   : 64,
        "tipoElastic": "texto",
        "columna"    : "si",
        "sistema"    : "no"
    }
    campo.update(propiedades)

    return campo

def texto_obligatorio(propiedades={}):
    propiedades["obligatorio"] = "si";
    campo = texto(propiedades)

    return campo

##############
# TEXTO BASE #
##############
def texto_base(propiedades={}):
    campo = {
        "titulo"     : "",
        "tipo"       : "texto",
        "defecto"    : "texto",
        "indexado"   : "no",
        "obligatorio": "no",
        "longitud"   : 512,
        "tipoElastic": "texto_base",
        "columna"    : "si",
        "sistema"    : "no"
    }
    campo.update(propiedades)

    return campo

def texto_base_obligatorio(propiedades={}):
    propiedades["obligatorio"] = "si";
    campo = texto_base(propiedades)

    return campo

###############
# LISTA TEXTO #
###############
def lista_texto(propiedades={}):
    campo = {
        "titulo"     : "",
        "tipo"       : "texto",
        "tipoElastic": "lista_texto",
        "externo"    : "si",
        "columna"    : "si",
        "sistema"    : "no"
    }
    campo.update(propiedades)

    return campo

#########
# CLAVE #
#########
def clave(propiedades={}):
    campo = {
        "titulo"     : "",
        "tipo"       : "texto",
        "defecto"    : "texto",
        "indexado"   : "no",
        "obligatorio": "no",
        "longitud"   : 64,
        "tipoElastic": "clave",
        "columna"    : "si",
        "sistema"    : "no"
    }

    campo.update(propiedades)

    return campo

def clave_obligatorio(propiedades={}):
    propiedades["obligatorio"] = "si";
    campo = clave(propiedades)

    return campo

######
# ID #
######
def id(propiedades={}):
    campo = {
        "titulo"     : "Id del registro",
        "tipo"       : "texto",
        "defecto"    : "uuid",
        #"unico"      : "si", genera error con primary key
        "obligatorio": "si",
        "longitud"   : 64,
        "tipoElastic": "clave",
        "columna"    : "si",
        "sistema"    : "no"
    }
    campo.update(propiedades)

    return campo

#########
# FECHA #
#########
def fecha(propiedades={}):
    campo = {
        "titulo"     : "",
        "tipo"       : "fecha",
        "indexado"   : "no",
        "obligatorio": "no",
        "tipoElastic": "fecha",
        "columna"    : "si",
        "sistema"    : "no"
    }
    campo.update(propiedades)

    return campo

def fecha_obligatorio(propiedades={}):
    propiedades["obligatorio"] = "si"
    propiedades["defecto"]     = "fecha_hora"
    campo = fecha(propiedades)

    return campo

##########
# ENTERO #
##########
def entero(propiedades={}):
    campo = {
        "titulo"     : "",
        "tipo"       : "entero",
        "defecto"    : "entero",
        "indexado"   : "no",
        "obligatorio": "no",
        "tipoElastic": "entero",
        "columna"    : "si",
        "sistema"    : "no"
    }
    campo.update(propiedades)

    return campo

########
# JSON #
########
def json(propiedades={}):
    campo = {
        "titulo"     : "",
        "tipo"       : "json",
        "defecto"    : "json",
        "indexado"   : "no",
        "obligatorio": "no",
        "tipoElastic": "objeto",
        "columna"    : "si",
        "sistema"    : "no"
    }
    campo.update(propiedades)

    return campo

###########
# EXTERNO #
###########
def texto_externo(propiedades={}):
    campo = {
        "titulo"     : "",
        "tipo"       : "texto",
        "longitud"   : 0,
        "tipoElastic": "texto",
        "externo"    : "si",
        "sistema"    : "no"
    }
    campo.update(propiedades)

    return campo

##################################
# Diccionario de tipos de campos #
##################################
diccionario_tipos = {
    'texto_externo'         : texto_externo,
    'entero'                : entero,
    'fecha_obligatorio'     : fecha_obligatorio,
    'fecha'                 : fecha,
    'id'                    : id,
    'clave'                 : clave,
    'lista_texto'           : lista_texto,
    'texto_base_obligatorio': texto_base_obligatorio,
    'texto_base'            : texto_base,
    'texto_obligatorio'     : texto_obligatorio,
    'texto'                 : texto,
    'json'                  : json
}