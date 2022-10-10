#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base        import globales 
from librerias.datos.estructuras import estructura_operaciones
from . import sqalchemy_comunes

###########################
# OPERACIONES DE CREACION #
###########################
def insertar(sesion, CLASE, datos={}, salva=True):
    #print("")
    #print("")
    #print("-------------------------------")    
    #print("INSERTAR:", CLASE)
    #print("-------------------------------")    
    #pprint.pprint(datos)
    #print("")
    #print("")
    nuevo = CLASE( **datos )
    sesion.add( nuevo )   
    if salva:
        sesion.commit()   
    
    return nuevo

def insertar_registro(ruta, CLASE, datos={}, retornar="diccionario", salva=True):
    sesion     = sqalchemy_comunes.nuevaSesion(ruta)
    idRegistro = datos.get("id", None)
    try:
        del datos["_usuario_"]
    except:
        pass

    if idRegistro in ["", None]:
        try:
            del datos["id"]
        except:
            pass
    nuevo      = insertar(sesion, CLASE, datos, salva)
    resultado  = sqalchemy_comunes.retornar_datos(nuevo, retornar)    
    sesion.close()

    return resultado

def insertar_registro_estructura(estructura, datos={}):
    definicion = globales.lee_definicion(estructura)
    CLASE      = globales.lee_clase(definicion["clase"])
    resultado  = insertar_registro('base', CLASE, datos)

    return resultado