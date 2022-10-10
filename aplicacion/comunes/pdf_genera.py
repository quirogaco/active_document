#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime, random 

from librerias.datos.sql    import sqalchemy_filtrar
from aplicacion.comunes     import manejo_plantillas
from aplicacion.especificos.configuracion_general import configuracion_general

############
# ENTRADAS #
############
# Recupera plantilla del canal y tipo de remitente
def recupera_plantilla(tipo_plantilla, canal_id=None):
    canal        = None
    plantilla    = None
    plantilla_id = None

    # Lee canal
    if canal_id != None:
        filtros = [ [ "id", "=", canal_id ] ]
        canales = sqalchemy_filtrar.filtrarOrdena(estructura="canales_comunicacion", filtros=filtros, ordenamientos=[])
        if len(canales) > 0:
            canal = canales[0]

    # Lee plantilla
    if canal != None:
        if tipo_plantilla == "WEB_JURIDICA":
            plantilla_id = canal["plantilla_juridica_id"]
    
        if tipo_plantilla == "WEB_NATURAL":
            plantilla_id = canal["plantilla_natural_id"]

        if tipo_plantilla == "WEB_ANONIMO":
            plantilla_id = canal["plantilla_anonima_id"]

    if plantilla_id != None:
        filtros    = [ [ "id", "=", plantilla_id ] ]
        plantillas = sqalchemy_filtrar.filtrarOrdena(estructura="plantillas", filtros=filtros, ordenamientos=[])
        if len(plantillas) > 0:
            plantilla = plantillas[0]

    return plantilla

# Genera PDF BASADO EN PLANTILLA
def generacion_pdf_radicado(datos, tipo_plantilla, id_tarea, web=False):
    canal_id = None
    ruta_pdf = "" 
    ruta_jpg = ""  

    if web == True:
        # Si se radico via pagina WEB
        configuracion = configuracion_general.leer_registro_configuracion("radicacion_canales")
        if configuracion != None:
            # Lee canal de comunicación        
            canales   = configuracion["datos"]        
            canal_id  = canales.get("canal_web", None)
    else:
        # Se radico desde formulario del sistema PQRS o VENTANILLA
        canal_id = datos["canal_radicado_id"]
    
    # Recupera plantilla 
    plantilla = recupera_plantilla(tipo_plantilla, canal_id)
    if plantilla != None:
        ruta_pdf, ruta_jpg = manejo_plantillas.crear_pdf_plantilla(plantilla["id"], datos, id_tarea)
        
    return ruta_pdf, ruta_jpg   


###########
# SALIDAS #
###########
def generacion_pdf_borrador(datos, id_tarea):
    ruta_pdf = "" 
    ruta_jpg = ""  
    if datos["borrador_id"] != None:
        ruta_pdf, ruta_jpg = manejo_plantillas.crear_pdf_borrador(datos["borrador_id"], datos, id_tarea)
        
    return ruta_pdf, ruta_jpg   