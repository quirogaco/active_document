#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from aplicacion.archivos   import archivo_operaciones

registro = archivo_operaciones.crear_registro_relacion("radicado_web_juridica", "jur-09939", "arc-95959")

print("reshgitro:", registro)