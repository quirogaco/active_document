#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.base import globales 

from librerias.flujos     import flujos_indexar_sql
from librerias.flujos     import flujos_indexar_eliminar_sql
from librerias.flujos     import flujos_insertar_sql
from librerias.flujos     import flujos_modificar_sql
from librerias.flujos     import flujos_eliminar_sql
from librerias.flujos     import flujos_leer_sql

from librerias.datos.sql         import sqalchemy_operaciones 
from librerias.datos.elastic     import elastic_operaciones
from librerias.datos.estructuras import estructura_operaciones_posteriores, estructura_operaciones_anteriores

##########################
# Operaciones con flujos #
##########################

# Indexa registro de ESTRUCTURA
def indexaEstructura(estructura, resultado, flush= True):
      definicion = globales.lee_definicion(estructura)
      indexa     = definicion.get('indexa') 
      if indexa == "si":
            idRegistro = resultado["datos"]["resultados"]["datos"]["id"]
            resultado  = flujos_indexar_sql.ejecutar("base", estructura, {"registroId": idRegistro, "flush": flush})

      return resultado

# Elimina registro del indice de ESTRUCTURA
def indexaEliminaEstructura(estructura, resultado, flush, id_tarea):
      definicion = globales.lee_definicion(estructura)
      indexa     = definicion.get('indexa') 
      if indexa == "si":
            idRegistro = resultado["datos"]["resultados"]["datos"]["id"]
            resultado  = flujos_indexar_eliminar_sql.ejecutar("base", estructura, {"registroId": idRegistro, "flush": flush}, id_tarea)

      return resultado

def manejo_error(operacion, resultado, e):      
      error = str(e)
      print("ERROR:", operacion, error)
      sale = {
            "datos"  : None,
            "errores": None
      }
      sale["error"] = "si"
      sale["datos"] = [error]
      resultado = sale

      return resultado

# Inserta registro de una ESTRUCTURA
def insertarEstructura(estructura, datos, archivos, id_tarea): 
      datos = estructura_operaciones_anteriores.operaciones(estructura, 'insertar', archivos, id_tarea, datos) 
      resultado = flujos_insertar_sql.ejecutar("base", estructura, datos, id_tarea) 

      if resultado["error"] == "no":         
            try:      
                  datos_resultado = resultado['datos']['resultados']['datos']
                  estructura_operaciones_posteriores.operaciones(estructura, 'insertar', archivos, id_tarea, datos_resultado)      
                  resultado = indexaEstructura(estructura, resultado, True)
            except Exception as e:                  
                  resultado = manejo_error("insertarEstructura", resultado, e)
      
      return resultado

# Modifica registro de una ESTRUCTURA
def modificarEstructura(estructura, datos, archivos, id_tarea): 
      datos = estructura_operaciones_anteriores.operaciones(estructura, 'modificar', archivos, id_tarea, datos)
      resultado = flujos_modificar_sql.ejecutar("base", estructura, datos, id_tarea)      
      if resultado["error"] == "no":
            try:
                  datos_resultado = resultado['datos']['resultados']['datos']
                  estructura_operaciones_posteriores.operaciones(estructura, 'modificar', archivos, id_tarea, datos_resultado)    
                  resultado = indexaEstructura(estructura, resultado, True)
            except Exception as e:                  
                  resultado = manejo_error("modificarEstructura", resultado, e)

      return resultado

# Elimina registro de una ESTRUCTURA
def eliminarEstructura(estructura, datos, archivos, id_tarea): 
      datos = estructura_operaciones_anteriores.operaciones(estructura, 'eliminar', archivos, id_tarea, datos) 
      resultado = flujos_eliminar_sql.ejecutar("base", estructura, datos, id_tarea)
      if resultado["error"] == "no":
            try:
                  datos_resultado = resultado['datos']['resultados']['datos']
                  estructura_operaciones_posteriores.operaciones(estructura, 'eliminar', archivos, id_tarea, datos_resultado)  
                  resultado = indexaEliminaEstructura(estructura, resultado, True, id_tarea)
            except Exception as e:                  
                  resultado = manejo_error("eliminarEstructura", resultado, e)
      
      return resultado

# Lee registro de una ESTRUCTURA
def leerRegistroEstructura(estructura, datos, archivos, id_tarea): 
      resultado = flujos_leer_sql.ejecutar("base", estructura, datos, id_tarea)
            
      return resultado

#########################
# Operaciones con datos #
#########################

# Lee campos con un atributo especifico
def campos_atributos(campos, atributo, valor):
      listado = []
      for campo, valores in campos.items():
            if valores.get(atributo, None) == valor:
                  listado.append(campo)

      return listado

import pprint

# LLama la función que convierte la estructura a diccionario plano
def normaliza_estructura_datos(estructura, datos, estricto=True):    
      resultado = datos
      funcion   = globales.lee_procesamiento(estructura, "normaliza_estructura")
      if funcion != None:
            resultado = funcion(estructura, datos, estricto)     
      
      return resultado

# LLama la función que crea la estructura de datos
def armar_estructura_datos(estructura, datos):    
      resultado = datos
      funcion   = globales.lee_procesamiento(estructura, "armar_estructura")
      if funcion != None:
            resultado = funcion(estructura, datos)

      return resultado

###########################################
# Funciones de pre y pos de la estructura #
###########################################
def preprocesa_estructura_datos(estructura, accion, datos, id_tarea):    
      resultado = datos
      funcion   = globales.lee_procesamiento(estructura, "pre_estructura")
      if funcion != None:
            resultado = funcion(estructura, accion, datos, id_tarea)
      
      return resultado

def postprocesa_estructura_datos(estructura, accion, datos, id_tarea):    
      resultado = datos
      funcion   = globales.lee_procesamiento(estructura, "post_estructura")
      if funcion != None:
            resultado = funcion(estructura, accion, datos, id_tarea)

      return resultado

########################
# Reindexar estructura #
########################
def reindexaEstructura(ruta, estructura, incremento=10):
      total_registros = sqalchemy_operaciones.contar_registros(ruta, estructura)
      for contador in range( 0, total_registros, incremento ):
            desde = contador
            hasta = (contador+incremento)
            datos = sqalchemy_operaciones.leer_rango(ruta, estructura, desde, hasta, extendido=True)
            elastic_operaciones.indexar_documentos(ruta, estructura, datos)