#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

import configuracion_base

from librerias.datos.base  import globales
from librerias.datos.minio import minio_acciones

atributos = minio_acciones.atributos_objeto("datos.prueba", "e-2021-2737470.pdf")
