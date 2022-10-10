#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, builtins,time, pprint
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.AL32UTF8"

from fastapi import Response
from fastapi.responses import HTMLResponse

#########################
# Configuración general #
#########################
# Argumentos
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-host',     type=str, default="0.0.0.0", help='ip direccion del servidor web')
parser.add_argument('-port',     type=int, default=9000,      help='puerto del servidor web')
parser.add_argument('-services', type=str, default="0.0.0.0", help='ip de los servicio del sistema')
parser.add_argument('-celery',   type=str, default="NO",      help='Si carga tareas celery workers')
parser.add_argument('-nodo',     type=str, default="001",     help='Nodo de ejecuci�n')
argumentos           = parser.parse_args()
builtins.appHost     = argumentos.host
builtins.appPort     = argumentos.port
builtins.appServices = argumentos.services
builtins.celeryRun   = argumentos.celery
builtins.nodo        = argumentos.nodo

# Esto es obligatorio para toda aplicacion y debe ir de primero
from  globalPaths import setPaths # globalPaths.py, debe estar en el mismo directorio del servidor.py
setPaths()

# INSTANCIA APLICACION
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from librerias.acappella.utils import utils
appfa = utils.getApp()
builtins.appfa = appfa # Publica app del servidor

from app_init import serverInit

import pprint

from sqlalchemy import desc

def valida_none(valor):
    if valor == None:
        return ""
    else:
        return str(valor).strip()


# ANEXO LOG
ANEXO_LOG         = builtins.DB_CLASES['DB_MIGRADO_ANEXOLOG_PQRS']

# ANEXO 
ANEXO             = builtins.DB_CLASES['DB_MIGRADO_ANEXO_PQRS']

# FUNCIONARIO
FUNCIONARIO_CLASE = builtins.DB_CLASES['DB_MIGRADO_FUNCIONARIO_PQRS']

# RADICADOS
RADICADO_CLASE    = builtins.DB_CLASES['DB_MIGRADO_RADICADO_PQRS']

def trae_remitente_datos(remitente_id, session):
    TERCERO_CLASE     = builtins.DB_CLASES['DB_MIGRADO_TERCERO_PQRS']
    datos             = {}
    remite_nombre     = ""
    nroidentificacion = ""
    direccion         = ""
    correoelectronico = ""
    telefonofijo      = ""
    telefonomovil     = ""
    remitente         = session.query( TERCERO_CLASE ).filter_by( id = remitente_id ).first()
    if remitente != None:
        if remitente.nombres not in ["", None]:
            remite_nombre = remitente.nombres
        else:
            remite_nombre = (valida_none(remitente.primer_nombre) + " " + valida_none(remitente.segundo_nombre) + " "  + 
                             valida_none(remitente.primer_apellido) + " "  + valida_none(remitente.segundo_apellido))
        
        remite_nombre.replace("   ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ")
        nroidentificacion = valida_none(remitente.nroidentificacion)
        direccion         = valida_none(remitente.direccion)
        correoelectronico = valida_none(remitente.correoelectronico)
        telefonofijo      = valida_none(remitente.telefonofijo)
        telefonomovil     = valida_none(remitente.telefonomovil)

    datos = {
        'nombre'           : remite_nombre,
        'nroidentificacion': nroidentificacion,
        'direccion'        : direccion,
        'correoelectronico': correoelectronico,
        'telefonofijo'     : telefonofijo,
        'telefonomovil'    : telefonomovil,
        ## Pais, ciudad, depeartamento
    }

    return datos

def busca_remitente(radicado_id, session):
    TRAZA_CLASE = builtins.DB_CLASES['DB_MIGRADO_TRAZABILIDAD_PQRS']
    datos = {}
    traza = session.query( TRAZA_CLASE ).filter_by( requ_id = radicado_id, traz_estado = "RADICADO" ).first()
    if traza == None:
        print("ERROR busca_remitente TRAZA:", radicado.id)
    else:
        datos = trae_remitente_datos(traza.usua_idejecutor, session)    
    
    #print(radicado.id, datos)

    return datos

def busca_remitente_nombre(remitente_id, session):
    datos = trae_remitente_datos(remitente_id, session)

    return datos.get('nombre', '')

def busca_funcionario(funcionario_id, session):
    nombre = ""
    funcionario = session.query( FUNCIONARIO_CLASE ).filter_by( id = funcionario_id ).first()
    if funcionario == None:
        pass
        #print("ERROR busca_funcionario:", funcionario_id)
    else:
        nombre = valida_none(funcionario.func_primernombre) + " " + valida_none(funcionario.func_primerapellido)
    
    #print(radicado.id, datos)

    return nombre

def data_log(log):
    accionante      = ""
    destinatario    = ""
    tipo_accionante = "FUNCIONARIO"
    if   log.traz_estado == "EN TRAMITE":
            # FUNCIONARIO EL MISMO
            accionante   = busca_funcionario(log.usua_idejecutor, session)
            destinatario = accionante

    elif log.traz_estado == "NO TRAMITADO":
            # FUNCIONARIO EL MISMO
            accionante   = busca_funcionario(log.usua_idejecutor, session)
            destinatario = accionante

    elif log.traz_estado == "RADICADO":
            # TERCERO EL MISMO
            accionante      = busca_remitente_nombre(log.usua_idejecutor, session)
            destinatario    = accionante
            tipo_accionante = "TERCERO"

    elif log.traz_estado == "RECHAZADO":
            # FUNCIONARIO EL MISMO
            accionante   = busca_funcionario(log.usua_idejecutor, session)
            destinatario = accionante

    elif log.traz_estado == "RESUELTO":
            # FUNCIONARIO EL MISMO
            accionante   = busca_funcionario(log.usua_idejecutor, session)
            destinatario = accionante

    elif log.traz_estado == "TRAMITADO":
            # FUNCIONARIO EL MISMO
            accionante   = busca_funcionario(log.usua_idejecutor, session)
            destinatario = accionante

    elif log.traz_estado == "TRASLADO":
            # FUNCIONARIO DISTINTO
            accionante   = busca_funcionario(log.usua_idejecutor, session)
            destinatario = busca_funcionario(log.usua_idasignado, session)

    data = {
        'id'             : log.id,
        'accionante'     : accionante,
        'destinatario'   : destinatario,
        'estado'         : log.traz_estado,
        'fecha'          : log.traz_fecha,
        'descripcion'    : log.traz_descripcion,
        'tipo_accionante': tipo_accionante
    }

    return data     

def busca_tramitelog(radicado, session):
    datos = []
    logs  = session.query( TRAZA_CLASE ).filter_by( requ_id = radicado.id).order_by( desc( TRAZA_CLASE.traz_fecha) ).all()
    for log in logs:        
        data = data_log(log)
        datos.append(data)

    return datos

def busca_anexos(radicado, session):
    datos = []    
    logs  = session.query( ANEXO_LOG ).filter_by( requ_id = radicado.id).order_by( desc( ANEXO_LOG.adju_fechacambio) ).all()
    for log in logs:
        anexos  = session.query( ANEXO ).filter_by( id = log.id ).all()
        for anexo in anexos:
            accionante = busca_funcionario(log.adju_registradopor, session)
            if accionante == "":
                accionante = log.adju_registradopor
                #print( "SIN ACCIONANTE:", log.adju_registradopor, busca_remitente(log.adju_registradopor, session), log.traz_id ) 
            data = {
                'id'            : anexo.id,
                'archivo_nombre': anexo.adju_nombre,
                'tipo_documento': "ANEXO",
                'accionante'    : accionante, 
                'fecha'         : log.adju_fechacambio
            }              
            datos.append(data)
      
    return datos

def busca_anexos_traza(radicado, trazas, session):
    datos = []    
    for traza in trazas:
        logs = session.query( ANEXO_LOG ).filter_by( traz_id = traza['id'] ).all()
        for log in logs:
            anexo      = session.query( ANEXO ).filter_by( id = log.id ).first()
            if (anexo != None):
                accionante = busca_funcionario(log.adju_registradopor, session)
                if accionante == "":
                    accionante = log.adju_registradopor
                data = {
                    'id'            : anexo.id,
                    'archivo_nombre': anexo.adju_nombre,
                    'tipo_documento': "RESPUESTA",
                    'accionante'    : accionante, 
                    'fecha'         : log.adju_fechacambio
                }              
                datos.append(data)
            #else:
            #  print("anexo no existe:", log.id)
      
    return datos

def busca_archivos_todos(radicado, trazas, session):
    datos  = []
    
    # anexos
    anexos = busca_anexos(radicado, session)
    datos  = datos + anexos

    # anexos por traza
    anexos_traza = busca_anexos_traza(radicado, trazas, session)
    datos        = datos + anexos_traza

    # ordena por fecha
    datos        = sorted(datos, key = lambda i: i['fecha'], reverse = True) 
    
    return datos
    
from operator import attrgetter

session = SQLSession()

pprint.pprint(dir(builtins))

radicados      = session.query( RADICADO_CLASE ).order_by( desc( RADICADO_CLASE.fecha_radicado) ).all()

# Arma infor del radicao
for radicado in radicados:
    radicado._indexar_primero_
    
    """
    # Remitente
    remitente_data = busca_remitente(radicado.id, session)
    
    # Trazabilidad
    logs           = busca_tramitelog(radicado, session)
    
    # Anexos
    anexos         = busca_archivos_todos(radicado, logs, session)
    """