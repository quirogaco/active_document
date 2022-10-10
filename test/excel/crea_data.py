#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
import configuracion_base

import trd.dependencia 
import trd.serie
import trd.subserie 
import trd.tipo

import pandas as pd

import panda_utilidades

import valida_data

############################
# crea estructura de datos #
############################
def prepare_estructura(df):
    estructura = {}
    dependencia = None
    serie, subserie, tipo = None, None, None
    for index in df.index:
        tipo = df['TIPO'][index] 
        match tipo:
            case "D":
                dependencia = df['CODIGO'][index]
                dato = {
                    "record": {
                        "tabla" : "TRD",                     
                        "codigo": dependencia,
                        "nombre": df.iat[index, valida_data.CI["NOMBRE_D"] ],
                        "dependencia_padre_id": None
                    },
                    "series": {},
                    "id": None
                }
                estructura[dependencia] = dato 
                serie, subserie, tipo = None, None, None

            case "S":
                serie = df['CODIGO'][index]
                dato = {
                    "record": {
                        "tabla"               : "TRD", 
                        "codigo"              : df.iat[index, valida_data.CI["CODIGO"]], 
                        "nombre"              : df.iat[index, valida_data.CI["NOMBRE_S"]],
                        "gestion"             : df.iat[index, valida_data.CI["GESTION"]],
                        "central"             : df.iat[index, valida_data.CI["CENTRAL"]],
                        "eliminacion"         : df.iat[index, valida_data.CI["ELIMINACION"]],
                        "seleccion"           : df.iat[index, valida_data.CI["SELECCION"]],
                        "conservacion"        : df.iat[index, valida_data.CI["CONSERVACION TOTAL"]],
                        "micro_digitalizacion": df.iat[index, valida_data.CI["MEDIO TECNICO"]],
                        "dependencia_id"      : None
                    },                    
                    "subseries": {},
                    "tipos": [],
                    "id": None
                }
                estructura[dependencia]["series"][serie] = dato 
                subserie, tipo = None, None

            case "SS":
                subserie = df['CODIGO'][index]
                dato = {
                    "record": {
                        "tabla"               : "TRD", 
                        "codigo"              : df.iat[index, valida_data.CI["CODIGO"]], 
                        "nombre"              : df.iat[index, valida_data.CI["NOMBRE_SS"]],
                        "gestion"             : df.iat[index, valida_data.CI["GESTION"]],
                        "central"             : df.iat[index, valida_data.CI["CENTRAL"]],
                        "eliminacion"         : df.iat[index, valida_data.CI["ELIMINACION"]],
                        "seleccion"           : df.iat[index, valida_data.CI["SELECCION"]],
                        "conservacion"        : df.iat[index, valida_data.CI["CONSERVACION TOTAL"]],
                        "micro_digitalizacion": df.iat[index, valida_data.CI["MEDIO TECNICO"]],
                        "serie_id"            : None
                    },                    
                    "tipos": [],
                    "id": None
                }
                estructura[dependencia]["series"][serie]["subseries"][subserie] = dato
                tipo = None

            case "T":
                dato = {
                    "record": {
                        "tabla"      : "TRD", 
                        "nombre"     : df.iat[index, valida_data.CI["NOMBRE_T"]],
                        "papel"      : df.iat[index, valida_data.CI["GESTION"]],
                        "electronico":  df.iat[index, valida_data.CI["CENTRAL"]],
                        "serie_id"   : None,
                        "subserie_id": None
                    },                    
                    "id": None
                }
                if subserie is None:
                    estructura[dependencia]["series"][serie]["tipos"].append(dato)
                else:
                    estructura[dependencia]["series"][serie]["subseries"][subserie]["tipos"].append(dato)

    return estructura 


def salvar_data(estructura, trd_id):
    dependencia_id, serie_id, subserie_id, tipo_id = None, None, None, None
    for dependencia in estructura.values():
        print("**********")
        pprint.pprint(dependencia)  

        # crea dependencia
        record = dependencia["record"]
        record["trd_id"] = trd_id
        dependencia_id = trd.dependencia.crea_registro(record, trd_id)["id"]

        # crea serie
        for serie in dependencia["series"].values():
            record = serie["record"]
            record["dependencia_id"] = dependencia_id 
            serie_id = trd.serie.crea_registro(record, trd_id)["id"]

            # crea tipo
            for tipo in serie["tipos"]:
                record = tipo["record"]
                record["serie_id"] = serie_id 
                tipo_id = trd.tipo.crea_registro(record, trd_id)["id"]
            
            # crea subserie
            for subserie in serie["subseries"].values():
                record = subserie["record"]
                record["serie_id"] = serie_id 
                subserie_id = trd.subserie.crea_registro(record, trd_id)["id"]

                # crea tipo
                for tipo in subserie["tipos"]:
                    record = tipo["record"]
                    record["subserie_id"] = subserie_id 
                    tipo_id = trd.tipo.crea_registro(record, trd_id)["id"]