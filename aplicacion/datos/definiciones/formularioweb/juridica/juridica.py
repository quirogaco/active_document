#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

from librerias.datos.base                import globales
from librerias.datos.validacion          import valida 
from librerias.datos.elastic             import elastic_utilidades
from librerias.datos.elastic             import elastic_operaciones
from aplicacion.datos.clases.clases_base import base_general_campos
from aplicacion.datos.estructuras        import baseGeneral_estructura
from aplicacion.datos.estructuras        import baseGeneral_estructura

campos = {
    "tipo_radicado": {
        "titulo"     : "Tipo radicado",
        "tipo"       : "texto",
        "longitud"   : 128,
        "tipoElastic": "clave_ordenado"
    },

    "nro_radicado": {
        "titulo"     : "Número radicado",
        "tipo"       : "texto",
        "longitud"   : 128,
        "tipoElastic": "clave_ordenado"
    },

    "fecha_radicado": {
        "titulo"     : "Fecha radicado",
        "tipo"       : "fechaHora",        
        "tipoElastic": "fechaHora_ordenado"
    },

    "tipo_entidad_id": {
        "titulo"     : "Tipo entidad",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 50,
        "tipoElastic": "clave_ordenado"
    },

    "nombre_entidad": {
        "titulo"     : "Nombre entidad",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 256,
        "tipoElastic": "texto_ordenado"
    },

    "nro_identificacion": {
        "titulo"     : "Nit entidad",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 128,
        "tipoElastic": "texto_ordenado"
    },

    "nombres": {
        "titulo"     : "Nombres remitente",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 256,
        "tipoElastic": "texto_ordenado"
    },

    "apellidos": {
        "titulo"     : "Apellidos remitente",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 256,
        "tipoElastic": "texto_ordenado"
    },

    "medio_notificacion": {
        "titulo"     : "Medio notificación",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 50,
        "tipoElastic": "clave_ordenado"
    },

    "correo": {
        "titulo"     : "Correo electrónico",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 256,
        "tipoElastic": "texto_ordenado"
    },

    "direccion": {
        "titulo"     : "Dirección notificacion",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 256,
        "tipoElastic": "texto_ordenado"
    },

    "ciudad_id": {
        "titulo"     : "Ciudad",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 60,        
        "defecto"    : "",
        "tipoElastic": "clave"
    },

    "detalle": {
        "titulo"     : "Descripcion",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 2048,
        "defecto"    : "",
        "tipoElastic": "clave"
    },

}
campos.update(base_general_campos.campos)

"""
    "genero_id": {
        "titulo"     : "Genero",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 60,
        "tipoElastic": "clave"
    },    

     "tipo_identificacion_id": {
        "titulo"     : "Tipo identificación",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 50,
        "tipoElastic": "clave_ordenado"
    },
"""

# Campos elastic
camposIndexamiento = {
    'tipo_entidad_nombre': {
        'tipoElastic': 'texto'
    },  

    'anexos_radicacion': {
        "tipoElastic": {
            'tipo'       : 'anidados',
            'propiedades': {
                'id'             : {
                    'tipoElastic': 'clave'
                }, 
                'ruta'     : {
                    'tipoElastic': 'texto'
                },  
                'archivo'   : {
                    'tipoElastic':'texto'
                },  
                'tipo'         :{
                    'tipoElastic': 'texto'
                },  
                'tamano'         :{
                    'tipoElastic': 'entero'
                }, 
            }
        }
    }
}

camposElastic = campos.copy()
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Formulario Web Juridico",
    "clase"       : "db_formulario_web",
    "estructura"  : "radicado_web_juridica",    
    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,

    # Referencias a otras estructuras
    "referencias" : [
        {
            "campoReferencia"    : "anexos_radicacion",
            "funcion"            : "leer_anexos_radicacion",
        },

        # Tipo entidad
        {
            "campoReferencia"    : "tipo_entidad_id",
            "atributosReferencia": [{
                "tipo_entidad_nombre": "nombre",
            }],
            "estructuraDestino": "tipo_entidad",
        },

    ],


    "campoIndice" : "id",
    "indexa"      : "si",

    "indexamiento": {}
}

# Publica definicion de estructura
globales.carga_definicion(definicion["estructura"], definicion)

##### VALIDACIÓN #######
# Genera modelo de validación
validador = valida.definirModelo(definicion["estructura"], definicion["campos"])
# Publica modelo de validacion
globales.carga_validador(definicion["estructura"], validador)

##### ELASTIC #######
# Genera modelo de elastic
elastic_modelo = elastic_utilidades.generaModelo(camposElastic, definicion["indexamiento"])
# Registra modelo de elastic
elastic_utilidades.registraModelo(
    definicion["estructura"], 
    elastic_modelo, 
    definicion["indexamiento"], 
    definicion.get("campoIndice", "id") 
)
elastic_operaciones.creaIndice(definicion["estructura"], "base")

# PROCESAMIENTO ESTRUCTURA
import random 
def pre_procesa(estructura, datos):
    print("")
    print("PREEPROCESA:")
    pprint.pprint(datos)
    radicado = "E-2021-" + str(random.randint(0, 10000))
    datos["nro_radicado"] = radicado
    return datos

globales.carga_procesamiento(definicion["estructura"], "pre_estructura", pre_procesa)
#globales.carga_procesamiento(definicion["estructura"], "normaliza_estructura", baseGeneral_estructura.normaliza_estructura)


###############################################
# FUNCIONES LOCALES DE OPERACIÓN E INDEXACIÓN #
###############################################

def leer_anexos_radicacion(registro):    
    return []

globales.carga_funcion_referencia(definicion["estructura"], "leer_anexos_radicacion", leer_anexos_radicacion)