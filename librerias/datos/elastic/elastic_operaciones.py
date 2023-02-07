    #!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint
from datetime import datetime
import operator

from dict_deep import deep_get
from elasticsearch import helpers

from . import elastic_busquedas
from librerias.datos.base import globales
from librerias.datos.sql import sqalchemy_leer

###############
# CREA INDICE #
###############
# Crea indice elastic
def creaIndice(estructura="", ruta="base"):    
    conexion = globales.lee_conexion_elastic(ruta)
    modelo   = globales.lee_modelo_elastic(estructura)    

    nombreIndice = estructura    
    if conexion.indices.exists( index=nombreIndice):
        #print( 'YA EXISTE: ', nombreIndice )
        pass
    else:
        print("")
        print("..........................")
        print( 'CREA NO EXISTE:', nombreIndice )  
        #print("conexion:", conexion)
        print( estructura)
        pprint.pprint(modelo["mapa"] )          
        mapping = modelo["mapa"]['mappings']
        setting = modelo["mapa"]['settings']
        print( 
            conexion.indices.create( 
                index=nombreIndice, 
                mappings=mapping, 
                settings=setting, 
                ignore=400
            ) 
        )   

    globales.carga_modelo_elastic(
        estructura="", 
        modelo={}, 
        mapa={}, 
        indexamiento={}, 
        indice="", 
        campoId=None
    )
    globales.carga_modelo_elastic(
        estructura, 
        modelo["modelo"], 
        modelo["mapa"], 
        modelo["indexamiento"], 
        nombreIndice,
        modelo["campoId"]
    )

##################
# ELIMINA INDICE #
##################
# Elimina indice elastic
def eliminaIndice(estructura="", ruta="base"):    
    conexion = globales.lee_conexion_elastic(ruta)
    conexion.indices.delete( index=estructura )

###############
# BULK INDEXA #
###############

def bulk_indexar(conexion, modelo, indice, datos=[], campoId="id"):
    # Prepara lote de datos
    sale       = None
    datos_bulk = []
    for dato in datos:
        paquete = {
            "_index" : indice,        
            "_id"    : dato[campoId],
            "_source": cargaDatos(dato, modelo)
        }  
        datos_bulk.append(paquete)    
    
    # Salva paquete de datos
    try:
        sale = helpers.bulk( 
            client=conexion, 
            actions=datos_bulk, 
            raise_on_exception=False 
        )
        conexion.indices.flush( index=indice )
    except Exception as e:
        print("BULK INDEXAR:", str(e))

    return sale

##########
# INDEXA #
##########
def cargaDatos(datos, modelo):
    datos_documento = {}
    for nombre, campo in modelo.items():
        tipo  = campo.get('type', 'text')
        valor = deep_get(datos, nombre)  
            
        # Buscar como asociar valor por defcto del campo
        if valor == None:
            valor = ""
        if type(valor) not in [ dict, list, datetime, int ]:
            if valor is None and tipo == 'text':
                valor = ""    
            valor = str(valor)

        if nombre.find(".") > -1:
            lista       = nombre.split(".")
            normalizado = lista[-1]
        else:
            normalizado = nombre
        datos_documento[normalizado] = valor
    
    return datos_documento

def salvaDocumento(conexion, indice, datos_documento, campoId="id", flush=False):
    try:        
        conexion.index( 
            index=indice, 
            id=datos_documento[campoId], 
            body=datos_documento 
        )             
        if flush:
            conexion.indices.flush(index=indice)
        else:
            conexion.indices.refresh(index=indice)            
    except Exception as error:
        print(" EEEEEEEEEEEERRR ->no se esta reportando ", str(error))
        datos_documento = (
            "Elastic indexar registrar datos:" + 
            type(error).__name__ + " : " + str(error)
        )
        
def indexar(conexion, modelo, indice, datos={}, campoId="id", flush=False):
    # JCR !! VALIDAR ERRORES
    continuar       = True
    datos_documento = {}
    datos_documento = cargaDatos(datos, modelo)    
    if continuar:
        salvaDocumento(
            conexion, 
            indice, 
            datos_documento, 
            campoId=campoId, 
            flush=flush
        )

    return datos_documento

# INDEXA UN DOCUMENTO
def indexar_documento(ruta, estructura, datos, flush=False):
    conexion  = globales.lee_conexion_elastic(ruta)
    modelo    = globales.lee_modelo_elastic(estructura)
    resultado = indexar(
        conexion, 
        modelo["modelo"], 
        modelo["indice"], 
        datos, 
        modelo["campoId"], 
        flush
    )     
    
    return resultado


# INDEXA UN REGISTRO
def indexar_registro(estructura, regitro_id):
    datos     = sqalchemy_leer.leer_un_registro(estructura, regitro_id)
    resultado = indexar_documento("base", estructura, datos, flush=True)
    
    return resultado

contador = 0
# INDEXA LISTA DE DOCUMENTOS
def indexar_documentos(ruta, estructura, datosLista):    
    conexion  = globales.lee_conexion_elastic(ruta)
    modelo    = globales.lee_modelo_elastic(estructura)
    indice    = modelo["indice"]
    modeloEl  = modelo["modelo"]
    campoId   = modelo["campoId"]

    for datos in datosLista:
        resultado = indexar(conexion, modeloEl, indice, datos, campoId, False)    
    conexion.indices.flush(indice)
    
    return resultado

###########
# ELIMINA #
###########
def eliminar(conexion, indice, registroId, campoId="id", flush=False):
    datos_documento = {}
    try:
            conexion.delete(index=indice, id=registroId,  refresh=True)      
            if flush:
                conexion.indices.flush(indice)
            else:
                conexion.indices.refresh(indice)            
    except Exception as error:
        datos_documento = (
            "Elastic eliminar registrar datos:" + 
            type(error).__name__ + " : " + str(error)
        )
    
    return {"id": registroId}

# ELIMINA DOCUMENTO INDEXADO
def indexar_elimina_documento(ruta, estructura, registroId, flush=False):
    conexion  = globales.lee_conexion_elastic(ruta)
    
    resultado = eliminar(
        conexion, 
        estructura, 
        registroId, 
        campoId="id", 
        flush=False
    )
    
    return resultado

# ELIMINA UN REGISTRO
def eliminar_registro(estructura, registroId, flush=True):
    conexion  = globales.lee_conexion_elastic("base")
    resultado = eliminar(
        conexion, 
        estructura, 
        registroId, 
        campoId="id", 
        flush=False
    )
    
    return resultado


#####################
# LEER UN DOCUMENTO #
#####################
def leerUno(conexion, indice, registroId):
    datos_documento = {}
    try:            
        datos_documento = conexion.get(index=indice, id=registroId)                    
    except Exception as error:
        datos_documento = (
            "Elastic un leer registro datos:" + 
            type(error).__name__ + " : " + str(error)
        )
    
    return datos_documento

# LEER DOCUMENTO INDEXADO
def indexar_leer_documento(ruta, estructura, registroId):
    conexion  = globales.lee_conexion_elastic(ruta)
    resultado = leerUno(conexion, estructura, registroId)
    
    return resultado

def indexar_recupera_documento(estructura, registroId):
    resultado = indexar_leer_documento("base", estructura, registroId)
    
    return resultado