#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, builtins

from librerias.datos.base  import globales

from . import crea_celery_app

generales_app = crea_celery_app.aplicacion_celery('generales_app', 'generales')

# Indexa una estructura
from librerias.datos.elastic import elastic_operaciones
@generales_app.task(name='indexar_estructura')
def indexar_estructura(**parametros):
    elastic_operaciones.indexar_registro(parametros["estructura"], parametros["registro_id"])  

globales.carga_funcion_general("indexar_estructura_cola", indexar_estructura, atributos={"tipo": "celery"})

# Manejar archivos
from aplicacion.archivos  import archivo_operaciones
@generales_app.task(name='manejo_archivos')
def manejo_archivos(**parametros):
    archivo_operaciones.manejo_archivos( 
        parametros["estructura"], 
        parametros["accion"], 
        parametros["datos"],
        parametros["tarea"], 
        parametros["archivos"], 
        parametros["id_tarea"],
        parametros["tipo_relacion"],
        parametros.get("cubeta", "contenedor.general")
    )

globales.carga_funcion_general("manejo_archivos_cola", manejo_archivos, atributos={"tipo": "celery"})