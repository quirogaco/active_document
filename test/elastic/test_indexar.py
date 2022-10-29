#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

import configuracion_base

from librerias.datos.elastic import elastic_operaciones
from librerias.datos.sql     import sqalchemy_leer
from librerias.datos.base    import globales

conexion   = globales.lee_conexion_elastic("base")

def recuperar(conexion, estructura):
    modelo = globales.lee_modelo_elastic(estructura)
    desde  = 0

    resultado = sqalchemy_leer.leer_todos("base", estructura, desde=0, hasta=10000)
    bulk      = elastic_operaciones.bulk_indexar(conexion, modelo["modelo"], modelo["indice"], resultado)
    print("")
    print("RESULTADO>>>" + estructura, len(resultado))    
    #pprint.pprint(resultado)
    print("")

#CONFIGURACIÓN
#recuperar(conexion, "global_base_general")
# recuperar(conexion, "configuracion_general")
# recuperar(conexion, "canales_comunicacion")
# recuperar(conexion, "roles")
# recuperar(conexion, "ubicaciones")
recuperar(conexion, "usuarios")
# recuperar(conexion, "dependencias")
# recuperar(conexion, "continentes")
# recuperar(conexion, "paises")
# recuperar(conexion, "departamentos")
# recuperar(conexion, "ciudades")
# recuperar(conexion, "grupo_usuarios")
# recuperar(conexion, "festivos")
# recuperar(conexion, "reportes_dinamicos")
# recuperar(conexion, "plantillas")
# recuperar(conexion, "consecutivos")
# recuperar(conexion, "tipo_identificaciones")
# recuperar(conexion, "genero")
# recuperar(conexion, "tipo_poblacion")
# recuperar(conexion, "rango_edad")
# recuperar(conexion, "discapacidad")
# recuperar(conexion, "tipo_terceros")
# recuperar(conexion, "tipo_peticiones")
# recuperar(conexion, "temas")
# recuperar(conexion, "subtemas")
# recuperar(conexion, "empresas_mensajeria")
# recuperar(conexion, "motivos_devolucion")
# recuperar(conexion, "permisos_archivo")
# recuperar(conexion, "tipo_peticiones")
# recuperar(conexion, "tramites")


#"""
# RADICACION GESTION
recuperar(conexion, "radicados_entrada")
recuperar(conexion, "radicados_salida")
recuperar(conexion, "radicados_interno")
recuperar(conexion, "peticiones")
recuperar(conexion, "copias")
#"""

#"""
# ARCHIVO
# recuperar(conexion, "agn_fondo_documental")
# recuperar(conexion, "agn_trd")
# recuperar(conexion, "agn_dependencia_trd")
# recuperar(conexion, "agn_serie_trd")
# recuperar(conexion, "agn_subserie_trd")
# recuperar(conexion, "agn_tipo_documental_trd")
# recuperar(conexion, "agn_documentos_trd")
# recuperar(conexion, "agn_expedientes_trd")

#recuperar(conexion, "datos_formularios_dinamicos")
#"""

#recuperar(conexion, "peticiones")
#recuperar(conexion, "radicados_entrada")

#recuperar(conexion, "agn_documentos_trd")
#recuperar(conexion, "agn_dependencia_trd")
#recuperar(conexion, "agn_serie_trd")
# recuperar(conexion, "agn_expedientes_trd")
#recuperar(conexion, "dependencias")
#recuperar(conexion, "agn_prestamos_trd")

#recuperar(conexion, "logs")