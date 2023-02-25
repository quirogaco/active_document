#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime, random 

from librerias.datos.sql import sqalchemy_leer
from librerias.datos.archivos import leer_archivo
from aplicacion.especificos.configuracion_general import configuracion_general
from aplicacion.trabajadores import utilidades
from aplicacion.trabajadores_base import radicados_celery
from librerias.email import email
from aplicacion.comunes import indexar_datos
from aplicacion.logs import crea_logs

# Envia correo notificando radicado
def notificar_correo(
    correos, 
    asunto, 
    pdf_ruta, 
    jpg_ruta, 
    anexos=[], 
    datos_log={}
):
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

        # Log de ntoficacion
        crea_logs.crea_log(datos_log)


# Funcion invocado desde celery
def enviar_correo_radicado(datos={}):
    tipo = datos.get("tipo", "ENTRADA") 
    radicado_id = datos.get("id", None)

    # Log de notificacion
    detalle = (
        "NOTIFICACION DE RADICADO A CUENTA: " + 
        datos["correos"]
    )
    datos_log = {
        "accionante_tipo": "SISTEMA",      
        "accionante_id": "",  
        "destinatario_tipo": "",      
        "destinatario_id": "", 
        "proceso": "GESTION",
        #"fuente": "radicados_salida",
        "fuente_id": radicado_id, 
        "accion": "NOTIFICAR",  
        "detalle": detalle,
        "estado": "RADICADO",  
        "detalle_estado": detalle
    }
    #
    if tipo == "ENTRADA":
        fuente = "radicados_entrada"
        radicado = sqalchemy_leer.leer_un_registro(
            fuente, 
            radicado_id
        )
        datos_log["fuente"] = fuente
        
    elif tipo == "SALIDA":
        fuente = "radicados_salida"
        radicado = sqalchemy_leer.leer_un_registro(
            fuente, 
            radicado_id
        )
        datos_log["fuente"] = fuente

    elif tipo == "INTERNO":
        fuente = "radicados_interno"
        radicado = sqalchemy_leer.leer_un_registro(
            fuente, 
            radicado_id
        )
        datos_log["fuente"] = fuente

    anexos = []
    for archivo in radicado["archivos"]:
        anexos.append( leer_archivo.salva_archivo_minio(archivo["id"]))

    notificar_correo(
        datos["correos"], 
        datos["asunto"], 
        datos["ruta_pdf"], 
        datos["ruta_jpg"],
        anexos,
        datos_log        
    )

    # Indexa de ultimo
    indexar_datos.indexar_estructura(
        fuente, 
        radicado_id, 
        retardo=120
    )


# Función que invoca llamado celery
def  invoca_enviar_correo_radicado(datos):
    radicados_celery.radicados_app_radicado_pdf_envia.apply_async(**utilidades.parametros(
        'radicados', 
        parametros={
            "datos": datos
        },
        retardo=120
    ))