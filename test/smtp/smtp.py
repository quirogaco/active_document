#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
import smtplib

import configuracion_base

from librerias.datos.elastic import elastic_operaciones
from librerias.datos.sql     import sqalchemy_leer
from librerias.datos.base    import globales

from librerias.email         import email

def enviar_mensaje_smtp(asunto, de, clave, para, direccion, puerto):
    mensaje = email.mensaje_texto(de, [para], asunto, asunto, archivos=[])
    texto   = mensaje.as_string()
    print("texto:", texto)
    server  = smtplib.SMTP(direccion, puerto)
    server.set_debuglevel(1)
    server.ehlo()
    print( server.starttls() )
    print( server.login(de, clave) )
    server.sendmail(de, [para], texto)
    print( server.quit() )    

enviar_mensaje_smtp("PRUEBA CORREO....", "ventanillaunicapruebas@esap.edu.co", "Fabian2021*", "quirogaco@gmail.com", "SMTP.OFFICE365.COM", "587")