#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, builtins, base64

from librerias.datos.sql     import sqalchemy_leer
from librerias.datos.sql     import sqalchemy_filtrar 
from aplicacion.especificos.radicados.gestion import logs
from librerias.documentos.conversion          import conversion

from . import crea_gestion_salida
from . import comunes_gestion

####################################
# MANEJO DE PLANTILLA Y BORRADORES #
####################################
from aplicacion.comunes       import manejo_plantillas, manejo_archivos
from librerias.datos.archivos import leer_archivo
from aplicacion.archivos      import archivo_operaciones

# Recupera archivo plantilla de borrador
def recuperar_archivo_plantilla(plantilla_id):
    nombre_archivo = ""
    filtros        = [ 
        [ "origen", "=", "plantillas" ], 
        [ "origen_id", "=", plantilla_id ] 
    ]
    relaciones     = sqalchemy_filtrar.filtrarOrdena(
        estructura="archivos_relacion", 
        filtros=filtros, 
        ordenamientos=[]
    )
    # Si existen relaciones 
    if len(relaciones) > 0:
        archivo_id     = relaciones[0]['archivo_id']            
        # Recupera archivo de minio
        nombre_archivo = leer_archivo.salva_archivo_minio(archivo_id) 

    return nombre_archivo

# Busca plantilla
def seleccion_plantilla(accion, datos={}, archivo=[], id_tarea=""):
    dependencia_id = datos["_usuario_"]["dependencia_id"]
    usuario_id = datos["_usuario_"]["id"]
    peticiones_id = datos["peticiones"]
    plantilla_id = datos["plantilla"]

    for peticion_id in peticiones_id:
        gestion = sqalchemy_leer.leer_un_registro(
            "peticiones", 
            peticion_id
        )     
        responsable = sqalchemy_leer.leer_un_registro(
            "usuarios", 
            usuario_id
        ) 
        radicado = sqalchemy_leer.leer_un_registro(
            "radicados_entrada", 
            gestion["origen_id"]
        ) 

        # Manejo del borrador
        nombre_archivo = recuperar_archivo_plantilla(plantilla_id)
        archivos = [{
            "nombre_completo": nombre_archivo,
            "nombre"         : ("borrador_" + peticion_id + ".docx")
        }]
        
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
        archivo_id = manejo_archivos.recupera_anexo_id(
            peticion_id, 
            "borrador"
        )
        
        # Actualiza peticion
        datos_modificados = {
            "borrador_id"   : archivo_id
        }
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)
        
        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": usuario_id,     
            "id"             : peticion_id, 
            "detalle"        : (
                "CREA BORRADOR DE RESPUESTA, " + responsable["nombre"] + 
                ", DE " + responsable["dependencia_nombre_completo"]
            )
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)

    return {"archivo_id": archivo_id}


# Recupera archivo borrador gestion
def recuperar_archivo_borrador_gestion(borrador_id):
    nombre_archivo = ""
    filtros = [ 
        [ "tipo_relacion", "=", "borrador" ], 
        [ "origen_id", "=", borrador_id ] 
    ]
    relaciones = sqalchemy_filtrar.filtrarOrdena(
        estructura="archivos_relacion", 
        filtros=filtros, 
        ordenamientos=[]
    )
    # Si existen relaciones 
    if len(relaciones) > 0:
        archivo_id = relaciones[0]['archivo_id']            
        # Recupera archivo de minio
        nombre_archivo = leer_archivo.salva_archivo_minio(archivo_id) 
        nombre_byte = nombre_archivo.encode('ascii')
        nombre_64 = base64.b64encode( nombre_byte )
        nombre_64_texto = str(nombre_64, 'utf-8')
        url = (
            builtins._appServiciosType + "://" + 
            str(builtins._appAnfitrion) + ":" + 
            str(builtins._appPuerto) +
            '/entregar_archivo_base64/' + nombre_64_texto
        )   
        parametros = {
            "filetype"  : "docx",
            "title"     : "convertido",
            "url"       : url
        }                
        nombre_archivo = conversion.a_pdfa(
        str(builtins._appServicios), 
        str(builtins._appServiciosPuerto), 
        parametros=parametros, 
        servicio=str(builtins._appServiciosType)
    )  

    return nombre_archivo

# Genera pdf del borrador
def pdf_borrador(accion, datos={}, archivo=[], id_tarea=""):
    peticion_id = datos["peticion"]    
    gestion     = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)     

    # Manejo del borrador
    nombre_archivo  = recuperar_archivo_borrador_gestion(peticion_id)
    nombre_byte     = nombre_archivo.encode('ascii')
    nombre_64       = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')
    
    return {"nombre_archivo": nombre_64_texto}