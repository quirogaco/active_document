#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.ejecucion  import llamados

# DEPENDENCIA
def indexar(estructura, registro_id, trd_id):
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
                'estructura' : "agn_trd", 
                'registro_id': trd_id
            }
        },
    ]
    llamados.ejecutar_secuencia(secuencia=secuencia, ubicacion="dependencia.py indexar_datos")  

# ACCESOS
def indexar_acceso(elemento, elemento_id, acceso_id):
    if (elemento == "dependencia"):
        estructura = "agn_dependencia_trd"

    elif (elemento == "serie"):
        estructura = "agn_serie_trd"

    elif (elemento == "subserie"):
        estructura = "agn_subserie_trd"

    elif (elemento == "tipo"):
        estructura = "agn_tipo_documental_trd"

    elif (elemento == "expediente"):
        estructura = "agn_expedientes_trd"

    secuencia = [
        {
            "funcion"   : "indexar_estructura_cola",
            "parametros": {
                'estructura' : estructura, 
                'registro_id': elemento_id
            }
        },

        {
            "funcion"   : "indexar_estructura_cola",
            "parametros": {
                'estructura' : "agn_accesos_trd", 
                'registro_id': acceso_id
            }
        },
    ]
    llamados.ejecutar_secuencia(secuencia=secuencia, ubicacion="dependencia.py indexar_datos") 

# PRESTAMOS
def indexar_prestamo(expediente_id, registro_id, retardo=30):
    secuencia = [
        {
            "funcion"   : "indexar_estructura_cola",
            "parametros": {
                'estructura' : "agn_expedientes_trd", 
                'registro_id': expediente_id
            }
        },

        {
            "funcion"   : "indexar_estructura_cola",
            "parametros": {
                'estructura' : "agn_prestamos_trd", 
                'registro_id': registro_id
            }
        },
    ]
    print("INDEXAR PRESTAMO.............................")
    llamados.ejecutar_secuencia(secuencia=secuencia, ubicacion="indexar_datos", retardo=retardo)
    
