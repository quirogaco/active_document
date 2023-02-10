#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

from librerias.datos.base import globales

gestion_basica = {
    "definicion": {
        "id"    : "53",
        "nombre": "GESTIÓN - Gestión de peticiones/tramites"
    },

    "grid": {
        "componente": "gestion_basica_grid",     
        "texto"     : "Gestión de Peticiones/Tramites",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Gestión",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "gestion_pantalla",      
        "texto"     : "Consulta Radicados",
        "tipo"      : "importar"
    }
}

consulta_gestion = {
    "definicion": {
        "id"    : "533",
        "nombre": "GESTIÓN - Dependencia historico"
    },

    "grid": {
        "componente": "grid_gestion_consulta",     
        "texto"     : "Gestión dependencia consulta",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Gestión",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "forma_salida_consulta",     
        "texto"     : "Gestión consulta salidas",
        "tipo"      : "importar",
    },

    "adicionales": [
        {
            "componente": "forma_radicado_consulta",      
            "texto"     : "Consulta Radicados Entrada",
            "tipo"      : "importar"
        },

        {
            "componente": "forma_interno_consulta",      
            "texto"     : "Consulta Radicados",
            "tipo"      : "importar"
        }
    ]
}

consulta_funcionario_gestion = {
    "definicion": {
        "id"    : "534",
        "nombre": "GESTIÓN - Funcionario historico"
    },

    "grid": {
        "componente": "grid_gestion_funcionario_consulta",     
        "texto"     : "Gestión funcionario consulta",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Gestión",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "forma_salida_consulta",     
        "texto"     : "Gestión consulta salidas",
        "tipo"      : "importar",
    },

    "adicionales": [
        {
            "componente": "forma_radicado_consulta",      
            "texto"     : "Consulta Radicados Entrada",
            "tipo"      : "importar"
        },

        {
            "componente": "forma_interno_consulta",      
            "texto"     : "Consulta Radicados",
            "tipo"      : "importar"
        }
    ]
}

gestion_pantalla = {
    "definicion": {
        "id"    : "553",
        "nombre": "GESTIÓN - Gestión peticiones"
    },

    "forma": {
        "componente": "gestion_pantalla",     
        "texto"     : "Gestión peticiones",
        "tipo"      : "importar",
    }
}

tablero_general = {
    "definicion": {
        "id"    : "54",
        "nombre": "GESTIÓN - Gestión seguimiento general"
    },

    "grid": {
        "componente": "tablero_general",     
        "texto"     : "Gestión seguimiento general",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Gestión",
        "tipo"      : "importar",
    }
}

opciones = [
    gestion_basica,
    tablero_general,
    gestion_pantalla,
    consulta_gestion,
    consulta_funcionario_gestion
]