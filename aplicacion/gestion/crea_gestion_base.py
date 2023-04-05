#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base         import globales
from librerias.utilidades         import basicas  
from librerias.flujos             import flujos_insertar_sql
from librerias.datos.estructuras  import estructura_operaciones
from librerias.datos.sql          import sqalchemy_modificar, sqalchemy_leer
from aplicacion.gestion.acciones  import acciones_detalle
from aplicacion.trabajadores_base import radicados_celery
from aplicacion.datos.redis       import redis_datos
from aplicacion.trabajadores      import utilidades
from aplicacion.logs              import crea_logs
from aplicacion.comunes           import manejo_archivos
from aplicacion.comunes           import indexar_datos
from .                            import notifica_gestion

def log_gestion(datos={}, id_tarea="", encolar=True):
    datos_tarea = redis_datos.lee_tarea_ejecucion(id_tarea)

    accion = datos["accion"]
    # Log del radicado
    datos_log = {
        "accionante_id"  : datos_tarea['_usuario_']['id'],        
        "destinatario_id": datos['destinatario_id'],     
        "proceso"        : acciones_detalle.acciones[accion]["PROCESO"],
        "fuente"         : "peticiones",
        "fuente_id"      : datos['id'], 
        "accion"         : acciones_detalle.acciones[accion]["ACCION"],  
        "detalle"        : datos['detalle'],
        "estado"         : acciones_detalle.acciones[accion]["ESTADO"],  
        "detalle_estado" : acciones_detalle.acciones[accion]["MENSAJE_ESTADO"]
    }

    if encolar == True:
        radicados_celery.crea_log.apply_async(**utilidades.parametros(
            'radicados', 
            parametros={
                "datos": datos_log
            }
        ))
    else:
        crea_logs.crea_log(datos=datos_log)

# Aactualiza radicado 
def actualiza_radicado(radicado_id, clase_radicado, id_tarea):
    CLASE_RADICADO = globales.lee_clase("gestor_radicados_entrada")
    nuevos_datos   = {
        "id"            : radicado_id,
        "clase_radicado": clase_radicado
    }
    sqalchemy_modificar.modificar_registro("base", CLASE_RADICADO, nuevos_datos)

# Crea regitro de gestión
def crea_registro_gestion(datos, archivos, id_tarea):
    # Dependencia y responsable
    dependencia_id = datos['gestion_dependencia_id']
    dependencia    = sqalchemy_leer.leer_un_registro("dependencias", dependencia_id)
    responsable_id = dependencia["pqrs_id"]
    detalle        = "ASIGNACIÓN POR COMPETENCIA A " + dependencia["pqrs_nombre"] + ", DE " + dependencia["nombre_completo"]
    
    # Petición
    horas_dias   = datos.get("gestion_horas_dias", None)
    total_tiempo = datos.get("gestion_total_tiempo", None)
    peticion_id  = datos["gestion_peticion_id"]
    peticion     = sqalchemy_leer.leer_un_registro("peticiones", peticion_id) 
    
    # Información del radicado
    radicado_id  = datos["id"]

    # Valores definitivos
    if (horas_dias == None):        
        horas_dias = peticion.horas_dias

    if (total_tiempo == None):       
        total_tiempo = peticion.total_tiempo    

    clase_radicado = datos.get("clase_radicado", "PQRS")
    
    # Crear registro GESTIÓN    
    data_registro = {
        'creado_por_id'  : "*",
        'fuente'         : clase_radicado,
        'tipo'           : "ENTRADA",
        'origen_id'      : radicado_id,
        "responsable_id" : responsable_id,
        "dependencia_id" : dependencia_id,
        "gestion_inicio" : basicas.fechaHora(),
        "peticion_id"    : peticion_id,
        "total_tiempo"   : total_tiempo,
        "horas_dias"     : horas_dias,
        "prioridad"      : datos["gestion_prioridad"]
    }
    uuid       = basicas.uuidTexto()
    estructura = "peticiones"
    resultado  = flujos_insertar_sql.ejecutar("base", estructura, data_registro, uuid)
    estructura_operaciones.indexaEstructura(estructura, resultado, True)

    # Crea archivos
    manejo_archivos.manejo("radicados_entrada", "insertar", {"id": radicado_id}, archivos, id_tarea ) #, cubeta = "plantillas")
    indexar_datos.indexar_estructura("radicados_entrada", radicado_id)

    # Log de creación registro gestión
    datos_log = {
        "accion"         : "ASIGNAR_DEPENDENCIA",
        "destinatario_id": responsable_id,     
        "id"             : resultado["datos"]["resultados"]["datos"]["id"], 
        "detalle"        : detalle
    }
    log_gestion(datos_log, id_tarea)

    # Notifica por correo al responsable
    notifica_gestion.notifica(radicado_id, responsable_id)