#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys

sys.path.append('D:\gestor_2021_vite')

from librerias.documentos.plantillas import word_plantilla
from librerias.documentos.conversion import conversion
from librerias.email                 import email

from fastapi.responses import FileResponse
from fastapi import FastAPI
import uvicorn

ip     = "192.168.0.6"
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
        
    ruta_destino  = conversion.a_pdfa("172.30.220.142", "80", parametros)
    html          = conversion.a_html_contenido("172.30.220.142", "80", parametros)
    

    print("")
    print("---------------------------------------------------")
    print("termina:", datetime.datetime.now()-ini)
    print("---------------------------------------------------")
    print("")

    de        = "quirogaco@gmail.com"
    clave     = "sreojrjewsjkxnml"
    para      = "quirogaco@gmail.com,fabigonz@esap.edu.co,viveros.60@gmail.com"
    para      = "quirogaco@gmail.com"
    asunto    = "Notificación de radicado [E-2021-474755]" 
    contenido = "Señor x"
    contenido = html
    print(contenido)
    archivos  = [ruta_destino]

    direccion_smtp = "smtp.gmail.com"
    puerto_smtp    = 587

    #mensaje = email.mensaje_texto(
    mensaje = email.mensaje_html(
        de, 
        para, 
        asunto, 
        contenido, 
        archivos=archivos
    )

    email.enviar_mensaje_smtp(
        mensaje, 
        de, 
        clave, 
        para, 
        direccion_smtp, 
        puerto_smtp
    )

    return {"ruta_destino": ruta_destino}

datos = {
    'titulo'         : 'Señor',
    'nombre_completo': 'Juan Carlos Rodríguez Ospina',
    'cargo'          : 'Ingeniero',
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

@app.get( '/entregar_archivo/{archivo}')
async def entregar_archivo( archivo: str ):
    global datos

    nombre_archivo = word_plantilla.mezcla_plantilla_archivos("D:/gestor_2021_vite/test/notificacion/entrada.docx", None, datos=datos)
    print("entregar_archivo:", nombre_archivo)

    return FileResponse( nombre_archivo, media_type='application/pdf', filename=nombre_archivo )

uvicorn.run(app, host=ip, port=puerto)