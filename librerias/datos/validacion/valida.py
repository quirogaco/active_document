#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from pydantic import create_model, ValidationError
from typing   import Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
from datetime import date, datetime, time, timedelta

from librerias.datos.base import globales 
from librerias.datos.sql  import sqalchemy_columnas_dinamicas

# Listado de errores de validación
def listadoErrores(errores):
    listado = []
    """
    [
        {
            "loc": [
            "codigo"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
    """
    for error in errores:
        listado.append({
            "campo"  : error["loc"][0],
            "mensaje": mensajesError.get(error["msg"], error["msg"])
        })

    return listado

# Valida datos
def valida_datos(datos, modelo):
    sale    = {
        "datos"  : None,
        "errores": None
    }
    try:
        datos         = modelo(**datos)
        sale["datos"] = datos.dict()
    except ValidationError as e:
        errores         = listadoErrores(e.errors()) 
        sale["errores"] = errores
    
    return sale

# Tipo definicion -> python, pydantic
tiposPydantic = {
    "texto"      : Union[str, bytes],
    "texto_lista": Optional[ List[str] ],
    "clave_lista": Union[str, Optional[ List[Optional[str]] ] ],
    "entero"     : int,
    "fecha"      : date,
    "fechaHora"  : datetime,
}

# Valores por defecto generales
tiposDefecto = {
    str  : "",
    int  : 0
}

# Errores traducción
mensajesError = {
    "field required"  : "Campo obligatorio",
}

# Valor por defecto del campo
def leerDefecto(nombre, valores, tipo):    
    defecto = valores.get("defecto", None)
    
    return defecto

# Tipo de valor del campo
def leerTipo(valores): 
    tipoValor = valores.get("validador", None) 
    if tipoValor == None:
        tipoValor = valores.get("tipo", "texto")    
    tipo      = tiposPydantic.get(tipoValor, str)

    return tipo

# Tipo de campo
def definirTipo(nombre, atributosBase):               
    defecto = atributosBase["defecto"]
    defecto = sqalchemy_columnas_dinamicas.columnas_valor_defecto.get(defecto, defecto)
    if callable(defecto):
        defecto = defecto()

    if (atributosBase["obligatorio"] == "si"):
        atributo = (atributosBase["tipo"], defecto)          
    else: 
        if (atributosBase["defecto"] == None):
            atributo = ( atributosBase["tipo"], tiposDefecto.get(atributosBase["tipo"], "") )  
        else:            
            atributo = ( Optional[ atributosBase["tipo"] ],  defecto )
    
    return atributo

# Define cada campo del modelo pydantic 
def definirModeloCampo(nombre, campo, valores):
    tipoBase      = leerTipo(valores)        
    atributosBase = {
        "obligatorio": valores.get("obligatorio", "no"), 
        "tipo"       : tipoBase,
        "defecto"    : leerDefecto(nombre, valores, tipoBase)
    }
    # Tipo de campo    
    atributoPydantic = definirTipo(nombre, atributosBase)
    
    return atributoPydantic

# Define modelo pydantic 
def definirModelo(nombre, campos):
    camposModelo = {}
    for campo, valores in campos.items():     
        sistema = valores.get("sistema", "no")           
        if sistema == "no":
            modelo = definirModeloCampo(nombre, campo, valores)
            camposModelo[campo] = modelo 

    modelo = create_model(nombre, **camposModelo)

    return modelo

# Define modelo pydantic y lo publica
def definePublicaModelo(nombre, campos):
    # Genera modelo de validación
    validador = definirModelo(nombre, campos)
    
    # Publica modelo de validacion
    globales.carga_validador(nombre, validador)
