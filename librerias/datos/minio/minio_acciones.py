#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, io
from librerias.datos.base  import globales

def crea_cubeta(bucket_nombre):
    conexion  = globales.lee_conexion_minio()

    resultado = None
    existe    = conexion.bucket_exists(bucket_nombre)
    if not existe:
        resultado = conexion.make_bucket(bucket_nombre)

    return resultado

def cargar_objeto_buffer(bucket_nombre, objeto_nombre, archivo_data):
    conexion  = globales.lee_conexion_minio()

    bucket_nombre = bucket_nombre.lower()
    objeto_nombre = objeto_nombre.lower()
    resultado     = None    
    crea_cubeta(bucket_nombre)
    
    # Tamaño
    #archivo_data.file.seek(0, os.SEEK_END)
    #tamano        = archivo_data.file.tell()
    tamano        = 1024
    #archivo_data.file.seek(0)    
    try:
        accion = conexion.put_object(
            bucket_nombre, 
            objeto_nombre,
            archivo_data, 
            tamano
        )
    except Exception as e:
        print("")
        print("..........................")
        print("cargar_objeto_buffer:", str(e))
        print("..........................")
        print("")

    resultado = {
        "accion": accion,
        "tamano": tamano
    } 

    return resultado

def cargar_objeto(bucket_nombre, objeto_nombre, archivo_nombre):
    conexion  = globales.lee_conexion_minio()

    bucket_nombre = bucket_nombre.lower()
    objeto_nombre = objeto_nombre.lower()
    crea_cubeta(bucket_nombre)
    resultado = None
    with open(archivo_nombre, 'rb') as archivo_data:
        archivo_stat = os.stat(archivo_nombre)
        accion = conexion.put_object(
            bucket_nombre, 
            objeto_nombre,
            archivo_data, 
            archivo_stat.st_size
        )

        resultado = {
            "accion": accion,
            "tamano": archivo_stat.st_size
        } 

    return resultado

def leer_objeto_buffer(bucket_nombre, objeto_nombre, buffer):
    conexion      = globales.lee_conexion_minio()
    bucket_nombre = bucket_nombre.lower()
    objeto_nombre = objeto_nombre.lower()    
    longitud      = 0
    datos         = conexion.get_object(bucket_nombre, objeto_nombre)
    for dato in datos.stream(32*1024):
        longitud += len(dato)            
        buffer.write(dato)    

    return longitud

def leer_objeto_archivo(bucket_nombre, objeto_nombre, archivo_nombre):
    bucket_nombre = bucket_nombre.lower()
    objeto_nombre = objeto_nombre.lower()    

    buffer = io.BytesIO()    
    leer_objeto_buffer(bucket_nombre, objeto_nombre, buffer)
    with open(archivo_nombre, "wb") as f:
        f.write(buffer.getbuffer())
    buffer.close()

def atributos_objeto(bucket_nombre, objeto_nombre):
    conexion  = globales.lee_conexion_minio()

    bucket_nombre = bucket_nombre.lower()
    objeto_nombre = objeto_nombre.lower()
    resultado     = conexion.stat_object(bucket_nombre, objeto_nombre)
    
    return resultado