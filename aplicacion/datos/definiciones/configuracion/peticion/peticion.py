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
    "codigo": {
        "titulo"     : "Codigo",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 50,
        "unico"      : "si",
        "tipoElastic": "clave_ordenado"
    },

    "nombre": {
        "titulo"     : "Nombre",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 512,
        "unico"      : "si",
        "tipoElastic": "texto_ordenado"
    },

    "total_dias": {
        "titulo"     : "Dias totales",
        "tipo"       : "entero",
        "obligatorio": "si",
        "tipoElastic": "entero"
    }, 

    "alertar_dias": {
        "titulo"     : "Dias para alertar",
        "tipo"       : "entero",
        "obligatorio": "si",
        "tipoElastic": "entero"
    },  

    "alertar_porcentaje": {
        "titulo"     : "Porcentaje para alertar",
        "tipo"       : "entero",
        "obligatorio": "si",
        "tipoElastic": "entero"
    },  

    "tipo_dias": {
        "titulo"     : "Tipo dias (Calendario/Habiles)",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 30,
        "tipoElastic": "clave_ordenado"
    },

    "dependencia_id": {
        "titulo"     : "Dependencia especifica",
        "tipo"       : "texto",
        "longitud"   : 60,
        "tipoElastic": "clave"
    },

    "pqrs": {
        "titulo"     : "Pqrs",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 30,
        "tipoElastic": "clave_ordenado"
    },

    "_estado_": {
        "titulo"     : "Estado",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 60,
        "unico"      : "si",
        "tipoElastic": "texto_ordenado"
    }
}
campos.update(base_general_campos.campos)

# Campos elastic
camposIndexamiento = {
    "dependencia_nombre": {
        "tipoElastic": "texto_ordenado"
    }
}

camposElastic = campos
camposElastic.update(camposIndexamiento)

definicion = {
    "descripcion" : "Peticiones",
    "clase"       : "base_general",
    "estructura"  : "peticion",    
    # Campos de la estructura
    "campos"      : campos,
    "camposIndexamiento": camposIndexamiento,

    # Referencias a otras estructuras
    "referencias" : [
        {
            # Información local
            "campoReferencia"    : "dependencia_id",
            "atributosReferencia": [{
                "ubicacion_nombre"   : "nombre",
            }],
            "modo"           : "simple",

            # Información destino
            "estructuraDestino": "dependencia",
            "campoDestino"     : "id",            
        },        
    ],

    "campoIndice" : "id",
    "indexa"      : "si",

    "indexamiento": {
        "busqueda": {
            "excludes": []
        },

        "mapeo": {
            "excludes": []
        }

    }
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
globales.carga_procesamiento(definicion["estructura"], "armar_estructura",     baseGeneral_estructura.armar_estructura)
globales.carga_procesamiento(definicion["estructura"], "normaliza_estructura", baseGeneral_estructura.normaliza_estructura)