#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general_campos
from librerias.datos.sql import sqalchemy_tipo_campos as tipos

campos = {
    "tipo_radicado": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Tipo de radicado", "longitud": 64}),
    
    # Sitio de radicación
    "radicado_en_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicado en id", "longitud": 64}),
    "radicado_en_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicado en"}),

    # Usuario que radico
    "radicado_por_id"    : tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicador id",     "longitud": 64}),
    "radicado_por_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Radicador"}),

    # Responde radicado
    "fecha_radicado"    : tipos.fecha_obligatorio(propiedades={"titulo": "Fecha radicado"}),    
    
    "nro_radicado"      : tipos.clave_obligatorio(propiedades={"titulo": "Numero de radicado", "longitud": 64}),    
    "asunto"            : tipos.texto(propiedades={"titulo": "Asunto", "longitud": 2048}),  

    # Trazabilidad
    "dependencias_id": tipos.clave(propiedades={"columna": "no", "titulo": "Dependencias id"}), 
    "funcionarios_id": tipos.clave(propiedades={"columna": "no", "titulo": "Funcionarios id"}),
}
campos.update(base_general_campos.campos)