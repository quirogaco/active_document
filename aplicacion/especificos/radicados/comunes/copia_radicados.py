#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime, random 

from aplicacion.trabajadores_base import radicados_celery
from librerias.datos.sql          import sqalchemy_leer
from aplicacion.trabajadores      import utilidades

#################
# DESTINATARIOS #
#################
def destinatario_salida(accion, datos, datos_tarea):
    destinatario_tipo = "tercero"
    ## TERCERO ID DEBE ESTAR CREADO DE ANTEMANO PARA QUE ESTO FUNCIONE
    ## SI NO LOS SABEMOS LO FORZAMOS A CREAR CON ID PREDEFINIDO
    destinatario_id   = datos.get('tercero_id')

    return destinatario_tipo, destinatario_id

def destinatario_lee(radicado_tipo, radicado_clase, accion, datos, datos_tarea):
    destinatario_tipo = ""
    destinatario_id   = ""
    if radicado_tipo == "SALIDA":
        destinatario_tipo, destinatario_id = destinatario_salida(accion, datos, datos_tarea)
        
    return destinatario_tipo, destinatario_id

##########
# FUENTE #
##########
def fuente_lee(radicado_tipo, radicado_clase):
    resultado = "radicados_entrada"

    if radicado_tipo == "SALIDA":
        resultado = "radicados_salida"
    
    if radicado_tipo == "INTERNO":
        resultado = "radicados_interno"

    return resultado

# Crea copia
from aplicacion.copias import crea_copias
def crea_copia_usuarios(fuente, radicado_tipo, radicado_id, nro_radicado, asunto, copias):
    for destino_id in copias:
        dato_copia = {
            "radicado_tipo"    : radicado_tipo,  
            "radicado_id"      : radicado_id,  
            "radicado_nro"     : nro_radicado,  
            "radicado_asunto"  : asunto,  
            "destinatario_tipo": "USUARIO",  
            "destinatario_id"  : destino_id,  
            "estado"           : "ASIGNADO"       
        }
        crea_copias.crea_copia(dato_copia) 
    
def usuarios_grupo(copia_grupos):
    usuarios = []
    """
    for copia_grupo_id in copia_grupos:
        grupo = sqalchemy_leer.leer_un_registro("grupo_usuarios", copia_grupo_id)  
        usuarios.append()
    """

    return usuarios

def copia_radicado(radicado_tipo, radicado_clase, radicado_id, nro_radicado, asunto, copia_usuarios, copia_grupos, copia_terceros):
    # Grupos a usuarios
    copias = usuarios_grupo(copia_grupos)
    copia_usuarios.extend(copias) 
    # Crea copias
    fuente = fuente_lee(radicado_tipo, radicado_clase)  
    crea_copia_usuarios(fuente, radicado_tipo, radicado_id,  nro_radicado, asunto, copia_usuarios)