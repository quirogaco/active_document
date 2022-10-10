#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import requests
import base64

usuario =  'esapuser'
clave   = '7v40RK5C'

#########
# LOGIN #
#########
# Url firma
url_login  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/authentication/api/Login"

# Informaci�n usuario PRUEBAS
data = {
    'usuario': usuario,
    'clave'  : clave
}

# Login para token de firma
respuesta = requests.post(url_login, json = data)
token     = respuesta.json()["token"]
print("token:", token)


#############
# ESTAMPADO #
#############
usuario_estampado = "899999054"
clave_estampado   = "9YZ/8ptbqtmfa+DpE3lzTxuRPsd1rNNyy8SY9O8E4URQhxG0eEKWOkEpyV9C/NzU2wvWz022wWqEoRIdP0fxpISuiyd9xxQx1WZDTyVg/lU="

# Url firma
url_firma  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/signature/api/sign/stamp"

# Encabezado de autenticaci�n
bearer     = "Bearer " + token
encabezado = {'Authorization': bearer}

# Pdf base 64
with open("d:/ntc4095.pdf", "rb") as pdf_file:
    pdf_base64 = base64.b64encode(pdf_file.read())

# Informaci�n firma
data = {
    'usuario': usuario_estampado,
    'clave'  : clave_estampado,
    'base64' : pdf_base64
}

# Estampar
pprint.pprint(encabezado)
respuesta = requests.post(url_firma, headers=encabezado, json=data)

# Respuesta
respuesta_json = respuesta.json()
pdf_64         = respuesta_json["base64"]

# Salva pdf
pdf_bytes = base64.b64decode(pdf_64, validate=True)
f = open('estampado.pdf', 'wb')
f.write(pdf_bytes)
f.close()