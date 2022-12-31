#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

from librerias.utilidades         import basicas  
from librerias.datos.sql          import sqalchemy_insertar
from librerias.datos.estructuras  import estructura_operaciones
from librerias.datos.sql          import sqalchemy_modificar, sqalchemy_leer, sqalchemy_filtrar

from aplicacion.comunes           import manejo_archivos
from aplicacion.comunes           import indexar_datos
from .                            import notifica_gestion, logs
 
# Cambia CLASE DE RADICADO 
def actualiza_radicado(radicado_id, clase_radicado, comentario_traslado, id_tarea):
    # Actualiza datos radicado
    radicado = sqalchemy_leer.leer_un_registro(
        "radicados_entrada", 
        radicado_id
    )
    atributos_ = radicado["atributos_"]
    atributos_["clase_radicado"] = clase_radicado
    nuevos_datos   = {
        "atributos_": atributos_
    }
    sqalchemy_modificar.modificar_un_registro(
        "radicados_entrada", 
        radicado_id, 
        nuevos_datos
    )

    # Log de creación registro gestión
    detalle = comentario_traslado + ", NUEVA CLASE: " + clase_radicado
    datos_log = {
        "accion"         : "CAMBIA_CLASE",
        "proceso"        : "ASIGNACION",
        "estado"         : "RADICADO", 
        "destinatario_id": "",     
        "id"             : radicado_id, 
        "detalle"        : detalle,
        "detalle_estado" : "CAMBIA CLASE RADICADO"
    }
    # Cola de log
    logs.log_radicado_entrada(datos_log, id_tarea)

# Crea registro de gestión
def crea_relacion_gestion(datos):
    sqalchemy_insertar.insertar_registro_estructura(
        "gestor_peticion_relaciones", 
        datos
    )

# Crea registro de gestión
def crea_registro_gestion(datos, archivos, id_tarea):
    clase_radicado = datos.get("clase_radicado", "PQRSD")
    
    # Dependencia y responsable
    peticion_id = datos["gestion_peticion_id"]
    peticion = sqalchemy_leer.leer_un_registro(
        "tipo_peticiones", 
        peticion_id
    )
    if clase_radicado == "TRAMITE":
        dependencia_id = peticion["dependencias_ids"][0]
    else:        
        dependencia_id = datos['gestion_dependencia_id']

    dependencia = sqalchemy_leer.leer_un_registro(
                      "dependencias", 
                      dependencia_id
                   )

    if clase_radicado == "DOCUMENTO":                
        responsable_id = dependencia["archivo_id"]
        responsable_nombre = dependencia["archivo_nombre"]
    else:
        responsable_id = dependencia["pqrs_id"]
        responsable_nombre = dependencia["pqrs_nombre"]

    detalle = (
        "ASIGNACIÓN POR COMPETENCIA A " +  
        responsable_nombre + ", DE " + 
        dependencia["nombre_completo"]
    )    
    horas_dias = datos.get("gestion_horas_dias", None)
    total_tiempo = datos.get("gestion_total_tiempo", None)    
     
    
    # Información del radicado
    radicado_id  = datos["id"]

    # Valores definitivos
    if (horas_dias == None):        
        horas_dias = peticion["horas_dias"]

    if (total_tiempo == None):       
        total_tiempo = peticion["total_tiempo "]   
    
    atributos_     = datos.get("atributos_", {})
    
    # Registro gestión
    data_registro = {
        'creado_por_id' : "*",
        "responsable_id": responsable_id,
        "dependencia_id": dependencia_id,
        "gestion_inicio": basicas.fechaHora(),
        "peticion_id"   : peticion_id,
        "total_tiempo"  : total_tiempo,
        "horas_dias"    : horas_dias,
        "prioridad"     : datos["gestion_prioridad"],
        "rapida"        : "NO",
        "colaborativa"  : "",
        "atributos_"    : atributos_
    }

    resultado  = sqalchemy_insertar.insertar_registro_estructura("peticiones", data_registro)
    gestion_id = resultado["id"]
    
    # Crear relación GESTIóN    
    datos_relacion = {
        'fuente'    : clase_radicado,
        'tipo'      : "ENTRADA",
        'origen_id' : radicado_id,
        'relacion'  : "GENERADOR",
        'gestion_id': gestion_id
    } 
    crea_relacion_gestion(datos_relacion)
    
    # Crea archivos
    manejo_archivos.manejo(
        "radicados_entrada", 
        "insertar", 
        {"id": radicado_id}, 
        archivos, 
        id_tarea 
    )

    # Log de creación registro gestión
    datos_log = {
        "accion"         : "ASIGNAR_DEPENDENCIA",
        "destinatario_id": responsable_id,     
        "id"             : gestion_id, 
        "detalle"        : detalle
    }
    logs.log_gestion(datos_log, id_tarea)

    # Log de resuelto en primera instancia
    resuelto_inmediato = atributos_.get("resuelto_inmediato", "NO")
    if (resuelto_inmediato == "SI"):        
        mensaje = (
            "FINALIZA EN PRIMER CONTACTO LA GESTIÓN - " + 
            atributos_["finalizado"]["finalizado_por_nombre"]
        )
        datos_log = {
            "accion"         : "FINALIZAR_PRIMER_CONTACTO",
            "destinatario_id": None,     
            "id"             : gestion_id, 
            "detalle"        : mensaje
        }
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, retardo=60)

    # Notifica por correo al responsable 
    notifica_gestion.invoca_enviar_notificado_gestion({
        "radicado_id": radicado_id, 
        "responsable_id": responsable_id
    })
   
    
    # Indexar estructuras
    indexar_datos.indexar_estructura("radicados_entrada", radicado_id, 90)
    indexar_datos.indexar_estructura("peticiones", gestion_id, 90)

# Crea COLABORATIVA
def crea_gestion_colaborativa(datos, peticion_id, id_tarea):
    usuario_id     = datos["_usuario_"]["id"]
    nombre         = datos["_usuario_"]["nombre"]
    responsable_id = datos["usuario"]
    comentario     = datos["comentario"]

    # Usuario responsable
    usuario = sqalchemy_leer.leer_un_registro("usuarios", responsable_id)
    dependencia_id = usuario["dependencia_id"]
    
    # Petición original
    peticion = sqalchemy_leer.leer_un_registro("peticiones", peticion_id) 
    
    # Radicado original 
    radicado       = sqalchemy_leer.leer_un_registro(
        "radicados_entrada", 
        peticion["origen_id"]
    )       
    clase_radicado = radicado["clase_radicado"]
    
    # Registro gestión
    data_registro = {
        'creado_por_id' : usuario_id,
        "responsable_id": responsable_id,
        "dependencia_id": dependencia_id,
        "gestion_inicio": basicas.fechaHora(),
        "peticion_id"   : peticion["peticion_id"],
        "borrador_id"   : peticion["borrador_id"],
        "total_tiempo"  : 0,
        "horas_dias"    : "NO",
        "prioridad"     : "NORMAL",
        "rapida"        : "NO",
        "colaborativa"  : peticion_id
    }
    resultado  = sqalchemy_insertar.insertar_registro_estructura(
        "peticiones", 
        data_registro
    )
    gestion_id = resultado["id"]
    
    # Crear relación GESTIóN    
    datos_relacion = {
        'fuente'    : clase_radicado,
        'tipo'      : "ENTRADA",
        'origen_id' : peticion["origen_id"],
        'relacion'  : "COOPERATIVA",
        'gestion_id': gestion_id
    } 
    crea_relacion_gestion(datos_relacion)
    
    # Log de creación registro gestión
    datos_log = {
        "accion"         : "ASIGNAR_DEPENDENCIA",
        "destinatario_id": responsable_id,     
        "id"             : peticion_id, 
        "detalle"        : ("SOLICITA COLABORATIVA: " + comentario)
    }
    logs.log_gestion(datos_log, id_tarea)

    # Indexar estructuras
    indexar_datos.indexar_estructura(
        "radicados_entrada", 
        peticion["origen_id"], 
        90
    )
    indexar_datos.indexar_estructura("peticiones", gestion_id, 90)