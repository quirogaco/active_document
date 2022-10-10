#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.base import globales 

def creaUnaTabla(ruta, CLASE):
    motor = globales.lee_motor_sql(ruta)
    globales.CLASE_BASE_SQL.metadata.create_all(motor, [CLASE.__table__]) 

def creaTablas(ruta):
    motor = globales.lee_motor_sql(ruta)
    globales.CLASE_BASE_SQL.metadata.create_all(motor)

# Leer datos
from .sqalchemy_leer import *

# Insertar datos
from .sqalchemy_insertar import *

# Modificar datos
from .sqalchemy_modificar import *

# Borrar datos
from .sqalchemy_borrar import *

# Borrar datos
from .sqalchemy_filtrar import *

