#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#####################################
# Configuraci�n inicial del sistema #
#####################################
from aplicacion.inicio   import configuracion 
configuracion.configuracion_general("base")

# Librerias de servicios
from aplicacion.servicios import *

# Importaci�n de librerias necesarias para el sistema
from aplicacion.inicio import carga_librerias

# Importaci�n de librerias necesarias para el sistema
from aplicacion.inicio import datosSql