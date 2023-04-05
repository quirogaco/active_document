#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, os, builtins, datetime

from aplicacion.especificos.configuracion_general import configuracion_general
from librerias.datos.sql             import sqalchemy_filtrar
from librerias.email                 import email

def notifica(radicado_id, responsable_id):
    print("")
    print("********************************************************************")
    print("********************* NOTIFICA RADICADO **************************")    
    print("")
    # Radicado
    filtros   = [ [ "id", "=", radicado_id ] ]
    radicados = sqalchemy_filtrar.filtrarOrdena(estructura="radicados_entrada", filtros=filtros, ordenamientos=[])

    # Usuario
    filtros   = [ [ "id", "=", responsable_id ] ]
    usuarios  = sqalchemy_filtrar.filtrarOrdena(estructura="usuarios", filtros=filtros, ordenamientos=[])

    # Notificiaci�n
    if (len(usuarios) > 0) and (len(radicados) > 0):
        usuario  = usuarios[0]
        radicado = radicados[0]
        correo   = usuario["correo"]
        pprint.pprint(usuario)
        print("--------------------------------")
        pprint.pprint(correo)
        # Si tiene correo
        if correo not in [", None"]:
            configuracion = configuracion_general.leer_registro_configuracion("radicacion_canales")
            if configuracion != None:
                canales   = configuracion["datos"]      
                # Cuenta origen  
                de             = canales.get("notificacion_usuario_smtp", None)
                clave          = canales.get("notificacion_clave_smtp", None)
                # Informaci�n SMTP
                direccion_smtp = canales.get("notificacion_servidor_smtp", None)
                puerto_smtp    = canales.get("notificacion_puerto_smtp", None)
                print("SMTP :", de, clave, direccion_smtp)

                asunto         = "Se asigno radicado [" + radicado["nro_radicado"] + "]"
                contenido      = asunto
                para           = correo.split(",")
                asunto         = asunto     
                archivos       = []
            
                print("NOTIFICA :", para)
                # Crea correo
                mensaje = email.mensaje_texto(
                    de, 
                    para, 
                    asunto, 
                    contenido,
                    archivos=archivos
                )

                # Envia correo
                email.enviar_mensaje_smtp(
                    mensaje, 
                    de, 
                    clave, 
                    para, 
                    direccion_smtp, 
                    puerto_smtp
                )

    print("********************************************************************")    
    print("")
    print("")