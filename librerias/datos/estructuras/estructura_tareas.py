#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from prefect import task
from prefect.triggers import all_successful

from . import estructura_operaciones
from librerias.datos.base import globales 
from librerias.datos.sql  import sqalchemy_leer

# Valida los duplicados de una estructura
@task(name="ESTRUCTURA valida duplicados", trigger=all_successful)
def validas_duplicados_tarea(flujo_data):    
    # Parametros
    estructura = flujo_data["parametros"]["estructura"]
    datos      = flujo_data["parametros"]["datos"]
    ruta       = flujo_data["parametros"]["ruta"]
    accion     = flujo_data["parametros"]["accion"]

    #############
    # Funciones #
    #############
    # Crea diccionario con campos y valores a validar duplicados
    definicion = globales.lee_definicion(estructura)    
    campos     = definicion.get("campos", {})
    unicos     = estructura_operaciones.campos_atributos(campos, "unico", "si")
    valores    = {}
    for unico in unicos:
        valor = datos.get(unico, None)
        if (valor != None) and (unico != "id"):
            valores[unico] = valor

    # Realiza validaciones
    errores = []
    CLASE   = globales.lee_clase(definicion["clase"])
    for campo, valor in valores.items():
        columna_estructura = getattr(CLASE, "_estructura_", None)
        columna            = getattr(CLASE, campo, None)
        if (type(columna) !=  type(None)):
            if (accion == "insertar"):
                existe = sqalchemy_leer.existe_registro(ruta, CLASE, [columna_estructura==estructura, columna==valor], False)
                if (existe == True):
                    mensaje = "Ya existe un registro para (" + definicion["descripcion"] + "), en campo (" + campo + "), con valor (" + valor + ")"
                    errores.append(mensaje)

            if (accion == "modificar"):
                existe       = sqalchemy_leer.existe_registro(ruta, CLASE, [columna_estructura==estructura, columna==valor], True)
                idOriginal   = datos.get("id",  None)
                idEncontrado = existe.get("id",  None)
                if (idEncontrado != None) and (idOriginal != idEncontrado):
                    mensaje = "Ya existe un registro para (" + definicion["descripcion"] + "), en campo (" + campo + "), con valor (" + valor + ")"
                    errores.append(mensaje)                

    # Genera error
    # Esta función no genera datos
    flujo_data["resultados"]["errores"] = errores

    if len(errores) > 0:
        raise ValueError(errores)

    return flujo_data

# Arma estructura de datos
@task(name="ESTRUCTURA armar estructura", trigger=all_successful)
def armar_estructura_tarea(flujo_data):    
    # Parametros
    estructura = flujo_data["parametros"]["estructura"]
    datos      = flujo_data["parametros"]["datos"]

    #############
    # Funciones #
    #############
    resultado = estructura_operaciones.armar_estructura_datos(estructura, datos)
    # Genera datos como parametros a la siguiente función 
    flujo_data["parametros"]["datos"] = resultado
    flujo_data["resultados"]["datos"] = resultado

    return flujo_data

# Unifica datos de registro original con nuevos datos
@task(name="ESTRUCTURA unifica datos", trigger=all_successful)
def unifica_datos(flujo_data):    
    # Parametros
    estructura = flujo_data["parametros"]["estructura"]
    datos      = flujo_data["parametros"]["datos"]
    ruta       = flujo_data["parametros"]["ruta"]
    
    #############
    # Funciones #
    #############    
    # Lee registro original    
    errores    = []    
    definicion = globales.lee_definicion(estructura)  
    CLASE      = globales.lee_clase(definicion["clase"])
    campoIndice = definicion["campoIndice"]
    registroId  = datos["id"]
    datosRegistro = sqalchemy_leer.leer_registroId(ruta, estructura, definicion, CLASE, registroId, campoIndice, retornar="diccionario")
    datosRegistro.update(datos)

    # Genera error
    # Esta función no genera datos
    flujo_data["parametros"]["datos"] = datosRegistro
    flujo_data["resultados"]["datos"] = datosRegistro

    if len(errores) > 0:
        raise ValueError(errores)

    return flujo_data


# Prepara información para operaciones
def limpia_datos(datos, campo):
    try:
        if campo != "id":
            del datos[campo]
    except:
        pass

    return datos

def datos_referencia(campoReferencia, campos_data, datos, datos_tarea):
    # Campo especifico de datos        
    #referencia       = datos.get(campoReferencia, None)
    valor_referencia = datos.get(campoReferencia, None)
    datos            = limpia_datos(datos, campoReferencia)
    datos_tarea["valorReferencia"] = valor_referencia

    # Lista de valores
    valor_datos = {} 
    if len(campos_data.keys()) > 0:        
        eliminar =  campos_data.get("eliminar", True)
        for elemento in campos_data.get("campos", []):
            valor = datos.get(elemento, None)
            valor_datos[elemento] = valor
            if (eliminar == True):
                datos = limpia_datos(datos, elemento)            
    datos_tarea["valor_datos"] = valor_datos

    #elif si es funcion falta
    # datos = funcion(datos)

    return datos_tarea

def carga_referencias(definicion, datos, accion, id_tarea):
    # Tarea de referencias a otras tablas
    referencias = definicion.get("referencias", [])
    for referencia in referencias:  
        externa = referencia.get('externa', None)
        if externa != None:
            # Tipo de operación "relacion" o clase_operacion, ej: terceros
            tipo_operacion  = referencia.get('tipo_operacion',  'relacion')
            clase_operacion = referencia.get('clase_operacion', None)
            if (clase_operacion != None):
                tipo_operacion = clase_operacion
            
            campoReferencia = referencia.get('campoReferencia')
            campos_data     = referencia.get('camposData', {})
            
            # Datos para ejecución posterior
            datos_tarea     = {
                'campoReferencia': campoReferencia,
                'tipo_relacion'  : externa.get('tipo_relacion', 'RELACION'),
                'cardinalidad'   : referencia.get('modo', 'simple'),
                'origen'         : definicion["clase"], 
                'origen_id'      : None,
                'origen_role'    : externa.get('origen_role', 'PADRE'),
                'destino'        : referencia.get('estructuraDestino'), 
                'destino_role'   : externa.get('destino_role', 'HIJO'),
            }            
            # Datos referencia
            datos_tarea = datos_referencia(campoReferencia, campos_data, datos, datos_tarea) 
            
            # Tarea a publicar
            tarea = {
                "tipo"  : tipo_operacion,
                "accion": accion,
                "datos" : datos_tarea
            }              

            globales.carga_tarea(id_tarea, tarea)
    
def carga_archivos(definicion, datos, accion, id_tarea):
    # Tarea de referencias archivos
    archivos = definicion.get("archivos", None)
    if archivos != None:  
        datos_tarea = {
            'tipo_relacion'  : archivos.get('tipo_relacion', 'ANEXOS'),
            'cardinalidad'   : archivos.get('modo', 'simple'),
            'origen'         : definicion["clase"], 
            'origen_id'      : None,
            'origen_role'    : archivos.get('origen_role', 'PADRE'),
            'archivo_id'     : None,
            'cubeta'         : definicion.get("cubeta", "archivos_repositorio")
        }            
        
        # Tarea a publicar
        tarea = {
            "tipo"  : "archivos",
            "accion": accion,
            "datos" : datos_tarea
        }              
        
        globales.carga_tarea(id_tarea, tarea)


# Relaciones, Terceros Archivos 
def publica_tareas(flujo_data):
    estructura = flujo_data["parametros"]["estructura"]
    datos      = flujo_data["parametros"]["datos"]
    accion     = flujo_data["parametros"]["accion"]  
    id_tarea   = flujo_data["parametros"]["id_tarea"]  
    definicion = globales.lee_definicion(estructura)

    # Tarea de referencias a otras tablas
    carga_referencias(definicion, datos, accion, id_tarea)

    # Tareas de archivo
    carga_archivos(definicion, datos, accion, id_tarea)
    
# Prepara datos para relaciones externas a otras tablas
# Anexar archivos, terceros
@task(name="ESTRUCTURA prepara operaciones", trigger=all_successful)
def prepara_operaciones(flujo_data):  
    publica_tareas(flujo_data)
    
    return flujo_data