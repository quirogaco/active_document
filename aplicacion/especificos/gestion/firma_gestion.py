#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, tempfile, pprint, datetime, builtins
import requests
import base64

from librerias.datos.minio   import minio_acciones
from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_leer, sqalchemy_filtrar 
from librerias.datos.elastic import elastic_operaciones
from librerias.utilidades    import basicas 

from aplicacion.comunes       import indexar_datos
from librerias.datos.archivos import leer_archivo

def recuperar_archivo_salida(salida_id):
    nombre_archivo = ""
    relacion       = {}
    archivo        = {}
    # Recupera registro borrador
    ordenar    = [ [ "descendente", "creado_en_" ] ]
    filtros    = [ [ "tipo_relacion", "=", "respuesta" ], [ "origen", "=", "radicados_salida" ], [ "origen_id", "=", salida_id ] ]
    relaciones = sqalchemy_filtrar.filtrarOrdena(estructura="archivos_relacion", filtros=filtros, ordenamientos=ordenar)        
    # Si existen relaciones 
    if len(relaciones) > 0:
        relacion   = relaciones[0]
        archivo_id = relacion['archivo_id']    
        archivo    = sqalchemy_leer.leer_un_registro("archivos_anexos", archivo_id)
        # Recupera archivo de minio
        nombre_archivo = leer_archivo.salva_archivo_minio(archivo_id) 

    return nombre_archivo, archivo

# Modifica registro de gestión 
def modifica_peticion(peticion_id, datos):
    sqalchemy_modificar.modificar_un_registro("peticiones", peticion_id, datos)
    elastic_operaciones.indexar_registro("peticiones", peticion_id)

    gestion = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)
    if gestion["origen_tipo"] == "ENTRADA":
        indexar_datos.indexar_estructura("radicados_entrada", gestion["origen_id"], retardo=120)

def firmar_salvar(url_firma, encabezado, data):
    # Firma documento
    respuesta = requests.post(
        url_firma, 
        headers=encabezado, 
        json=data,
        verify=False
    )

    # Respuesta  
    respuesta_json = respuesta.json()
    # str obliga a que json compolete la descarga
    # si no se hace genera None
    pdf_64         = str(respuesta_json["documentoFirmado"])

    # Salva pdf
    ruta_destino = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + "." + "pdf"
    pdf_bytes    = base64.b64decode(pdf_64, validate=True)
    f = open(ruta_destino, 'wb')
    f.write(pdf_bytes)
    f.close()

    return ruta_destino

def firmar_leer(firmar_id):
    archivo_firmar, relacion = recuperar_archivo_salida(firmar_id)
    with open(archivo_firmar, "rb") as pdf_file:
        pdf_base64 = base64.b64encode(pdf_file.read())

    return pdf_base64, relacion
    
def firmar_documento(firmar_id):
    #########
    # LOGIN #
    #########
    # Url firma
    url_login  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/authentication/api/Login"
    # Información usuario PRUEBAS
    data = {
        'usuario': 'esapuser',
        'clave'  : '7v40RK5C'
    }
    # Login para token de firma
    respuesta = requests.post(
        url_login, 
        json = data,
        verify=False
    )
    token     = respuesta.json()["token"]

    #########
    # FIRMA #
    #########
    # Url firma
    url_firma  = "https://8uw10ruhfj.execute-api.us-east-2.amazonaws.com/qa/signature/api/sign/pades"
    # Encabezado de autenticacón
    bearer     = "Bearer " + token
    encabezado = {'Authorization': bearer}
    # Información firma
    pdf_base64, relacion = firmar_leer(firmar_id)

    # Datos envio
    data = {
        'numeroDocumento': '52412',        # Documento certificado que me entregan despues de registrar formalmente el certificado
        'base64'         : pdf_base64,
        'clave'          : '2K8G5TYLMP',
        "conLTV"         : False,
        "conEstampa"     : False,
        "conEstampa"     : False,
        "firmaVisible"   : False
    }


    firmado = firmar_salvar(url_firma, encabezado, data)

    return firmado, relacion

def firmar(accion, datos={}, archivo=[], id_tarea=""):    
    clave      = datos["datos"]["clave"]  
    usuario    = datos["datos"]["usuario"]  
    firmar_ids = datos["datos"]["firmar_ids"]  

    print("FIRMAR:")
    print(clave, usuario, firmar_ids)
    for firmar_id in firmar_ids:
        print("FIRMANDO:", firmar_id)
        firmado, relacion = firmar_documento(firmar_id)
        minio_acciones.cargar_objeto( relacion["cubeta"], relacion["nombre"], firmado)
        print("<------FIRMADO----->", firmado)
    
    return {}