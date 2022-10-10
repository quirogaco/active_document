#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import builtins, pprint

from fastapi                 import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles     import StaticFiles
import uvicorn

# Manejo de CORS
origins = [
    "*"
]

# Aplicación de servidor web
def servidor(titulo="Servidor SGDEA", debug=False):
    print("....................")
    servidorWeb = FastAPI(
        debug = debug, 
        title = titulo,
        reload= True
    )

    servidorWeb.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    builtins._app = servidorWeb

    return servidorWeb

"""
# Archivos estaticos
def archivos_estaticos(servidor, rutas):
    for ruta in rutas:
        servidor.mount(ruta['ruta'], StaticFiles(directory=ruta['directorio']), name=ruta['nombre'])

# Ejecuta servidor web
def ejecutaServidor(servidor, host='localhost', puerto=80, trabajadores=1, nivel_log="debug"):   
    uvicorn.run(servidor, host=host, port=puerto, workers=trabajadores, log_level=nivel_log)

from pathlib import Path

# Subir servidor web
def subirServidor(servidorWeb, host='localhost', puerto=80, trabajadores=1, nivel_log="debug", titulo="Servidor SGDEA", debug=False):   
    print("subirServidor:", servidorWeb, host, puerto)

    uvicorn.run(_app, host=host, port=puerto, workers=trabajadores, log_level=nivel_log)
"""