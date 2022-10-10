#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base        import globales 
from librerias.datos.estructuras import estructura_operaciones
from . import sqalchemy_comunes

def modificar(sesion, CLASE, idRegistro, datos={}):
    try:
        del datos["_usuario_"]
    except:
        pass
    registro = sqalchemy_comunes.leer_registroIdClase(sesion, CLASE, idRegistro)    
    for key, value in datos.items():
        atributo = str( type( getattr(CLASE, key, None) ) )
        if  (atributo.find("associationproxy") == -1) and \
            ( atributo.find("NoneType") == -1)        and \
            ( atributo.find("property") == -1):
            setattr(registro, key, value)            
    sesion.commit() 
    
    return registro      

def modificar_registro(ruta, CLASE, datos={}, retornar="diccionario"):    
    idRegistro = datos.get("id", None)
    del datos["id"]
    resultado = {}
    if idRegistro != None:
        sesion    = sqalchemy_comunes.nuevaSesion(ruta)
        registro  = modificar(sesion, CLASE, idRegistro, datos)
        resultado = sqalchemy_comunes.retornar_datos(registro, retornar)    
        sesion.close()
    
    return resultado

# Modificar un registro, estructutra
def modificar_un_registro(estructura, registro_id, datos):
    definicion  = globales.lee_definicion(estructura)
    CLASE       = globales.lee_clase(definicion["clase"])
    datos["id"] = registro_id
    resultado   = modificar_registro("base", CLASE, datos)
    
    return resultado