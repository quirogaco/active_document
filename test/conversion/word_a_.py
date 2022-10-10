#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime

from parent_import import parentdir
word_plantilla = parentdir.parentdir.librerias.plantillas.word.word_plantilla


datos = {
    "datos": {
        'titulo'         : 'Señor su majesta',
        'nombre_completo': 'Juan Carlos Rodríguez Ospina',
        'cargo'          : 'Ingeniersimo',
        '_img_imagen1'   : {
            'ruta' : 'D:/gestor_2021/test/wordplantillas/imagen1.png',
            #'alto' : 50,
            #'ancho': 120
        },
        '_img_imagen2'   : {
            'ruta' : 'D:/gestor_2021/test/wordplantillas/Imagen2.jpg',
            #'alto' : 100,
            #'ancho': 100
        },
        '_img_imagen3'   : {
            'ruta' : 'D:/gestor_2021/test/wordplantillas/imagen3.png',
            'alto' : 15,
            'ancho': 100
        },
    }
}
word_plantilla.mezcla_plantilla_archivos("D:/gestor_2021/test/wordplantillas/entrada.docx", "D:/gestor_2021/test/wordplantillas/salida.docx", datos=datos)

only_office = parentdir.parentdir.librerias.conversion.only_office

print("only_office:", only_office)

from fastapi.responses import ORJSONResponse
from fastapi.responses import FileResponse
from fastapi import FastAPI
import uvicorn

ip     = "192.168.0.13"
puerto = 999

app = FastAPI()

@app.get("/")
def convertir():
    ini = datetime.datetime.now()
    url = "http://" + ip + ":" + str(puerto) + '/entregar_archivo/' + "archivo_word_a_convertir.docx"
    parametros = {
        "async"     : False,
        "filetype"  : "docx",
        "key"       : "22244",
        #"outputtype": "pdf",
        #"outputtype": "jpg",
        #"outputtype": "png",
        "outputtype": "pdfa",        
        "title"     : "convertido",
        "url"       : url
    }

    contenido = only_office.convertir_archivos("172.24.153.161", "80", parametros)

    #sale = open("D:/gestor_2021/test/conversion/sale.pdf", "wb")
    #sale = open("D:/gestor_2021/test/conversion/sale.jpg", "wb")
    sale = open("D:/gestor_2021/test/conversion/sale_a.pdf", "wb")
    sale.write(contenido)
    sale.close()

    print("termina:", datetime.datetime.now()-ini)
    return {"Hello": "World"}

@app.get( '/entregar_archivo/{archivo}', response_class=ORJSONResponse )
async def entregar_archivo( archivo: str ):
    print("archivo_id:", archivo)
    nombre_archivo = "D:/gestor_2021/test/wordplantillas/salida.docx"

    print("entrega:", nombre_archivo)

    # Esto debe corregirse el media_type
    return FileResponse( nombre_archivo, media_type='application/pdf', filename=nombre_archivo )

uvicorn.run(app, host=ip, port=puerto)