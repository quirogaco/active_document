#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, os, tempfile
import requests

from librerias.utilidades import basicas  

def salvar_convertido(contenido, ruta_destino=None, tipo_archivo="pdf"):
    # Archivo pdf destino"
    if ruta_destino == None:
        directorio   = tempfile.gettempdir()
        ruta_destino = directorio + os.sep + basicas.uuidTexto() + "." + tipo_archivo

    sale = open(ruta_destino, "wb")
    sale.write(contenido)
    sale.close()

    return ruta_destino

def llamar_conversion(url, puerto, parametros={}, servicio="http"):
    parametros['key'] =  basicas.uuidTexto()
    url_completa      = servicio + "://" + url + ":" + str(puerto) + "/ConvertService.ashx"
    encabezado        = {'accept': 'application/json'}
    retorna           = requests.post( 
        url_completa, 
        json=parametros, 
        headers=encabezado,
        verify=False
    )
    respuesta         = retorna.json()
    print("-------------------")
    pprint.pprint(respuesta)
    fileUrl           = respuesta['fileUrl']
    pdfConvertido     = requests.get(fileUrl)

    return pdfConvertido.content


# PDF - FORMATO 
def crear_pdf(url, puerto, parametros={}, ruta_destino=None):
    contenido      = llamar_conversion(url, puerto, parametros)
    ruta_respuesta = salvar_convertido(contenido, ruta_destino=ruta_destino, tipo_archivo="pdf")
    
    return ruta_respuesta

def a_pdf(url, puerto, parametros={}, ruta_destino=None):
    parametros['outputtype'] =  "pdf"
    
    return crear_pdf(url, puerto, parametros, ruta_destino)

def a_pdfa(url, puerto, parametros={}, ruta_destino=None):
    parametros['outputtype'] =  "pdfa"
    
    return crear_pdf(url, puerto, parametros, ruta_destino)


# HTML - FORMATO 
def a_html(url, puerto, parametros={}, ruta_destino=None):
    parametros['outputtype'] =  "html"
    contenido      = llamar_conversion(url, puerto, parametros)
    ruta_respuesta = salvar_convertido(contenido, ruta_destino=ruta_destino, tipo_archivo="html")
    
    return ruta_respuesta

def a_html_contenido(url, puerto, parametros={}):
    parametros['outputtype'] =  "html"
    contenido = llamar_conversion(url, puerto, parametros)
    
    return contenido


# PNG - FORMATO 
def a_png(url, puerto, parametros={}, ruta_destino=None):
    parametros['outputtype'] =  "png"
    contenido      = llamar_conversion(url, puerto, parametros)
    ruta_respuesta = salvar_convertido(contenido, ruta_destino=ruta_destino, tipo_archivo="png")
    
    return ruta_respuesta

# JPG - FORMATO 
def a_jpg(url, puerto, parametros={}, ruta_destino=None):
    parametros['outputtype'] =  "jpg"
    contenido      = llamar_conversion(url, puerto, parametros)
    ruta_respuesta = salvar_convertido(contenido, ruta_destino=ruta_destino, tipo_archivo="jpg")
    
    return ruta_respuesta