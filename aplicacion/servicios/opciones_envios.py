#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base import globales

planilla_grid = {
    "definicion": {
        "id"    : "444",
        "nombre": "ENVIOS - Manejo de planillas de envio fisico"
    },

    "grid": {
        "componente": "planilla_grid",     
        "texto"     : "Manejo de planillas de envio fisico",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Envios",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "ventana_planilla",      
        "texto"     : "Crea plantilla",
        "navegar"   : "no",
        "tipo"      : "importar"
    }
}

envios_grid = {
    "definicion": {
        "id"    : "445",
        "nombre": "ENVIOS - Envios"
    },

    "grid": {
        "componente": "envios_grid",     
        "texto"     : "Envios grid",
        "icon"      : "",      
        "navegar"   : "NO",
        "padre"     : "Envios",
        "tipo"      : "importar",
    }
}

devoluciones_grid = {
    "definicion": {
        "id"    : "446",
        "nombre": "ENVIOS - Devoluciones"
    },

    "grid": {
        "componente": "devoluciones_grid",     
        "texto"     : "Devoluciones",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Envios",
        "tipo"      : "importar",
    }
}

envio_electronico_grid = {
    "definicion": {
        "id"    : "447",
        "nombre": "ENVIOS - Envios electronicos"
    },

    "grid": {
        "componente": "envio_electronico_grid",     
        "texto"     : "Envios electronicos",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Envios",
        "tipo"      : "importar",
    }
}

destinatarios_listado = {
    "definicion": {
        "id"    : "48",
        "nombre": "ENVIOS - Listados destinatarios salidas"
    },

    "grid": {
        "componente": "destinatarios_listado_grid",     
        "texto"     : "Listados destinatarios salidas",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Envios masivos",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "ventana_listado",      
        "texto"     : "Ventana listado",
        "navegar"   : "no",
        "tipo"      : "importar"
    }
}

ventanilla_masivos = {
    "definicion": {
        "id"    : "49",
        "nombre": "ENVIOS - Genera masivos de salida"
    },

    "forma": {
        "componente": "salida_masiva",      
        "texto"     : "Genera masivos de salida",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Envios masivos"
    }
}

destinatarios_listado_interno = {
    "definicion": {
        "id"    : "50",
        "nombre": "ENVIOS - Listados destinatarios internos"
    },

    "grid": {
        "componente": "destinatarios_listado_interno_grid",     
        "texto"     : "Listados destinatarios internos",
        "icon"      : "",      
        "navegar"   : "si",
        "padre"     : "Envios masivos",
        "tipo"      : "importar",
    },

    "forma": {
        "componente": "ventana_listado_interno",      
        "texto"     : "Ventana listado interno",
        "navegar"   : "no",
        "tipo"      : "importar"
    }
}

ventanilla_masivos_interno = {
    "definicion": {
        "id"    : "51",
        "nombre": "ENVIOS - Genera masivos de internos"
    },

    "forma": {
        "componente": "interno_masiva",      
        "texto"     : "Genera masivos de internos",
        "tipo"      : "importar",
        "navegar"   : "si",
        "padre"     : "Envios masivos"
    }
}

opciones = [
    planilla_grid,
    envios_grid,
    devoluciones_grid,
    envio_electronico_grid,
    destinatarios_listado,
    ventanilla_masivos,
    destinatarios_listado_interno,
    ventanilla_masivos_interno
]