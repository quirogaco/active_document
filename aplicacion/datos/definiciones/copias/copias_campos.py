#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from librerias.datos.sql import sqalchemy_tipo_campos as tipos
from librerias.datos.sql import sqalchemy_leer

def radicado_atributo(self, atributo):    
    valor = "" 

    if self.radicado_tipo == "ENTRADA":
        entrada = sqalchemy_leer.leer_un_registro("radicados_entrada", self.radicado_id)  
        if entrada != None:
            valor = entrada[atributo]

    if self.radicado_tipo == "SALIDA":
        salida = sqalchemy_leer.leer_un_registro("radicados_salida", self.radicado_id)  
        if salida != None:
            valor = salida[atributo]
    
    if self.radicado_tipo == "INTERNO":
        interno = sqalchemy_leer.leer_un_registro("radicados_interno", self.radicado_id)  
        if interno != None:
            valor = interno[atributo]

    return valor

def radicado_nro(self):        
    return radicado_atributo(self, "nro_radicado")

def radicado_asunto(self): 
    return radicado_atributo(self, "asunto")

def destinatario_nombre(self):
    nombre = "" 

    if self.destinatario_tipo == "USUARIO":
        usuario = sqalchemy_leer.leer_un_registro("usuarios", self.destinatario_id)  
        if usuario != None:
            nombre = usuario['nombre']

    if self.destinatario_tipo == "TERCERO":
        tercero = sqalchemy_leer.leer_un_registro("terceros", self.destinatario_id)  
        if tercero != None:
            nombre = tercero['nombre_completo']

    if self.destinatario_tipo == "GRUPO":
        grupo = sqalchemy_leer.leer_un_registro("grupo_usuarios", self.destinatario_id)  
        if grupo != None:
            nombre = grupo['nombre']

    return nombre

campos = {
    # RADICADO
    "radicado_tipo"  : tipos.clave(propiedades={"titulo": "Radicado tipo", "longitud": 64}),  
    "radicado_id"    : tipos.clave(propiedades={"titulo": "Radicado id", "longitud": 64}),  
    "radicado_nro"   : tipos.texto(propiedades={"titulo": "Radicado numero", "longitud": 250, "reporte": "SI"}),   
    "radicado_asunto": tipos.texto(propiedades={"titulo": "Radicado asunto", "longitud": 250, "reporte": "SI"}),   
    
    # Destinatario
    "destinatario_tipo"  : tipos.clave(propiedades={"titulo": "Destinatario tipo", "longitud": 64}),  
    "destinatario_id"    : tipos.clave(propiedades={"titulo": "Destinatario id", "longitud": 64}),  
    "destinatario_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Destinatario nombre", "longitud": 250, "reporte": "SI", "propiedad": destinatario_nombre}),   
        
    # Estado
    "estado"             : tipos.clave(propiedades={"titulo": "Estado", "longitud": 64, "reporte": "SI", "defecto":"ASIGNADO"})
}