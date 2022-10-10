    #!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint
from librerias.datos.base import globales

#################
# Ordenamientos #
#################
def crear_ordenamientos(ordenamientos=[]):
    # ordenamientos => [{'codigo': 1}, {'id': 1}]
    listaOrdenamiento = [] 
    for ordenamiento in ordenamientos: 
        campo = list(ordenamiento.keys())[0]
        orden = list(ordenamiento.values())[0]
        if campo != "id":
            if orden == 0:
                campo = "-" + campo
            campo = campo + ".normalizado"
            listaOrdenamiento.append(campo)

    return listaOrdenamiento

def asigna_ordenamientos(busqueda, orden_lista):
    ordenamientos = crear_ordenamientos(orden_lista)
    for orden in ordenamientos:
        busqueda = busqueda.sort(orden)

    return busqueda

def prepararOrdenamiento(busqueda, estructura, parametros, definicion):
    ordenamientos = parametros.get("ordenamientos", []) 
    listaOrdenamiento = crear_ordenamientos(ordenamientos)
    for orden in listaOrdenamiento:
        busqueda = busqueda.sort(orden)

    return busqueda