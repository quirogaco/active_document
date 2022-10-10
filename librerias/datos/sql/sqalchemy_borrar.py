#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base        import globales 
from librerias.datos.estructuras import estructura_operaciones
from . import sqalchemy_comunes

##########################
# OPERACIONES DE BORRADO #
##########################

def eliminar(sesion, CLASE, idRegistro, retornar="diccionario"):
    resultado = {} 
    registro  = sqalchemy_comunes.leer_registroIdClase(sesion, CLASE, idRegistro)    
    if registro != None:
        resultado = sqalchemy_comunes.retornar_datos(registro, retornar) 
        sesion.delete(registro)
        sesion.commit() 
    
    return resultado

def eliminar_registro(ruta, CLASE, datos={}, retornar="diccionario"):
    idRegistro = datos.get("id", None)
    sesion     = sqalchemy_comunes.nuevaSesion(ruta)
    resultado  = eliminar(sesion, CLASE, idRegistro)
    sesion.close()

    return resultado

# Borrar un registro, estructutra
def borrar_un_registro(estructura, registro_id):
    definicion = globales.lee_definicion(estructura)
    CLASE      = globales.lee_clase(definicion["clase"])
    sesion     = sqalchemy_comunes.nuevaSesion("base")
    resultado  = eliminar(sesion, CLASE, registro_id)
    sesion.close()
    
    return resultado