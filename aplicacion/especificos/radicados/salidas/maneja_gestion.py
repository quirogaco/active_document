#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime, random

from aplicacion.datos.redis import redis_datos
from librerias.datos.sql import (
    sqalchemy_modificar, 
    sqalchemy_leer, 
    sqalchemy_filtrar, 
    sqalchemy_insertar
)
from librerias.datos.elastic import elastic_operaciones

from aplicacion.comunes import indexar_datos
from aplicacion.logs import crea_logs
from aplicacion.especificos.radicados.gestion import logs

# indexa peticion
def indexa_peticion(gestion, peticion_id):
    elastic_operaciones.indexar_registro("peticiones", peticion_id)
    # Actualiza ENTRADA
    if gestion["origen_tipo"] == "ENTRADA":
        indexar_datos.indexar_estructura(
            "radicados_entrada", 
            gestion["origen_id"], 
            retardo=120
        )

# Modifica registro de gestión 
def modifica_peticion(gestion, peticion_id, datos):
    sqalchemy_modificar.modificar_un_registro("peticiones", peticion_id, datos)
    indexa_peticion(gestion, peticion_id)

def actualiza(radicado_datos, peticion_id, id_tarea):
    # Información de la tarea
    datos_tarea = redis_datos.lee_tarea_ejecucion(id_tarea)
    # Trae petición
    gestion = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)
    # Trae radicado Entrada     
    radicado = sqalchemy_leer.leer_un_registro(
        "radicados_entrada", 
        gestion["origen_id"]
    )

    print("")
    print("")
    print("")
    print("......... SALIDA................");
    pprint.pprint(radicado_datos);
    respuesta_tipo = radicado_datos.get("respuesta_tipo", "FINAL")
    medio_notificacion = radicado_datos.get("medio_notificacion", "CORREO")
    atributos_ = gestion["atributos_"]
    if respuesta_tipo == "FINAL":
        estado = "FINALIZADO"
        detalle_estado = "FINALIZADO CON RADICACIÓN DE SALIDA" 
        # Actualiza petición
        atributos_["finalizado"] = {
            "fecha_respuesta": datetime.datetime.now(),        
            "finalizado_comentario": (
                "CONTESTADO CON RADICADO [" + 
                radicado_datos["nro_radicado"] + "] "
            ),
            "finalizado_en": datetime.datetime.now(),        
            "fecha_respuesta" : datetime.datetime.now()
        }
        datos_modificados = {
            "atributos_": atributos_
        }
        modifica_peticion(gestion, peticion_id, datos_modificados)        
    else:
        estado = respuesta_tipo
        detalle_estado = "CONSTESTADO CON RADICACIÓN DE SALIDA - " + estado
        datos_log = {
            "accion": "ASIGNAR_RESPONSABLE",
            "destinatario_id": datos_tarea['_usuario_']['id'],     
            "id": peticion_id, 
            "detalle": (
                "RADICA SALIDA CON NRO [" + 
                radicado_datos["nro_radicado"] + "] "
            )
        }
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)    
        
    # SALIDA -> Log del radicado 
    accionante_id = datos_tarea['_usuario_']['id']
    if (radicado != None):
        datos_log = {
            "accionante_tipo": "USUARIO",      
            "accionante_id": accionante_id,    
            "destinatario_tipo": "",      
            "destinatario_id": "",     
            "proceso": "GESTION",
            "fuente": "radicados_salida",
            "fuente_id": radicado_datos["id"], 
            "accion": "RESPONDER",  
            "detalle": ( 
                "RESPUESTA DE RADICADO CON #: " + 
                radicado_datos["nro_radicado"] + " - " + estado
            ),
            "estado": estado,  
            "detalle_estado": detalle_estado
        }
        crea_logs.crea_log(datos_log)

    # ENTRADA -> Asigna Pdf respuesta 
    ordenamientos = [ [ "descendente", "creado_en_" ] ]
    filtros       = [ 
        [ "tipo_relacion", "=", "respuesta" ], 
        [ "origen_id", "=", radicado_datos["id"] ] 
    ]
    relaciones    = sqalchemy_filtrar.filtrarOrdena(
        estructura="archivos_relacion", 
        filtros=filtros, 
        ordenamientos=ordenamientos
    )
    if len(relaciones) > 0:
        relacion       = relaciones[0]
        datos_relacion = {
            'archivo_id'   : relacion["archivo_id"],
            'cardinalidad' : relacion["cardinalidad"],
            'origen'       : "radicados_entrada",
            'origen_id'    : gestion["origen_id"],
            'origen_role'  : 'padre',
            'tipo_relacion': 'respuesta'
        }
        sqalchemy_insertar.insertar_registro_estructura(
            "archivos_relacion", 
            datos_relacion
        )

    # ENTRADA -> Log del radicado 
    accionante_id   = datos_tarea['_usuario_']['id']
    datos_log = {
        "accionante_tipo": "USUARIO",      
        "accionante_id": accionante_id,    
        "destinatario_tipo": "",      
        "destinatario_id": "",     
        "proceso": "GESTION",
        "fuente": "radicados_entrada",
        "fuente_id": gestion["origen_id"], 
        "accion": "RESPONDER",  
        "detalle": ( 
                "RESPUESTA DE RADICADO CON #: " + 
                radicado_datos["nro_radicado"] + " - " + respuesta_tipo
            ),
        "estado": estado,  
        "detalle_estado": detalle_estado
    }
    crea_logs.crea_log(datos_log)

    indexa_peticion(gestion, peticion_id)
    
    return {} 