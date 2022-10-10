#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime
import yaml
from parent_import import parentdir

basicas         = parentdir.parentdir.librerias.utilidades.basicas
configuracion   = parentdir.parentdir.aplicacion.inicio.configuracion
globales        = parentdir.parentdir.librerias.datos.base.globales
base_general    = parentdir.parentdir.aplicacion.datos.clases.clases_base.base_general
sqalchemy_conectar    = parentdir.parentdir.librerias.datos.sql.sqalchemy_conectar
sqalchemy_operaciones      = parentdir.parentdir.librerias.datos.sql.sqalchemy_operaciones
elastic_conectar           = parentdir.parentdir.librerias.datos.elastic.elastic_conectar
elastic_filtros_tipo       = parentdir.parentdir.librerias.datos.elastic.elastic_filtros_tipo
flujos_insertar_sql        = parentdir.parentdir.librerias.flujos.flujos_insertar_sql
flujos_indexar_sql         = parentdir.parentdir.librerias.flujos.flujos_indexar_sql
estructura_operaciones_sql = parentdir.parentdir.librerias.datos.estructuras.estructura_operaciones_sql

# Conexión ELASTIC
import datos_es
print("--->", datos_es)
globales.carga_configuracion_elastic("base", datos_es.datos)
elastic_conectar.conectarElastic("base")

"""
busqueda = Search(using=client, index="conexion").
    .filter("term", category="search") \
    .query("match", title="python")   \
    .exclude("match", description="beta")
"""

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl import Q as Q_dsl

conexion = globales.lee_conexion_elastic("base")

print("conexión:", conexion)


from elasticsearch_dsl import Q as Q_dsl

#filtro = Q_dsl("term", codigo="03")
#filtro = Q_dsl("match", adicional="rodríguez") & Q_dsl("match", codigo="OCHO")
#filtro = Q_dsl("prefix", nombre="*bo")
#filtro = Q_dsl("query_string", query = "*ra*", fields=["nombre"])
#filtro = Q_dsl("query_string", query = "bo", fields=["nombre"])

#filtro = elastic_filtros_tipo.contiene_texto("nombre", "ra")
#filtro = elastic_filtros_tipo.no_contiene_texto("nombre", "ru")
#filtro = elastic_filtros_tipo.comienza_con("nombre", "www")
#filtro = elastic_filtros_tipo.termina_con("nombre", "DOR")
#filtro = elastic_filtros_tipo.texto_igual("nombre", "argentina")
#filtro = elastic_filtros_tipo.texto_diferente("nombre", "chile")
filtro = elastic_filtros_tipo.texto_blanco("codigo")
print(filtro)


busqueda  = Search(using=conexion, index="pais").filter(filtro)
#busqueda  = Search(using=conexion, index="pais")
resultado = busqueda.execute()

#for hit in resultado:
#    print(hit)

pprint.pprint(resultado.to_dict())
#print(yaml.dump(resultado.hits.hits, default_flow_style=False))

"""
pp = pprint.PrettyPrinter(indent=4)
for hit in resultado.hits.hits:
    pp.pprint(hit)
"""