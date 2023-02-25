#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, pprint, builtins

#########################
# Variables de ambiente #
#########################
from dotenv import dotenv_values

try:
    _ambiente_ = dotenv_values(".env") 
except:
    pass

if len(_ambiente_.keys()) == 0:    
    _ambiente_ = dotenv_values("../../.env") 
    
builtins._appServicios = _ambiente_['CFG_SERVICIOS_URL']
builtins._appAnfitrion = _ambiente_['CFG_DATA_HOST']
builtins._appPuerto    = _ambiente_['CFG_DATA_PORT']

import rutaGlobal
rutaGlobal.publicaRutas(builtins._appServicios)

import carga_inicial