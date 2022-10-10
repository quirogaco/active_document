#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
import configuracion_base

import trd.dependencia 
import trd.serie
import trd.subserie 
import trd.tipo

print("trd.dependencia:", trd.dependencia)

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
    "ELIMINACION"   : 9,
    "SELECCION"     : 10,
    "CONSERVACION"  : 11,
    "MICROFILMACION": 12,
    "PAPEL"         : 13,
    "ELECTRONICO"   : 14
}

# Validacion basica de datos
def validaColumna_ID(df):
    df.iloc[:, CI["ID"]] = panda_utilidades.validar_numerico_entero(df, CI["ID"])
    datos = df.iloc[:, CI["ID"]].tolist()
    
    return panda_utilidades.isUnique(datos)

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

def validaColumna_NOMBRE_BASE(df, indice):
    df.iloc[:, indice] = panda_utilidades.llenar_con(df, indice, "")
    nombres_invalidos  = []
    for idx, nombre in enumerate(df.iloc[:, indice]):
        if (nombre == ""):
            nombres_invalidos.append( (idx, df.iloc[:, indice][idx]) )

    return nombres_invalidos

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

def validaColumna_GESTION(df):
    indice             = CI["GESTION"]
    df.iloc[:, indice] = panda_utilidades.validar_numerico_entero(df, indice)
    df.loc[((df.TIPO != "S") & (df.TIPO != "SS")), "GESTION"] = ''
    valores_invalidos  = []
    for idx, valor in enumerate(df.iloc[:, indice]):
        if (df.iloc[:, CI["TIPO"]][idx] in ["S", "SS"]):
            if (isinstance(valor, int) == False or valor == 0):
                valores_invalidos.append( (idx, df.iloc[:, indice][idx]) )

    return valores_invalidos

def validaColumna_CENTRAL(df):
    indice             = CI["CENTRAL"]
    df.iloc[:, indice] = panda_utilidades.validar_numerico_entero(df, indice)
    df.loc[((df.TIPO != "S") & (df.TIPO != "SS")), "CENTRAL"] = ''
    valores_invalidos  = []
    for idx, valor in enumerate(df.iloc[:, indice]):
        if (df.iloc[:, CI["TIPO"]][idx] in ["S", "SS"]):
            if (isinstance(valor, int) == False or valor == 0):
                valores_invalidos.append( (idx, df.iloc[:, indice][idx]) )

    return valores_invalidos

def validaColumna_ASIGNADO(df, indice, expresion, columna):
    df.iloc[:, indice] = panda_utilidades.llenar_con(df, indice, "NO")
    df.iloc[:, indice] = panda_utilidades.reemplazar_con(df, indice, "X", "SI")
    df.iloc[:, indice] = panda_utilidades.reemplazar_con(df, indice, "x", "SI")
    df.loc[expresion, columna] = ''

############################################
# Validacion de jerarquia en la estructura #
############################################
def valida_jerarquia_padre(anterior, actual, fila):
    mensaje = ""
    try:
        tipo_anterior = anterior[CI["TIPO"]]
    except:
        tipo_anterior = ""
    tipo_actual = actual[CI["TIPO"]]
    
    match tipo_actual:
        case "S":
            if tipo_anterior != "D":
                mensaje = "JERARQUIA: Serie mal ubicada (debe ir despues de una Dependencia) [" + str(fila) + "], " + str([str(x) for x in actual])

        case "SS":
            if tipo_anterior != "S":
                mensaje = "JERARQUIA: SubSerie mal ubicada (debe ir despues de una Serie) [" + str(fila) + "], " + str([str(x) for x in actual])

        case "T":
            if tipo_anterior not in ["S", "SS", "T"]:
                mensaje = "JERARQUIA: Tipo mal ubicado (debe ir despues de una Serie o Subberie) [" + str(fila) + "], " + str([str(x) for x in actual])
        
    return mensaje

def valida_jerarquia(df):
    mensajes = []
    anterior = []
    for fila in range(len(df)):
        actual  = df.iloc[fila,]
        mensaje = valida_jerarquia_padre(anterior, actual, fila)
        if mensaje != "":
            mensajes.append(mensaje)
        anterior = actual
    
    return mensajes

######################
# Crea registros TRD #
######################
def crea_registro(tipo_actual, trd_id, datos):
    registro = {"id": None}
    match tipo_actual:
        case "D":
            registro = trd.dependencia.crea_registro(datos, trd_id)

        case "S":            
            registro = trd.serie.crea_registro(datos, trd_id)

        case "SS":
            registro = trd.subserie.crea_registro(datos, trd_id)

        case "T":
            registro = trd.tipo.crea_registro(datos, trd_id)

    return registro

def crea_datos(trd_id, actual, anterior_tipo, anterior_id, registro):
    tipo_actual = actual[CI["TIPO"]]
    datos       = {}
    match tipo_actual:
        case "D":
            datos = {
                "tabla" : "TRD", 
                "codigo": actual[CI["CODIGO"]], 
                "nombre": actual[CI["NOMBRE_D"]],
                "trd_id": trd_id                 
            }
            if anterior_tipo == "D":
                datos["dependencia_padre_id"] = anterior_id

        case "S":            
            datos = {
                "tabla"               : "TRD", 
                "codigo"              : actual[CI["CODIGO"]], 
                "nombre"              : actual[CI["NOMBRE_S"]],
                "gestion"             : actual[CI["GESTION"]],
                "central"             : actual[CI["CENTRAL"]],
                "eliminacion"         : actual[CI["ELIMINACION"]],
                "seleccion"           : actual[CI["SELECCION"]],
                "conservacion"        : actual[CI["CONSERVACION"]],
                "micro_digitalizacion": actual[CI["MICROFILMACION"]],
                "dependencia_id"      : anterior_id
            }    

        case "SS":
            datos = {
                "tabla"               : "TRD", 
                "codigo"              : actual[CI["CODIGO"]], 
                "nombre"              : actual[CI["NOMBRE_SS"]],
                "gestion"             : actual[CI["GESTION"]],
                "central"             : actual[CI["CENTRAL"]],
                "eliminacion"         : actual[CI["ELIMINACION"]],
                "seleccion"           : actual[CI["SELECCION"]],
                "conservacion"        : actual[CI["CONSERVACION"]],
                "micro_digitalizacion": actual[CI["MICROFILMACION"]],
                "serie_id"            : anterior_id
            }  

        case "T":
            datos = {
                "tabla"      : "TRD", 
                "nombre"     : actual[CI["NOMBRE_T"]],
                "papel"      : actual[CI["PAPEL"]],
                "electronico": actual[CI["ELECTRONICO"]]
            } 
            if anterior_tipo == "S":
                datos["serie_id"] = anterior_id
            if anterior_tipo == "SS":
                datos["subserie_id"] = anterior_id
            if anterior_tipo == "T":
                datos["serie_id"]    = registro["serie_id"]
                datos["subserie_id"] = registro["subserie_id"]

    return datos

def crea_registros(df):
    registro      = None
    anterior_tipo = None
    anterior_id   = None
    # temporales
    trd_id = "a346656f-e35a-11ec-8431-086266b539c1"
    for fila in range(len(df)):
        actual        = df.iloc[fila,]
        tipo_actual   = actual[CI["TIPO"]]
        datos         = crea_datos(trd_id, actual, anterior_tipo, anterior_id, registro)
        print("")
        print("")        
        print("**********")
        pprint.pprint(datos)
        registro      = crea_registro(tipo_actual, trd_id, datos)
        print(registro)
        print("")
        print("")        
        anterior_tipo = tipo_actual
        anterior_id   = registro["id"]

def preparacion_inicial(df):
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
    validaColumna_ASIGNADO(df, CI["CONSERVACION"],   ((df.TIPO != "S") & (df.TIPO != "SS") ), "CONSERVACION")
    validaColumna_ASIGNADO(df, CI["MICROFILMACION"], ((df.TIPO != "S") & (df.TIPO != "SS") ), "MICROFILMACION")
    
    validaColumna_ASIGNADO(df, CI["PAPEL"],       (df.TIPO != "T"), "PAPEL")
    validaColumna_ASIGNADO(df, CI["ELECTRONICO"], (df.TIPO != "T"), "ELECTRONICO")
    mensajes.extend(valida_jerarquia(df))
   
    return mensajes

df = pd.read_excel ('trd.xlsx')

mensajes = preparacion_inicial(df)
pprint.pprint(mensajes)

#if len(mensajes) == 0:
crea_registros(df)

print("")
print("")
print(df)