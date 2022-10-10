#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

from librerias.datos.base import globales

contenido_pantalla = {
    "definicion": {
        "id"    : "11",
        "nombre": "ENTRADA - Pantalla principal"
    },

    "forma": {
        "componente": "contenido_pantalla",      
        "texto"     : "Pantalla principal",
        "tipo"      : "importar",
        "navegar"   : "no",
        "padre"     : ""
    }
}

#######################
# FORMULARIO DINAMICO #
#######################
formulario_constructor = {
    "definicion": {
        "id"    : "12",
        "nombre": "CONFIGURACIÓN - Formulario constructor"
    },

    "forma": {
        "componente": "formulario_constructor",     
        "texto"     : "Formulario constructor",
        "navegar"   : "si",
        "tipo"      : "importar",
    }
}

#########################
# DISEÑADOR DE REPORTES #
#########################
disenador_reportes = {
    "definicion": {
        "id"    : "199",
        "nombre": "CONFIGURACIÓN - Diseñador de Reportes Dinamicos"
    },

    "grid": {
        "componente": "reportes_dinamicos_grid",     
        "texto"     : "Diseño de Reportes Dinamicos",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Configuración",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "formulario_reportes_dinamicos",     
        "texto"     : "Diseñador de reportes",
        "tipo"      : "importar",
    }
}

#########################
# IMPRESIÓN DE REPORTES #
#########################
impresion_reportes = {
    "definicion": {
        "id"    : "1333",
        "nombre": "REPORTES - Impresión"
    },

    "grid": {
        "componente": "grid_reportes_imprime",     
        "texto"     : "Impresión de reportes",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Configuración",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "formulario_reportes_imprime",     
        "texto"     : "Impresión de reportes",
        "tipo"      : "importar",
    }
}


#########################
# DISEÑADOR DE REPORTES #
#########################
disenador_formularios = {
    "definicion": {
        "id"    : "133",
        "nombre": "CONFIGURACIÓN - Diseñador de Formularios Dinamicos"
    },

    "grid": {
        "componente": "formularios_dinamicos_grid",     
        "texto"     : "Diseño de Formularios Dinamicos",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Configuración",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "formulario_constructor",     
        "texto"     : "Diseñador de formularios",
        "padre"     : "Diseñador de formularios",
        "navegar"   : "si",
        "tipo"      : "importar",
    }
}
    
#######################
# DISEÑADOR DE FLUJOS #
#######################
disenador_flujos = {
    "definicion": {
        "id"    : "1334",
        "nombre": "CONFIGURACIÓN - Diseñador de Flujos Dinamicos"
    },

    "grid": {
        "componente": "flujos_dinamicos_grid",     
        "texto"     : "Diseño de Flujos Dinamicos",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Configuración",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "flujos_dinamicos_forma",     
        "texto"     : "Diseñador de flujos",        
        "tipo"      : "importar",
    }
}

opciones = [
    contenido_pantalla,
    #formulario_constructor,
    disenador_reportes,
    impresion_reportes,
    #disenador_formularios,
    #disenador_flujos
]