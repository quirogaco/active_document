#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, sys
import os, builtins

sys.path.append('D:\gestor_2021_vite')

#########################
# Configuracion general #
#########################
# Argumentos
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-host',     type=str, default="0.0.0.0", help='ip direccion del servidor web')
parser.add_argument('-port',     type=int, default=9000,      help='puerto del servidor web')
parser.add_argument('-services', type=str, default="0.0.0.0", help='ip de los servicio del sistema')
parser.add_argument('-celery',   type=str, default="NO",      help='Si carga tareas celery workers')
parser.add_argument('-nodo',     type=str, default="001",     help='Nodo de ejecuciï¿œn')
argumentos            = parser.parse_args()
builtins._appAnfitrion = argumentos.host
builtins._appPuerto    = argumentos.port
builtins._appServicios = argumentos.services
builtins._celeryRun    = argumentos.celery
builtins._nodo         = argumentos.nodo


###########################################
# Configuración ruta global importaciones #
###########################################
import rutaGlobal

rutaGlobal.publicaRutas(builtins._appServicios)

#####################################
# Configuración inicial del sistema #
#####################################
from aplicacion.inicio   import configuracion 

configuracion.configuracion_general("base")

# Librerias de servicios
from aplicacion.servicios import *

# Importación de librerias necesarias para el sistema
print("-----------------------")
from aplicacion.inicio import carga_librerias

# Define servidor, PERO NO LO SUBE
from librerias.web.fastapi  import servidor 
servidor.servidor(titulo="Servidor SGDEA")


# Librerias de enlaces basicos GET, POST, etc
from aplicacion.servidor import *
