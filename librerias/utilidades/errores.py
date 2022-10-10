#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, sys, traceback

traceback_template = '''Traceback (most recent call last):
   File "%(filename)s", line %(lineno)s, in %(name)s
   %(type)s: %(message)s\n'''

def busca_error():
   exc_type, exc_value, exc_traceback = sys.exc_info()
   
   
   traceback_details = {
      'filename': exc_traceback.tb_frame.f_code.co_filename,
      'lineno'  : exc_traceback.tb_lineno,
      'name'    : exc_traceback.tb_frame.f_code.co_name,
      'type'    : exc_type.__name__,
      'message' : str(exc_value), # or see traceback._some_str()
   }
   del(exc_type, exc_value, exc_traceback) 

   ruta_error  = traceback.format_exc()
   texto_error = traceback_template % traceback_details 

   return texto_error, ruta_error

def mostrar_errores():
   texto_error, ruta_error = busca_error()
   print(ruta_error)
   print(texto_error)

   raise ValueError([ruta_error])