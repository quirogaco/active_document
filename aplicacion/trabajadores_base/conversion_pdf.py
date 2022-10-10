#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, builtins, datetime

from librerias.datos.base  import globales

from . import crea_celery_app

generales_app = crea_celery_app.aplicacion_celery('conversion_pdf', 'conversion_pdf')

# Convierte archivos pdf a Pdf/a y Ocr
from aplicacion.documentos.conversion import tarea_convertir
@generales_app.task(name='conversion_pdf')
def conversion_pdf_a_pdfa_ocr(**parametros):
    print("")
    print("")
    print("------------------------------------------")
    print("CONVERTIR ARCHIVOS PDF (OCR, PDF/A) Y EXTRAER TEXTO >>>> ... ", datetime.datetime.now())
    tarea_convertir.valida_sin_ocr_pfda()
