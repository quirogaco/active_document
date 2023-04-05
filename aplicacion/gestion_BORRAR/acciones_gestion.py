#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.sql         import sqalchemy_modificar, sqalchemy_leer
from librerias.datos.sql         import sqalchemy_filtrar 
from aplicacion.gestion.acciones import acciones_detalle
from librerias.datos.elastic     import elastic_operaciones
from aplicacion.comunes          import indexar_datos
from .                           import crea_gestion_base

def modifica_peticion(peticion_id, datos):
    sqalchemy_modificar.modificar_un_registro("peticiones", peticion_id, datos)

def asignar_responsable(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    peticiones_id = datos["peticiones"]
    anterior_id   = datos["_usuario_"]["id"]
    usuario_id    = datos["usuario"]
    comentario    = datos["comentario"]
    usuario       = sqalchemy_leer.leer_un_registro("usuarios", usuario_id)
    for peticion_id in peticiones_id:
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,            
            "responsable_id": usuario["id"],
            "dependencia_id": usuario["dependencia_id"]
        }
        modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": usuario["id"],     
            "id"             : peticion_id, 
            "detalle"        : "ASIGNACIÓN RESPONSABLE " + usuario["nombre"] + ", DE " + usuario["dependencia_nombre_completo"]
        }
        # Log indexa la peticion
        crea_gestion_base.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)

        return {}

def devolver_dependencia(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    # DEPENDENCIA pqrs
    dependencia_id = "481bd2a9-de03-11eb-8320-006073b60f8a"
    dependencia    = sqalchemy_leer.leer_un_registro("dependencias", dependencia_id)
    anterior_id    = datos["_usuario_"]["id"]    
    usuario_id     = dependencia["pqrs_id"]
    peticiones_id  = datos["peticiones"]
    comentario     = datos["comentario"]
    for peticion_id in peticiones_id:
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,     
            "responsable_id": usuario_id,
            "dependencia_id": dependencia_id
        }
        modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": usuario_id,     
            "id"             : peticion_id, 
            "detalle"        : "DEVOLUCIÓN DEPENDENCIA ASIGNADORA " + dependencia["pqrs_nombre"] + ", DE " + dependencia["nombre_completo"]
        }
        # Log indexa la peticion
        crea_gestion_base.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
        
    return {}

def trasladar_dependencia(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["dependencia"]
    dependencia    = sqalchemy_leer.leer_un_registro("dependencias", dependencia_id)
    anterior_id    = datos["_usuario_"]["id"]    
    usuario_id     = dependencia["pqrs_id"]
    peticiones_id  = datos["peticiones"]
    comentario     = datos["comentario"]
    for peticion_id in peticiones_id:
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,     
            "responsable_id": usuario_id,
            "dependencia_id": dependencia_id
        }
        modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": usuario_id,     
            "id"             : peticion_id, 
            "detalle"        : "SE TRASLADA A " + dependencia["pqrs_nombre"] + ", DE " + dependencia["nombre_completo"]
        }
        # Log indexa la peticion
        crea_gestion_base.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
        
    return {}

def enviar_visto_bueno(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["_usuario_"]["dependencia_id"]
    dependencia    = sqalchemy_leer.leer_un_registro("dependencias", dependencia_id)
    anterior_id    = datos["_usuario_"]["id"]
    responsable_id = dependencia["jefe_id"]   
    responsable    = sqalchemy_leer.leer_un_registro("usuarios", responsable_id) 
    peticiones_id  = datos["peticiones"]
    comentario     = datos["comentario"]
    for peticion_id in peticiones_id:
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,            
            "responsable_id": responsable_id,
            "dependencia_id": dependencia_id
        }
        modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": responsable_id,     
            "id"             : peticion_id, 
            "detalle"        : "SE ENVIA A VISTO BUENO " + responsable["nombre"] + ", DE " + responsable["dependencia_nombre_completo"]
        }
        # Log indexa la peticion
        crea_gestion_base.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
    
    return {}

def devolver_revision(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["_usuario_"]["dependencia_id"]
    anterior_id    = datos["_usuario_"]["id"]
    peticiones_id  = datos["peticiones"]
    comentario     = datos["comentario"]
    for peticion_id in peticiones_id:
        gestion        = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)     
        responsable_id = gestion["anterior_id"]   
        responsable    = sqalchemy_leer.leer_un_registro("usuarios", responsable_id) 
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,            
            "responsable_id": responsable_id,
            "dependencia_id": dependencia_id
        }
        modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": responsable_id,     
            "id"             : peticion_id, 
            "detalle"        : "SE DEVUELVE A REVISIÓN " + responsable["nombre"] + ", DE " + responsable["dependencia_nombre_completo"]
        }
        # Log indexa la peticion
        crea_gestion_base.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
    
    return {}

def aprobar_radicar(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["_usuario_"]["dependencia_id"]
    anterior_id    = datos["_usuario_"]["id"]
    peticiones_id  = datos["peticiones"]
    comentario     = datos["comentario"]
    for peticion_id in peticiones_id:
        gestion        = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)     
        responsable_id = gestion["anterior_id"]   
        responsable    = sqalchemy_leer.leer_un_registro("usuarios", responsable_id) 
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,            
            "responsable_id": responsable_id,
            "dependencia_id": dependencia_id
        }
        modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": responsable_id,     
            "id"             : peticion_id, 
            "detalle"        : "SE APRUEBA PARA RADICACIÓN " + responsable["nombre"] + ", DE " + responsable["dependencia_nombre_completo"]
        }
        # Log indexa la peticion
        crea_gestion_base.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
    
    return {}

#######################
# MANEJO DE PLANTILLA #
#######################

from aplicacion.comunes       import manejo_plantillas, manejo_archivos
from librerias.datos.archivos import leer_archivo
from aplicacion.archivos      import archivo_operaciones

def recuperar_archivo_plantilla(plantilla_id):
    nombre_archivo = ""
    filtros        = [ [ "origen", "=", "plantillas" ], [ "origen_id", "=", plantilla_id ] ]
    relaciones     = sqalchemy_filtrar.filtrarOrdena(estructura="archivos_relacion", filtros=filtros, ordenamientos=[])
    # Si existen relaciones 
    if len(relaciones) > 0:
        archivo_id     = relaciones[0]['archivo_id']            
        # Recupera archivo de minio
        nombre_archivo = leer_archivo.salva_archivo_minio(archivo_id) 

    return nombre_archivo

def seleccion_plantilla(accion, datos={}, archivo=[], acciones={}, id_tarea=""):
    dependencia_id = datos["_usuario_"]["dependencia_id"]
    usuario_id     = datos["_usuario_"]["id"]
    peticiones_id  = datos["peticiones"]
    plantilla_id   = datos["plantilla"]

    print("seleccion_plantilla:")
    pprint.pprint(datos)
    for peticion_id in peticiones_id:
        gestion        = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)     
        responsable    = sqalchemy_leer.leer_un_registro("usuarios", usuario_id) 
        radicado       = sqalchemy_leer.leer_un_registro("radicados_entrada", gestion["origen_id"]) 

        # Manejo del borrador
        nombre_archivo = recuperar_archivo_plantilla(plantilla_id)
        archivos = [{
            "nombre_completo": nombre_archivo,
            "nombre"         : ("borrador_" + peticion_id + ".docx")
        }]
        print("nombre_archivo:", nombre_archivo)   
        archivo_operaciones.manejo_archivos( 
            "peticiones", 
            "insertar",
            {"id":peticion_id},
            {},
            archivos, 
            id_tarea,
            "borrador",
            "borradores"
        )
        archivo_id = manejo_archivos.recupera_anexo_id(peticion_id, "borrador")
        print("archivo_id:", archivo_id)

        # Actualiza peticion
        datos_modificados = {
            "borrador_id"   : archivo_id
        }
        modifica_peticion(peticion_id, datos_modificados)
        indexar_datos.indexar_estructura("peticiones", peticion_id)

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": usuario_id,     
            "id"             : peticion_id, 
            "detalle"        : "CREA BORRADOR DE RESPUESTA, " + responsable["nombre"] + ", DE " + responsable["dependencia_nombre_completo"]
        }
        # Log indexa la peticion
        crea_gestion_base.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)

    return {"archivo_id": archivo_id}

acciones_funcion = {
    "ASIGNAR_RESPONSABLE"  : asignar_responsable,
    "DEVOLVER_DEPENDENCIA" : devolver_dependencia,
    "TRASLADAR_DEPENDENCIA": trasladar_dependencia,
    "ENVIAR_VISTO_BUENO"   : enviar_visto_bueno,
    "DEVOLVER_REVISION"    : devolver_revision,
    "APROBAR_RADICAR"      : aprobar_radicar,
    "SELECCION_PLANTILLA"  : seleccion_plantilla
}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]
    print("")
    print("")
    print("------------------------------------------------")
    print('/acciones_ejecuta:') 
    print('datos:')
    pprint.pprint(datos)   
    print('archivos:', archivos)
    acciones = acciones_detalle.acciones[accion]
    funcion  = acciones_funcion[accion]
    pprint.pprint(acciones)
    resultado = funcion(accion, datos, archivos, acciones, id_tarea)
    print("------------------------------------------------")
    print("")
    print("")

    return resultado
