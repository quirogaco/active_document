#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, pickle

import configuracion_base

from librerias.utilidades import basicas  
from librerias.flujos     import flujos_insertar_sql
from librerias.datos.sql  import sqalchemy_comunes
from librerias.datos.sql  import sqalchemy_insertar
from librerias.datos.base import globales 


# Carga datos
archivo = open("D:\ocr_extrae_texto\data_final.pkl", 'rb')
datos   = pickle.load(archivo)
archivo.close()

"""
BD---
    un_administrativa
    un_productora    
    serie           
    subserie        
    asunto          
    id_persona
    ano              
    fecha_inicial
    fecha_final
    carpeta
    periodo
    nombre
    apellido 
    codigo_esap
    archivo_pdf 
    archivo_ocr

DICCIONARIO--
    unidad
    oficina
    serie
    subserie
    asunto
    id
    ano
    inicial
    final
    carpeta
    periodo'
    nombre
    apellido
    codigo_esap
    archivo_pdf
    archivo_ocr
"""
def crea_registro(datos):
    registro = {
        'un_administrativa': datos.get('unidad', '').strip(),
        'un_productora'    : datos.get('oficina', '').strip(),
        'asunto'           : datos.get('asunto', '').strip(),
        'serie'            : datos.get('serie', '').strip(),
        'subserie'         : datos.get('subserie ', '').strip(),
        'asunto'           : datos.get('asunto', '').strip(),
        'id_persona'       : datos.get('id', '').strip(),
        'ano'              : datos.get('ano', '').strip(),
        'fecha_inicial'    : datos.get('inicial', '').strip(),
        'fecha_final'      : datos.get('final', '').strip(),
        'carpeta'          : datos.get('carpeta', '').strip(),
        'periodo'          : datos.get('periodo', '').strip(),
        'nombre'           : datos.get('nombre', '').strip(),
        'apellido'         : datos.get('apellido', '').strip(),
        'codigo_esap'      : datos.get('codigo_esap', '').strip(),
        'archivo_pdf'      : datos.get('pdf', '').strip(),
        'archivo_ocr'      : datos.get('ocr', '').strip(),
    }

    return registro

# Crea registros
CLASE  = globales.lee_clase("db_migrado_archivo_historico")
sesion = sqalchemy_comunes.nuevaSesion('base')
print("CLASE:", sesion, CLASE)

contador = 0
total    = 0
for dato in datos:
    contador += 1    
    total    += 1     
    registro = crea_registro(dato)
    #pprint.pprint(registro)
    sqalchemy_insertar.insertar(sesion, CLASE, registro, False)
    if contador > 20000:
        sesion.commit()
        contador = 0
        print(total) 
        #break   

sesion.commit()
sesion.close()
