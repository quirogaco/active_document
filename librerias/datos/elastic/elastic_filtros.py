#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
from elasticsearch_dsl import Q as Q_dsl
from nested_lookup import nested_lookup

from librerias.utilidades import basicas 
from . import elastic_filtros_tipo

# Si lista de filtros SOLO tiene listas como elementos
def contiene_solo_listas(filtros):
    contiene = True
    for filtro in filtros:        
        if not isinstance(filtro, list):
            contiene = False
    
    return contiene

# Si lista de filtros tiene alguna lista como elemento
def contieneLista(filtros):
    contiene = False
    for filtro in filtros:
        if isinstance(filtro, list):
            contiene = True
    
    return contiene

# Filtro basico
def esFiltroPlano(filtro):
    # ["departamento_nombre", "=", "Amazonas"]
    esPlano = True
    for indice, elemento in enumerate(filtro):
        if not (type(elemento) is str):
            esPlano = False

    return esPlano

# Tipo de filtro dev
def tipoFiltro(filtro):
    tipo     = ""
    longitud = len(filtro)
    if   longitud == 3:
        if esFiltroPlano(filtro):
            tipo = "binario"
        else:
            print("contiene_solo_listas:", contiene_solo_listas(filtro))
            if contiene_solo_listas(filtro):
                tipo = "lista"
            else:
                tipo = "grupo"  

    elif longitud == 2:
        if esFiltroPlano(filtro):
            tipo = "unario"
        else:
            if contiene_solo_listas(filtro):
                tipo = "lista"
            else:
                tipo = "grupo"  
    
    elif longitud > 3:
        if contiene_solo_listas(filtro):
            tipo = "lista"
        else:
            tipo = "lista_binarios"

    return tipo

###########
# Filtros #
###########

# Lee definiciòn del campo
def traeDefinicionCampo(definicion, campo):
    # Campos de la estructura     
    nested             = None  
    campos             = dict(definicion.get("campos", {}))
    camposIndexamiento = dict(definicion.get("camposIndexamiento", {}))
    campos.update(camposIndexamiento) 
    if (campo.find(".") > -1):       
        nombres         = campo.split(".")
        # Path de nested query
        nested          = ".".join(nombres[0:-1])

        # Valor de la ultima propiedad -> base.ultima
        propiedad       = nombres[-1]
        
        # Definiciòn base -> base.ultima
        definicionBase  = campos.get(nested, None)

        # Definicion del campo anidado
        definicionCampo = nested_lookup(propiedad, definicionBase)[0]
    else:
        definicionCampo   = campos.get(campo, None) 

    return definicionCampo, nested

# Crea filtro para un campo
def crear_filtro_campo(
    definicion, 
    campoBusqueda, 
    operacionBusqueda, 
    valorBusqueda
):        
    # Informaciòn para filtro   
    elasticFiltro = None
    definicionCampo, nested  = traeDefinicionCampo(definicion, campoBusqueda)
    # Tipo de campo
    # Campo no existe
    if definicionCampo is not None: 
        tipoCampo  = definicionCampo.get("tipoElastic", "texto")  

        # Expresiòn en espaòol de operacion contiene, igual, etc
        expresionFiltro = elastic_filtros_tipo.expresionesEspanol.get(
            operacionBusqueda, 
            "contiene"
        )   
            
        # Diccionario de tipos de filtro por tipo de campo: texto, clave, 
        tipoFiltroDiccionario = elastic_filtros_tipo.filtrosElasticTipo.get(
            tipoCampo, 
            "texto"
        ) #definicionCampo
        
        # Filtro por tipo de campo y expresiòn
        elasticFiltroFuncion  = tipoFiltroDiccionario.get(
            expresionFiltro, 
            "texto"
        )        
        if not isinstance(elasticFiltroFuncion, str):    
            elasticFiltro = elasticFiltroFuncion(campoBusqueda, valorBusqueda)    
            if nested != None:
                resaltar = definicion.get('resaltar', [])
                if campoBusqueda in resaltar:
                    inner_hits = {
                        "_source"  : {},
                        "size"     : 10,
                        "highlight": {
                            "type"                   : "fvh",
                            "pre_tags"               : "<xxyyzzemxxyyzz>", 
                            "post_tags"              : "</em>",
                            "number_of_fragments"    : 3,
                            "fragment_size"          : 50,                            
                            "boundary_scanner_locale": "es-ES",                             
                            "fields"                 : {
                                campoBusqueda: {}
                            }
                        }
                    }   
                    elasticFiltro = Q_dsl( 
                        "nested", 
                        path=nested, 
                        query = elasticFiltro, 
                        inner_hits=inner_hits 
                    )
                else:
                    elasticFiltro = Q_dsl( 
                        "nested", 
                        path=nested, 
                        query = elasticFiltro
                    )
        
    return elasticFiltro

# Crea query booleano
def filtroGrupo(agrupador, primerQuery, segundoQuery):
    if agrupador == "and":
        query = Q_dsl( primerQuery & segundoQuery )
    else:
        # "or"
        query = Q_dsl( primerQuery | segundoQuery )

    return query

# Tipo elemento del grupo
def tipoElemento(elemento):
    tipo = "filtro"
    if (type(elemento) is str):
        tipo = "booleano"

    return tipo 

def esPar(numero):
    mod = numero % 2
    if mod > 0:
        return False
    else:
        return True

# Crea query grupo
def creaFiltroGrupo(definicion, filtro):
    primerFiltro  = filtro[0]
    agrupador     = filtro[1]
    segundoFiltro = filtro[2]   
    
    # Crea el query
    primerQuery   = crear_filtros(definicion, primerFiltro)
    segundoQuery  = crear_filtros(definicion, segundoFiltro)
    if   (primerQuery != None) and (segundoQuery == None):
        elasticFiltro = primerQuery
    elif (primerQuery == None) and (segundoQuery != None):
        elasticFiltro = segundoQuery
    elif (primerQuery == None) and (segundoQuery == None):
        elasticFiltro = None
    else:
        elasticFiltro = filtroGrupo(agrupador, primerQuery, segundoQuery)  
        resto         = filtro[3:]  
        
        agrupador    = None
        segundoQuery = None
        for indice, elemento in enumerate(resto): 
            par  = esPar(indice)
            if par == True:
                agrupador = elemento
            else:
                segundoQuery = crear_filtros(definicion, elemento)
            
            if (agrupador != None) and (segundoQuery != None):
                elasticFiltro = filtroGrupo(
                    agrupador, 
                    elasticFiltro, 
                    segundoQuery
                )  
                agrupador     = None
                segundoQuery  = None

    return elasticFiltro

from itertools import zip_longest
def lista_binarios(definicion, filtros):  
    # print("")
    # print("+++++++++++++++++++++++")
    # pprint.pprint(filtros)
    # iter es necesario para avanzar en la lista 
    args = [iter(filtros)] * 2
    pairs = (zip_longest(fillvalue=None, *args))
    filtro_ultimo = None
    conector_anterior = None
    filtros_elastic = []
    for filtro, conector in pairs:
        # print("")
        # print(".....", filtro)
        campo, operacion, valor = filtro
        # print("campo, operacion, valor, conector -->", campo, operacion, valor, conector)
        ####################
        # Prepara el query #
        ####################
        # Tipo de campo
        definicionCampo, nested = traeDefinicionCampo(definicion, campo)
        tipoCampo = definicionCampo.get("tipoElastic", "texto")
        # Operacion de busqueda
        expresionFiltro = elastic_filtros_tipo.expresionesEspanol.get(
            operacion, 
            "contiene"
        )   
        # Diccionario de operaciones asociadas al tipo de campo
        tipoFiltroDiccionario = elastic_filtros_tipo.filtrosElasticTipo.get(
            tipoCampo, 
            "texto"
        ) #definicionCampo
        # Operacion especifica por tipo de campo
        elasticFiltroFuncion = tipoFiltroDiccionario.get(
            expresionFiltro, 
            "texto"
        )        
        # Filtro elastic
        #elasticFiltro = elasticFiltroFuncion(campo, valor)
        elasticFiltro = crear_filtro_campo(definicion, campo, operacion, valor)
        if (filtro_ultimo is not None) and (conector_anterior is not None):
            elasticFiltro = filtroGrupo(
                conector_anterior, 
                filtro_ultimo, 
                elasticFiltro
            )
            filtro_ultimo = elasticFiltro
            conector_anterior = conector
            filtros_elastic.append(elasticFiltro)
        
        # Prepara secuencia de filtros
        if filtro_ultimo is None:
            filtro_ultimo = elasticFiltro
        
        if conector_anterior is None:
            conector_anterior = conector

    # print("&&&&&")
    # pprint.pprint(filtro_ultimo)
    # print("")
    # print("")

    # se retorna el ultimo que es el acumulado de tos los campos
    return filtro_ultimo

# Crea filtro basado en expresiones digitadas en selec o tagbox
def crear_filtro_sencillo(parametros, definicion):    
    elasticFiltro     = None
    operacionBusqueda = parametros.get('operacionBusqueda', None)
    campoBusqueda     = parametros.get('campoBusqueda', None)
    valorBusqueda     = parametros.get('valorBusqueda', None)        
    if (campoBusqueda != None) and (operacionBusqueda != None) and \
    (valorBusqueda not in [None, '']):
        elasticFiltro = crear_filtro_campo(
            definicion, 
            campoBusqueda, 
            operacionBusqueda, 
            valorBusqueda
        )    

    return elasticFiltro

# Crea filtro basico [campo, operador, valor]
def crearFiltroBinario(definicion, filtro):
    campoBusqueda     = filtro[0] 
    operacionBusqueda = filtro[1] 
    valorBusqueda     = filtro[2]
    elasticFiltro     = crear_filtro_campo(
        definicion, 
        campoBusqueda, 
        operacionBusqueda, 
        valorBusqueda
    )

    return elasticFiltro

# Si lista de filtros tiene algun valor
def contieneValores(filtros):
    contiene = True
    for filtro in filtros:
        if   isinstance(filtro, list) and len(filtro) == 0:
            contiene = False
        elif isinstance(filtro, dict) and len(filtro.keys()) == 0:
            contiene = False
        #elif (filtro in [None, ""]):
        #    contiene = False
    
    return contiene

def lista_filtros(definicion, filtros):
    filtro_lista = []                    
    for filtro in filtros:
        tipo = tipoFiltro(filtro)
        if ( tipo == 'binario' ):            
            nuevo_filtro = crearFiltroBinario(definicion, filtro)
        
        if ( tipo == "grupo"):
            nuevo_filtro = creaFiltroGrupo(definicion, filtro )

        if ( tipo == "lista_binarios"):
            nuevo_filtro = lista_binarios(definicion, filtro )

        if ( tipo == "unario"): # conector or -and
            nuevo_filtro = filtro

        if nuevo_filtro != None:
            filtro_lista.append( nuevo_filtro)  

    return filtro_lista       

# Crea los filtros basados en lista de filtros
def crear_filtros(definicion, filtros):
    filtroElastic = None
    #print("crear_filtros-------->>>", len(filtros)    )
    if contieneValores(filtros):
        if (contieneLista(filtros)):  
            tipoGlobal = tipoFiltro(filtros)   
            #print("TIPO GLOBAL:", tipoGlobal)         
            if (tipoGlobal == "grupo"):
                #print("crear_filtros->GRUPO:", tipoGlobal)   
                filtroElastic = creaFiltroGrupo(definicion, filtros)
            else:
                if (tipoGlobal == "lista"):  
                    #print("crear_filtros->LISTA:", tipoGlobal)                                      
                    filtro_lista = lista_filtros(definicion, filtros)                    
                    query = filtro_lista.pop()
                    conector = "&"
                    for filtro in filtro_lista:
                        if filtro == "or":
                            conector = "|"
                        else:
                            if conector == "&":
                                query = Q_dsl( query & filtro )
                            else:
                                query = Q_dsl( query | filtro )
                    filtroElastic = query                     
                else:                      
                    filtro_lista = lista_filtros(definicion, filtros)                                    
                    query = filtro_lista.pop()
                    conector = "&"
                    for filtro in filtro_lista:
                        if filtro == "or":
                            conector = "|"
                        else:
                            if conector == "&":
                                query = Q_dsl( query & filtro )
                            else:
                                query = Q_dsl( query | filtro )
                    filtroElastic = query                     
                    # for filtro in filtros:
                    #     print("FILTRO:", tipoFiltro(filtro), filtro)    
                    #     if ( tipoFiltro(filtro) == 'binario' ):            
                    #         filtroElastic = crearFiltroBinario(definicion, filtro)
        else:
            #print("crear_filtros->DIRECTO:")    
            # Filtro directo
            if ( len(filtros) > 0 ):                       
                filtroElastic = crearFiltroBinario(definicion, filtros)


    return filtroElastic

# Crea todos los filtros de la busqueda
def prepararFiltros(busqueda, parametros, definicion):
    # Filtro sencillo (ej. select, tagbox)
    sencillo = crear_filtro_sencillo(parametros, definicion)    
    
    # if (filtro != None):        
    #     busqueda = busqueda.query(filtro)
    # else:
        
    # Filtros panel, busqueda y encabezados
    filtros = parametros.get("filtros", []) 
    # print("&&&&&&&&&&&&&&&&&&&&&&&&")
    # print(filtros)
    filtro  = crear_filtros(definicion, filtros)
    if (filtro != None):
        if sencillo != None:
            filtro = Q_dsl( sencillo & filtro )
        busqueda = busqueda.query(filtro)
    else:
        if sencillo != None:
            filtro = sencillo
            busqueda = busqueda.query(filtro)

    return busqueda