#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from librerias.flujos     import flujos_leer_sql

datos = {
    "id": "8a2cf5de-7add-11eb-80a9-006073b60f8a"
}
resultado = flujos_leer_sql.ejecutar("base", "continente", datos)

print("")
print("")
print("resultado:")
pprint.pprint(resultado)
