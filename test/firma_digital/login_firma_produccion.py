#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import requests
import base64

#########
# LOGIN #
#########
# Url firma
#url_login  = "https://hdko60xft2.execute-api.us-east-2.amazonaws.com/pro/authentication/api/Login"
url_login  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/authentication/api/Login"
#url_login  = "https://tsa.gse.com.co"

# Informaci�n usuario PRUEBAS
data = {
    'usuario': 'esapuser',
    #'clave'  : 'oukVV4eb8I'
    'clave'  : '7v40RK5C'
}


# Login para token de firma
respuesta = requests.post(url_login, json = data)
print(respuesta.json())
token     = respuesta.json()["token"]

#########
# FIRMA #
#########
# Url firma
#url_firma  = "https://hdko60xft2.execute-api.us-east-2.amazonaws.com/pro/signature/api/sign/pades"
url_firma  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/signature/api/sign/pades"
#url_firma  = "https://tsa.gse.com.co"

# Encabezado de autenticaci�n
bearer     = "Bearer " + token
encabezado = {'Authorization': bearer}

# Informaci�n firma
# Pdf base 64
with open("d:/ntc4095.pdf", "rb") as pdf_file:
    pdf_base64 = base64.b64encode(pdf_file.read())

# Datos envio
data = {
    'numeroDocumento': '52412',
    'base64'         : pdf_base64,
    #'clave'          : 'oukVV4eb8I', 
    #'clave'          : '2K8G5TYLMP',      
    'clave'          : 'Escuela11',
    "conLTV"         : False,
    "conEstampa"     : False,
    "conEstampa"     : False,
    "firmaVisible"   : False
}

# Login para token de firma
respuesta = requests.post(url_firma, headers=encabezado, json=data)

print("respuesta")
pprint.pprint(respuesta.json())
#print("respuesta:", respuesta.text)