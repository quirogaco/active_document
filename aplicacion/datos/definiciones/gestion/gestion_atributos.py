#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime

# Base general con atributos basicos
from librerias.datos.sql  import sqalchemy_leer
from librerias.datos.sql  import sqalchemy_filtrar
from librerias.utilidades import vencimientos

############################
# INFORMACION DEL RADICADO #
############################
def carga_radicado(_r):    
    if getattr(_r, "_radicado", None) is None:
        radicado = {}
        filtros    = [ [ "gestion_id", "=", _r.id ] ]
        relaciones = sqalchemy_filtrar.filtrarOrdena(estructura="gestor_peticion_relaciones", filtros=filtros, ordenamientos=[])         
        for relacion in relaciones:
            radicado = relacion  
        setattr(_r, "_radicado", radicado )
      
def origen_tipo(_r):
    carga_radicado(_r)

    return _r._radicado.get("tipo", "ENTRADA")

def clase_radicado(_r):
    carga_radicado(_r)

    return _r._radicado.get("fuente", "VENTANILLA")

def nro_radicado(_r):
    nro = ""
    if (_r.origen_tipo == "ENTRADA"):
        carga_radicado(_r)
        nro = _r._radicado.get("nro_radicado", "")
    elif (_r.origen_tipo == "SALIDA"):
        nro = "BORRADOR"
    elif (_r.origen_tipo == "INTERNO"):
        nro = "BORRADOR"
    
    return nro

def fecha_radicado(_r):
    fecha = ""
    if (_r.origen_tipo == "ENTRADA"):
        carga_radicado(_r)
        fecha = _r._radicado.get("fecha_radicado", "")
    elif (_r.origen_tipo == "SALIDA"):
        fecha = _r.gestion_inicio
    elif (_r.origen_tipo == "INTERNO"):
        fecha = _r.gestion_inicio
    
    return fecha

def tercero_nombres_apellidos(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("tercero_nombres_apellidos", "")

def tercero_razon_social(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("tercero_razon_social", "")

def tercero_clase(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("tercero_clase", "")

def tercero_tipo_tercero_nombre(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("tercero_tipo_tercero_nombre", "")

def asunto(_r):
    asunto = ""
    if   (_r.origen_tipo == "ENTRADA"):
        carga_radicado(_r)
        asunto = _r._radicado.get("asunto", "")
    elif (_r.origen_tipo == "SALIDA"):
        salida_borrador = _r.atributos_.get("salida_borrador", {})
        asunto = salida_borrador.get("asunto", "")
    elif (_r.origen_tipo == "INTERNO"):
        interno_borrador = _r.atributos_.get("interno_borrador", {})
        asunto = interno_borrador.get("asunto", "")
    
    return asunto

def origen_id(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("origen_id", "")

###################
# INFORMACION TRD #
###################
def trd_dependencia_nombre(_r):
    nombre        = ""
    trd           = _r.atributos_.get("trd", {})
    expediente_id = trd.get("expediente", None)
    if expediente_id != None:
        expediente = sqalchemy_leer.leer_un_registro("agn_expedientes_trd", expediente_id)
        if (expediente != None):
            serie_id = expediente["serie_id"]
            serie    = sqalchemy_leer.leer_un_registro("agn_serie_trd", serie_id)
            if (serie != None):
                nombre = serie["dependencia_nombre"]
    
    return nombre

def expediente_nombre(_r):        
    nombre        = ""
    trd           = _r.atributos_.get("trd", {})
    expediente_id = trd.get("expediente", None)
    if expediente_id != None:
        expediente = sqalchemy_leer.leer_un_registro("agn_expedientes_trd", expediente_id)
        if (expediente != None):
            nombre = expediente["nombre"]
    
    return nombre

def tipo_nombre(_r):
    nombre  = ""
    trd     = _r.atributos_.get("trd", {})
    tipo_id = trd.get("tipo_documental", None)
    if tipo_id != None:
        tipo = sqalchemy_leer.leer_un_registro("agn_tipo_documental_trd",tipo_id)
        if (tipo != None):
            nombre = tipo["nombre"]
    
    return nombre

#######################
# INFORMACION GESTIÓN #
#######################
# Valor númerico 1
def valor_gestion(_r):
    return 1

# Fecha de vencimiento
def vence_en(_r):
    festivos      = [] # Cargarlos de base de datos
    dias_festivos = sqalchemy_leer.leer_todos("base", "festivos", desde=0, hasta=1000)
    for dia_festivo in dias_festivos:
        festivo = dia_festivo["festivo"]
        if isinstance(festivo, str) == True:
            festivo = datetime.datetime.fromisoformat(festivo)
        festivos.append(festivo)
    
    # No tiene en cuenta HORA O DIAS
    vence = vencimientos.siguiente_fecha_habil_dias(_r.gestion_inicio, _r.total_tiempo, festivos)
    
    return vence

# Fecha de respuesta
def fecha_respuesta(_r):
    finalizado = _r.atributos_.get("finalizado", {})
    fecha      = finalizado.get("fecha_respuesta", None)

    return fecha

# Finalizador ID, Finalizacion MANUAL
def finalizado_por_id(_r):
    finalizado = _r.atributos_.get("finalizado", {})
    valor      = finalizado.get("finalizado_por_id", "")
    
    return valor

# Finalizador NOMBRE, Finalizacion MANUAL
def finalizado_por_nombre(_r):
    finalizado = _r.atributos_.get("finalizado", {})
    valor      = finalizado.get("finalizado_por_nombre", "")
    
    return valor

# Finalizador FECHA, Finalizacion MANUAL
def finalizado_en(_r):
    finalizado = _r.atributos_.get("finalizado", {})
    valor      = finalizado.get("finalizado_en", None)
    
    return valor

# Finalizador COMENTARIO, Finalizacion MANUAL
def finalizado_comentario(_r):
    finalizado = _r.atributos_.get("finalizado", {})
    valor      = finalizado.get("finalizado_comentario", "")
    
    return valor

# Estado general (PENDIENTE, FINALIZADO)
def estado_gestion(_r):
    estado = "PENDIENTE"     
    # Estado por gestión
    if (_r.fecha_respuesta is not None) or (_r.finalizado_por_id not in [None, ""]):
        estado = "FINALIZADO"
    else:
        if (_r.estado_ == "DEVUELTO"):
            estado = "FINALIZADO"
        
    return estado
 
# Modo de finalización (RESPUESTA, MANUAL)
def finalizado_modo(_r):
    modo = ""
    if _r.fecha_respuesta is not None:
        modo = "RESPUESTA"
    elif _r.finalizado_por_id not in [None, ""]:
        estado = "MANUAL"
    
    return modo

# Estado vencimiento (TERMINOS, VENCIDO)
def estado_vencimiento(_r):
    comparar = datetime.datetime.now() 
    vence    = _r.vence_en
    # Si no tiene fecha de respuesta, compara fecha actual
    if _r.fecha_respuesta != None:
        comparar = _r.fecha_respuesta

    if (comparar.replace(tzinfo=None) <= vence.replace(tzinfo=None)):
        modo = "TERMINOS"
    else:
        modo = "VENCIDO"

    return modo

# Dias para vencer o vencidos
def dias_vencimiento(_r):
    festivos  = [] # Cargarlos de base de datos
    # No tiene en cuenta HORA O DIAS
    fecha_hoy = datetime.datetime.now() 
    dias      = vencimientos.diferencia_en_dias_habiles( fecha_hoy, _r.vence_en, festivos )

    return dias

def logs_gestion(_r):
    logs = list(_r.logs)
    
    return sorted(logs, key=lambda x: x['creado_en_'])

def etapa_gestion(_r):
    etapa = ""
    logs  = _r.logs_gestion
    if len(logs) > 0:
        etapa = logs[-1]["detalle_estado"]
    
    return etapa

def etapa_estado(_r):
    etapa = ""
    logs  = _r.logs_gestion
    if len(logs) > 0:
        etapa = logs[-1]["estado"]
    
    return etapa

# Tipo de gestión
def tipo_gestion(_r):
    tipo = "GESTION"     
    if   (_r.rapida == "SI"):
        tipo = "RAPIDA"
    elif (_r.colaborativa not in ["", None]):
        tipo = "COLABORATIVA"
        
    return tipo 