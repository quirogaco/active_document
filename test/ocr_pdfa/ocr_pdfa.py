#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys

sys.path.append('D:\gestor_2021_vite')

from librerias.documentos.plantillas import word_plantilla
from librerias.documentos.conversion import conversion

datos = {
    'titulo'         : 'Señor su majesta',
    'nombre_completo': 'Juan Carlos Rodríguez Ospina',
    'cargo'          : 'Ingenierisimo',
    '_img_imagen1'   : {
        'ruta' : 'D:/gestor_2021_vite/test/wordplantillas/imagen1.png',
        #'alto' : 50,
        #'ancho': 120
    },
    '_img_imagen2'   : {
        'ruta' : 'D:/gestor_2021_vite/test/wordplantillas/Imagen2.jpg',
        #'alto' : 100,
        #'ancho': 100
    },
    '_img_imagen3'   : {
        'ruta' : 'D:/gestor_2021_vite/test/wordplantillas/imagen3.png',
        'alto' : 15,
        'ancho': 100
    },
}

word_plantilla.mezcla_plantilla_archivos("D:/gestor_2021_vite/test/wordplantillas/entrada.docx", "D:/gestor_2021_vite/test/wordplantillas/salida.docx", datos=datos)


from fastapi.responses import ORJSONResponse
from fastapi.responses import FileResponse
from fastapi import FastAPI
import uvicorn

ip     = "192.168.0.19"
puerto = 999

app = FastAPI()

@app.get("/")
def convertir():
    ini = datetime.datetime.now()
    url = "http://" + ip + ":" + str(puerto) + '/entregar_archivo/' + "archivo_word_a_convertir.docx"    
    parametros = {
        "filetype"  : "docx",
        "title"     : "convertido",
        "url"       : url
    }
    print("")
    print("")
    print("url:", url)
    print("")
    print("")
        
    #contenido  = conversion.a_pdf("172.30.41.179", "80", parametros)
    contenido  = conversion.a_pdfa("172.30.41.179", "80", parametros)
    sale = open("D:/gestor_2021_vite/test/ocr_pdfa/salida1.pdf", "wb")
    sale.write(contenido)
    sale.close()
    #ocr_pdfa.pdf_ocr_pdfa( "172.24.153.161", "5000", "D:/OrientDB.pdf", "D:/gestor_2021/test/ocr_pdfa/sale_pdfa.pdf" )

    print("termina:", datetime.datetime.now()-ini)
    print("")
    print("")

    return {"Hello": "World"}

@app.get( '/entregar_archivo/{archivo}', response_class=ORJSONResponse )
async def entregar_archivo( archivo: str ):
    print("")
    print("")
    print("entregar_archivo -> archivo_id:", archivo)
    nombre_archivo = "D:/gestor_2021_vite/test/ocr_pdfa/salida1.docx"

    print("entrega:", nombre_archivo)
    print("")
    print("")
    # Esto debe corregirse el media_type
    return FileResponse( nombre_archivo, media_type='application/pdf', filename=nombre_archivo )

uvicorn.run(app, host=ip, port=puerto)