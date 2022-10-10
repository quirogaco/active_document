#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import requests
import base64

def firmar_salvar(url_firma, encabezado, data):
    # Firma documento
    respuesta = requests.post(url_firma, headers=encabezado, json=data)

    # Respuesta  
    respuesta_json = respuesta.json()
    # str obliga a que json compolete la descarga
    # si no se hace genera None
    pdf_64         = str(respuesta_json["documentoFirmado"])

    # Salva pdf
    pdf_bytes      = base64.b64decode(pdf_64, validate=True)
    f = open('firmado.pdf', 'wb')
    f.write(pdf_bytes)
    f.close()
    
def firmar_documento():
    #########
    # LOGIN #
    #########
    # Url firma
    url_login  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/authentication/api/Login"
    # Informaci�n usuario PRUEBAS
    data = {
        'usuario': 'esapuser',
        'clave'  : '7v40RK5C'
        #'clave': 'oukVV4eb8I'
    }
    # Login para token de firma
    respuesta = requests.post(url_login, json = data)
    token     = respuesta.json()["token"]

    #########
    # FIRMA #
    #########
    # Url firma
    url_firma  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/signature/api/sign/pades"
    # Encabezado de autenticac�n
    bearer     = "Bearer " + token
    encabezado = {'Authorization': bearer}
    # Informaci�n firma
    # Pdf base 64
    #with open("d:/Activiti_User_Guide.pdf", "rb") as pdf_file:
    with open("d:/MODIFCADO.pdf", "rb") as pdf_file:
        pdf_base64 = base64.b64encode(pdf_file.read())

    # Datos envio
    """
    data = {
        'numeroDocumento': '52412',        # Documento certificado que me entregan despues de registrar formalmente el certificado
        'base64'         : pdf_base64,
        'clave'          : '2K8G5TYLMP', # Clave certificado que me entregan despues de registrar formalmente el certificado
        "conLTV"         : False,
        "conEstampa"     : False,
        "conEstampa"     : False,
        "firmaVisible"   : False
    }
    """

    data = {
        'numeroDocumento': '52412',        # Documento certificado que me entregan despues de registrar formalmente el certificado
        'base64'         : pdf_base64,
        'clave'          : 'Escuela11', # Clave certificado que me entregan despues de registrar formalmente el certificado        
        #'clave'          : '2K8G5TYLMP',
        "conLTV"         : False,
        "conEstampa"     : False,
        "conEstampa"     : False,
        "firmaVisible"   : False
    }

    firmar_salvar(url_firma, encabezado, data)

firmar_documento()