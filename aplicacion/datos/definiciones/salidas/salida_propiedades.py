#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
from sqlalchemy import desc

from librerias.datos.sql  import sqalchemy_filtrar
from librerias.datos.base import globales

#####################
# FIRMA ELECTRONICA #
#####################
# Requiere firma electonica
def firma_electronica(r_):
    firma = "NO"
    if r_.tipo_firma.find("ELECTRONICA") > -1:
        firma = "SI"

    return firma

# Se firmado electronicamente
def firmado_electronica(r_):
    proceso_firma = r_.atributos_.get("proceso_firma", {})
    firmado       = proceso_firma.get("firmado_electronica", "NO")

    return firmado

# Se firmado electronicamente
def firmado_electronica_por(r_):
    proceso_firma = r_.atributos_.get("proceso_firma", {})
    firmado       = proceso_firma.get("firmado_electronica_por", "")

    return firmado

# Si esta firmado
def esta_firmado(r_):
    firmado = "NO"
    if "DIGITAL" in r_.tipo_firma:
        firmado = "SI"
    # FALTA VALIDAR POR FIRMA FISICA O ELECTRONICA

    return firmado


########
# LOGS #
########
def logs_salida(sesion, r_):
    logs = []

    return logs

# def logs_gestion(sesion, r_):
#     logs = []
#     # Busca gestion
#     for gestion_id in r_.gestion_id:
#         filtros = [ [ "fuente_id", "=", gestion_id ] ]
#         logs.extend( sqalchemy_filtrar.filtrarOrdena(estructura="logs", filtros=filtros, ordenamientos=[]) )   

#     return logs

def logs_radicado(sesion, r_):
    filtros = [ [ "fuente_id", "=", r_.id ] ]
    logs = sqalchemy_filtrar.filtrarOrdena(estructura="logs", filtros=filtros, ordenamientos=[])
    
    return logs

def logs(sesion, r_):
    lista_logs = []
    # Logs vinculados
    radicado = logs_radicado(sesion, r_)
    #gestion = logs_gestion(sesion, r_)
    
    # Log ordenado
    lista_logs.extend(radicado)
    #lista_logs.extend(gestion)
    lista_logs.sort(key=lambda x: x["creado_en_"], reverse=True)    
    setattr(r_, "logs", lista_logs)

############
# ARCHIVOS #
############
# Nombres de archivos
def archivos_nombres(sesion, r_):
    nombres = [ archivo["detalle"] for archivo in r_.archivos ]    
    setattr(r_, "archivos_nombres", ", ".join(nombres))

# Pdf base
def pdf_base(sesion, r_):
    RELACION_CLASE = globales.lee_clase("global_base_relacion_archivo")
    pdf            = {}
    for archivo in r_.archivos:
        if archivo['tipo_archivo'] == 'pdf':
            relacion = sesion.query(RELACION_CLASE).filter( RELACION_CLASE.archivo_id == archivo["id"] ).first()        
            if (relacion != None) and (relacion.tipo_relacion == "respuesta"):
                print("archivo_id", archivo["id"])
                pdf = archivo     
    setattr(r_, "pdf_base", pdf)