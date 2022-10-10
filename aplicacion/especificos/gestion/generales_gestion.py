#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, builtins, base64

from librerias.datos.base    import globales
from librerias.datos.sql     import sqalchemy_modificar, sqalchemy_leer
from librerias.datos.sql     import sqalchemy_filtrar 
from librerias.datos.sql     import sqalchemy_comunes
from librerias.datos.elastic import elastic_operaciones
from librerias.utilidades    import basicas 

from aplicacion.comunes                       import indexar_datos
from aplicacion.especificos.archivos_acciones import acciones
from aplicacion.especificos.gestion.acciones  import acciones_detalle
from aplicacion.especificos.radicados.gestion import logs
from librerias.documentos.conversion          import conversion

from . import comunes_gestion

def peticion_real(peticion_id):
    peticion = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)   
    if (peticion["colaborativa"] not in [None, ""]):
        peticion_id = peticion["colaborativa"]

    return peticion_id

# Guarda comentario
def crea_comentario(accion, datos={}, archivo=[], id_tarea=""):  
    # Deine petición
    peticiones_id = datos["peticiones"]
    peticion_id   = peticion_real(peticiones_id[0])  
    peticiones_id = [peticion_id]

    # Gestión
    usuario_id    = datos["_usuario_"]["id"]
    nombre        = datos["_usuario_"]["nombre"]
    comentario    = datos["comentario"]
    usuario       = sqalchemy_leer.leer_un_registro("usuarios", usuario_id)
    
    # Crea anotación
    gestion         = sqalchemy_leer.leer_un_registro("peticiones", peticiones_id[0])
    atributos_      = gestion["atributos_"]
    anotaciones     = atributos_.get("anotaciones", [])
    anotacion_datos = {
        "anotacion": comentario,
        "usuario"  : nombre,
        "fecha"    : datetime.datetime.now()
    } 
    anotaciones.append(anotacion_datos)
    atributos_["anotaciones"] = anotaciones
    
    for peticion_id in peticiones_id:        
        # Modifica registro
        datos_modificados = {
            "atributos_": atributos_
        }
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)
        
        # Log de acción
        mensaje = "CREA ANOTACIÓN " + usuario["nombre"] + ", " + comentario
        datos_log = {
            "accion"         : accion,
            "destinatario_id": None,     
            "id"             : peticion_id, 
            "detalle"        : mensaje
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
    
    return {}

# Asigna TRD a documento
def asigna_trd(accion, datos={}, archivo=[], id_tarea=""):  
    peticiones_id   = datos["peticiones"]
    usuario_id      = datos["_usuario_"]["id"]
    nombre          = datos["_usuario_"]["nombre"]
    expediente      = datos["expediente"]
    tipo_documental = datos["tipo_documental"]
    usuario         = sqalchemy_leer.leer_un_registro("usuarios", usuario_id)
    
    # Asigna TRD
    gestion         = sqalchemy_leer.leer_un_registro("peticiones", peticiones_id[0])
    atributos_      = gestion["atributos_"]
    trd_datos       = {
        "expediente"     : expediente,
        "tipo_documental": tipo_documental
    } 
    atributos_["trd"] = trd_datos
    
    for peticion_id in peticiones_id:        
        # Modifica registro
        datos_modificados = {
            "atributos_": atributos_
        }
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)
        
        # Log de acción
        mensaje = "ASIGNA EXPEDIENTE Y TIPO DOCUMENTAL (TRD)" + usuario["nombre"]
        datos_log = {
            "accion"         : accion,
            "destinatario_id": None,     
            "id"             : peticion_id, 
            "detalle"        : mensaje
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
    
    return {}

# Finalización manual de gestion
def finalizar_manual(accion, datos={}, archivo=[], id_tarea=""):  
    usuario_id    = datos["_usuario_"]["id"]
    nombre        = datos["_usuario_"]["nombre"]
    usuario       = sqalchemy_leer.leer_un_registro("usuarios", usuario_id)
    peticiones_id = datos["peticiones"]
    comentario    = datos["comentario"]    

    # Finaliza
    gestion         = sqalchemy_leer.leer_un_registro("peticiones", peticiones_id[0])
    atributos_      = gestion["atributos_"]
    finaliza_datos  = {
        "finalizado_por_id"    : usuario_id,
        "finalizado_por_nombre": nombre,
        "finalizado_en"        : datetime.datetime.now(),
        "finalizado_comentario": comentario,
    } 
    atributos_["finalizado"] = finaliza_datos
    
    for peticion_id in peticiones_id:        
        # Modifica registro
        datos_modificados = {
            "atributos_": atributos_
        }
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)
        
        # Log de acción
        mensaje = "FINALIZA MANUALMENTE LA GESTIÓN" + usuario["nombre"]
        datos_log = {
            "accion"         : accion,
            "destinatario_id": None,     
            "id"             : peticion_id, 
            "detalle"        : mensaje
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
    
    return {}