#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins, io

import configuracion_base

from librerias.datos.base  import globales
from librerias.datos.minio import minio_acciones


buffer = io.BytesIO()
minio_acciones.leer_objeto_buffer("datos.prueba", "e-2021-2737470.pdf", buffer)

with open("d:\salida.pdf", "wb") as f:
    f.write(buffer.getbuffer())
