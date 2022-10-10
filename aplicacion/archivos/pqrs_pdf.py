#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from pathlib import Path

from librerias.datos.sql      import sqalchemy_leer
from librerias.flujos         import flujos_leer_sql
from librerias.datos.archivos import leer_archivo

def pdf_pqrs(operacion, clase, descarga, encabezados, parametros, pdf_id, id_tarea):
      """
      datos = {
            "id": pdf_id
      }
      registro       = flujos_leer_sql.ejecutar("base", "archivo_historico_migrado", datos)
      """
      radicado_id, fecha, archivo_id = pdf_id.split('_')
      archivo_nombre =  '/mnt/repositorioCacIG/adjuntos/' + fecha[0:4] + "/" + radicado_id + "/" + archivo_id
      print("RUTA:", archivo_nombre)
      registro       = sqalchemy_leer.leer_un_registro("anexo_pqr", pdf_id)  
      print("registro:", registro)
      #registro        = resultado["datos"]["resultados"]["datos"]
      #archivo_nombre  = registro['archivo_pdf']
      ruta            = Path(archivo_nombre)
      archivo         = ruta.open('rb')
      archivo_tamano  = ruta.stat().st_size

      datos           = leer_archivo.archivo_pdf_visor(encabezados, archivo, descarga, archivo_tamano) 

      return datos

# Publica función de llamado
CONFIGURACION_GENERAL["manejo_pdf"]["pqrs"] = pdf_pqrs
