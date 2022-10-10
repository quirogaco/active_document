#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from sqlalchemy.sql.expression       import and_
from sqlalchemy.orm                  import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from librerias.datos.base  import globales 
# Crea relaciones a otras tablas
# Se debe invocar al terminar de cargar todas las CLASES
relaciones_contador = 0

def relacion_base(clase_nombre, relacion):
    global relaciones_contador

    #################
    # Datos destino #
    #################
    estructura_destino = relacion["estructura_destino"]
    definicion_destino = globales.lee_definicion(estructura_destino)
    CLASE_DESTINO      = globales.lee_clase(definicion_destino['clase']) # Clase
    campo_destino      = relacion["campo_destino"]                       # Campo para filtro de relación
    columna_destino    = getattr(CLASE_DESTINO, campo_destino, None)     # Columna para relación

    ################
    # Datos origen #
    ################
    campo_referencia     = relacion["campo_referencia"]          # Campo local que cruza con campo destino       
    # Campo a traer por proxy, lista de diccionarios     
    # Clave campo local, valor campo remoto
    atributos_referencia = relacion["atributos_referencia"]      
    modo                 = relacion["modo"]
    CLASE                = globales.lee_clase(clase_nombre)
    columna_referencia   = getattr(CLASE, campo_referencia) #, None) # Columna local que cruza con columna destino

    ###################
    # Filtro primario #
    ###################
    filtro_primario      = and_(columna_referencia == columna_destino)
    
    ############
    # Relacion #
    ############
    usarlista = False
    if modo == "multiple":
        usarlista = True

    relacion_SQL = relationship(
        CLASE_DESTINO,
        primaryjoin  = filtro_primario,
        foreign_keys = columna_referencia,
        remote_side  = columna_destino,

        viewonly     = True,
        uselist      = usarlista,
        lazy         = 'select'
    )
    relaciones_contador += 1
    nombre_relacion      = "relacion_" + campo_referencia + "_" + str(relaciones_contador)
    setattr(CLASE, nombre_relacion, relacion_SQL)  

    ##########
    # Proxys #
    ##########
    for atributo_referencia in atributos_referencia:
        for atributo, referencia in atributo_referencia.items():
            proxy = association_proxy(
                nombre_relacion, 
                referencia
            )            
            setattr(CLASE, atributo, proxy)  

def origen_destino(clase_nombre, relacion, externa):
    atributos = {}

    ################
    # Datos origen #
    ################
    atributos["campo_referencia"]     = relacion["campo_referencia"]          # Campo local que cruza con campo destino       
    # Campo a traer por proxy, lista de diccionarios     
    # Clave campo local, valor campo remoto
    atributos["atributos_referencia"] = relacion["atributos_referencia"]      
    atributos["modo"]                 = relacion["modo"]
    atributos["CLASE"]                = globales.lee_clase(clase_nombre)
    atributos["columna_referencia"]   = getattr(atributos["CLASE"] , "id", None) # Columna local que cruza con columna destino
    atributos["tipo_relacion"]        = externa.get("tipo_relacion", None)

    #################
    # Datos destino #
    #################
    atributos["estructura_destino"] = relacion["estructura_destino"]
    atributos["definicion_destino"] = globales.lee_definicion(atributos["estructura_destino"])
    atributos["CLASE_DESTINO"]      = globales.lee_clase(atributos["definicion_destino"]['clase']) # Clase
    atributos["campo_destino"]      = relacion["campo_destino"]                       # Campo para filtro de relación
    atributos["columna_destino"]    = getattr(atributos["CLASE_DESTINO"], atributos["campo_destino"], None)     # Columna para relación

    return atributos

def intermedia(tipo_externa="relacion"):
    atributos = {}

    ####################
    # Datos intermedio #
    ####################
    if tipo_externa == 'relacion':
        atributos["RELACIONES_CLASE"]   = globales.lee_clase("global_base_relacion_estructura")
        atributos["columna_origen_id"]  = getattr(atributos["RELACIONES_CLASE"], "origen_id")
        atributos["columna_destino_id"] = getattr(atributos["RELACIONES_CLASE"], "destino_id")
        
    if tipo_externa == 'archivos':
        atributos["RELACIONES_CLASE"]   = globales.lee_clase("global_base_relacion_archivo")
        atributos["columna_origen_id"]  = getattr(atributos["RELACIONES_CLASE"], "origen_id")
        atributos["columna_destino_id"] = getattr(atributos["RELACIONES_CLASE"], "archivo_id")

    return atributos
    
def relacion_estructura(clase_nombre, relacion, externa, tipo_externa):
    global relaciones_contador

    # Atributos Origen, Destino
    atributos = origen_destino(clase_nombre, relacion, externa)

    # Datos Intermedio
    atributos_intermedio = intermedia(tipo_externa)

    ###################
    # Filtro primario #
    ###################
    filtro_primario   = and_(atributos["columna_referencia"]            == atributos_intermedio["columna_origen_id"])
    filtro_secundario = and_(atributos_intermedio["columna_destino_id"] == atributos["columna_destino"])
    
    ############
    # Relacion #
    ############
    usarlista = False
    if atributos["modo"] == "multiple":
        usarlista = True

    relacion_SQL = relationship(
        atributos["CLASE_DESTINO"], 

        primaryjoin  = filtro_primario,
        foreign_keys = [
            atributos["columna_referencia"],             
            atributos["columna_destino"],
            atributos_intermedio["columna_origen_id"], 
            atributos_intermedio["columna_destino_id"]
        ],
        remote_side  = atributos_intermedio["columna_origen_id"],
    
        secondary     = atributos_intermedio["RELACIONES_CLASE"].__table__,
        secondaryjoin = filtro_secundario,    
        viewonly      = True,
        uselist       = usarlista,
        lazy          = 'select'
    )
    relaciones_contador += 1
    nombre               = atributos["campo_referencia"]
    if (atributos["tipo_relacion"] != None):
        nombre = atributos["tipo_relacion"]
    nombre_relacion      = "relacion_" + nombre + "_" + str(relaciones_contador)
    setattr(atributos["CLASE"], nombre_relacion, relacion_SQL)  
    ##########
    # Proxys #
    ##########
    for atributo_referencia in atributos["atributos_referencia"]:
        for atributo, referencia in atributo_referencia.items():
            proxy = association_proxy(
                nombre_relacion, 
                referencia
            )
            setattr(atributos["CLASE"], atributo, proxy)
    
def relacion_externa(clase_nombre, relacion):
    externa      = relacion['externa']
    tipo_externa = externa.get('tipo', 'relacion')

    # Relacion a externas basicas, ej. Terceros
    if tipo_externa == 'relacion':       
        relacion_estructura(clase_nombre, relacion, externa, tipo_externa)
    
    # Relación a archivos
    if tipo_externa == 'archivos':       
        relacion_estructura(clase_nombre, relacion, externa, tipo_externa)