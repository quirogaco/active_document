#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales

#########################
# ARCHIVO CONFIGURACION #
#########################

permisos_archivo = {
   "definicion": {
      "id"    : "144",
      "nombre": "CONFIGURACI�N - ARCHIVO - Permisos archivo"
   },

   "grid": {
      "clase"     : "grid",
      "componente": "permisos_archivo_grid",     
      "texto"     : "Permisos archivo",
      "icon"      : "",
      "navegar"   : "si",
      "padre"     : "Configuraci�n - ARCHIVO",
      "tipo"      : "importar",
   },

   "forma": {
      "componente": "permisos_archivo_formulario",     
      "texto"     : "Permisos archivo",
      "tipo"      : "importar",
   }
}


opciones = [
   # Permisos archivo
   permisos_archivo
]