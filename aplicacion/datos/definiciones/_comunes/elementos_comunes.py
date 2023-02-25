#!/usr/bin/python
# -*- coding: utf-8 -*-

from librerias.datos.base import globales
from librerias.datos.validacion import valida 
from librerias.datos.elastic import elastic_utilidades

#####################
# FUNCIONES COMUNES #
#####################

# Funcion que crea modelo validacion y elastic
def publicaValidaElastic(definicion, camposElastic):
    # Publica definicion de estructura
    globales.carga_definicion(definicion["estructura"], definicion)

    ##### VALIDACIÒN #######
    valida.definePublicaModelo(definicion["estructura"], definicion["campos"])

    ##### ELASTIC #######
    elastic_utilidades.generaRegistraModelo(camposElastic, definicion)


from aplicacion.datos.estructuras import baseGeneral_estructura

# Procesamiento estructura baseGeneral
def procesaBaseGeneral(definicion):
    globales.carga_procesamiento(
        definicion["estructura"], 
        "armar_estructura",
         baseGeneral_estructura.armar_estructura
    )

    globales.carga_procesamiento(
        definicion["estructura"], 
        "normaliza_estructura", 
        baseGeneral_estructura.normaliza_estructura
    )