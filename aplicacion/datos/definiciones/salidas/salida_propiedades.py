#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

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