#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Definiciones sql
from librerias.datos.sql                 import sqalchemy_declarativa_base as dbase

# Clases
from librerias.datos.base                import globales 

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general

# Clase de datos, basica
class GLOBAL_ARCHIVOS_ELECTRONICOS(base_general.DB_BASE_GENERAL, globales.CLASE_BASE_SQL):
    # Serializar esos campos a diccionario
    __serialization__ = dbase.serializa_base([
        'cubeta',
        'nombre',
        'detalle',
        'ruta',  
        'tipo_archivo',
        'tamano',
        'folios',
        'texto_extraido',
        'pdf_a',
        'base',
        'creado_por_id',
        'creado_por_nombre'
    ])

    # Campos fijos de la tabla
    __basicos__ = [
        'cubeta',
        'nombre',
        'detalle',
        'ruta',  
        'tipo_archivo',
        'tamano',
        'folios',
        'texto_extraido',
        'pdf_a',
        'base',
        'creado_por_id',
        'creado_por_nombre'
    ]

    # Creador id
    creado_por_id  = dbase.Column( dbase.Unicode(64), index=True, nullable=True, default="")
    # Atributo de MINIO
    cubeta         = dbase.Column( dbase.Unicode(1024), index=True, nullable=False, default="*")
    # Nombre del archivo, objeto para MINIO
    nombre         = dbase.Column( dbase.Unicode(1024), index=True, nullable=False)
    # Detalle
    detalle        = dbase.Column( dbase.Unicode(1024), index=True, nullable=False, default="ANEXO")
    # Ruta del archivo
    ruta           = dbase.Column( dbase.Unicode(1024), index=True, nullable=True)
    # Tipo pdf, docx
    tipo_archivo   = dbase.Column( dbase.Unicode(32),   index=True)
    # Tamano del archivo
    tamano         = dbase.Column( dbase.Integer,   index=True)
    # Folios
    folios         = dbase.Column( dbase.Integer,   index=True)
    # Texto extraido
    texto_extraido = dbase.Column( dbase.Unicode(32), index=True, default="NO")
    # Convertido a PDF/A
    pdf_a          = dbase.Column( dbase.Unicode(32), index=True, default="NO")
    # Archivo base, ej. Es el PDF del radicado
    base           = dbase.Column( dbase.Unicode(32), index=True, default="NO")

    @property
    def _completo_(self):
        return dict(self.to_dict(5))

globales.carga_clase("global_base_archivo_electronico", GLOBAL_ARCHIVOS_ELECTRONICOS)