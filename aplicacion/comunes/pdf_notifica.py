#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint, datetime, random 

from aplicacion.comunes import manejo_archivos
 
from . import pdf_envia
from . import pdf_genera 

# Insertar anexo a RADICADO ENTRADA
def insertar_anexos(estructura, nro_radicado, radicado_id, archivo, tipo_archivo, id_tarea, tipo_relacion = "notificacion"):
    archivos = [{
        "nombre_completo": archivo,
        "nombre"         : ("notifica_radicado_" + nro_radicado + ".pdf")
    }]
    manejo_archivos.manejo(estructura, "insertar", {"id":radicado_id}, archivos, id_tarea, tipo_relacion)

# ENTRADA -> Genera plantilla, notifica por correo, y anexo notificación
def notifica_entrada(datos, id_tarea):
    # Genera PLANTILLA
    ruta_pdf = "" 
    ruta_jpg = ""  
    plantillas_tipo = {
        "ANONIMO" : "WEB_ANONIMO",
        "NATURAL" : "WEB_NATURAL",
        "JURIDICA": "WEB_JURIDICA"
    }    

    # Selecciona tipo plantilla
    tipo_plantilla = ""
    web = False
    formulario_web = datos.get("formulario_web", None)    
    if (formulario_web not in ["", None]):    
        # Formulario WEB
        web = True
        tipo_plantilla = plantillas_tipo[formulario_web]
    else:
        # Radicados PQRS, DOCUMENTO, TRAMITE
        clase_radicado = datos.get("clase_radicado", None)
        tercero_clase = datos.get("clase", None)
        #print("clase_radicado, tercero_clase: ", clase_radicado, tercero_clase)
        if (clase_radicado in ["PQRSD", "DOCUMENTO", "TRAMITE"]) and (tercero_clase in ["ANONIMO", "NATURAL", "JURIDICA"]):
            tipo_plantilla = plantillas_tipo[tercero_clase]
        #print("tipo_plantilla: ", tipo_plantilla)
        
    # Genera PDF   
    if tipo_plantilla not in ["", None]:
        ruta_pdf, ruta_jpg = pdf_genera.generacion_pdf_radicado(datos, tipo_plantilla, id_tarea, web)

    # Inserta anexo de notificación al radicado.
    if ruta_pdf != "":
        insertar_anexos("radicados_entrada", datos["nro_radicado"], datos["id"], ruta_pdf, "notificacion", id_tarea, "notificacion")

    # Notifica PDF Radicación
    correos = datos["correo_electronico"]
    if (correos not in ["", None]) and (ruta_pdf not in ["", None]) :
        asunto = "Notifica Radicación con número: [" + datos["nro_radicado"] + "]"
        pdf_envia.invoca_enviar_correo_radicado({"correos": correos, "asunto": asunto, "ruta_pdf": ruta_pdf, "ruta_jpg": ruta_jpg})
    
    return ruta_pdf, ruta_jpg

# SALIDA -> Genera pdf, notifica por correo, y anexo notificación
def notifica_salida(datos, id_tarea):    
    # Genera PDF
    ruta_pdf, ruta_jpg = pdf_genera.generacion_pdf_borrador(datos, id_tarea)

    # Inserta anexo de notificación al radicado.
    if ruta_pdf != "":                         
        insertar_anexos("radicados_salida", datos["nro_radicado"], datos["id"], ruta_pdf, "respuesta", id_tarea, "respuesta")

    # Notifica PDF Radicación
    # correos = datos["correo_electronico"]
    # if (correos not in ["", None]) and (ruta_pdf not in ["", None]) :
    #     asunto = "Notifica Radicación con número: [" + datos["nro_radicado"] + "]"
    #     pdf_envia.invoca_enviar_correo_radicado({"correos": correos, "asunto": asunto, "ruta_pdf": ruta_pdf, "ruta_jpg": ruta_jpg})
    
    return ruta_pdf, ruta_jpg  

def pdf_notificacion(radicado_tipo, datos, id_tarea):
    # print("")
    # print("................................")
    # print("pdf_notificacion")
    # pprint.pprint(datos)
    if radicado_tipo == "ENTRADA":
        notifica_entrada(datos, id_tarea)

    if radicado_tipo == "SALIDA":
        notifica_salida(datos, id_tarea)