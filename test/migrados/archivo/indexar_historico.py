#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import configuracion_base

from librerias.datos.elastic import elastic_operaciones
from librerias.datos.sql     import sqalchemy_operaciones 
from librerias.datos.base    import globales

conexion  = globales.lee_conexion_elastic("base")
modelo    = globales.lee_modelo_elastic("archivo_historico_migrado")
pprint.pprint(  list(modelo["modelo"].keys())  )

print("ELASTIC:", conexion ) #, modelo)

# Query
#resultado = sqalchemy_operaciones.leer_todos("base", "archivo_historico_migrado", False, "objeto")
#"""

desde = 50000
for limite in range(55000, 222000, 500):
    print(desde, limite)
    resultado = sqalchemy_operaciones.leer_todos("base", "archivo_historico_migrado", desde=desde, hasta=limite)
    print("inicia>>>>>>>>>>>>>>>", len(resultado))
    bulk  = elastic_operaciones.bulk_indexar(conexion, modelo["modelo"], modelo["indice"], resultado)
    desde = limite

print(len(resultado))
#"""