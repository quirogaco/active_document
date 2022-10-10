#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, pathlib, pprint

from PyPDF2 import PdfFileReader

from librerias.datos.sql   import sqalchemy_filtrar 

###################################
# Crea un archivo Minio           #
# Crea registro en la:            #
###################################
def indexa_archivos(estructura, registro_id, cardinalidad=""):   
   # Relaciones de archivos a estructura
   ordenar     = [ [ "descendente", "creado_en_" ] ]
   filtros     = [ [ "origen", "=", estructura ], [ "origen_id", "=", registro_id ] ]
   relaciones  = sqalchemy_filtrar.filtrarOrdena(estructura="archivos_relacion", filtros=filtros, ordenamientos=ordenar)
   archivos_id = [ relacion["archivo_id"] for relacion in relaciones ] 

   # Información de archivos
   ordenar     = [ [ "descendente", "creado_en_" ] ]
   filtros     = [ [ "id", "in", archivos_id ] ]
   archivos    = sqalchemy_filtrar.filtrarOrdena(estructura="archivos_electronicos", filtros=filtros, ordenamientos=ordenar)
   
   # Datos de indexamiento por archivo
   datos_archivos = []
   for archivo in archivos:
      datos = {
         'id'               : archivo["id"],
         'actualizado_en_'  : archivo['actualizado_en_'],
         'creado_en__'      : archivo['creado_en_'],
         'base'             : archivo['base'],         
         'creado_por_id'    : archivo['creado_por_id'],
         'creado_por_nombre': archivo['creado_por_nombre'],
         'cubeta'           : archivo['cubeta'],
         'detalle'          : archivo['detalle'],
         'estado_'          : archivo['estado_'],
         'folios'           : archivo['folios'],
         'nombre'           : archivo['nombre'],
         'pdf_a'            : archivo['pdf_a'],
         'ruta'             : archivo['ruta'],
         'tamano'           : archivo['tamano'],
         'texto_extraido'   : archivo['texto_extraido'],
         'tipo_archivo'     : archivo['tipo_archivo']
      }
      datos_archivos.append(datos)

   return datos_archivos