#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, os, builtins, datetime

from librerias.datos.sql             import sqalchemy_filtrar
from librerias.documentos.plantillas import word_plantilla
from librerias.documentos.conversion import conversion
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

    # Notificiación
    if (len(usuarios) > 0) and (len(radicados) > 0):
        usuario  = usuarios[0]
        radicado = radicados[0]
        correo   = usuario["correo"]
        pprint.pprint(usuario)
        print("--------------------------------")
        pprint.pprint(correo)
        # Si tiene correo
        if correo not in [", None"]:
            asunto         = "Se asigno radicado [" + radicado["nro_radicado"] + "]"
            contenido      = asunto
            # Datos
            de             = "quirogaco@gmail.com"
            clave          = "sreojrjewsjkxnml"
            para           = correo.split(",")
            asunto         = asunto     
            archivos       = []
            # Direccion servidor correo
            direccion_smtp = "smtp.gmail.com"
            puerto_smtp    = 587

            print("NOTIFICA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA:", para)
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