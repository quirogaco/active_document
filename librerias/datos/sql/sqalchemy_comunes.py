#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales 

# Retorna el objeto del registro original
def leer_registroIdClase(sesion, CLASE, registroId, campoId="id"):
    resultado = None
    columna   = getattr(CLASE, campoId, None)
    if (type(columna) !=  type(None)):  
        registro  = sesion.query(CLASE).filter(*[columna==registroId]).first()
        resultado = registro
        
    return resultado

# Retorna una session Sqlalchemy
def nuevaSesion(ruta):
    creador = globales.lee_sesion_sql(ruta)

    return creador()

################################
# RESULTADO DE OPERACIONES SQL #
################################

def valida_atributos(datos):
    # Preprara datos _atributos_
    atributos_ = datos.get("atributos_", None)  
    # Normaliza los datos a diccionario plano
    if atributos_ != None:
        datos.update(atributos_)         

    return datos

def retornar_datos(sqlResultado, retornar="diccionario"):
    resultado = None
    if   (retornar == "objeto"):
        resultado = sqlResultado
    else: 
        resultado = dict( sqlResultado.to_dict(5) )
        resultado = valida_atributos(resultado)
        
    return resultado