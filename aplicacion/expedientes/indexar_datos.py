#!/usr/bin/python
# -*- coding: iso-8859-15 -*-


# Indexa TRD Y ESTRUCTURA
from librerias.ejecucion  import llamados

def indexar_estructura(estructura, registro_id):
    secuencia = [
        {
            "funcion"   : "indexar_estructura_cola",
            "parametros": {
                'estructura' : estructura, 
                'registro_id': registro_id
            }
        }
    ]
    llamados.ejecutar_secuencia(secuencia=secuencia, ubicacion="indexar_datos")  

def indexar(estructura, registro_id, expediente_id):
    secuencia = [
        {
            "funcion"   : "indexar_estructura_cola",
            "parametros": {
                'estructura' : estructura, 
                'registro_id': registro_id
            }
        },

        {
            "funcion"   : "indexar_estructura_cola",
            "parametros": {
                'estructura' : "agn_expedientes_trd", 
                'registro_id': expediente_id
            }
        },
    ]
    llamados.ejecutar_secuencia(secuencia=secuencia, ubicacion="expedientes.py indexar_datos",retardo=30)  


def salvar_anexos(accion, datos, archivos, id_tarea):
    secuencia = [
        {
            "funcion"   : "manejo_archivos_cola",
            "parametros": {
                "estructura"   : "agn_documentos_trd",
                "accion"       : accion,
                "datos"        : datos,
                "tarea"        : {},
                "archivos"     : archivos,
                "id_tarea"     : id_tarea,
                "tipo_relacion": "documento",
                "cubeta"       : "AGN"
            }
        }
    ]
    llamados.ejecutar_secuencia(secuencia=secuencia, ubicacion="indexar_datos")  