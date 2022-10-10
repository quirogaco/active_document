#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint,sys

sys.path.append('D:\gestor_2021_vite')

from librerias.documentos.plantillas import word_plantilla

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

word_plantilla.mezcla_plantilla_archivos("D:/gestor_2021_vite/test/wordplantillas/entrada.docx", "D:/gestor_2021_vite/test/wordplantillas/salida.docx", datos=datos)

