#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, pathlib, pprint

from sqlalchemy.sql.expression import and_

from librerias.datos.base  import globales
from librerias.datos.sql   import sqalchemy_comunes
from librerias.datos.sql   import sqalchemy_insertar, sqalchemy_filtrar 

########################################
# Crea registro de relacion ESTRUCTURA #
########################################
def crear_registro_relacion(   
    tipo_relacion, # Ej. COORDINADORES_DEPENDENCIA
    cardinalidad,  # multiple, simple
    origen,        # Estructura origen   
    origen_id,     # Id estructura origen
    origen_role,   # Role estructura origen
    destino,       # Estructura destino   
    destino_id,    # Id estructura destino
    destino_role,  # Role estructura destino
):
    ##########################
    # Crea registro relación #
    ##########################
    CLASE  = globales.lee_clase("global_base_relacion_estructura")
    data = {
        'tipo_relacion': tipo_relacion,
        'cardinalidad' : cardinalidad,
        'origen'       : origen, 
        'origen_id'    : origen_id,
        'origen_role'  : origen_role,
        'destino'      : destino, 
        'destino_id'   : destino_id,
        'destino_role' : destino_role
    }
    
    registro = sqalchemy_insertar.insertar_registro('base', CLASE, data)
    
    return registro

# Insertar registros de relacion
def eliminar_relacion(datos, tarea):
    datos_accion  = tarea.get('datos', None)
    tipo_relacion = datos_accion["tipo_relacion"]  # Ej. COORDINADORES_DEPENDENCIA
    origen        = datos_accion["origen"]         # Estructura origen   
    origen_id     = datos.get("id")                # Id estructura origen
    CLASE         = globales.lee_clase("global_base_relacion_estructura")

    sesion = sqalchemy_comunes.nuevaSesion("base")    
    query  = sesion.query(CLASE).filter( 
        and_(
            CLASE.tipo_relacion == tipo_relacion, 
            CLASE.origen        == origen, 
            CLASE.origen_id     == origen_id 
        ) 
    )
    registros = query.delete()
    sesion.commit()
    sesion.close()

def insertar_relacion(datos, tarea):
    datos_accion     = tarea.get('datos', None)
    valorReferencias = datos_accion.get('valorReferencia', None)
    if valorReferencias != None:
        if isinstance(valorReferencias, str):
            valorReferencias = valorReferencias.split(",")

        for valorReferencia in valorReferencias:
            if valorReferencia != None and valorReferencia != '':                
                id_creado     = datos.get("id")
                tipo_relacion = datos_accion["tipo_relacion"]  # Ej. COORDINADORES_DEPENDENCIA
                cardinalidad  = datos_accion["cardinalidad"]   # multiple, simple
                origen        = datos_accion["origen"]         # Estructura origen   
                origen_id     = id_creado                      # Id estructura origen
                origen_role   = datos_accion["origen_role"]    # Role estructura origen
                destino       = datos_accion["destino"]        # Estructura destino   
                destino_id    = valorReferencia                # Id estructura destino
                destino_role  = datos_accion["destino_role"]   # Role estructura destino
                crear_registro_relacion(   
                    tipo_relacion,
                    cardinalidad,
                    origen,  
                    origen_id,
                    origen_role,
                    destino,  
                    destino_id,
                    destino_role
                )                

def manejo_relaciones(estructura, accion, datos, tarea, archivos, id_tarea):
    accion = tarea.get('accion', None) 
    if   accion == 'insertar':
        insertar_relacion(datos, tarea)

    elif accion == 'modificar':
        eliminar_relacion(datos, tarea)
        insertar_relacion(datos, tarea)
        
    elif accion == 'eliminar':
        eliminar_relacion(datos, tarea)
        
CONFIGURACION_GENERAL["FUNCIONES_TAREAS"]['relaciones_externas'] = manejo_relaciones