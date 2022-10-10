#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pprint

from librerias.datos.sql     import sqalchemy_insertar
from librerias.datos.elastic import elastic_operaciones

def crea_log(datos={}):
    datos_log = {
        # Accionante
        "accionante_tipo"  : datos["accionante_tipo"],   
        "accionante_id"    : datos["accionante_id"],        
        # Destinatario
        "destinatario_tipo": datos["destinatario_tipo"],           
        "destinatario_id"  : datos["destinatario_id"],          
        # proceso: RADICACION, GESTION, ENVIOS, ETC
        "proceso"          : datos["proceso"],    
        # fuente: ENTRADA, SALIDA, GESTION
        "fuente"           : datos["fuente"],       
        "fuente_id"        : datos["fuente_id"],
        # Acción realizada
        "accion"           : datos["accion"],
        "detalle"          : datos["detalle"],
        # Estado resulatdo del objeto proceso
        "estado"           : datos["estado"],
        # Mensaje para grillas y formas, asociado al estado
        "detalle_estado"   : datos["detalle_estado"],
    }

    resultado = sqalchemy_insertar.insertar_registro_estructura("logs", datos_log)
    # Indexar registro gestión
    elastic_operaciones.indexar_registro(datos["fuente"], datos["fuente_id"])
    
    return resultado