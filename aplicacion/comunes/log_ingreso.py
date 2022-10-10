#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime, random 

from aplicacion.comunes  import indexar_datos
from librerias.datos.sql import sqalchemy_insertar

def crea_log(accion, codigo, ip_maquina, estado):
    # Log del radicado
    datos_log = {
        "accion"    : accion,      
        "codigo"    : codigo,    
        "ip_maquina": ip_maquina,    
        "estado"    : estado,
        "accion_en" : datetime.datetime.now()
    }

    resultado = sqalchemy_insertar.insertar_registro_estructura("logs_ingreso", datos_log)
    indexar_datos.indexar_estructura("logs_ingreso", resultado["id"])