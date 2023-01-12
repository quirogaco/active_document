#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime, random 

from librerias.datos.sql import sqalchemy_leer
from librerias.datos.archivos import leer_archivo
from aplicacion.especificos.configuracion_general import configuracion_general
from aplicacion.trabajadores import utilidades
from aplicacion.trabajadores_base import radicados_celery
from librerias.email import email

# Envia correo notificando radicado
def notificar_correo(correos, asunto, pdf_ruta, jpg_ruta, anexos=[]):
    #de             = "quirogaco@gmail.com"
    #clave          = "sreojrjewsjkxnml"
     #direccion_smtp = "smtp.gmail.com"

    #de             = "ventanillaunicapruebas@esap.edu.co"
    #clave          = "Fabian2021*"
    #direccion_smtp = "SMTP.OFFICE365.COM"
    #puerto_smtp    = 587

    #print("CELERY ENVIA-1")
    
    # Carga datos de conexión
    configuracion = configuracion_general.leer_registro_configuracion("radicacion_canales")
    if configuracion != None:
        canales   = configuracion["datos"] 
        # Cuenta origen  
        de             = canales.get("notificacion_usuario_smtp", None)
        clave          = canales.get("notificacion_clave_smtp", None)
        # Información SMTP
        direccion_smtp = canales.get("notificacion_servidor_smtp", None)
        puerto_smtp    = canales.get("notificacion_puerto_smtp", None)

        """
        print("")       
        print("****************-1") 
        print("de, clave, direccion_smtp, puerto_smtp :", de, clave, direccion_smtp, puerto_smtp) 
        print("") 
        """

        # Información correo
        para = correos.split(",")
        asunto = asunto     
        #archivos       = list(set([pdf_ruta] + anexos))
        archivos = anexos
        
        # Envio de correo
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

# Funcion invocado desde celery
def enviar_correo_radicado(datos={}):
    tipo = datos.get("tipo", "ENTRADA") 
    radicado_id = datos.get("id", None)
    if tipo == "ENTRADA":
        radicado = sqalchemy_leer.leer_un_registro(
            "radicados_entrada", 
            radicado_id
        )
    else:
        radicado = sqalchemy_leer.leer_un_registro(
            "radicados_salida", 
            radicado_id
        ) 

    anexos = []
    for archivo in radicado["archivos"]:
        anexos.append( leer_archivo.salva_archivo_minio(archivo["id"]))

    notificar_correo(
        datos["correos"], 
        datos["asunto"], 
        datos["ruta_pdf"], 
        datos["ruta_jpg"],
        anexos
    )

# Función que invoca llamado celery
def invoca_enviar_correo_radicado(datos):
    radicados_celery.radicados_app_radicado_pdf_envia.apply_async(**utilidades.parametros(
        'radicados', 
        parametros={
            "datos": datos
        },
        retardo=120
    ))