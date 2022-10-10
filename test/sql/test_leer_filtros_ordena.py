#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from librerias.datos.sql  import sqalchemy_operaciones 

resultado = sqalchemy_operaciones.leer_todos("base", "radicado_pqr", True)

print("")
print("")
print("resultado:", len(resultado))
#pprint.pprint(resultado)
