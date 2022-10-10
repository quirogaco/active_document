#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales

########
# PQRS #
########
radicado_web_juridico = {
    "definicion": {
        "id"    : "35",
        "nombre": "RADICACI�N - Radicaci�n Persona JURIDICA"
    },

    "grid": {
        "componente": "radicado_general_grid",     
        "texto"     : "Radicaci�n Persona JURIDICA",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Formularios web",
    },

    "forma": {
        "componente": "radicado_juridica_forma",      
        "texto"     : "Entradas radicados Ventanilla",
        "tipo"      : "importar"
    }
}

radicado_web_natural = {
    "definicion": {
        "id"    : "36",
        "nombre": "RADICACI�N - Radicaci�n Persona Natural"
    },

    "grid": {
        "componente": "natural_radicados_grid",     
        "texto"     : "Radicaci�n Persona Natural",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Formularios web",
    },

    "forma": {
        "componente": "natural_web_forma",      
        "texto"     : "Entradas radicados Web",
        "tipo"      : "importar"
    }
}

radicado_web_anonimo = {
    "definicion": {
        "id"    : "37",
        "nombre": "RADICACI�N - Radicaci�n Anonimo"
    },

    "grid": {
        "componente": "anonimo_radicados_grid",     
        "texto"     : "Radicaci�n Anonimo",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Formularios web",
    },

    "forma": {
        "componente": "anonimo_web_forma",      
        "texto"     : "Entradas radicados Web",
        "tipo"      : "importar"
    }
}

asignar_pqrs = {
    "definicion": {
        "id"    : "38",
        "nombre": "RADICACI�N - Asignaci�n y traslado de radicados PQRS"
    },

    "grid": {
        "componente": "grid_pqrs_asigna_grid",     
        "texto"     : "Asignaci�n y traslado de radicados PQRS",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "PQRS",
        "tipo"      : "importar",
    },   

    "forma": {
        "componente": "forma_pqrs_asigna",      
        "texto"     : "Asignaci�n y traslado de PQRS",
        "tipo"      : "importar"
    }
}

pqrs_radicado = {
    "definicion": {
        "id"    : "39",
        "nombre": "RADICACI�N - Radicaci�n PQRS"
    },

    "grid": {
        "componente": "grid_radica_asigna_grid",     
        "texto"     : "Radicaci�n",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "PQRS",
    },

    "forma": {
        "componente": "pqrs_radicado_forma",      
        "texto"     : "Radicaci�n PQRS",
        "tipo"      : "importar"
    },

    "adicionales": [
        {
            "componente": "forma_radicado_consulta",      
            "texto"     : "Consulta Radicados",
            "tipo"      : "importar"
        }
    ]
}

#######################
# VENTANILLA RADICADO #
#######################

ventanilla_radicado = {
    "definicion": {
        "id"    : "41",
        "nombre": "RADICACI�N - Radicaci�n"
    },

    "grid": {
        "componente": "ventanilla_radicado_grid",     
        "texto"     : "Radicaci�n",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Ventanilla Radicaci�n",
        "tipo"      : "importar"
    },

    "forma": {
        "componente": "forma_radicado_consulta",      
        "texto"     : "Consulta Radicados",
        "tipo"      : "importar"
    },

    "adicionales": [
        {
            "componente": "ventanilla_radicado_forma",      
            "texto"     : "Radica entradas",
            "tipo"      : "importar"
        }
    ]

}

ventanilla_radicado_consulta = {
    "definicion": {
        "id"    : "41",
        "nombre": "RADICACI�N - Consulta Radicados"
    },

    "forma": {
        "componente": "forma_radicado_consulta",      
        "texto"     : "Consulta Radicados",
        "tipo"      : "importar"
    }
}

#####################
# VENTANILLA SALIDA #
#####################
ventanilla_salida = {
    "definicion": {
        "id"    : "42",
        "nombre": "CONSULTA - Salidas"
    },

    "grid": {
        "componente": "grid_ventanilla_salida",     
        "texto"     : "Salidas",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Salidas",
    },

    "forma": {
        "componente": "forma_salida_consulta",      
        "texto"     : "Consulta Salida",
        "tipo"      : "importar"
    }
}

######################
# VENTANILLA INTERNO #
######################
ventanilla_interno = {
    "definicion": {
        "id"    : "543",
        "nombre": "RADICACI�N - Radicaci�n Interno"
    },

    "grid": {
        "componente": "ventanilla_interno_grid",     
        "texto"     : "Radicaci�n Interno",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Ventanilla Radicaci�n",
    },

    "forma": {
        "componente": "ventanilla_interno_forma",      
        "texto"     : "Radicaci�n Ventanilla Interno",
        "tipo"      : "importar"
    }
}

ventanilla_interno_consulta = {
    "definicion": {
        "id"    : "5543",
        "nombre": "RADICACI�N - Consulta Radicados Interno"
    },

    "forma": {
        "componente": "ventanilla_interno_consulta",      
        "texto"     : "Consulta Radicados Interno",
        "tipo"      : "importar"
    }
}

################
# CONSULTA WEB #
################
consulta_radicados_web = {
    "definicion": {
        "id"    : "100",
        "nombre": "WEB - CONSULTA ESTADO RADICADO"
    },

    "grid": {
        "componente": "ventanilla_interno_grid",     
        "texto"     : "Radicaci�n Interno",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Ventanilla Radicaci�n",
    },
}

################
# RADICA CORREO #
################
correos_grid = {
    "definicion": {
        "id"    : "110",
        "nombre": "RADICACI�N - CORREOS POR RADICAR"
    },

    "grid": {
        "componente": "correos_grid",     
        "texto"     : "Radicaci�n de Correos",
        "navegar"   : "si",
        "padre"     : "Ventanilla Radicaci�n",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "ventanilla_radicado_forma",      
        "texto"     : "Radicaci�n Ventanilla",
        "tipo"      : "importar"
    }
}


opciones = [
    radicado_web_juridico,

    radicado_web_natural,

    radicado_web_anonimo,

    asignar_pqrs,
    
    pqrs_radicado,

    ventanilla_radicado,
    ventanilla_radicado_consulta,

    ventanilla_salida,

    ventanilla_interno,
    ventanilla_interno_consulta,

    consulta_radicados_web,

    correos_grid
]