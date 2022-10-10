#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import builtins, pprint

######################
# Crea servidor WEB #
######################
from librerias.web.fastapi  import servidor 
# Debe crearse primero para _app, este disponible
#_app = servidor.servidor(titulo="Servidor SGDEA", debug=False)
_app = servidor.servidor(titulo="Servidor SGDEA", debug=True)

@_app.on_event("startup")
async def startup_event():
    #print("INICIO WEB")
    pass

@_app.on_event("shutdown")
def shutdown_event():
    #print("FINALIZA WEB")
    pass

from fastapi           import Request
from fastapi.responses import JSONResponse

from librerias.utilidades import errores

#"""
@_app.middleware("http")
async def error_global(request: Request, call_next):
    try:
        respuesta = await call_next(request)
        
    except Exception as e:
        print("-------------------")
        print("EXCPEPTION:", str(e))
        print("-------------------")
        
        texto_error, ruta_error = errores.busca_error()


        print("")
        print("")    
        print("******** ERROR GLOBAL ******************")
        print(ruta_error)
        print(texto_error)
        print("****************************************")
        print("")
        print("")
    
        respuesta = JSONResponse(
            status_code = 500,
            headers     = {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Methods": "POST, PUT, GET, OPTIONS, DELETE",
                "Access-Control-Max-Age"      : "86400"
            },
            content     = {
                "error": ruta_error
            }
        )
        
        print("++++++++++++++++++++++++++++++++++")
    
    return respuesta
    #"""