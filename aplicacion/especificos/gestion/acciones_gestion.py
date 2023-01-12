#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint, datetime, builtins, base64

from librerias.datos.base    import globales
from librerias.datos.sql     import sqalchemy_leer
from librerias.datos.sql     import sqalchemy_comunes
from aplicacion.especificos.gestion.acciones  import acciones_detalle
from aplicacion.especificos.radicados.gestion import logs

from . import crea_gestion_salida
from . import crea_gestion_interno
from . import comunes_gestion
from . import colaborativa_gestion

# Asigna responsable gestión
def asignar_responsable(accion, datos={}, archivo=[], id_tarea=""):    
    print("")
    print("asignar_responsable:")
    pprint.pprint(datos)
    print("")
    print("")    
    peticiones_id = datos["peticiones"]
    anterior_id   = datos["_usuario_"]["id"]
    usuario_id    = datos["usuario"]
    comentario    = datos["comentario"]
    rapida        = datos.get("rapida", "NO")
    usuario       = sqalchemy_leer.leer_un_registro("usuarios", usuario_id)
    
    for peticion_id in peticiones_id:        
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,            
            "responsable_id": usuario["id"],
            "dependencia_id": usuario["dependencia_id"],
            "rapida"        : rapida
        }
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)
        
        # Log de acción
        mensaje = (
            "RESPONSABLE " + usuario["nombre"] + ", DE " + 
            usuario["dependencia_nombre_completo"] + ", " + comentario
        )
        if (rapida == "SI"):
            mensaje = (
                "RESPONSABLE RESPUESTA RAPIDA" + usuario["nombre"] + ", DE " + 
                usuario["dependencia_nombre_completo"] + ", " + comentario
            )

        datos_log = {
            "accion"         : accion,
            "destinatario_id": usuario["id"],     
            "id"             : peticion_id, 
            "detalle"        : mensaje
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
    
    return {}

# Devuelve a asistencial dependencia
def devolver_dependencia_asignadora(accion, datos={}, archivo=[], id_tarea=""): 
    GESTION_CLASE = globales.lee_clase("gestor_peticiones")
    GESTION_RELACIONES_CLASE = globales.lee_clase("gestor_peticion_relaciones")
    sesion = sqalchemy_comunes.nuevaSesion("base")    

    # DEPENDENCIA pqrs
    usuario_id = datos["_usuario_"]["id"]
    anterior_id = "*"   
    dependencia_id = "*" 
    peticiones_id = datos["peticiones"]
    comentario = datos["comentario"]
    for peticion_id in peticiones_id:
        # Relacion
        relacion = sesion.query(GESTION_RELACIONES_CLASE).filter( 
            GESTION_RELACIONES_CLASE.gestion_id == peticion_id 
        ).first()
        relacion.estado_ = "DEVUELTO"
        sesion.commit()        

        # Modifica registro
        datos_modificados = {
            "anterior_id": anterior_id,      
            "responsable_id": usuario_id,
            "dependencia_id": dependencia_id,
            "estado_": "DEVUELTO"
        }
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = {
            "accion": accion,
            "destinatario_id": "",     
            "id": peticion_id, 
            "detalle": comentario
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
        
    sesion.close()

    return {}

# Traslada a otra dependencia
def trasladar_dependencia(accion, datos={}, archivo=[], id_tarea=""):
    dependencia_id = datos["dependencia"]
    dependencia    = sqalchemy_leer.leer_un_registro(
        "dependencias", 
        dependencia_id
    )
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
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": usuario_id,     
            "id"             : peticion_id, 
            "detalle"        : (
                "SE TRASLADA A " + dependencia["pqrs_nombre"] + ", DE " + 
                dependencia["nombre_completo"] + " - " + comentario
            )
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
        
    return {}

# Envia a visto bueno
def enviar_visto_bueno(accion, datos={}, archivo=[], id_tarea=""):
    dependencia_id = datos["_usuario_"]["dependencia_id"]
    dependencia    = sqalchemy_leer.leer_un_registro(
        "dependencias", 
        dependencia_id
    )
    anterior_id    = datos["_usuario_"]["id"]
    responsable_id = dependencia["jefe_id"]   
    responsable    = sqalchemy_leer.leer_un_registro("usuarios", responsable_id) 
    peticiones_id  = datos["peticiones"]
    comentario     = datos["comentario"]
    print("enviar_visto_bueno-0:")
    for peticion_id in peticiones_id:
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,            
            "responsable_id": responsable_id,
            "dependencia_id": dependencia_id
        }
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)
        print("enviar_visto_bueno-1:")

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": responsable_id,     
            "id"             : peticion_id, 
            "detalle"        : (
                "SE ENVIA A VISTO BUENO " + responsable["nombre"] + ", DE " + 
                responsable["dependencia_nombre_completo"] + " - " + comentario
            )
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
        print("enviar_visto_bueno-0:")
    
    return {}

# Jefe devuelve a revision del profesional
def devolver_revision(accion, datos={}, archivo=[], id_tarea=""):
    dependencia_id = datos["_usuario_"]["dependencia_id"]
    anterior_id    = datos["_usuario_"]["id"]
    peticiones_id  = datos["peticiones"]
    comentario     = datos["comentario"]
    for peticion_id in peticiones_id:
        gestion = sqalchemy_leer.leer_un_registro(
            "peticiones", 
            peticion_id
        )     
        responsable_id = gestion["anterior_id"]   
        responsable = sqalchemy_leer.leer_un_registro(
            "usuarios", 
            responsable_id
        ) 
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,            
            "responsable_id": responsable_id,
            "dependencia_id": dependencia_id
        }
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": responsable_id,     
            "id"             : peticion_id, 
            "detalle"        : (
                "SE DEVUELVE A REVISIÓN " + responsable["nombre"] + ", DE " + 
                responsable["dependencia_nombre_completo"] + " - " + comentario
            )
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
    
    return {}

# Funcionario devuelve a asignador de la dependencia
def devolver_asignador(accion, datos={}, archivo=[], id_tarea=""):  
    dependencia_id = datos["_usuario_"]["dependencia_id"]
    anterior_id    = datos["_usuario_"]["id"]
    peticiones_id  = datos["peticiones"]
    comentario     = datos["comentario"]    
    for peticion_id in peticiones_id:
        # Gestion
        gestion = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)     
        responsable_id = gestion["anterior_id"]   
        responsable = sqalchemy_leer.leer_un_registro("usuarios", responsable_id) 
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,            
            "responsable_id": responsable_id,
            "dependencia_id": dependencia_id,
            "dependencia_id": dependencia_id,
        }
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = {
            "accion"         : accion,
            "destinatario_id": responsable_id,     
            "id"             : peticion_id, 
            "detalle": (
                "SE DEVUELVE A ASIGANDOR " + responsable["nombre"] + ", DE " + 
                responsable["dependencia_nombre_completo"] + " - " + comentario
            )
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)

    return {}

# Jefe aprueba para radicar
def aprobar_radicar(accion, datos={}, archivo=[], id_tarea=""):
    dependencia_id = datos["_usuario_"]["dependencia_id"]
    anterior_id    = datos["_usuario_"]["id"]
    peticiones_id  = datos["peticiones"]
    comentario     = datos["comentario"]
    for peticion_id in peticiones_id:
        gestion = sqalchemy_leer.leer_un_registro("peticiones", peticion_id)     
        responsable_id = gestion["anterior_id"]   
        responsable = sqalchemy_leer.leer_un_registro("usuarios", responsable_id) 
        # Modifica registro
        datos_modificados = {
            "anterior_id"   : anterior_id,            
            "responsable_id": responsable_id,
            "dependencia_id": dependencia_id
        }
        comunes_gestion.modifica_peticion(peticion_id, datos_modificados)

        # Log de acción
        datos_log = { 
            "accion"         : accion,
            "destinatario_id": responsable_id,     
            "id"             : peticion_id, 
            "detalle"        : (
                "SE APRUEBA PARA RADICACIÓN " + responsable["nombre"] + 
                ", DE "+ responsable["dependencia_nombre_completo"] + " - " + 
                comentario
            )
        }
        # Log indexa la peticion
        logs.log_gestion(datos=datos_log, id_tarea=id_tarea, encolar=False)
    
    return {}

from . import archivos_gestion
from . import generales_gestion
from . import firma_gestion

acciones_funcion = {
    "ANEXA_ARCHIVO"        : comunes_gestion.anexar_gestion,
    "CREA_COMENTARIO"      : generales_gestion.crea_comentario,
    "ASIGNA_TRD"           : generales_gestion.asigna_trd, 
    "ASIGNAR_RESPONSABLE"  : asignar_responsable,
    "DEVOLVER_DEPENDENCIA" : devolver_dependencia_asignadora, # DEVUELVE DEPENDENCIA ASIGNADORA PQRS, VENTANILLA
    "TRASLADAR_DEPENDENCIA": trasladar_dependencia,
    "ENVIAR_VISTO_BUENO"   : enviar_visto_bueno,
    "DEVOLVER_REVISION"    : devolver_revision,
    "APROBAR_RADICAR"      : aprobar_radicar,
    "FINALIZAR_MANUAL"     : generales_gestion.finalizar_manual,
    "SELECCION_PLANTILLA"  : archivos_gestion.seleccion_plantilla,
    "DEVOLVER_ASIGNADOR"   : devolver_asignador, # SIGANDO DEPENDENCIA
    "PDF_BORRADOR"         : archivos_gestion.pdf_borrador,
    "CREA_COLABORATIVA"    : colaborativa_gestion.crea_colaborativa,
    
    # SALIDAS
    "CREA_BORRADOR_SALIDA" : crea_gestion_salida.crea_registro_gestion,
    # INTERNOS
    "CREA_BORRADOR_INTERNO": crea_gestion_interno.crea_registro_gestion,

    # FIRMA DIGITAL
    "FIRMA_BORRADOR"       : firma_gestion.firmar
}

def acciones_ejecuta(datos={}, archivos=[], id_tarea=""):
    accion = datos["accion"]
    acciones = acciones_detalle.acciones_entrada[accion]
    funcion  = acciones_funcion[accion]
    resultado = funcion(accion, datos, archivos, id_tarea)
   
    return resultado