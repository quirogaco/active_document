#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from pathlib import Path

from librerias.flujos         import flujos_leer_sql
from librerias.datos.archivos import leer_archivo
from librerias.datos.sql      import sqalchemy_filtrar
from aplicacion.comunes       import manejo_archivos

def radicado_pdf(operacion, clase, descarga, encabezados, parametros, pdf_radicado, id_tarea):
   datos          = ""
   nombre_archivo = ""
   tipo_radicado, nro_radicado = pdf_radicado.split("__")
   nombre_archivo = manejo_archivos.recupera_anexo_especifico_radicado(nro_radicado, tipo_radicado="ENTRADA", tipo_anexo="notificacion")         
   print("nombre_archivo:::", nombre_archivo)
   if nombre_archivo != "":
      datos = leer_archivo.descarga_archivo(nombre_archivo)
   
   return datos

# Publica función de llamado
CONFIGURACION_GENERAL["manejo_pdf"]["radicado_pdf"] = radicado_pdf