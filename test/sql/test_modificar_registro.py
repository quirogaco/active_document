#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from librerias.utilidades import basicas  
from librerias.flujos     import flujos_modificar_sql

datos = {
    "id"        : "9e229045-7b66-11eb-838f-006073b60f8a",
    "codigo"    : "0000-modificado-09",
    "nombre"    : "0000->AFRICA-modificado-09",
    #"_creado_en_"    : datetime.datetime.now(),
    #"_creado_en_"     : datetime.datetime(year=2010, month=3,  day=20),
    #"_actualizado_en_": datetime.datetime(year=2011, month=2, day=1)
}
resultado = flujos_modificar_sql.ejecutar("base", "continente", datos)

print("")
print("")
print("resultado:")
pprint.pprint(resultado)
