#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

referencia_terceros = {
    "clase_operacion": "terceros",          
    "campoReferencia": "id", 
    "camposData"         : {
        "accion": "eliminar",
        "campos": [
            "tercero_id",
            "tercero_clase", 
            "tercero_tipo_tercero_id",
            "tercero_tipo_tercero_nombre",
            "tercero_tipo_identificacion_id", 
            "tercero_tipo_identificacion_nombre", 
            "tercero_nro_identificacion", 
            "tercero_razon_social", 
            "tercero_cargo",
            "tercero_nombres", 
            "tercero_apellidos",
            "tercero_correo_electronico", 
            "tercero_direccion", 
            "tercero_codigo_postal", 
            "tercero_telefono", 
            "tercero_telefono_movil", 
            "tercero_fax", 
            "tercero_ciudad_id", 
            "tercero_ciudad_nombre",
            "tercero_nombre_completo",
            "tercero_nombres_apellidos"
        ]
    },
    "atributosReferencia": [{
        "tercero_id"                        : "id",
        "tercero_clase"                     : "clase",
        "tercero_tipo_tercero_id"           : "tipo_tercero_id",
        "tercero_tipo_tercero_nombre"       : "tipo_tercero_nombre",
        "tercero_tipo_identificacion_id"    : "tipo_identificacion_id",
        "tercero_tipo_identificacion_nombre": "tipo_identificacion_nombre",
        "tercero_nro_identificacion"        : "nro_identificacion",
        "tercero_razon_social"              : "razon_social",            
        "tercero_cargo"                     : "cargo",
        "tercero_nombres"                   : "nombres",
        "tercero_apellidos"                 : "apellidos",
        "tercero_correo_electronico"        : "correo_electronico",
        "tercero_direccion"                 : "direccion",
        "tercero_codigo_postal"             : "codigo_postal",
        "tercero_telefono"                  : "telefono",
        "tercero_telefono_movil"            : "telefono_movil",
        "tercero_fax"                       : "fax",
        "tercero_ciudad_id"                 : "ciudad_id",   
        "tercero_ciudad_nombre"             : "ciudad_nombre",
        "tercero_nombre_completo"           : "nombre_completo" ,  
        "tercero_nombres_apellidos"         : "nombres_apellidos"
    }],            
    "estructuraDestino": "terceros",
    "campoDestino"     : "id",  
    "externa"          : {
        "tipo_relacion": "REMITENTE_RADICADO"            
    }          
}