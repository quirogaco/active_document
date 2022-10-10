#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from librerias.datos.sql         import sqalchemy_operaciones 
from librerias.datos.estructuras import estructura_operaciones

#resultado = sqalchemy_operaciones.leer_todos("base", "radicado_pqr", True)

#total = sqalchemy_operaciones.contar_registros("base", "radicado_pqr")

#estructura_operaciones.reindexaEstructura("base", "radicado_pqr")

estructura_operaciones.reindexaEstructura("base", "ubicacion")


print("")
print("")
#print("resultado:", len(resultado))
#pprint.pprint(resultado)
