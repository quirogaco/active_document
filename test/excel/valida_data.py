#!/usr/bin/python
# -*- coding: utf-8 -*-
import configuracion_base

import pandas as pd

import panda_utilidades

CI = {
    "ID"            : 0,
    "TIPO"          : 1,
    "CODIGO"        : 2,
    "NOMBRE_D"      : 3,
    "NOMBRE_S"      : 4,
    "NOMBRE_SS"     : 5,
    "NOMBRE_T"      : 6,
    "GESTION"       : 7,
    "CENTRAL"       : 8,
    "CONSERVACION TOTAL": 9,
    "ELIMINACION"   : 10,
    "SELECCION"     : 11,
    "MEDIO TECNICO" : 12,
    "PAPEL"         : 13,
    "ELECTRONICO"   : 14
}

# id es numerico y unico
def validaColumna_ID(df):
    df.iloc[:, CI["ID"]] = panda_utilidades.validar_numerico_entero(df, CI["ID"])
    datos = df.iloc[:, CI["ID"]].tolist()
    
    return panda_utilidades.isUnique(datos)

# tipo es valido
def validaColumna_TIPO(df):
    indice = CI["TIPO"]
    df.iloc[:, indice] = panda_utilidades.llenar_con(df, indice, "")
    df.iloc[:, indice] = df.iloc[:, indice].str.upper()
    tipos           = ["D", "S", "SS", "T"]
    invalidos       = df.iloc[:, indice].isin(tipos)
    tipos_invalidos = []
    for idx, valido in enumerate(invalidos):
        if valido == False:
            tipos_invalidos.append( (idx, df.iloc[:, indice][idx]) )

    return tipos_invalidos

# codigo es obligatorio para D,S,SS
def validaColumna_CODIGO(df):
    tipo               = CI["TIPO"]
    indice             = CI["CODIGO"]
    df.iloc[:, indice] = panda_utilidades.llenar_con(df, indice, "")
    df.iloc[:, indice] = df.iloc[:, indice].str.upper()
    codigos_invalidos  = []
    for idx, codigo in enumerate(df.iloc[:, indice]):
        if (df.iloc[:, tipo][idx] in ["D", "S", "SS"]) and (codigo == ""):
            codigos_invalidos.append( (idx, df.iloc[:, indice][idx]) )

    return codigos_invalidos

# nombre es obligatorio
def validaColumna_NOMBRE_BASE(df, indice):
    df.iloc[:, indice] = panda_utilidades.llenar_con(df, indice, "")
    nombres_invalidos  = []
    for idx, nombre in enumerate(df.iloc[:, indice]):
        if (nombre == ""):
            nombres_invalidos.append( (idx, df.iloc[:, indice][idx]) )

    return nombres_invalidos

# valida nombres obligatorios para cada columna especifica
def validaColumna_NOMBRE(df):    
    nombres_invalidos  = []
    # limpia columnas
    df.iloc[:, CI["NOMBRE_D"]] = panda_utilidades.llenar_con(df, CI["NOMBRE_D"], "")
    df.iloc[:, CI["NOMBRE_D"]] = df.iloc[:, CI["NOMBRE_D"]].str.upper()
    df.iloc[:, CI["NOMBRE_S"]] = panda_utilidades.llenar_con(df, CI["NOMBRE_S"], "")
    df.iloc[:, CI["NOMBRE_S"]] = df.iloc[:, CI["NOMBRE_S"]].str.upper()
    df.iloc[:, CI["NOMBRE_SS"]] = panda_utilidades.llenar_con(df, CI["NOMBRE_SS"], "")
    df.iloc[:, CI["NOMBRE_SS"]] = df.iloc[:, CI["NOMBRE_SS"]].str.upper()
    df.iloc[:, CI["NOMBRE_T"]] = panda_utilidades.llenar_con(df, CI["NOMBRE_T"], "")
    df.iloc[:, CI["NOMBRE_T"]] = df.iloc[:, CI["NOMBRE_T"]].str.upper()

    tipo               = CI["TIPO"]
    for idx, tipo in enumerate(df.iloc[:, tipo]):
        nombre = ""
        indice = -1
        match tipo:
            case "D":
                indice = CI["NOMBRE_D"]
                
            case "S":            
                indice = CI["NOMBRE_S"]

            case "SS":
                indice = CI["NOMBRE_SS"]

            case "T":
                indice = CI["NOMBRE_T"]
        
        nombre = df.iat[idx, indice]
        if (nombre == ""):
            nombres_invalidos.append( (idx, df.iloc[:, indice][idx]) )
   
    return nombres_invalidos

# asigna valor 0 si no tiene
def validaColumna_GESTION(df):
    indice             = CI["GESTION"]
    df.iloc[:, indice] = panda_utilidades.validar_numerico_entero(df, indice)
    df.loc[((df.TIPO != "S") & (df.TIPO != "SS")), "GESTION"] = ''
    for idx, valor in enumerate(df.iloc[:, indice]):
        if (df.iloc[:, CI["TIPO"]][idx] in ["S", "SS"]):
            if ( not isinstance(valor, int) ):
                df.iat[idx, indice] = 0
                
    return []

# asigna valor 0 si no tiene
def validaColumna_CENTRAL(df):
    indice             = CI["CENTRAL"]
    df.iloc[:, indice] = panda_utilidades.validar_numerico_entero(df, indice)
    df.loc[((df.TIPO != "S") & (df.TIPO != "SS")), "CENTRAL"] = ''
    for idx, valor in enumerate(df.iloc[:, indice]):
        if (df.iloc[:, CI["TIPO"]][idx] in ["S", "SS"]):
            if ( not isinstance(valor, int) ):
                df.iat[idx, indice] = 0

    return []

def validaColumna_ASIGNADO(df, indice, expresion, columna):
    df.iloc[:, indice] = panda_utilidades.llenar_con(df, indice, "NO")
    df.iloc[:, indice] = panda_utilidades.reemplazar_con(df, indice, "X", "SI")
    df.iloc[:, indice] = panda_utilidades.reemplazar_con(df, indice, "x", "SI")
    df.loc[expresion, columna] = ''

def validar(df):
    # Columnas titulos a mayuscula
    mensajes = []
    df.columns = df.columns.str.upper()

    # Vacio
    empty = panda_utilidades.isEmpty(df) 
    if empty == True:
        mensajes.append("Archivo vacio")
   
    # Consecutivo unico
    uniques = validaColumna_ID(df)  
    if uniques ==  False:
        mensajes.append("ID no contiene valores unicos")
   
    # Tipos de registros
    tipos = validaColumna_TIPO(df)
    if len(tipos) > 0:
        mensajes.append("TIPO contiene valores invalidos" + str(tipos))
   
    # Codigo: DEPENDENCIA, SERIE, SUBSERIE
    codigos = validaColumna_CODIGO(df)
    if len(codigos) > 0:
        mensajes.append("CODIGO contiene valores invalidos" + str(codigos))
   
    # Nombre: DEPENDENCIA, SERIE, SUBSERIE
    nombres = validaColumna_NOMBRE(df)
    if len(nombres) > 0:
        mensajes.append("NOMBRE contiene valores invalidos" + str(nombres))

    # Gestion en años
    gestion = validaColumna_GESTION(df)
    if len(gestion) > 0:
        mensajes.append("GESTION contiene valores cero o no numericos" + str(gestion))

    # Central en años
    central = validaColumna_CENTRAL(df)
    if len(central) > 0:
        mensajes.append("CENTRAL contiene valores cero o no numericos" + str(central))

    # Eliminacion, Seleccion, Conservacion, Microfilmacion
    # Papel, Electronico
    validaColumna_ASIGNADO(df, CI["ELIMINACION"],    ((df.TIPO != "S") & (df.TIPO != "SS") ), "ELIMINACION")
    validaColumna_ASIGNADO(df, CI["SELECCION"],      ((df.TIPO != "S") & (df.TIPO != "SS") ), "SELECCION")
    validaColumna_ASIGNADO(df, CI["CONSERVACION TOTAL"], ((df.TIPO != "S") & (df.TIPO != "SS") ), "CONSERVACION TOTAL")
    validaColumna_ASIGNADO(df, CI["MEDIO TECNICO"], ((df.TIPO != "S") & (df.TIPO != "SS") ), "MEDIO TECNICO")
    
    validaColumna_ASIGNADO(df, CI["PAPEL"],       (df.TIPO != "T"), "PAPEL")
    validaColumna_ASIGNADO(df, CI["ELECTRONICO"], (df.TIPO != "T"), "ELECTRONICO")

    return mensajes
