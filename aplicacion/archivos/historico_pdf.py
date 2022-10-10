#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from pathlib import Path

from librerias.flujos         import flujos_leer_sql
from librerias.datos.archivos import leer_archivo

def pdf_historico(operacion, clase, descarga, encabezados, parametros, pdf_id, id_tarea):
   datos = {
      "id": pdf_id
   }
   resultado       = flujos_leer_sql.ejecutar("base", "archivo_historico_migrado", datos)
   registro        = resultado["datos"]["resultados"]["datos"]
   archivo_nombre  = registro['archivo_pdf']
   ruta            = Path(archivo_nombre)  
   print("")
   print("")
   print("*********************pdf_historico*******************************:", archivo_nombre)
   print("")
   print("")
   if descarga == "no":
      archivo         = ruta.open('rb')
      archivo_tamano  = ruta.stat().st_size
      datos = leer_archivo.archivo_pdf_visor(encabezados, archivo, descarga, archivo_tamano) 
   else:
      datos = leer_archivo.descarga_archivo(ruta)
   
   return datos

# Publica función de llamado
CONFIGURACION_GENERAL["manejo_pdf"]["historico"] = pdf_historico
