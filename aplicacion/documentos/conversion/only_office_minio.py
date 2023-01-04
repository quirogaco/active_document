#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import builtins, os, pprint, tempfile

from librerias.datos.sql import sqalchemy_leer
from fastapi.responses   import ORJSONResponse
from fastapi             import Request
import requests

from librerias.datos.minio    import minio_acciones
from librerias.datos.archivos import leer_archivo
from librerias.utilidades     import basicas  

@_app.get( '/entregar_archivo_minio/{archivo}')
async def entregar_archivo_minio(archivo:str):
    archivo_id = archivo.split("___")[0]
    
    return leer_archivo.descarga_archivo_minio("", "", "", archivo_id)

@_app.post( '/salvar_archivo_minio', response_class=ORJSONResponse )
async def salvar_archivo_minio( request: Request ):
    parametros    = await request.json()
    forcesavetype = parametros.get('forcesavetype', -1)
    status        = parametros.get('status', -1)
    url           = parametros.get('url', "")
    if ( (forcesavetype in [0, 1, 2]) and (status in [1, 2, 6]) ) or (status == 2): 
        archivo_id = parametros['key'].split("___")[0]   
        archivo    = sqalchemy_leer.leer_un_registro("archivos_anexos", archivo_id)          
        url = parametros['url']
        pos = url.find('/cache') 
        url = (
            #builtins._appServiciosType + "://" + 
            "http://" + # si se envia https molesta..
            str(builtins._appServicios) + ":80" + url[pos:]
        ) 
        print("")  
        print("")  
        print("")  
        print("...........................")  
        print("URL>>>>>>>:", url)
        print("")  
        print("")  
        print("")  
        print("...........................")          
        modificado = requests.get(
            url,
            verify=False
        )
        nombre_archivo = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + "." + archivo['tipo_archivo']
        word = open(nombre_archivo , "wb")
        word.write(modificado.content)
        word.close()
        minio_acciones.cargar_objeto(archivo['cubeta'], archivo['nombre'], nombre_archivo)
        
    return { "error": 0 }