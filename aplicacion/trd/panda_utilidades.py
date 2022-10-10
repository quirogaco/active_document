#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

def isEmpty(df):
    if (df.shape[0] == 0):
        return True
    else:
        return False

def isUnique(data):
    return pd.Series(data).is_unique

def validar_numerico_entero(df, indice, errors='ignore'):
    datos = df.iloc[:, indice].fillna(0)

    return pd.to_numeric(datos, errors=errors, downcast="integer")

def llenar_con(df, indice, value=0):
    datos = df.iloc[:, indice].fillna(value)

    return datos

def reemplazar_con(df, indice, original, nuevo_valor=""):
    datos = df.iloc[:, indice].replace([original], nuevo_valor)

    return datos