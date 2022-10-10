#!/usr/bin/python
# -*- coding: utf-8 -*-

import mimetypes, builtins, os, pprint

from fastapi.responses import FileResponse, ORJSONResponse
from fastapi           import Request

@_app.get( '/entregar_archivo_id/{archivo_id}')
async def entregar_archivo_id( archivo_id: str ):
    print("entregar_archivo - archivo_id:", )
    #nombre_archivo = word_plantilla.mezcla_plantilla_archivos("D:/gestor_2021_vite/test/notificacion/entrada.docx", None, datos=datos)    
    nombre_archivo = word_plantilla.mezcla_plantilla_archivos("D:/gestor_2021_vite/temporal/salida.docx", None, datos=datos)    
    media_type     = mimetypes.MimeTypes().guess_type(nombre_archivo)[0]
    print("entregar_archivo:", nombre_archivo, media_type)

    return FileResponse( nombre_archivo, media_type=media_type, filename=nombre_archivo )

@_app.get( '/entregar_archivo_temporal/{archivo_nombre}')
async def entregar_archivo_temporal( archivo_nombre: str ):
    print("entregar_archivo_temporal-0:", archivo_nombre)
    archivo_nombre = builtins.rutaBase + 'temporal' + os.sep + archivo_nombre
    media_type     = mimetypes.MimeTypes().guess_type(archivo_nombre)[0]
    print("entregar_archivo_temporal-1:", archivo_nombre, media_type)

    return FileResponse( archivo_nombre, media_type=media_type, filename=archivo_nombre )

@_app.get( '/entregar_archivo_disco/{archivo_nombre}')
async def entregar_archivo_disco( archivo_nombre: str ):
    archivo_nombre = builtins.rutaBase + 'temporal' + os.sep + "salida.docx"    
    print("entregar_archivo disco-0:", archivo_nombre)
    media_type     = mimetypes.MimeTypes().guess_type(archivo_nombre)[0]
    print("entregar_archivo disco-1:", archivo_nombre, media_type)

    return FileResponse( archivo_nombre, media_type=media_type, filename=archivo_nombre )

import base64
@_app.get( '/entregar_archivo_base64/{archivo_base64}')
async def entregar_archivo_base64( archivo_base64: str ):
    print("entregar_archivo_base64-0:")
    # Texto Base 64 a byte
    archivo_nombre_byte   = bytes(archivo_base64, 'utf8')
    # Base 64 a texto original
    decodificado          = base64.b64decode( archivo_nombre_byte.decode('ascii') )
    # Byte a texto
    archivo_nombre        = str( decodificado, 'utf-8')
    media_type            = mimetypes.MimeTypes().guess_type(archivo_nombre)[0]
    print("entregar_archivo_base64-1", archivo_nombre, media_type)

    return FileResponse( archivo_nombre, media_type=media_type, filename=archivo_nombre )
    
@_app.get( '/entregar_archivo_parametros/{archivo}/{tipo}')
async def entregar_archivo_parametros( archivo:str, tipo:str ):
    print("entregar_archivo_parametros:", archivo, tipo)
    nombre_archivo = "D:/gestor_2021_vite/temporal/salida.docx" 
    media_type     = mimetypes.MimeTypes().guess_type(nombre_archivo)[0]
    print("entregar_archivo:", nombre_archivo, media_type)

    return FileResponse( nombre_archivo, media_type=media_type, filename=nombre_archivo )

# Integración con onlyoffice con borradores
import requests
@_app.post( '/salvarOnlyOffice', response_class=ORJSONResponse )
async def salvarOnlyOffice( request: Request ):
    parametros = await request.json()
    print("parametros:")
    pprint.pprint(parametros)
    forcesavetype = parametros.get('forcesavetype', -1)
    status        = parametros.get('status', -1)
    url           = parametros.get('url', "")
    print("")
    print("********************* salvarBorradoresWord *********************", forcesavetype, status, url)    
            
    if ( (forcesavetype in [0, 1, 2]) and (status in [1, 2, 6]) ) or (status == 2):      
        borrador_id    = parametros['key']
        print("SALVAA...", borrador_id)
        ubicacion_uuid = borrador_id.find("___")
        if ubicacion_uuid > -1:
            borrador_id = borrador_id[0:ubicacion_uuid]
        url = parametros['url']
        print("url-0:", url)
        pos = url.find('/cache') 
        url = "http://" + str(builtins._appServicios) + ":80" + url[pos:]   
        print("url-1:", url)
        modificado = requests.get(url)
        print(len(modificado.content))
        word     = open("D:/gestor_2021_vite/temporal/salida.docx" , "wb")
        word.write(modificado.content)
        word.close()

    return { "error": 0 }

print("CARGA ONLY OFFICE,,,,")