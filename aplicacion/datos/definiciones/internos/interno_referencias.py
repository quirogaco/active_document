#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime

from aplicacion.datos.comunes.referencias import archivos, terceros

referencias = [
    # Sitio de radicaci�n 
    {
        "campoReferencia"    : "radicado_en",
        "atributosReferencia": [{
            "radicado_en_nombre": "nombre",
            "radicado_en_id"    : "id"
        }],
        "estructuraDestino": "ubicaciones",
        # "externa"          : {
        #     "tipo_relacion": "SITIO_DE_RADICACION"            
        # } 
    },

    # Usuario que radico 
    {
        "campoReferencia"    : "radicado_por",
        "atributosReferencia": [{
            "radicado_por_nombre": "nombre",
            "radicado_por_id"    : "id"
        }],
        "estructuraDestino": "usuarios",
        # "externa"          : {
        #     "tipo_relacion": "RADICADOR"            
        # } 
    },

    # Dependencia envia
    {
        "campoReferencia"    : "dependencia_envia_id",
        "atributosReferencia": [{
            "dependencia_envia_nombre": "nombre"
        }],
        "estructuraDestino": "dependencias",
    },

    # Usuario envia
    {
        "campoReferencia"    : "funcionario_envia_id",
        "atributosReferencia": [{
            "funcionario_envia_nombre": "nombre",
        }],
        "estructuraDestino": "usuarios"
    },

    # Dependencia recibe
    {
        "campoReferencia"    : "dependencia_recibe_id",
        "atributosReferencia": [{
            "dependencia_recibe_nombre": "nombre"
        }],
        "estructuraDestino": "dependencias",
    },

    # Usuario recibe
    {
        "campoReferencia"    : "funcionario_recibe_id",
        "atributosReferencia": [{
            "funcionario_recibe_nombre": "nombre",
        }],
        "estructuraDestino": "usuarios"
    },

    archivos.referencia_archivo
]