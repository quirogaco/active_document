#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################
# ConfiguraciÓn inicial del sistema #
#####################################
from aplicacion.inicio  import configuracion 
configuracion.configuracion_general("base")

# Librerias de servicios
from aplicacion.servicios import *

# ImportaciÓn de librerias necesarias para el sistema
from aplicacion.inicio import carga_librerias

# ImportaciÓn de librerias necesarias para el sistema
from aplicacion.inicio import datosSql