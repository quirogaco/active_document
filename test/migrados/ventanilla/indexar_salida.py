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
modelo    = globales.lee_modelo_elastic("salidas_ventanilla")
#pprint.pprint(  list(modelo["modelo"].keys())  )

#pprint.pprint(  list(CONFIGURACION_GENERAL["DEFINICIONES_SQL"].keys())  )

print("ELASTIC:", conexion ) #, modelo)

desde = 0
#for limite in range(0, 1400000, 500):
for limite in range(0, 140000, 2000):
    print(desde, limite)    
    resultado = sqalchemy_operaciones.leer_todos("base", "salidas_ventanilla", extendido=True, desde=desde, hasta=limite)
    #pprint.pprint(resultado)

    """
    print("")
    for r in resultado:
        print(r["id"])
        pprint.pprint(r["anexos"])
    """
    print("inicia>>>>>>>>>>>>>>>", len(resultado))
    bulk  = elastic_operaciones.bulk_indexar(conexion, modelo["modelo"], modelo["indice"], resultado)
    desde = limite
    #break

print(len(resultado))
#"""