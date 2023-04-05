#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from pathlib import Path

from librerias.flujos         import flujos_leer_sql
from librerias.datos.archivos import leer_archivo

def pdf_historico(operacion, clase, descarga, encabezados, parametros, pdf_id):
   datos = {
      "id": pdf_id
   }
   resultado       = flujos_leer_sql.ejecutar("base", "archivo_historico_migrado", datos)
   registro        = resultado["datos"]["resultados"]["datos"]
   archivo_nombre  = registro['archivo_pdf']
   #archivo_nombre  = 'D:/19_005.pdf'
   #archivo_nombre  = 'D:/Activiti_User_Guide.pdf'
   #archivo_nombre  = 'D:/Formulario_Persona_Juridica_Software.pdf'
   #archivo_nombre  = 'D:/B.pdf'
   ruta            = Path(archivo_nombre)
   archivo         = ruta.open('rb')
   archivo_tamano  = ruta.stat().st_size
   print("")
   print("")
   print("*********************pdf_historico*******************************:", archivo_nombre)
   print("")
   print("")
   datos           = leer_archivo.archivo(encabezados, archivo, descarga, archivo_tamano) 
  
   return datos

# Publica función de llamado
CONFIGURACION_GENERAL["manejo_pdf"]["historico"] = pdf_historico
