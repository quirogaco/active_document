#!/usr/bin/python
# -*- coding: utf-8 -*-

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
    url_completa = servicio + "://" + url + ":" + str(puerto) + "/ConvertService.ashx"
    encabezado = {'accept': 'application/json'}
    print("")
    print("")
    print("0--- llamar_conversion", url_completa)
    retorna = requests.post( 
        url_completa, 
        json=parametros, 
        headers=encabezado,
        verify=False
        #verify='/docker_data/only_office/data/certs/raiz.cer',
        # cert=(
        #     '/docker_data/only_office/data/certs/onlyoffice.crt', 
        #     '/docker_data/only_office/data/certs/onlyoffice.key'
        # )     
    )
    print(retorna.text)
    respuesta = retorna.json()
    pprint.pprint(respuesta)
    fileUrl = respuesta['fileUrl']
    print("1--- llamar_conversion -> fileUrl", fileUrl)
    pdfConvertido = requests.get(
        fileUrl,
        verify=False
    )

    return pdfConvertido.content


# PDF - FORMATO 
def crear_pdf(url, puerto, parametros={}, ruta_destino=None, servicio="http"):
    contenido      = llamar_conversion(url, puerto, parametros, servicio)
    ruta_respuesta = salvar_convertido(contenido, ruta_destino=ruta_destino, tipo_archivo="pdf")
    
    return ruta_respuesta

def a_pdf(url, puerto, parametros={}, ruta_destino=None):
    parametros['outputtype'] =  "pdf"
    
    return crear_pdf(url, puerto, parametros, ruta_destino)

def a_pdfa(url, puerto, parametros={}, ruta_destino=None, servicio="http"):
    parametros['outputtype'] =  "pdfa"
    
    return crear_pdf(url, puerto, parametros, ruta_destino, servicio)


# HTML - FORMATO 
def a_html(url, puerto, parametros={}, ruta_destino=None, servicio="http"):
    parametros['outputtype'] =  "html"
    contenido      = llamar_conversion(url, puerto, parametros, servicio)
    ruta_respuesta = salvar_convertido(contenido, ruta_destino=ruta_destino, tipo_archivo="html")
    
    return ruta_respuesta

def a_html_contenido(url, puerto, parametros={}, servicio="http"):
    parametros['outputtype'] =  "html"
    contenido = llamar_conversion(url, puerto, parametros, servicio)
    
    return contenido


# PNG - FORMATO 
def a_png(url, puerto, parametros={}, ruta_destino=None, servicio="http"):
    parametros['outputtype'] =  "png"
    contenido      = llamar_conversion(url, puerto, parametros, servicio)
    ruta_respuesta = salvar_convertido(contenido, ruta_destino=ruta_destino, tipo_archivo="png")
    
    return ruta_respuesta

# JPG - FORMATO 
def a_jpg(url, puerto, parametros={}, ruta_destino=None, servicio="http"):
    parametros['outputtype'] =  "jpg"
    contenido      = llamar_conversion(url, puerto, parametros, servicio)
    ruta_respuesta = salvar_convertido(contenido, ruta_destino=ruta_destino, tipo_archivo="jpg")
    
    return ruta_respuesta