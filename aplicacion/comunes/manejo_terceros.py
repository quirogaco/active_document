#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.sql     import sqalchemy_insertar
from aplicacion.comunes      import registro_relacion
from librerias.datos.elastic import elastic_operaciones 

def crear_registro_tercero( origen, datos, radicado_id, id_tarea=""):
    # Crea tercero
    radicado ="NO"
    if origen in ["ENTRADA", "SALIDA"]:
        radicado ="SI"
    
    datos_tercero = {
        "radicado"              : radicado,  
        "clase"                 : datos["clase"],   
        "tipo_tercero_id"       : datos["tipo_tercero_id"],   
        "tipo_identificacion_id": datos["tipo_identificacion_id"],           
        "nro_identificacion"    : datos["nro_identificacion"],   
        "razon_social"          : datos["razon_social"],  
        "cargo"                 : datos["cargo"],   
        "nombres"               : datos["nombres"], 
        "apellidos"             : datos["apellidos"], 
        "correo_electronico"    : datos["correo_electronico"], 
        "direccion"             : datos["direccion"], 
        "codigo_postal"         : datos["codigo_postal"], 
        "telefono"              : datos["telefono"], 
        "telefono_movil"        : datos["telefono_movil"], 
        "fax"                   : datos["fax"], 
        "ciudad_id"             : datos["ciudad_id"] 
    }

    # RELACIÓN RADICADO TERCERO
    estructura_origen = ""
    role              = ""
    if origen == "SALIDA":
        estructura_origen = "gestor_radicados_salida"
        role   = "DESTINATARIOS" 

    tercero = sqalchemy_insertar.insertar_registro_estructura("terceros", datos_tercero)
    elastic_operaciones.indexar_registro("terceros", tercero["id"])  

    registro_relacion.crear_registro_relacion(   
        estructura_origen,     # Estructura origen
        radicado_id,           # Id de la estructura origen
        "PADRE",               # Role registro origen
        "config_terceros",     # Estructura destino
        tercero["id"],       # Id de la estructura destino
        role,                  # Role registro destino
        "DESTINATARIO SALIDA", # Tipo de relación origen-destino
        "SIMPLE"               # Cardinalida simple, multiple
    )

    return tercero