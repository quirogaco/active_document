#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import builtins, pprint

#########################
# Variables de ambiente #
#########################
from dotenv import dotenv_values

_ambiente_ = dotenv_values(".env") 

#########################
# Configuracion general #
#########################
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('servidor:_app',  type=str, default="",        help='Servidor aplicación')
parser.add_argument('--host',         type=str, default="0.0.0.0", help='ip direccion del servidor web')
parser.add_argument('--port',         type=int, default=9000,      help='puerto del servidor web')
parser.add_argument('--workers',      type=int, default=1,         help='trabajadores')
parser.add_argument('--env-file',     type=str, default=".env",    help='archivo configuración')
parser.add_argument('--reload',       action='store_true')
parser.add_argument('--log-level')
parser.add_argument('--loop asyncio')
parser.add_argument('--ssl-keyfile')
parser.add_argument('--ssl-certfile')

argumentos              = parser.parse_args()
builtins._appAnfitrion  = argumentos.host
builtins._appPuerto     = argumentos.port
builtins._appServicios  = _ambiente_['CFG_SERVICIOS_URL']
#builtins._segundoPuerto = 9000
builtins._segundoPuerto = argumentos.port

