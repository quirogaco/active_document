#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Base general con atributos basicos
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.base                   import globales

campos = {
    "origen"            : tipos.clave_obligatorio(propiedades={"titulo": "Origen", "longitud": 60}),  
    "dependencia_id"    : tipos.clave_obligatorio(propiedades={"titulo": "Dependencia id", "longitud": 60}), 
    "dependencia_nombre": tipos.clave_obligatorio(propiedades={"columna": "no", "titulo": "Dependencia nombre", "longitud": 60}),      
    "detalle"           : tipos.texto(propiedades={"titulo": "Descripción", "longitud": 512}), 
    "destinatarios"     : tipos.json(propiedades={"titulo": "Listado Destinatarios", "defecto": 'json'}), 
}

indexamiento = {}