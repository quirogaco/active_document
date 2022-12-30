#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
import os
import tempfile
import base64
import builtins

from librerias.documentos.plantillas import word_plantilla
from librerias.documentos.conversion import conversion
from librerias.datos.sql             import sqalchemy_filtrar 
from librerias.datos.archivos        import leer_archivo
from librerias.utilidades            import basicas  

def genera_pdf_plantilla(plantilla_base, archivo_destino="", datos={}, imagen=True):
    if archivo_destino == "":
        archivo_destino = tempfile.gettempdir() + os.sep + basicas.uuidTexto() + ".docx"
    
    nombre_archivo  = word_plantilla.mezcla_plantilla_archivos(plantilla_base, archivo_destino, datos)  
    nombre_byte     = nombre_archivo.encode('ascii')
    nombre_64       = base64.b64encode( nombre_byte )
    nombre_64_texto = str(nombre_64, 'utf-8')
    url = "http://" + str(builtins._appAnfitrion) + ":" + str(builtins._segundoPuerto) + '/entregar_archivo_base64/' + nombre_64_texto    
    parametros = {
        "filetype"  : "docx",
        "title"     : "convertido",
        "url"       : url
    }
            
    ruta_destino  = conversion.a_pdfa(str(builtins._appServicios), "80", parametros)  
    jpg_ruta      = ""
    if (imagen == True):  
        jpg_ruta = conversion.a_jpg(str(builtins._appServicios), "80", parametros)   

    return ruta_destino, jpg_ruta      

############
# ENTRADAS #
############
def datos_radicado():
    keys = [
        "radicado_en_id",
        "radicado_en_nombre",
        "radicado_por_id",
        "radicado_por_nombre",
        "clase_radicado",
        "medio_radicado",
        "canal_radicado_id",
        "canal_radicado_nombre",
        "canal_medio",
        "tipo_web",
        "nro_radicado",
        "fecha_radicado", 
        "medio_notificacion",
        "asunto",
        "fecha_documento",
        "radicado_remitente",
        "empresa_mensajeria_id",
        "empresa_mensajeria_nombre",   
        "numero_guia",
        "nro_folios",
        "anexos",
        "entidad_traslada",  
        "persona_traslada",
        "reserva",
        "tercero_id" ,  
        "tercero_clase",
        "tercero_tipo_tercero_id", 
        "tercero_tipo_tercero_nombre",
        "tercero_tipo_identificacion_id",
        "tercero_tipo_identificacion_nombre",  
        "tercero_nro_identificacion",
        "tercero_razon_social",
        "tercero_cargo",
        "tercero_nombres",         
        "tercero_apellidos",           
        "tercero_correo_electronico",
        "tercero_direccion",
        "tercero_codigo_postal",
        "tercero_telefono",
        "tercero_telefono_movil",
        "tercero_fax", 
        "tercero_ciudad_id",
        "tercero_ciudad_nombre",  
        "tercero_nombre_completo",
        "archivos_nombres"
    ]

def recuperar_archivo_plantilla(plantilla):
    nombre_archivo = ""
    # Recupera registro de la plantilla
    ordenar    = [ [ "descendente", "creado_en_" ] ]
    filtros    = [ [ "id", "=", plantilla ] ]
    plantillas = sqalchemy_filtrar.filtrarOrdena(estructura="plantillas", filtros=filtros, ordenamientos=ordenar)
    # Si existen plantillas 
    if len(plantillas) > 0:
        # Recupera registro de relación a archivos
        plantilla_id = plantillas[0]["id"]            
        filtros      = [ [ "origen", "=", "plantillas" ], [ "origen_id", "=", plantilla_id ] ]
        relaciones   = sqalchemy_filtrar.filtrarOrdena(estructura="archivos_relacion", filtros=filtros, ordenamientos=ordenar)        
        # Si existen relaciones 
        if len(relaciones) > 0:
            archivo_id     = relaciones[0]['archivo_id']    
            # Recupera archivo de minio
            nombre_archivo = leer_archivo.salva_archivo_minio(archivo_id) 

    return nombre_archivo

def crear_pdf_plantilla(plantilla, datos, id_tarea):
    print("")
    print("")
    print("DATOS")
    print("")
    print("")
    pprint.pprint(datos)
    nombre_archivo  = recuperar_archivo_plantilla(plantilla)    
    ruta_destino, jpg_ruta = genera_pdf_plantilla(nombre_archivo, "", datos)

    return ruta_destino, jpg_ruta  

def crear_pdf_archivo(archivo_id, datos, id_tarea):
    nombre_archivo         = leer_archivo.salva_archivo_minio(archivo_id)    
    ruta_destino, jpg_ruta = genera_pdf_plantilla(nombre_archivo, "", datos)

    return ruta_destino, jpg_ruta 

###########
# SALIDAS #
###########
def recuperar_archivo_borrador(borrador_id):
    nombre_archivo = ""
    # Recupera registro borrador
    ordenar    = [ [ "descendente", "creado_en_" ] ]
    filtros    = [ [ "tipo_relacion", "=", "borrador" ], [ "origen", "=", "peticiones" ], [ "archivo_id", "=", borrador_id ] ]
    relaciones = sqalchemy_filtrar.filtrarOrdena(estructura="archivos_relacion", filtros=filtros, ordenamientos=ordenar)        
    # Si existen relaciones 
    print("recuperar_archivo_borrador:", relaciones)
    if len(relaciones) > 0:
        archivo_id     = relaciones[0]['archivo_id']    
        # Recupera archivo de minio
        nombre_archivo = leer_archivo.salva_archivo_minio(archivo_id) 

    return nombre_archivo

def crear_pdf_borrador(borrador_id, datos, id_tarea):
    nombre_archivo         = recuperar_archivo_borrador(borrador_id)
    ruta_destino, jpg_ruta = genera_pdf_plantilla(nombre_archivo, "", datos)

    return ruta_destino, jpg_ruta  
