#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from librerias.datos.base  import globales
from librerias.datos.minio import minio_acciones

minio_acciones.leer_objeto_archivo("datos.prueba", "e-2021-2737470.pdf", "e:/ARCHIVO_leido.pdf")