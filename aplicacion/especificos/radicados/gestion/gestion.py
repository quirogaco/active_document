#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, datetime

from librerias.datos.sql import (
    sqalchemy_modificar, 
    sqalchemy_leer, 
    sqalchemy_comunes, 
    sqalchemy_insertar
)
from aplicacion.datos.redis import redis_datos

from librerias.utilidades import basicas  
from librerias.datos.sql  import sqalchemy_filtrar
from librerias.datos.base import globales
from librerias.datos.elastic import elastic_operaciones
from aplicacion.comunes import indexar_datos
from . import crea_gestion_base

##########################
#  RUTINAS DE VENTANILLA #
##########################    
def asigna_ventanilla(accion, datos={}, archivos=[], id_tarea=""):
    datos_ventanilla = datos["datos"]    
    radicado_id = datos_ventanilla["id"]
    es_pqrs = datos_ventanilla.get("es_pqrs", None)
    if es_pqrs == "PQRSD":
        crea_gestion_base.actualiza_radicado(
            radicado_id, 
            "PQRSD", 
            "", 
            id_tarea
        )        
    else:
        crea_gestion_base.crea_registro_gestion(
            datos_ventanilla, 
            archivos, 
            id_tarea
        )

    # Deberia ser un flush corto solo un campo JCR
    elastic_operaciones.indexar_registro("radicados_entrada", radicado_id)
    resultado  =  {
        "accion": accion,
        "estado": "",
        "mensaje": "",
        "datos": {}
    }

    return resultado


####################
#  RUTINAS DE PQRS #
####################
# Asignado por formulario web o traslado ventanilla
def pqrs_gestion(estructura, accion, datos, tarea, archivos, id_tarea):    
    resultado = {}
    datos = datos["datos"]  
    radicado_id = datos["id"]
    es_ventanilla = datos.get("es_ventanilla", "NO")
    if es_ventanilla == "NO":
        # Formulario asigna no tiene esta opcion
        datos["resuelto_inmediato"] = "NO" 
        crea_gestion_base.crea_registro_gestion(datos, archivos, id_tarea)
    else:
        crea_gestion_base.actualiza_radicado(
            radicado_id, 
            "PQRSD", 
            id_tarea
        )

    # Indexar radicado de nuevo
    estructura_operaciones_sql.indexar_registro_SQL(
        "base", 
        "radicados_entrada", 
        radicado_id, 
        True
    )

    return resultado

# Radicado por formulario completo
# Radicado
def asigna_pqrs(accion, datos={}, archivos=[], id_tarea=""):   
    datos_pqrs = datos["datos"]    
    radicado_id = datos_pqrs["id"]
    es_ventanilla = datos_pqrs.get("es_ventanilla", None)
    comentario_traslado = datos_pqrs["comentario_traslado"]
    if es_ventanilla == "SI":
        crea_gestion_base.actualiza_radicado(
            radicado_id, 
            "DOCUMENTO", 
            comentario_traslado, 
            id_tarea
        )        
    else:
        resuelto_inmediato = datos_pqrs.get("resuelto_inmediato", "NO")
        if (resuelto_inmediato == "SI"):
            datos_pqrs["gestion_horas_dias"] = "DIAS"
            datos_pqrs["gestion_total_tiempo"] = 0
            datos_pqrs["atributos_"] = {'resuelto_inmediato': 'SI'}
            datos_pqrs["atributos_"]["finalizado"] = {
                "finalizado_por_id"    : datos['_usuario_']['id'],
                "finalizado_por_nombre": datos['_usuario_']['nombre'],
                "finalizado_en"        : datetime.datetime.now(),
                "finalizado_comentario": (
                    "RESUELTO EN PRIMER CONTACTO, " + 
                    datos_pqrs.get("comentario_traslado", "")
                )
            } 

        crea_gestion_base.crea_registro_gestion(datos_pqrs, archivos, id_tarea)

    # Indexar radicado de nuevo, inmediato para refrescar
    # Deberia ser un flush corto solo un campo JCR
    elastic_operaciones.indexar_registro("radicados_entrada", radicado_id)
    resultado  =  {
        "accion": accion,
        "estado": "",
        "mensaje": "",
        "datos": {}
    }
    
    return resultado


# Gestion radicado interno
def asigna_interno(accion, datos={}, archivos=[], id_tarea=""):   
    datos_interno = datos
    radicado_id = datos_interno["id"]
    datos_interno["clase_radicado"] = "INTERNO"
    datos_interno["gestion_horas_dias"] = "DIAS"
    datos_interno["gestion_total_tiempo"] = 0
    crea_gestion_base.crea_registro_gestion(datos_interno, archivos, id_tarea)

    # Indexar radicado de nuevo, inmediato para refrescar
    # Deberia ser un flush corto solo un campo JCR
    elastic_operaciones.indexar_registro("radicados_interno", radicado_id)
    resultado  =  {
        "accion": accion,
        "estado": "",
        "mensaje": "",
        "datos": {}
    }
    
    return resultado

from aplicacion.logs import crea_logs
# Asigna radicado de reposición
def asigna_reposicion(accion, datos={}, repone_id="", id_tarea=""):   
    sesion = sqalchemy_comunes.nuevaSesion("base")   

    # Información de la tarea
    datos_tarea = redis_datos.lee_tarea_ejecucion(id_tarea)
  
    # ENTRADA que repone
    repone = sqalchemy_leer.leer_un_registro("radicados_entrada", repone_id)

    # PETICIÓN que repone
    GESTION_CLASE = globales.lee_clase("gestor_peticiones")
    GESTION_RELACIONES_CLASE = globales.lee_clase("gestor_peticion_relaciones")
    relacion = sesion.query(GESTION_RELACIONES_CLASE).filter( 
        GESTION_RELACIONES_CLASE.origen_id == repone_id 
    ).first()
    if relacion != None:
        peticion  = sesion.query(GESTION_CLASE).filter( 
            relacion.gestion_id == GESTION_CLASE.id 
        ).first()
        if peticion != None:
            atributos_ = peticion.atributos_           
            atributos_["finalizado"] = {
                "finalizado_por_id": "",
                "finalizado_por_nombre": "",
                "finalizado_en": None,
                "finalizado_comentario": "",
            } 
            repone_datos = {
                "atributos_": atributos_,
                "gestion_inicio": basicas.fechaHora(),
            } 
            sqalchemy_modificar.modificar_un_registro(
                "peticiones", 
                peticion.id, 
                repone_datos
            )

            ##########################
            # RADICADO QUE SE REPONE #
            ##########################
            # ENTRADA -> Asigna Pdf del radicado de reposición a radicado que se repone
            ordenamientos = [ [ "descendente", "creado_en_" ] ]
            filtros = [ 
                [ "tipo_relacion", "=", "notificacion" ], 
                [ "origen_id", "=", datos["id"] ] 
            ]
            relaciones = sqalchemy_filtrar.filtrarOrdena(
                estructura="archivos_relacion", 
                filtros=filtros, 
                ordenamientos=ordenamientos
            )
            if len(relaciones) > 0:
                relacion = relaciones[0]
                datos_relacion = {
                    'archivo_id': relacion["archivo_id"],
                    'cardinalidad': relacion["cardinalidad"],
                    'origen': "radicados_entrada",
                    'origen_id': repone_id,
                    'origen_role': 'padre',
                    'tipo_relacion': 'repone'
                }
                sqalchemy_insertar.insertar_registro_estructura(
                    "archivos_relacion", 
                    datos_relacion
                )

            # REPUESTO -> Log del radicado que se repone
            accionante_id = datos_tarea['_usuario_']['id']
            repuesto = sqalchemy_leer.leer_un_registro(
                "radicados_entrada", 
                repone_id
            )
            datos_log = {
                "accionante_tipo": "USUARIO",      
                "accionante_id": accionante_id,    
                "destinatario_tipo": "",      
                "destinatario_id": "",     
                "proceso": "RADICADO",
                "fuente": "radicados_entrada",
                "fuente_id": repone_id, 
                "accion": "REPONER",  
                "detalle": ( 
                    "REPOSICIÓN CON RADICADO #: " + 
                    datos["nro_radicado"]
                ),
                "estado": "ACTIVADO",  
                "detalle_estado": "REPOSICIÓN RADICADO",  
            }
            crea_logs.crea_log(datos_log)
            indexar_datos.indexar_estructura("radicados_entrada", repone_id)

            #######################
            # RADICADO QUE REPONE #
            #######################
            # REPONE -> Log del radicado que repone                        
            datos_log = {
                "accionante_tipo": "USUARIO",      
                "accionante_id": accionante_id,    
                "destinatario_tipo": "",      
                "destinatario_id": "",     
                "proceso": "RADICADO",
                "fuente": "radicados_entrada",
                "fuente_id": datos["id"], 
                "accion": "REPONER",  
                "detalle": ( 
                    "REPONE RADICADO CON #: " + 
                    repuesto["nro_radicado"]
                ),
                "estado": "ACTIVADO",  
                "detalle_estado": "REPONE RADICADO",  
            }
            crea_logs.crea_log(datos_log)
            indexar_datos.indexar_estructura("radicados_entrada", datos["id"])

            # Indexa gestión
            indexar_datos.indexar_estructura("peticiones", peticion.id)

    sesion.close()

    return {}