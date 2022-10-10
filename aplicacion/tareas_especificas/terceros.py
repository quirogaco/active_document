#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from sqlalchemy.sql.expression import and_

from librerias.flujos      import flujos_indexar_sql
from librerias.datos.base  import globales
from librerias.datos.sql   import sqalchemy_comunes
from librerias.datos.sql   import sqalchemy_insertar, sqalchemy_filtrar 

########################################
# Crea registro de relacion ESTRUCTURA #
########################################                          
def crear_registro_tercero( estructura, accion, datos, tarea, archivos, id_tarea):
    CLASE  = globales.lee_clase("config_terceros")
    sesion = sqalchemy_comunes.nuevaSesion("base")    

    print("")
    print("")
    print("CREAR TERCERO:")
    print("00000000000")
    pprint.pprint(datos)    

    #########################
    # Validar que no exista #
    #########################
    
    ##########################
    # Crea registro tercero  #
    ##########################
    # fALTA TIPO D EENTIDAD Y TIPO DE REMITENTE, DEBE SER UNA SOLA TABLA
    valores_terceros = tarea['datos']['valor_datos']

    ################
    # Crea TERCERO #
    ################
    # Tipo de entidad, tipo de persona 
    tipo_web = datos.get("tipo_web", None)
    datos_tercero = {
        "clase"                 : valores_terceros.get("tercero_clase", None),   
        "tipo_tercero_id"       : valores_terceros.get("tercero_tipo_tercero_id", None),   
        "tipo_identificacion_id": valores_terceros.get("tercero_tipo_identificacion_id", None),           
        "nro_identificacion"    : valores_terceros.get("tercero_nro_identificacion", ""),   
        "razon_social"          : valores_terceros.get("tercero_razon_social", ""),  
        "cargo"                 : valores_terceros.get("tercero_cargo", ""),   
        "nombres"               : valores_terceros.get("tercero_nombres", ""), 
        "apellidos"             : valores_terceros.get("tercero_apellidos", ""), 
        "correo_electronico"    : valores_terceros.get("tercero_correo_electronico", ""), 
        "direccion"             : valores_terceros.get("tercero_direccion", ""), 
        "codigo_postal"         : valores_terceros.get("tercero_codigo_postal", ""), 
        "telefono"              : valores_terceros.get("tercero_telefono", ""), 
        "telefono_movil"        : valores_terceros.get("tercero_telefono_movil", ""), 
        "fax"                   : valores_terceros.get("tercero_fax", ""), 
        "ciudad_id"             : valores_terceros.get("tercero_ciudad_id", "") 
    }
    if datos_tercero["clase"] is None:
        datos_tercero["clase"] = tipo_web

    registro  = sqalchemy_insertar.insertar_registro('base', CLASE, datos_tercero)
    resultado = flujos_indexar_sql.ejecutar("base", "terceros", {"registroId": registro["id"], "flush": True})

    ################################
    # Crea relación con el TERCERO #
    ################################
    funcion = CONFIGURACION_GENERAL["FUNCIONES_TAREAS"].get("relaciones_externas", None)
    if funcion != None:
        tarea['datos']['valorReferencia'] = registro['id']
        funcion(estructura, accion, datos, tarea, archivos, id_tarea)

    sesion.close()

    print("")
    print("")

    return resultado
    
CONFIGURACION_GENERAL["TAREAS_ESPECIFICAS"]["terceros"] = crear_registro_tercero