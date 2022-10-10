#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
import configuracion_base

import pandas as pd

from librerias.datos.sql import sqalchemy_insertar
from librerias.ejecucion  import llamados


def indexar(estructura, registro_id):
    secuencia = [
        {
            "funcion"   : "indexar_estructura_cola",
            "parametros": {
                'estructura' : estructura, 
                'registro_id': registro_id
            }
        }
    ]
    llamados.ejecutar_secuencia(secuencia=secuencia, ubicacion="test usauriosindexar_datos")  

def cargar_datos(filename):
    df = pd.read_excel (filename)
    for index, row in df.iterrows():
        datos = {                    
            "codigo": row["codigo"], 
            "nombre": row["nombre"],
            "correo": row["correo"],
            "clave" : "456"
        }
        resultado = sqalchemy_insertar.insertar_registro_estructura("usuarios", datos)
        indexar("usuarios", resultado["id"])

cargar_datos("./usuarios.xlsx")
