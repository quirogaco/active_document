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
        "nombre": "RADICACIóN - Radicación Persona JURIDICA"
    },

    "grid": {
        "componente": "radicado_general_grid",     
        "texto"     : "Radicación Persona JURIDICA",
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
        "nombre": "RADICACIóN - Radicación Persona Natural"
    },

    "grid": {
        "componente": "natural_radicados_grid",     
        "texto"     : "Radicación Persona Natural",
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
        "nombre": "RADICACIóN - Radicación Anonimo"
    },

    "grid": {
        "componente": "anonimo_radicados_grid",     
        "texto"     : "Radicación Anonimo",
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
        "nombre": "RADICACIóN - Asignación y traslado de radicados PQRS"
    },

    "grid": {
        "componente": "grid_pqrs_asigna_grid",     
        "texto"     : "Asignación y traslado de radicados PQRS",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "PQRS",
        "tipo"      : "importar",
    },   

    "forma": {
        "componente": "forma_pqrs_asigna",      
        "texto"     : "Asignación y traslado de PQRS",
        "tipo"      : "importar"
    }
}

pqrs_radicado = {
    "definicion": {
        "id"    : "39",
        "nombre": "RADICACIóN - Radicación PQRS"
    },

    "grid": {
        "componente": "grid_radica_asigna_grid",     
        "texto"     : "Radicación",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "PQRS",
    },

    "forma": {
        "componente": "pqrs_radicado_forma",      
        "texto"     : "Radicación PQRS",
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
        "nombre": "RADICACIóN - Radicación"
    },

    "grid": {
        "componente": "ventanilla_radicado_grid",     
        "texto"     : "Radicación",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Ventanilla Radicación",
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
        "nombre": "RADICACIóN - Consulta Radicados"
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
        "nombre": "RADICACIóN - Radicación Interno"
    },

    "grid": {
        "componente": "ventanilla_interno_grid",     
        "texto"     : "Radicación Interno",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Ventanilla Radicación",
    },

    "forma": {
        "componente": "ventanilla_interno_forma",      
        "texto"     : "Radicación Ventanilla Interno",
        "tipo"      : "importar"
    }
}

ventanilla_interno_consulta = {
    "definicion": {
        "id"    : "5543",
        "nombre": "RADICACIóN - Consulta Radicados Interno"
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
        "texto"     : "Radicación Interno",
        "icon"      : "",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Ventanilla Radicación",
    },
}

################
# RADICA CORREO #
################
correos_grid = {
    "definicion": {
        "id"    : "110",
        "nombre": "RADICACIóN - CORREOS POR RADICAR"
    },

    "grid": {
        "componente": "correos_grid",     
        "texto"     : "Radicación de Correos",
        "navegar"   : "si",
        "padre"     : "Ventanilla Radicación",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "ventanilla_radicado_forma",      
        "texto"     : "Radicación Ventanilla",
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

    #ventanilla_salida,

    #ventanilla_interno,
    ventanilla_interno_consulta,

    consulta_radicados_web,

    correos_grid
]