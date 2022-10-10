#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random 
import builtins
import tempfile
import mimetypes, builtins, os, pprint
import uuid

from fastapi.responses import FileResponse
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from PIL import Image
from PIL import ImageDraw

from librerias.datos.sql import sqalchemy_leer

#@_app.get( '/crear_codigo_barras/{texto}')
#async def codigo_barras( texto: str ):
  
def _paint_text(self, xpos, ypos):
    pass

def _init(self, code):
    size = (450, 150)
    self._image = Image.new(self.mode, size, self.background)
    self._draw = ImageDraw.Draw(self._image)


#ImageWriter._paint_text = _paint_text
ImageWriter._init = _init
directorio_temporal = tempfile.gettempdir() + os.path.sep

@_app.get( '/codigo_barras/{texto}')
async def codigo_barras(texto:str):
    nombre_unico = directorio_temporal + str(uuid.uuid4())
    code128 = barcode.get_barcode_class('code128')
    writer = ImageWriter()
    my_ean = code128(texto, writer=writer)
    nombre_archivo = my_ean.save(nombre_unico)
    fp = BytesIO()
    my_ean.write(fp)
    media_type = mimetypes.MimeTypes().guess_type(nombre_archivo)[0]
    
    return FileResponse( 
        nombre_archivo, 
        media_type=media_type, 
        filename=nombre_archivo 
    )


@_app.get( '/logo_entidad')
async def logo_entidad():
    ruta = builtins.rutaBase + "aplicacion/especificos/radicados/labels/"
    nombre_archivo = ruta + "logo.png"    
    media_type = mimetypes.MimeTypes().guess_type(nombre_archivo)[0]
    
    return FileResponse( 
        nombre_archivo, 
        media_type=media_type, 
        filename=nombre_archivo 
    )


def label_entrada(accion, datos, archivos, id_tarea):
    pass

def label_salida(accion, datos, archivos, id_tarea):
    pass

def label_interno(accion, datos, archivos, id_tarea):
    pass

acciones_funcion = {    
    # ENTRADAS
    "label__salida" : label_salida,

    # SALIDAS
    "label__salida" : label_salida,

    # INTERNOS
    "label_interno": label_interno,
}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]

    # print("")
    # print("")
    # print("------------------------------------------------")
    # print('/ESPECIFICOS LABELS -> acciones_ejecuta:', id_tarea) 
    # print('datos:')
    # pprint.pprint(datos)   
    # print('archivos:', archivos)
    
    resultado = datos
    funcion   = acciones_funcion[accion]
    resultado = funcion(accion, datos, archivos, id_tarea)
    #print("------------------------------------------------")
    #print("")
    #print("")

    retorna = datos
    retorna["datos"] = resultado

    return retorna