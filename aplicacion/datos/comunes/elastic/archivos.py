#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.sql import sqalchemy_tipo_campos as tipos

# Campos archivos
archivos_estructura = {
    "tipoElastic": {
        'tipo'       : 'anidados',
        "propiedades": {
            "creado_por_id"    : tipos.texto(propiedades={"titulo": "Creado por id"}),
            "creado_por_nombre": tipos.clave(propiedades={"titulo": "Creado por"}),                
            "creado_en"        : tipos.texto(propiedades={"titulo": "Creado en"}),
            "actualizado_en"   : tipos.texto(propiedades={"titulo": "Actualizado en"}), 
            "cubeta"           : tipos.texto(propiedades={"titulo": "Cubeta"}), 
            "nombre"           : tipos.texto(propiedades={"titulo": "Nombre"}), 
            "detalle"          : tipos.texto(propiedades={"titulo": "Descripción"}), 
            "ruta"             : tipos.texto(propiedades={"titulo": "Ruta"}), 
            "tipo_archivo"     : tipos.texto(propiedades={"titulo": "Tipo de archivo"}), 
            "tamano"           : tipos.entero(propiedades={"titulo": "Tamaóo"}), 
            "folios"           : tipos.entero(propiedades={"titulo": "Folios"}), 
            "texto_extraido"   : tipos.texto(propiedades={"titulo": "Texto extraido"}),
            'texto'            : tipos.texto(propiedades={"titulo": "Texto indexar"}), 
            "pdf_a"            : tipos.texto(propiedades={"titulo": "PDF/A"}),             
            'id'               : tipos.texto(propiedades={"titulo": "Id archivo"}),
            'version'          : tipos.entero(propiedades={"titulo": "Versión"}),
            'base'             : tipos.entero(propiedades={"titulo": "Archivo base"})
        }
    }
}