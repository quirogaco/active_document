#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.sql     import sqalchemy_insertar
from librerias.datos.elastic import elastic_operaciones

def crea_copia(datos={}):
    datos_copia = {
        "radicado_tipo"    : datos["radicado_tipo"],  
        "radicado_id"      : datos["radicado_id"],
        "radicado_nro"     : datos["radicado_nro"], 
        "radicado_asunto"  : datos["radicado_asunto"],
        "destinatario_tipo": datos["destinatario_tipo"],
        "destinatario_id"  : datos["destinatario_id"],
        "estado"           : datos["estado"]
    }
    resultado = sqalchemy_insertar.insertar_registro_estructura("copias", datos_copia)

    # Indexar registro gesti�n
    #elastic_operaciones.indexar_registro(datos["fuente"], datos["radicado_id"])
    
    return resultado