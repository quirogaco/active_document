#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import builtins, sys, pprint

import argumentos
import finaliza

######################
# Crea servidor WEB #
######################
import servidor_web
# Debe crearse primero para _app, este disponible
_app = servidor_web._app

###########################################
# Configuración ruta global importaciones #
###########################################
import rutaGlobal
rutaGlobal.publicaRutas(builtins._appServicios)

import carga_inicial
from aplicacion.inicio import carga_servicios

# Librerias de enlaces basicos GET, POST, etc
from aplicacion.servidor import *