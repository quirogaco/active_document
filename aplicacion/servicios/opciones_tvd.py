#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales

###########
# TVD AGN #
###########
# TVD GRID
tvd_basica = {
    "definicion": {
        "id"    : "67",
        "nombre": "TVD - Manejo de Tablas de Valoración Grilla"
    },

    "grid": {
        "componente": "tvd_basica_grid",     
        "texto"     : "Manejo de Tablas de Valoración",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Archivo TVD",
        "tipo"      : "importar",
    }
}

tvd_pantalla = {
    "definicion": {
        "id"    : "68",
        "nombre": "TVD - Manejo de Tablas de Valoración Pantalla"
    },

    "forma": {
        "componente": "tvd_pantalla",     
        "texto"     : "Pantalla  tvd",
        "tipo"      : "importar",
    }
}

# TVD EXPEDIENTE GRID
tvd_expediente_basica = {
    "definicion": {
        "id"    : "69",
        "nombre": "TVD - Manejo de Expedientes TVD Grilla"
    },

    "grid": {
        "componente": "tvd_expediente_basica_grid",     
        "texto"     : "Manejo de Expedientes TVD",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Archivo TVD",
        "tipo"      : "importar",
    }
}

tvd_pantalla_expediente = {
    "definicion": {
        "id"    : "70",
        "nombre": "TVD - Manejo de Expedientes TVD Pantalla"
    },

    "forma": {
        "componente": "tvd_pantalla_expediente",     
        "texto"     : "Pantalla  Expediente TVD",
        "tipo"      : "importar",
    }
}

opciones = [
    tvd_basica,
    tvd_pantalla,
    tvd_expediente_basica,
    tvd_pantalla_expediente
]