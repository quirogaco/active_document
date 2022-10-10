#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.utilidades import basicas  
from librerias.datos.sql  import sqalchemy_insertar
from librerias.datos.sql  import sqalchemy_leer
from aplicacion.comunes   import indexar_datos
from aplicacion.especificos.radicados.gestion import logs
 
# Crea registro de gestión
def crea_relacion_gestion(datos):
    sqalchemy_insertar.insertar_registro_estructura("gestor_peticion_relaciones", datos)

# Crea registro de gestión
def crea_registro_gestion(accion, datos={}, archivo=[], id_tarea=""):
    usuario_id     = datos["_usuario_"]["id"]
    dependencia_id = datos["_usuario_"]["dependencia_id"]
    nombre         = datos["_usuario_"]["nombre"]
    comentario     = datos["comentario"]
    detalle        = "CREACIÓN DE BORRADOR INTERNO, POR " + nombre
    # Registro gestión
    data_registro = {
        'creado_por_id'  : usuario_id,
        "responsable_id" : usuario_id,
        "dependencia_id" : dependencia_id,
        "gestion_inicio" : basicas.fechaHora(),
        "peticion_id"    : "*",
        "total_tiempo"   : 0,
        "horas_dias"     : "DIAS",
        "prioridad"      : "MEDIA",
        "rapida"         : "NO",
        "atributos_"     : {
            "interno_borrador": {
                "asunto": comentario
            }
        }
    }
    resultado  = sqalchemy_insertar.insertar_registro_estructura("peticiones", data_registro)
    gestion_id = resultado["id"]
    
    # Crear relación GESTIÓN    
    datos_relacion = {
        'fuente'    : 'BORRADOR',
        'tipo'      : 'INTERNO',
        'origen_id' : basicas.uuidTexto(),
        'relacion'  : 'GENERADOR',
        'gestion_id': gestion_id
    } 
    crea_relacion_gestion(datos_relacion)

    # Indexar estructuras
    indexar_datos.indexar_estructura("peticiones", gestion_id, 0)
    
    # Log de creación registro gestión
    datos_log = {
        "accion"         : "ASIGNAR_RESPONSABLE",
        "destinatario_id": usuario_id,     
        "id"             : gestion_id, 
        "detalle"        : detalle
    }
    logs.log_gestion(datos_log, id_tarea)