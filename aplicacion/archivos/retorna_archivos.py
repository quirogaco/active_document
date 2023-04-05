#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from datetime import datetime

from librerias.datos.base    import globales
from librerias.datos.elastic import elastic_busquedas


# Ejecuta la consulta sobre ELASTIC, los datos viene en texto.
def ejecutar(estructura, parametros):
   definicion = globales.lee_definicion(estructura);
   resultado  = elastic_busquedas.ejecutar(estructura, parametros, definicion)

   return resultado