#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
import os
import tempfile
import base64
import builtins

from librerias.documentos.plantillas import word_plantilla
from librerias.documentos.conversion import conversion
from librerias.datos.sql import sqalchemy_filtrar 
from librerias.datos.archivos import leer_archivo
from librerias.utilidades import basicas  

def genera_pdf_plantilla(
    plantilla_base, 
    archivo_destino="", 
    datos={}, 
    imagen=True
):
    if archivo_destino == "":
        archivo_destino = (
            tempfile.gettempdir() + 
            os.sep + basicas.uuidTexto() + ".docx"
        )
    
    nombre_archivo  = word_plantilla.mezcla_plantilla_archivos(
        plantilla_base, 
        archivo_destino, 
        datos
    )  
    nombre_byte = nombre_archivo.encode('ascii')
    nombre_64 = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')
    url = (
        builtins._appServiciosType + "://" + 
        str(builtins._appAnfitrion) + ":" + 
        str(builtins._appPuerto) + '/entregar_archivo_base64/' + 
        nombre_64_texto
    )
    parametros = {
        "filetype"  : "docx",
        "title"     : "convertido",
        "url"       : url
    }
            
    ruta_destino  = conversion.a_pdfa(
        str(builtins._appServicios), 
        str(builtins._appServiciosPuerto), 
        parametros=parametros, 
        servicio=str(builtins._appServiciosType)
    )  
    jpg_ruta      = ""
    if (imagen == True):  
        jpg_ruta = conversion.a_jpg(str(builtins._appServicios), 
        str(builtins._appServiciosPuerto), 
        parametros=parametros, 
        servicio=str(builtins._appServiciosType)
    )   

    return ruta_destino, jpg_ruta      

############
# ENTRADAS #
############
def recuperar_archivo_plantilla(plantilla):
    nombre_archivo = ""
    # Recupera registro de la plantilla
    ordenar    = [ [ "descendente", "creado_en_" ] ]
    filtros    = [ [ "id", "=", plantilla ] ]
    plantillas = sqalchemy_filtrar.filtrarOrdena(
        estructura="plantillas", 
        filtros=filtros, 
        ordenamientos=ordenar
    )
    # Si existen plantillas 
    if len(plantillas) > 0:
        # Recupera registro de relación a archivos
        plantilla_id = plantillas[0]["id"]            
        filtros      = [ 
            [ "origen", "=", "plantillas" ], 
            [ "origen_id", "=", plantilla_id ] 
        ]
        relaciones   = sqalchemy_filtrar.filtrarOrdena(
            estructura="archivos_relacion", 
            filtros=filtros, 
            ordenamientos=ordenar
        )        
        # Si existen relaciones 
        if len(relaciones) > 0:
            archivo_id     = relaciones[0]['archivo_id']    
            # Recupera archivo de minio
            nombre_archivo = leer_archivo.salva_archivo_minio(archivo_id)

    return nombre_archivo

def crear_pdf_plantilla(plantilla, datos, id_tarea):
    nombre_archivo  = recuperar_archivo_plantilla(plantilla)    
    ruta_destino, jpg_ruta = genera_pdf_plantilla(nombre_archivo, "", datos)

    return ruta_destino, jpg_ruta  

def crear_pdf_archivo(archivo_id, datos, id_tarea):
    nombre_archivo         = leer_archivo.salva_archivo_minio(archivo_id)    
    ruta_destino, jpg_ruta = genera_pdf_plantilla(nombre_archivo, "", datos)

    return ruta_destino, jpg_ruta 

###########
# SALIDAS #
###########
def recuperar_archivo_borrador(borrador_id):
    nombre_archivo = ""
    # Recupera registro borrador
    ordenar    = [ [ "descendente", "creado_en_" ] ]
    filtros    = [ 
        [ "tipo_relacion", "=", "borrador" ], 
        [ "origen", "=", "peticiones" ], 
        [ "archivo_id", "=", borrador_id ] 
    ]
    relaciones = sqalchemy_filtrar.filtrarOrdena(
        estructura="archivos_relacion", 
        filtros=filtros, 
        ordenamientos=ordenar
    )        
    # Si existen relaciones 
    if len(relaciones) > 0:
        archivo_id     = relaciones[0]['archivo_id']    
        # Recupera archivo de minio
        nombre_archivo = leer_archivo.salva_archivo_minio(archivo_id) 

    return nombre_archivo

def crear_pdf_borrador(borrador_id, datos, id_tarea):
    nombre_archivo         = recuperar_archivo_borrador(borrador_id)
    ruta_destino, jpg_ruta = genera_pdf_plantilla(nombre_archivo, "", datos)

    return ruta_destino, jpg_ruta  