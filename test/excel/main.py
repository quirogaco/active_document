#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint
import pandas as pd
import configuracion_base

import valida_data
import crea_data

def preparacion_inicial(df):
    mensajes = valida_data.validar(df)

    """
    estructura = prepare_estructura(df)
    pprint.pprint(estructura, width=200)
    """
    #print("")
    #print("")
    #print("MENSAJES:")
    #pprint.pprint(mensajes, width=500)

    return mensajes

def cargar_datos(filename):
    df = pd.read_excel ('trd_test.xlsx')
    mensajes = preparacion_inicial(df)
    if len(mensajes) == 0:
        print("")
        print("")
        estructura = crea_data.prepare_estructura(df)
        trd_id = "bc2c9b02-e58b-11ec-80bd-086266b539c1"
        crea_data.salvar_data(estructura, trd_id)
        
        return []
    else:
        
        return mensajes
    
    #df.to_excel('./ouput.xlsx', index = False)        
    #pd.set_option('display.max_columns', None)
    #pd.set_option('display.max_rows', None)

cargar_datos("trd_test.xlsx")
