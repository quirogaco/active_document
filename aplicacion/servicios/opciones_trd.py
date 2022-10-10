#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

from librerias.datos.base import globales

################
# AGN ARCHIVOS #
################
# FONDOS DOCUMENTALES
agn_fondos = {
    "definicion": {
        "id"    : "56",
        "nombre": "TRD - Fondos Documentales"
    },

    "grid": {
        "clase"     : "grid",
        "componente": "agn_fondo_documental_grid",     
        "texto"     : "Fondos Documentales",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Archivo",
        "tipo"      : "remota"
    },

    "forma": {
        "clase"     : "forma",     
        "componente": "agn_fondo_documental_forma",      
        "texto"     : "Manejo de fondos",
        "tipo"      : "remota"
    }
}

###########
# TRD AGN #
###########
# TRD GRID
trd_basica = {
    "definicion": {
        "id"    : "57",
        "nombre": "TRD - Manejo de Tablas de Retención Grilla"
    },

    "grid": {
        "componente": "trd_basica_grid",     
        "texto"     : "Manejo de Tablas de Retención",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Archivo TRD",
        "tipo"      : "importar",
    }
}

trd_pantalla = {
    "definicion": {
        "id"    : "58",
        "nombre": "TRD - Manejo de Tablas de Retención Pantalla"
    },

    "forma": {
        "componente": "trd_pantalla",     
        "texto"     : "Pantalla  trd",
        "tipo"      : "importar",
    }
}

# EXPEDIENTE GRID
expediente_basica = {
    "definicion": {
        "id"    : "59",
        "nombre": "TRD - Manejo de Expedientes TRD Grilla"
    },

    "grid": {
        "componente": "expediente_basica_grid",     
        "texto"     : "Manejo de Expedientes TRD",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Archivo TRD",
        "tipo"      : "importar",
    }
}

pantalla_expediente = {
    "definicion": {
        "id"    : "60",
        "nombre": "TRD - Manejo de Expedientes TRD Pantalla"
    },

    "forma": {
        "componente": "pantalla_expediente",     
        "texto"     : "Pantalla  Expediente",
        "tipo"      : "importar",
    }
}

# EXPEDIENTE CONSULTA GRID
expediente_consulta_basica = {
    "definicion": {
        "id"    : "61",
        "nombre": "TRD - Consulta Expedientes TRD Grilla"
    },

    "grid": {
        "componente": "expediente_consulta_basica_grid",     
        "texto"     : "Consulta Expedientes TRD",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Archivo TRD",
        "tipo"      : "importar",
    }
}

pantalla_consulta_expediente = {
    "definicion": {
        "id"    : "62",
        "nombre": "TRD - Consulta Expedientes TRD Pantalla"
    },

    "forma": {
        "componente": "pantalla_consulta_expediente",     
        "texto"     : "Consulta Expediente",
        "tipo"      : "importar",
    }
}

# EXPEDIENTE PRESTAMO
prestamo_basica = {
    "definicion": {
        "id"    : "63",
        "nombre": "TRD - Prestamo Expedientes"
    },

    "grid": {
        "componente": "prestamo_basica_grid",     
        "texto"     : "Prestamo Expedientes",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Prestamos expedientes",
        "tipo"      : "importar",
    }
}

# TRANSFERENCIA GRID
transferencia_basica = {
    "definicion": {
        "id"    : "64",
        "nombre": "TRD - Manejo de Transferencia Primaria Grilla"
    },

    "grid": {
        "componente": "transferencia_basica_grid",     
        "texto"     : "Manejo de Transferencia Primaria",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Archivo TRD",
        "tipo"      : "importar",
    }
}

pantalla_transferencia = {
    "definicion": {
        "id"    : "65",
        "nombre": "TRD - Manejo de Transferencia Primaria Pantalla"
    },

    "forma": {
        "componente": "pantalla_transferencia",     
        "texto"     : "Pantalla Transferencia Primaria",
        "tipo"      : "importar",
    }
}

# Transferencias  oficina
expediente_transfiere = {
    "definicion": {
        "id"    : "599",
        "nombre": "TRD - Manejo de Expedientes a transferir"
    },

    "grid": {
        "componente": "expediente_transfiere_grid",     
        "texto"     : "Manejo de Expedientes a transferir",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Archivo TRD",
        "tipo"      : "importar",
    }
}


# Disposicion final
expediente_disposicion = {
    "definicion": {
        "id"    : "599",
        "nombre": "TRD - Manejo de Disposición final"
    },

    "grid": {
        "componente": "expediente_disposicion_grid",     
        "texto"     : "Manejo de Disposición final",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Archivo TRD",
        "tipo"      : "importar",
    }
}

opciones = [
    agn_fondos,
    trd_basica,
    trd_pantalla,
    expediente_basica,
    pantalla_expediente,
    expediente_consulta_basica,
    pantalla_consulta_expediente,
    prestamo_basica,
    transferencia_basica,
    pantalla_transferencia,
    expediente_transfiere,
    expediente_disposicion
]