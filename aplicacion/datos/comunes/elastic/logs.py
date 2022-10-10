#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.sql import sqalchemy_tipo_campos as tipos

# Campos logs
logs_estructura = {
    "tipoElastic": {
        'tipo'       : 'anidados',
        "propiedades": {
            "accionante_id"      : tipos.texto(propiedades={"titulo": "Accionante id"}), 
            "accionante_nombre"  : tipos.texto(propiedades={"titulo": "Accionante nombre"}), 
            "destinatario_id"    : tipos.texto(propiedades={"titulo": "Destinatario id"}), 
            "destinatario_nombre": tipos.texto(propiedades={"titulo": "Destinatario nombre"}), 
            "proceso"            : tipos.texto(propiedades={"titulo": "Proceso log"}), 
            "fuente"             : tipos.texto(propiedades={"titulo": "Fuente"}), 
            "fuente_id"          : tipos.texto(propiedades={"titulo": "Id del elemento fuente"}), 
            "accion"             : tipos.texto(propiedades={"titulo": "Accion"}),
            "detalle"            : tipos.texto(propiedades={"titulo": "Detalle"}), 
            "estado"             : tipos.texto(propiedades={"titulo": "Estado"}),             
            "detalle_estado"     : tipos.texto(propiedades={"titulo": "Detalle estado"}),
            "creado_en_"         : tipos.fecha_obligatorio(propiedades={"titulo": "Fecha creación"}),  
        }
    }
}

    