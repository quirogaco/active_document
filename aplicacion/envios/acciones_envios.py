#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

from fastapi.responses import FileResponse

from librerias.datos.base import globales 
from librerias.datos.sql import sqalchemy_modificar, sqalchemy_comunes, sqalchemy_leer, sqalchemy_insertar, sqalchemy_borrar
from librerias.datos.elastic import elastic_operaciones

def crear_registro_envio(accion, datos={}):
    datos = datos["datos"]
    datos_item = {
        "radicado_id"      : datos["radicado_id"],  
        "nro_radicado"     : datos["nro_radicado"],   
        "destinatario"     : datos["destinatario"],   
        "tipo"             : "ORIGINAL",         
        "direccion"        : datos["direccion"],   
        "ubicacion"        : datos["ubicacion"],
        "planilla_id"      : '',   
        "estado"           : "CREADO",
        "guia_envio"       : datos["guia_envio"],   
        "guia_devolucion"  : "",
        "motivo_devolucion": ""
    }    
    resultado = sqalchemy_insertar.insertar_registro_estructura("envios_fisicos", datos_item)
    resultado["accion"]     = accion
    resultado["id_temporal"] = datos["id_temporal"]
    
    return resultado

def modificar_registro_envio(accion, datos={}):
    datos       = datos["datos"]
    registro_id = datos["id"]
    datos_item = {
        "direccion"        : datos["direccion"],   
        "ubicacion"        : datos["ubicacion"],
        "guia_envio"       : datos["guia_envio"],
        "guia_devolucion"  : datos["guia_devolucion"],
        "motivo_devolucion": datos["motivo_devolucion"] 
    }    
    resultado = sqalchemy_modificar.modificar_un_registro("envios_fisicos", registro_id, datos_item)
    resultado["accion"] = accion

    return resultado
    
def borrar_registro_envio(accion, datos={}):
    envio_id   = datos["datos"]
    resultado  = sqalchemy_borrar.borrar_un_registro("envios_fisicos", envio_id)
    resultado["accion"] = accion
    
    return resultado

def leer_registros_creados():
    definicion = globales.lee_definicion("envios_fisicos")
    CLASE      = globales.lee_clase(definicion["clase"])
    sesion     = sqalchemy_comunes.nuevaSesion("base")   
    registros  = sesion.query(CLASE).filter( CLASE.estado == "CREADO" )
    elementos  = []
    for registro in registros: 
        normalizado = sqalchemy_comunes.retornar_datos(registro, "diccionario") 
        elementos.append( normalizado )                
    sesion.close()

    return elementos

def leer_registros_planilla(planilla_id):
    definicion = globales.lee_definicion("envios_fisicos")
    CLASE      = globales.lee_clase(definicion["clase"])
    sesion     = sqalchemy_comunes.nuevaSesion("base")   
    #registros  = sesion.query(CLASE).filter( CLASE.planilla_id == planilla_id )
    registros  = sesion.query(CLASE).all()
    elementos  = []
    for registro in registros: 
        normalizado = sqalchemy_comunes.retornar_datos(registro, "diccionario") 
        elementos.append( normalizado )                
    sesion.close()

    return elementos

def cargar_registros_envio(accion, datos={}):
    elementos = leer_registros_creados()
    resultado = {
        "registros": elementos,
        "accion"   : accion
    }

    return resultado

def crear_planilla_envio(accion, datos={}):
    datos_item = {
        "detalle": datos["datos"]
    }    
    planilla = sqalchemy_insertar.insertar_registro_estructura("planilla_envios_fisicos", datos_item)
    elastic_operaciones.indexar_registro("planilla_envios_fisicos", planilla["id"])

    elementos = leer_registros_creados()    
    for elemento in elementos:
        registro_id = elemento["id"]
        datos_item = {
            "planilla_id": planilla["id"],   
            "estado"     : "PENDIENTE",
        }    
        resultado = sqalchemy_modificar.modificar_un_registro("envios_fisicos", registro_id, datos_item)


    resultado = {
        "accion": accion
    }

    return resultado

def cargar_envios(accion, datos={}):
    #planilla_id = datos["datos"]
    planilla_id = None
    registros   = leer_registros_planilla(planilla_id)
    
    return {
        "accion"   : accion,
        "registros": registros
    }

def imprimir_planilla_envio(accion, datos={}):
    planilla_id = datos["datos"][0]
    envios      = leer_registros_planilla(planilla_id)
    planilla    = sqalchemy_leer.leer_un_registro("planilla_envios_fisicos", planilla_id)

    print("planilla_id", planilla_id)
    pprint.pprint(planilla)

    #print("resgistros planilla")
    #pprint.pprint(envios)

    ruta_base = ("D:/gestor_2021_vite/temporal/entrada.docx").replace("\\", "/")

    return FileResponse(ruta_base)

from librerias.email                 import email
def enviar_correo(accion, datos={}):
    salida_id = datos["datos"]
    salida    = sqalchemy_leer.leer_un_registro("radicados_salida", salida_id)
    correo    = salida["tercero_correo_electronico"]
    print("salida_id", salida_id)
    pprint.pprint(correo)

    de        = "quirogaco@gmail.com"
    clave     = "sreojrjewsjkxnml"
    #para      = ["quirogaco@gmail.com", "fabigonz@esap.edu.co", "viveros.60@gmail.com"]
    para      = [correo, "fabigonz@esap.edu.co", "carmlago@esap.edu.co"]
    asunto    = "Notificaci�n de radicado "     
    archivos  = ["D:/gestor_2021_vite/temporal/S-2021-4010.pdf"]

    direccion_smtp = "smtp.gmail.com"
    puerto_smtp    = 587

    #mensaje = email.mensaje_texto(
    mensaje = email.mensaje_imagen(
        de, 
        para, 
        asunto, 
        "D:/gestor_2021_vite/temporal/logo.jpg", 
        archivos=archivos
    )

    email.enviar_mensaje_smtp(
        mensaje, 
        de, 
        clave, 
        para, 
        direccion_smtp, 
        puerto_smtp
    )

    return {}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]
    print("")
    print("")
    print("------------------------------------------------")
    print('/acciones_ejecuta:', accion, id_tarea) 
    print('datos:')
    pprint.pprint(datos)   
    resultado = {}

    if accion == "crear":
        resultado = crear_registro_envio(accion, datos)

    if accion == "modificar":
        resultado = modificar_registro_envio(accion, datos)

    if accion == "borrar":
        resultado = borrar_registro_envio(accion, datos)

    if accion == "cargar":
        resultado = cargar_registros_envio(accion, datos)

    if accion == "crear_planilla":
        resultado = crear_planilla_envio(accion, datos)

    if accion == "cargar_envios":
        resultado = cargar_envios(accion, datos)

    if accion == "imprimir_planilla":
        resultado = imprimir_planilla_envio(accion, datos)

    if accion == "enviar_correo":
        resultado = enviar_correo(accion, datos)

    return resultado
