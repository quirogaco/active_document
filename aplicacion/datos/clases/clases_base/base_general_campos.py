#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

campos = {
    "id": {
        "titulo"     : "Id del registro",
        "tipo"       : "uuid",
        "obligatorio": "si",
        "longitud"   : 50,
        "unico"      : "si",
        "sistema"    : "si",
        "tipoElastic": "texto"
    },

    "estado_": {
        "titulo"     : "Estado del registro",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 20,
        "sistema"    : "si",
        "tipoElastic": "texto"
    },

    "creado_en_": {
        "titulo"     : "Fecha de creación",
        "tipo"       : "fechaHora",
        "obligatorio": "si",
        "sistema"    : "si",
        "tipoElastic": "fecha"
    },

    "actualizado_en_": {
        "titulo"     : "Fecha de actualización",
        "tipo"       : "fechaHora",
        "obligatorio": "si",
        "sistema"    : "si",
        "tipoElastic": "fecha"
    },

    "codigo_unidad_": {
        "titulo"     : "Codigo de la unidad",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 20,
        "sistema"    : "si",
        "tipoElastic": "texto"
    },

    "codigo_organizacion_": {
        "titulo"     : "Codigo de la organización",
        "tipo"       : "texto",
        "obligatorio": "si",
        "longitud"   : 20,
        "sistema"    : "si",
        "tipoElastic": "texto"
    },
}