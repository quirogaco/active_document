#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime, random 

from librerias.datos.base   import globales
from librerias.datos.sql    import sqalchemy_leer, sqalchemy_filtrar
from aplicacion.datos.redis import redis_datos
from aplicacion.comunes     import manejo_plantillas, manejo_archivos
from aplicacion.especificos.configuracion_general import configuracion_general

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
        # Se radico desde formulario del sistema PQRS o VENTANILL
        canal_id = datos["canal_radicado_id"]
    
    # Recupera plantilla
    plantilla = recupera_plantilla(tipo_plantilla, canal_id)
    if plantilla != None:
        ruta_pdf, ruta_jpg = manejo_plantillas.crear_pdf_plantilla(plantilla["tipo"], datos, id_tarea)
        
    return ruta_pdf, ruta_jpg   

from librerias.email import email

def notificar_correo(correos, asunto, pdf_ruta, jpg_ruta):
    # Datos
    de             = "quirogaco@gmail.com"
    clave          = "sreojrjewsjkxnml"
    para           = correos.split(",")
    asunto         = asunto     
    archivos       = [ pdf_ruta]
    # Direccion servidor correo
    direccion_smtp = "smtp.gmail.com"
    puerto_smtp    = 587

    mensaje = email.mensaje_imagen(
        de, 
        para, 
        asunto, 
        jpg_ruta, 
        archivos=archivos
    )

    email.enviar_mensaje_smtp(
        mensaje, 
        de, 
        clave, 
        para, 
        direccion_smtp, 
        puerto_smtp
    )

def insertar_anexos(nro_radicado, radicado_id, archivo, tipo_archivo, id_tarea):
    archivos = [{
        "nombre_completo": archivo,
        "nombre"         : ("notifica_radicado_" + nro_radicado + ".pdf")
    }]
    manejo_archivos.manejo("plantillas", "insertar", {"id":radicado_id}, archivos, id_tarea, tipo_relacion = "notificacion") #, "plantillas")

def pdf_notificacion(datos, id_tarea):
    # Genera PLANTILLA
    ruta_pdf        = "" 
    ruta_jpg        = ""  
    plantilla       = ""       
    plantillas_tipo = {
        "ANONIMO" : "WEB_ANONIMO",
        "NATURAL" : "WEB_NATURAL",
        "JURIDICA": "WEB_JURIDICA"
    }
    # Si es formulario WEB
    web            = False
    medio_radicado = datos.get("medio_radicado", None)    
    tipo_web       = datos.get("tipo_web", "")
    if (medio_radicado == "WEB") and (tipo_web in ["ANONIMO", "NATURAL", "JURIDICA"]):    
        web            = True    
        tipo_plantilla = plantillas_tipo[tipo_web]

    # Radicados PQRS, VENTANILLA     
    if (medio_radicado is None):
        clase_radicado = datos.get("clase_radicado", None)
        tercero_clase  = datos.get("tercero_clase", None)
        if (clase_radicado in ["PQRS", "VENTANILLA"]) and (tercero_clase in ["ANONIMO", "NATURAL", "JURIDICA"]):
            tipo_plantilla = plantillas_tipo[tercero_clase]
    
    if tipo_plantilla not in ["", None]:
        print("tipo_plantilla:", tipo_plantilla)
        ruta_pdf, ruta_jpg = generacion_pdf_radicado(datos, tipo_plantilla, id_tarea, web)
        print("ruta_pdf, ruta_jpg:", ruta_pdf, ruta_jpg)
        

    # Notifica PDF Radicaciï¿œn
    correos = datos["tercero_correo_electronico"]
    if (correos not in ["", None]) and (ruta_pdf not in ["", None]) :
        asunto = "Notifica Radicaciï¿œn con # [" + datos["nro_radicado"] + "]"
        notificar_correo(correos, asunto, ruta_pdf, ruta_jpg)

    if ruta_pdf != "":
        insertar_anexos(datos["nro_radicado"], datos["id"], ruta_pdf, "notificacion", id_tarea)
        
    return ruta_pdf, ruta_jpg