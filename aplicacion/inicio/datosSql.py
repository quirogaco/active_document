#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import builtins, pprint

#from librerias.datos.base    import globales 
from librerias.datos.sql import sqalchemy_operaciones

sqalchemy_operaciones.creaTablas("base")