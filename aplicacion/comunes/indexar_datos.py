#!/usr/bin/python
# -*- coding: iso-8859-15 -*-


# Indexa TRD Y ESTRUCTURA
from librerias.ejecucion  import llamados

def indexar_estructura(estructura, registro_id, retardo=0):
    secuencia = [
        {
            "funcion"   : "indexar_estructura_cola",
            "parametros": {
                'estructura' : estructura, 
                'registro_id': registro_id,                
            }
        }
    ]
    llamados.ejecutar_secuencia(secuencia=secuencia, ubicacion="indexar_datos", retardo=retardo)