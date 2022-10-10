#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from librerias.datos.sql import sqalchemy_leer

registro_id = "94cbf492-d2ef-11eb-a4dd-acfdce646f0d"
resultado   = sqalchemy_leer.leer_un_registro("radicados_entrada", registro_id)

print("")
print("")
print("resultado:")
pprint.pprint(resultado)
