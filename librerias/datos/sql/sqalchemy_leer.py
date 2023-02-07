#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import pprint, operator, copy

from librerias.datos.base import globales 
from librerias.datos.estructuras import estructura_operaciones
from . import sqalchemy_comunes

#############################
# # OPERACIONES DE CONSULTA #
#############################

# Existe registro
def existe(sesion, CLASE, filtros=[], completo=False):
    query     = sesion.query(CLASE).filter(*filtros)
    resultado = query.first()
    if  (completo == True) and (resultado != None):
        resultado = sqalchemy_comunes.retornar_datos(resultado)        
        return resultado

    elif (completo == True) and (resultado == None):
        return {}

    elif (completo == False):
        valor = True if (resultado != None) else False
        return valor
    
def existe_registro(ruta, CLASE, filtros=[], completo=False):
    sesion    = sqalchemy_comunes.nuevaSesion(ruta)    
    resultado = existe(sesion, CLASE, filtros, completo)
    sesion.close()

    return resultado
        
def crea_query_id(sesion, CLASE, registroId, campoId="id"):
    CLASE_QUERY = copy.deepcopy(CLASE)
    columna     = getattr(CLASE_QUERY, campoId, None)
    query       = sesion.query(CLASE_QUERY).filter( *[columna==registroId] )

    return query    

# Lee un registro
def leer_registroSimple(
    ruta, 
    CLASE, 
    registroId, 
    campoId="id", 
    retornar="diccionario"):
    resultado = None    
    columna   = getattr(CLASE, campoId, None)
    if (type(columna) !=  type(None)): 
        sesion    = sqalchemy_comunes.nuevaSesion(ruta) 
        query     = crea_query_id(sesion, CLASE, registroId, campoId)     
        registro  = query.first()
        if registro != None:
            resultado = sqalchemy_comunes.retornar_datos(registro, retornar)
            
        sesion.close()        
    
    return resultado

# Referencias por llamdo a funci�n
def referenciasFuncion(ruta, funcion, referencia, normalizado):     
    campoReferencia = referencia.get('campoReferencia', None)
    datosReferencia = funcion(normalizado)
    datos           = {}
    datos[campoReferencia] = datosReferencia
    normalizado.update(datos)
    
    return normalizado

# Referencias por lectura
def referenciasLectura(ruta, referencia, normalizado):
    # Campos destino
    estructuraDestino = referencia.get('estructuraDestino', None)
    definicionDestino = globales.lee_definicion(estructuraDestino)
    CLASEDESTINO      = globales.lee_clase(definicionDestino['clase'])
    campoDestino      = referencia.get('campoDestino', 'id')
    
    # Campos local
    campoReferencia     = referencia.get('campoReferencia', None)
    atributosReferencia = referencia.get('atributosReferencia', None)
    modo                = referencia.get('modo', "simple")
    valorReferencia     = normalizado.get(campoReferencia, None)

    # valida valores None 
    if isinstance(valorReferencia, list):
        if (len(valorReferencia) > 0):
            valorReferencia = valorReferencia[0]
        else:
            valorReferencia = None

    if (modo=="lista"):
        print("")
        print("")
        print("referenciasLectura:", valorReferencia, atributosReferencia)
        print("")
        print("")
        print("")

    if (valorReferencia not in [None, "", "None", "none", "NONE"]):            
        registro = leer_registroExtendido(
            ruta, 
            estructuraDestino, 
            definicionDestino, 
            CLASEDESTINO, 
            valorReferencia, 
            campoDestino
        )
        datosDestino = {}
        for atributo in atributosReferencia:
            for local, referencia in atributo.items(): 
                datosDestino[local] = registro.get(referencia, None)    
        normalizado.update(datosDestino)
    
    return normalizado

# Retorna la informaci�n extendida del reistro
def informacionExtendida(ruta, estructura, definicion, resultado):
    normalizado = estructura_operaciones.normaliza_estructura_datos(
        estructura, 
        resultado, 
        False
    )
    referencias = list(definicion.get("referencias", []))    
    for referencia in referencias:   
        nombreFuncion           = referencia.get('funcion', None)
        if nombreFuncion != None:
            funcion = globales.lee_funcion_referencia(
                estructura, 
                nombreFuncion
            )
            normalizado = referenciasFuncion(
                ruta,
                funcion, 
                referencia, 
                normalizado
            )
        else:
            normalizado = referenciasLectura(ruta, referencia, normalizado)    
    
    return normalizado

# Lee registros con referencias
def leer_registroExtendido(
    ruta, 
    estructura, 
    definicion, 
    CLASE, 
    registroId, 
    campoId
):
    normalizado = leer_registroSimple(ruta, CLASE, registroId, campoId)
    #normalizado = informacionExtendida(ruta, estructura, definicion, resultado)
    return normalizado

# Lee un registro
def leer_registroId(
    ruta, 
    estructura, 
    definicion, 
    CLASE, 
    registroId, 
    campoId="id", 
    extendido=False, 
    retornar="diccionario"
):
    #if extendido == False:
    resultado = leer_registroSimple(ruta, CLASE, registroId, campoId)
    #else:
    #    resultado = leer_registroExtendido(ruta, estructura, definicion, CLASE, registroId, campoId)

    return resultado

# Lee un registro, estructutra
def leer_un_registro(estructura, registro_id):
    definicion = globales.lee_definicion(estructura)
    CLASE      = globales.lee_clase(definicion["clase"])
    resultado  = leer_registroId(
        "base", 
        estructura, 
        definicion, 
        CLASE, 
        registro_id
    )
    
    return resultado

# Lee todos los registros
def leer_todos(
    ruta, 
    estructura, 
    extendido=False, 
    retornar="diccionario", 
    desde=0, 
    hasta=1000
):
    definicion = globales.lee_definicion(estructura)
    CLASE = globales.lee_clase(definicion["clase"])
    sesion = sqalchemy_comunes.nuevaSesion(ruta)   
    registros = sesion.query(CLASE)[desde:hasta]
    resultado = []
    if (extendido == False) and (retornar == "objeto"):
        resultado = registros
    else:
        for registro in registros: 
            # Formato del registro
            if (retornar == "objeto"):
                normalizado = registro
            else:
                normalizado = sqalchemy_comunes.retornar_datos(
                    registro, 
                    retornar
                ) 

            # Datos extendidos
            if extendido == True:
                normalizado = informacionExtendida(
                    ruta, 
                    estructura, 
                    definicion, 
                    normalizado
                )  

            resultado.append( normalizado )
                
    sesion.close()

    return resultado

# Leer todos los registros por rango
def leer_rango(
    ruta, 
    estructura, 
    desde=0, 
    hasta=0, 
    extendido=False, 
    retornar="diccionario"
):
    definicion = globales.lee_definicion(estructura)
    CLASE      = globales.lee_clase(definicion["clase"])
    sesion     = sqalchemy_comunes.nuevaSesion(ruta)      
    registros  = sesion.query(CLASE)[desde : hasta]
    resultado  = []
    print(len(registros))
    for registro in registros:  
        normalizado = sqalchemy_comunes.retornar_datos(registro, retornar)         
        if extendido == True:
            normalizado = informacionExtendida(
                ruta, 
                estructura, 
                definicion, 
                normalizado
            )     
        resultado.append( normalizado )    
    sesion.close()

    return resultado

# Contar los registros
def contar_registros(ruta, estructura):
    definicion = globales.lee_definicion(estructura)
    CLASE      = globales.lee_clase(definicion["clase"])
    sesion     = sqalchemy_comunes.nuevaSesion(ruta)      
    total      = sesion.query(CLASE).count()
    sesion.close()

    return total