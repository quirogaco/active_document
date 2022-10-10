#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales

gestion_basica = {
    "definicion": {
        "id"    : "53",
        "nombre": "GESTI�N - Gesti�n de peticiones/tramites"
    },

    "grid": {
        "componente": "gestion_basica_grid",     
        "texto"     : "Gesti�n de Peticiones/Tramites",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Gesti�n",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "gestion_pantalla",      
        "texto"     : "Consulta Radicados",
        "tipo"      : "importar"
    }
}

gestion_pantalla = {
    "definicion": {
        "id"    : "553",
        "nombre": "GESTI�N - Gesti�n peticiones"
    },

    "forma": {
        "componente": "gestion_pantalla",     
        "texto"     : "Gesti�n peticiones",
        "tipo"      : "importar",
    }
}

tablero_general = {
    "definicion": {
        "id"    : "54",
        "nombre": "GESTI�N - Gesti�n seguimiento general"
    },

    "grid": {
        "componente": "tablero_general",     
        "texto"     : "Gesti�n seguimiento general",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Gesti�n",
        "tipo"      : "importar",
    }
}

opciones = [
    gestion_basica,
    tablero_general,
    gestion_pantalla
]