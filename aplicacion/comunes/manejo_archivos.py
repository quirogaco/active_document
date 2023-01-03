#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint
# REMOTAS
from librerias.ejecucion import llamados

def manejo(
    estructura, 
    accion, 
    datos, 
    archivos, 
    id_tarea, 
    tipo_relacion = "anexos", 
    cubeta = "contenedor.general"
):
    secuencia = [
        {
            "funcion"   : "manejo_archivos_cola",
            "parametros": {
                "estructura"   : estructura,
                "accion"       : accion,
                "datos"        : datos,
                "tarea"        : {},
                "archivos"     : archivos,
                "id_tarea"     : id_tarea,
                "tipo_relacion": tipo_relacion,
                "cubeta"       : cubeta
            }
        }
    ]
    llamados.ejecutar_secuencia(
        secuencia=secuencia, 
        ubicacion="comunes manejo archivos"
    )  

# MANEJO ANEXOS
from librerias.datos.archivos import leer_archivo
from librerias.datos.sql import sqalchemy_filtrar

def buca_anexo_especifico_id(origen_id, tipo_anexo="notificacion"):
    archivos   = []
    # Relaciones
    ordenar = [ [ "descendente", "creado_en_" ] ]
    filtros = [ 
        [ "origen_id", "=", origen_id ], 
        [ "tipo_relacion", "=", tipo_anexo] 
    ]
    relaciones = sqalchemy_filtrar.filtrarOrdena(
        estructura="archivos_relacion", 
        filtros=filtros, 
        ordenamientos=ordenar
    )
    if len(relaciones) > 0:
        # Archivos
        filtros  = [ [ "id", "=", relaciones[0]["archivo_id"] ] ]
        archivos = sqalchemy_filtrar.filtrarOrdena(
            estructura="archivos_electronicos", 
            filtros=filtros, 
            ordenamientos=[]
        )
    
    return archivos

def recupera_anexo_id(origen_id, tipo_anexo="notificacion"):
    anexo_id = ""    
    archivos = buca_anexo_especifico_id(origen_id, tipo_anexo)
    if len(archivos) > 0:
        anexo_id = archivos[0]["id"]

    return anexo_id

def recupera_anexo_especifico_id(origen_id, tipo_anexo="notificacion"):
    nombre_archivo = ""    
    archivos      = buca_anexo_especifico_id(origen_id, tipo_anexo)
    if len(archivos) > 0:
        nombre_archivo = leer_archivo.salva_archivo_minio(archivos[0]["id"]) 

    return nombre_archivo

def recupera_anexo_especifico_radicado(
    nro_radicado, 
    tipo_radicado="ENTRADA", 
    tipo_anexo="notificacion"
):
    nombre_archivo = ""
    if tipo_radicado == "ENTRADA":
        # Informacion del radicado
        filtros   = [ [ "nro_radicado", "=", nro_radicado ] ]
        radicados = sqalchemy_filtrar.filtrarOrdena(
            estructura="radicados_entrada", 
            filtros=filtros, 
            ordenamientos=[]
        )
        if len(radicados) > 0:
            nombre_archivo = recupera_anexo_especifico_id(
                radicados[0]["id"], 
                tipo_anexo
            )

    return nombre_archivo