#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint, datetime, random 

from librerias.datos.base   import globales
from librerias.datos.sql    import sqalchemy_leer, sqalchemy_filtrar
from aplicacion.datos.redis import redis_datos

def pre_procesa(estructura, operacion, datos, id_tarea):
    """
    print("")
    print("--------------------------------------------------------")    
    print("pre_procesa")
    pprint.pprint(datos)
    """

    # Datos que vienen de formulario de asignacion de PQRS
    tema_dependencia_id    = datos.get("tema_dependencia_id")
    subtema_dependencia_id = datos.get("subtema_dependencia_id")    
    # Datos que vienen de formulario de radicacion PQRS
    if tema_dependencia_id in ["", None]:
        tema_dependencia_id    = datos.get("tema_dependencia_radica_id")
    if subtema_dependencia_id in ["", None]:
        subtema_dependencia_id = datos.get("subtema_dependencia_radica_id")
    datos["tema_dependencia_id"]    = tema_dependencia_id
    datos["subtema_dependencia_id"] = subtema_dependencia_id

    radicado = "E-2022-" + str(random.randint(0, 10000))
    datos["nro_radicado"]   = radicado
    datos["fecha_radicado"] = datetime.datetime.now()
    """
    print("--------------------------------------------------------")
    print("")
    """

    # validar fecha del documento y valores basicos

    return datos
globales.carga_procesamiento("radicados_entrada", "pre_estructura", pre_procesa)
#globales.carga_procesamiento("radicados_entrada", "post_estructura", post_procesa)

#############################
# PROCESOS FINALES RADICADO #
#############################

from aplicacion.trabajadores import utilidades
from aplicacion.trabajadores_base import radicados_celery

def responsable_lee(dependencia_id):
    dependencia = sqalchemy_leer.leer_un_registro("dependencias", dependencia_id)
    responsable = "" if ( dependencia is None ) else dependencia["pqrs_id"]
    
    return responsable
    
# Crea gestion y notifica    
def gestion(datos, id_tarea):
    # Crea registro gestion
    radicados_celery.ventanilla_gestion.apply_async(**utilidades.parametros(
        'radicados', 
        parametros={
            "datos"   : datos, 
            "archivos": [],
            "id_tarea": id_tarea
        }
    ))

# Crea logs radicado y gestion   
from aplicacion.especificos.gestion.acciones import acciones_detalle
def log_radicado(datos, id_tarea):
    datos_tarea = redis_datos.lee_tarea_ejecucion(id_tarea)
    
    # Log del radicado
    datos_log = {
        "accionante_id"  : datos_tarea['_usuario_']['id'],        
        "destinatario_id": responsable_lee(datos['gestion_dependencia_id']),      
        "proceso"        : acciones_detalle.acciones["RADICAR"]["PROCESO"],
        "fuente"         : "radicados_entrada",
        "fuente_id"      : datos['id'], 
        "accion"         : acciones_detalle.acciones["RADICAR"]["ACCION"],  
        "detalle"        : ( "RADICACION ENTRADA, CON #: " + datos["nro_radicado"] + " - " + datos["clase_radicado"]),
        "estado"         : acciones_detalle.acciones["RADICAR"]["ESTADO"],  
        "detalle_estado" : acciones_detalle.acciones["RADICAR"]["MENSAJE_ESTADO"]
    }
    radicados_celery.crea_log.apply_async(**utilidades.parametros(
        'radicados', 
        parametros={
            "datos": datos_log
        }
    ))

from . import pdf_notifica

def ultima_procesa(estructura, operacion, datos, tarea, archivos, id_tarea):
    # Recuperar registro creado es neceario datos no trae informacion completa
    filtros   = [ [ "id", "=", datos["id"] ] ]
    radicados = sqalchemy_filtrar.filtrarOrdena(estructura="radicados_entrada", filtros=filtros, ordenamientos=[])
    datos     = radicados[0]

    # Genera pdf del radicado y notifica por correo
    pdf_notifica.pdf_notificacion(datos, id_tarea)

    # Gestion del radicado    
    medio_radicado = datos.get("medio_radicado", None)    
    # Cuando es WEB llega a servicio al ciudadano y debe ser enrutado manualmente        
    if medio_radicado != "WEB": # "WEB", "VENTANILLA"
        gestion(datos, id_tarea)
        # Log de radicacion
        log_radicado(datos, id_tarea)
    
    return datos
globales.carga_procesamiento("radicados_entrada", "ultima_estructura", ultima_procesa)