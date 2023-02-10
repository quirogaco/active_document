#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
from sqlalchemy import desc

from librerias.datos.sql  import sqalchemy_filtrar
from librerias.datos.base import globales

def tipo_radicado(r_):
    return "INTERNO"


def gestion_asignada_peticion(sesion, r_):
    campos = {
        #"gestion_id"                : "id",
        # Responsable
        "gestion_responsable_id"    : "responsable_id",
        "gestion_responsable_nombre": "responsable_nombre",
        
        # Dependencia responsable            
        "gestion_dependencia_id"    : "dependencia_id",
        "gestion_dependencia_nombre": "dependencia_nombre",
        
        # Petición
        "gestion_peticion_id"    : "peticion_id",
        "gestion_peticion_nombre": "peticion_nombre",
        
        # Terminos de respuesta basicos            
        "gestion_horas_dias"  : "horas_dias",
        "gestion_total_tiempo": "total_tiempo",
        "gestion_prioridad"   : "prioridad",
        
        # Estado, vencimiento
        "gestion_inicio"  : "gestion_inicio",
        "gestion_vence_en": "vence_en",
        "gestion_estado"  : "estado_gestion",
        "gestion_etapa"   : "etapa_gestion",
        "gestion_estado_vencimiento": "estado_vencimiento"
    }
    # Valores por defecto
    for label, valor in campos.items():
        setattr(r_, label, None)
    setattr(r_, "gestion_relacion", None)

    # Valores de gestion    
    gestion_id = [] 
    asignada = "NO"
    GESTION_CLASE = globales.lee_clase("gestor_peticiones")
    GESTION_RELACIONES_CLASE = globales.lee_clase("gestor_peticion_relaciones")
    relaciones = sesion.query(GESTION_RELACIONES_CLASE).filter( GESTION_RELACIONES_CLASE.origen_id == r_.id ). \
                    order_by( desc( GESTION_RELACIONES_CLASE.creado_en_) ).all()
    for relacion in relaciones:
        setattr(r_, "gestion_relacion", relacion.estado_)
        if relacion is not None: # and relacion.estado_ == "ACTIVO": # estado_ -> DEVUELTO, cuando se regresa a servicio ciudadano o ventanilla
            peticion = sesion.query(GESTION_CLASE).filter( relacion.gestion_id == GESTION_CLASE.id ).first()
            if peticion != None:
                atributos_ = getattr(r_, "atributos_", {})                    
                gestion_id.append(peticion.id) # id de gestion
                if relacion.estado_ == "ACTIVO": # si esta asigando para filtrar por pendientes de asignacion
                    asignada = "SI"                                 
                for label_radicado, label_gestion in campos.items():
                    valor = getattr(peticion, label_gestion)
                    atributos_[label_radicado] = valor
                    setattr(r_, label_radicado, valor)
                #setattr(r_, "label_radicado", label_radicado)
    
    setattr(r_, "gestion_id", gestion_id)
    setattr(r_, "gestion_asignada_peticion", asignada)

#####################
# FIRMA ELECTRONICA #
#####################
# Requiere firma electonica
def firma_electronica(r_):
    firma = "NO"
    if r_.tipo_firma.find("ELECTRONICA") > -1:
        firma = "SI"

    return firma

# Se firmado electronicamente
def firmado_electronica(r_):
    proceso_firma = r_.atributos_.get("proceso_firma", {})
    firmado       = proceso_firma.get("firmado_electronica", "NO")

    return firmado

# Se firmado electronicamente
def firmado_electronica_por(r_):
    proceso_firma = r_.atributos_.get("proceso_firma", {})
    firmado       = proceso_firma.get("firmado_electronica_por", "")

    return firmado

# Si esta firmado
def esta_firmado(r_):
    firmado = "NO"
    if "DIGITAL" in r_.tipo_firma:
        firmado = "SI"
    # FALTA VALIDAR POR FIRMA FISICA O ELECTRONICA

    return firmado


########
# LOGS #
########
def logs_salida(sesion, r_):
    logs = []

    return logs

# def logs_gestion(sesion, r_):
#     logs = []
#     # Busca gestion
#     for gestion_id in r_.gestion_id:
#         filtros = [ [ "fuente_id", "=", gestion_id ] ]
#         logs.extend( sqalchemy_filtrar.filtrarOrdena(estructura="logs", filtros=filtros, ordenamientos=[]) )   

#     return logs

def logs_radicado(sesion, r_):
    filtros = [ [ "fuente_id", "=", r_.id ] ]
    logs = sqalchemy_filtrar.filtrarOrdena(estructura="logs", filtros=filtros, ordenamientos=[])
    
    return logs

def logs(sesion, r_):
    lista_logs = []
    # Logs vinculados
    radicado = logs_radicado(sesion, r_)
    #gestion = logs_gestion(sesion, r_)
    
    # Log ordenado
    lista_logs.extend(radicado)
    #lista_logs.extend(gestion)
    lista_logs.sort(key=lambda x: x["creado_en_"], reverse=True)    
    setattr(r_, "logs", lista_logs)

############
# ARCHIVOS #
############
# Nombres de archivos
def archivos_nombres(sesion, r_):
    nombres = [ archivo["detalle"] for archivo in r_.archivos ]    
    setattr(r_, "archivos_nombres", ", ".join(nombres))

# Pdf base
def pdf_base(sesion, r_):
    RELACION_CLASE = globales.lee_clase("global_base_relacion_archivo")
    pdf            = {}
    for archivo in r_.archivos:
        if archivo['tipo_archivo'] == 'pdf':
            relacion = sesion.query(RELACION_CLASE).filter( RELACION_CLASE.archivo_id == archivo["id"] ).first()        
            if (relacion != None) and (relacion.tipo_relacion == "respuesta"):
                #print("archivo_id", archivo["id"])
                pdf = archivo     
    setattr(r_, "pdf_base", pdf)


################
# TRAZABILIDAD #
################

def dependencias_id(r_):
    return list(set([r_.dependencia_envia_id, r_.dependencia_recibe_id]))

def funcionarios_id(r_):   
    return list(set([
        r_.radicado_por_id, 
        r_.funcionario_envia_id,
        r_.funcionario_recibe_id
    ]))


#####################
# Información comun #
#####################

def remite_ent_dep_nombre(r_):
    dato = ""
    if (r_.dependencia_envia_nombre not in ["", None]):
        dato = str(r_.dependencia_envia_nombre)
    
    return dato


def remite_per_fun_nombre(r_):
    dato = ""
    if (r_.funcionario_envia_nombre not in ["", None]):
       dato = str(r_.funcionario_envia_nombre)
    
    return dato


def recibe_ent_dep_nombre(r_):
    dato = ""
    if (r_.dependencia_recibe_nombre not in ["", None]):
       dato = str(r_.dependencia_recibe_nombre)
    
    return dato


def recibe_per_fun_nombre(r_):
    dato = ""
    if (r_.funcionario_recibe_nombre not in ["", None]):
       dato = str(r_.funcionario_recibe_nombre)
    
    return dato