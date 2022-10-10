#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from box import Box

# Conexión
datos = Box(default_box=True)
datos.sqlnombre = 'oracle'
datos.direccion = 'XE'
datos.nombre    = ''
datos.usuario   = 'GESTOR_360'
datos.clave     = '12345678'