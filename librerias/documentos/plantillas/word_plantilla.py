#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, os

import  tempfile, copy

from docxtpl     import DocxTemplate, RichText, InlineImage
from docx.shared import Mm, Inches, Pt

from librerias.utilidades import basicas  

def mezcla_plantilla_archivos(ruta_origen, ruta_destino, datos={}, ancho=60, alto=15): 
    datos_mezcla = copy.deepcopy(datos)  
    # Archivo word destino"
    if ruta_destino == None:
        directorio   = tempfile.gettempdir()
        ruta_destino = directorio + os.sep + basicas.uuidTexto() + ".docx"
    print("mezcla_plantilla_archivos:", ruta_origen)
    plantilla = DocxTemplate( ruta_origen )
    # Imagenes
    for nombre, atributo in datos_mezcla.items():     
        if isinstance(atributo, dict):            
            ruta          = atributo.get("ruta")
            ancho_        = atributo.get("ancho", ancho)
            alto_         = atributo.get("alto", alto)            
            imagenInterna = InlineImage( plantilla, ruta, width=Mm(ancho_), height=Mm(alto_) )    
            datos_mezcla[nombre] = imagenInterna

    parametros = {
        "datos": datos_mezcla
    } 
    try:
        plantilla.render( parametros )
        plantilla.save( ruta_destino )
    except Exception as e:
            print( "error mezclando archivos plantilla ", ruta_destino, str( e ) )
    
    return ruta_destino