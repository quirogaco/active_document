#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from fastapi.responses        import FileResponse

from librerias.datos.base    import globales 
from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_comunes, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones
