#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from box import Box

# Conexión
datos = Box(default_box=True)
datos.ip        = '172.24.164.97'
datos.port      = '9200'
datos.timeout   = 2400
