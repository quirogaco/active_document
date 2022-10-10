#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, types

from sqlalchemy     import desc, asc

from librerias.datos.base        import globales 
from librerias.datos.estructuras import estructura_operaciones
from . import sqalchemy_comunes
from . import sqalchemy_leer

#######################
# OPERACIONES FILTROS #
#######################

operacionesFiltro = {}

# Leer registros por filtros y ordenamiento
def leer_filtros_ordenamiento(ruta, estructura, filtrosSql=[], ordenamientos=[], extendido=False, retornar="diccionario"):
    definicion   = globales.lee_definicion(estructura)
    CLASE        = globales.lee_clase(definicion["clase"])

    resultado    = []     
    sesion       = sqalchemy_comunes.nuevaSesion(ruta)      
    query        = sesion.query(CLASE)

    # Aplica filtros
    if len(filtrosSql)> 0:
        query = query.filter(*filtrosSql)

    # Aplica ordenamiento
    if len(ordenamientos)> 0:
        query = query.order_by(*ordenamientos)

    # Ejecuta query
    #print(query.statement.compile(compile_kwargs={"literal_binds": True}))
    registros = query.all()
    

    for registro in registros:  
        normalizado = sqalchemy_comunes.retornar_datos(registro, retornar)         
        if extendido == True:
            normalizado = sqalchemy_leer.informacionExtendida(ruta, estructura, definicion, normalizado)     
        resultado.append( normalizado )
    
    sesion.close()

    return resultado

# Crea filtro
def creaFiltro(operador, columnaSql, valor):
    filtroSql = None
    if operador == "=":
        filtroSql = (columnaSql == valor)

    if operador == "in":
        filtroSql = (columnaSql.in_(valor))

    return filtroSql

# Crea Orden
def creaOrden(orden, columnaSql):
    ordenSql = None
    if orden == "descendente":
        ordenSql = desc(columnaSql)

    if orden == "ascendente":
        ordenSql = asc(columnaSql)

    return ordenSql

# Lee todos los registros
def filtrarOrdena(ruta="base", estructura="", filtros=[], ordenamientos=[], extendido=False, retornar="diccionario"):
    definicion = globales.lee_definicion(estructura)
    CLASE      = globales.lee_clase(definicion["clase"])
    
    # Crea filtros 
    filtrosSql = []
    for filtro in filtros:
        # Campo de filtro
        columna    = filtro[0]
        columnaSql = getattr(CLASE, columna, None)
        # operación del filtro
        operador   = filtro[1]
        # Valor del filtro
        valor      = filtro[2]

        filtroSql  = creaFiltro(operador, columnaSql, valor)
        
        if (type(filtroSql) != type(None)):
            filtrosSql.append(filtroSql)

    # [ "descendente", "traz_fecha" ]
    OrdenamientoSql = []
    for ordenar in ordenamientos:
        # Orden
        orden      = ordenar[0]
        # Campo de orden
        columna    = ordenar[1]
        columnaSql = getattr(CLASE, columna, None)

        ordenSql   = creaOrden(orden, columnaSql)
        
        if (type(ordenSql) != type(None)):
            OrdenamientoSql.append(ordenSql)

    resultado = leer_filtros_ordenamiento(ruta, estructura, filtrosSql, OrdenamientoSql, extendido, retornar)

    return resultado