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

salidas_gestion = {
    "definicion": {
        "id"    : "533",
        "nombre": "GESTIÓN - Manejo de salidas"
    },

    "grid": {
        "componente": "grid_gestion_salida",     
        "texto"     : "Gestión de Salidas oficina",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Gestión",
        "tipo"      : "importar",
    },

    # "forma": {
    #     "componente": "gestion_pantalla",      
    #     "texto"     : "Consulta Radicados",
    #     "tipo"      : "importar"
    # }
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
    salidas_gestion
]