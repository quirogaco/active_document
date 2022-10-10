#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from aplicacion.archivos   import archivo_operaciones

# registro = archivo_operaciones.crear_archivo("d:/FP0000000004.pdf", "e-2021-82.pdf", "datos.test")
registro   = archivo_operaciones.leer_archivo("datos.prueba", "e-2021-81.pdf", "e:/leido_archivo.pdf")

print("registro:", registro)