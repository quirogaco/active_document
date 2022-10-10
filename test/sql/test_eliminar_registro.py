#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from librerias.utilidades import basicas  
from librerias.flujos     import flujos_eliminar_sql

datos = {
    "id": "d4728317-7adb-11eb-aa27-006073b60f8a"
}
resultado = flujos_eliminar_sql.ejecutar("base", "continente", datos)

print("")
print("")
print("resultado:")
pprint.pprint(resultado)
