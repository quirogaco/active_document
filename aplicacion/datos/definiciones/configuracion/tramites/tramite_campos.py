#!/usr/bin/python
# -*- coding: utf-8 -*-

# Base general con atributos basicos
from librerias.datos.sql import sqalchemy_tipo_campos as tipos

def notifica_id(r_):
    flujo       = r_.flujo 
    notifica_id = flujo.get("notifica_id", [])

    return notifica_id

def bpmn(r_):
    flujo = r_.flujo 
    bpmn  = flujo.get("bpmn", {}).get("xml", "")

    return bpmn

campos = {
    # Acción realizada
    "nombre"           : tipos.clave(propiedades={"titulo": "Accion", "longitud": 64, "reporte": "SI"}), 
    "detalle"          : tipos.texto(propiedades={"titulo": "Detalle", "longitud": 512, "reporte": "SI"}),  

    "total_tiempo"      : tipos.entero(propiedades={"titulo": "Tiempo total", "reporte": "SI"}), 
    "alertar_tiempo"    : tipos.texto(propiedades={"titulo": "Tiempo para alertar ", "reporte": "SI"}),      
    "alertar_porcentaje": tipos.texto(propiedades={"titulo": "Porcentaje para alertar", "reporte": "SI"}),       
    "horas_dias"        : tipos.texto_obligatorio(propiedades={"titulo": "Horas ó dias", "longitud": 32, "reporte": "SI"}),       
    "tipo_tiempo"       : tipos.texto_obligatorio(propiedades={"titulo": "Calculo de tiempo en", "longitud": 32, "reporte": "SI"}),  

    # formulario
    "formulario_id"    : tipos.clave(propiedades={"titulo": "Formulario asociado", "longitud": 64}),  
    "formulario_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Formulario  nombre", "longitud": 250, "reporte": "SI"}), 

    # Bpmn - Definicion
    # version_bpmn = "2.0"
    # notifica_id = lista a notificar
    # bpmn        = contenido xml
    "flujo"      : tipos.json(propiedades={"titulo": "Definición bpmn del flujo", "defecto": 'json'}), 
    "notifica_id": tipos.clave(propiedades={"columna": "no", "titulo": "Notificar id's", "propiedad": notifica_id}),   
    "bpmn"       : tipos.texto(propiedades={"columna": "no", "titulo": "Bpmn", "propiedad": bpmn})   
}