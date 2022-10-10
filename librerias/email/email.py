#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, sys, os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.base      import MIMEBase
from email                import encoders
from email.mime.image     import MIMEImage

def mensaje_base(de, para, asunto, archivos=[]):
    mensaje            = MIMEMultipart()
    # Remitente
    mensaje['From']    = de
    # Destinatario
    print("para:", para, type(para))
    mensaje['To']      = ",".join(para)
    # Asunto
    mensaje['Subject'] = asunto
    # Anexos
    for archivo_nombre in archivos:
        archivo_anexo = open(archivo_nombre, 'rb')
        carga_util    = MIMEBase('application', 'octate-stream')
        carga_util.set_payload((archivo_anexo).read())
        encoders.encode_base64(carga_util) 
        carga_util.add_header('Content-Disposition', "attachment", filename=os.path.basename(archivo_nombre) )
        mensaje.attach(carga_util)
        
    return mensaje

def mensaje_texto(de, para, asunto, contenido, archivos=[]):
    mensaje = mensaje_base(de, para, asunto, archivos)
    mensaje.attach(MIMEText(contenido, 'plain', 'utf-8'))
        
    return mensaje

def mensaje_html(de, para, asunto, contenido, archivos=[]):
    mensaje = mensaje_base(de, para, asunto, archivos)
    mensaje.attach(MIMEText(contenido, 'html', 'utf-8'))
        
    return mensaje

def mensaje_imagen(de, para, asunto, imagen, archivos=[]):
    html = """\
    <html>
        <head></head>
        <body>
            <img src="cid:imagen_contenido.jpg">
        </body>
    </html>
    """
    mensaje = mensaje_base(de, para, asunto, archivos)
    mensaje.attach(MIMEText(html, 'html', 'utf-8'))

    with open(imagen, 'rb') as fi:
        mensaje_imagen = MIMEImage(fi.read())

    mensaje_imagen.add_header('Content-ID', '<imagen_contenido.jpg>')
    mensaje_imagen.add_header('X-Attachment-Id', 'imagen_contenido.jpg')
    mensaje_imagen.add_header('Content-Disposition', 'inline', filename='imagen_contenido.jpg')
    mensaje.attach(mensaje_imagen)
        
    return mensaje

def enviar_mensaje_smtp(mensaje, de, clave, para, direccion, puerto):
    print("")
    print("++++++++++ EMAIL")
    print("")
    print("de, clave:", de, clave)
    print("")
    print("")
    print("")
    
    texto  = mensaje.as_string()
    server = smtplib.SMTP(direccion, puerto)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(de, clave)
    server.sendmail(de, para, texto)
    server.quit()    