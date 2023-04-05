#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# TEXTO ANALIZADO FULL TEXTO
texto = {
    'store'      : True,
    'type'       : "text",
    'term_vector': 'with_positions_offsets',  # Terms, positions, and character offsets are stored.
    'analyzer'   : "no_accent"
}

# TEXTO CON CAMPOS PARA ORDENAMIENTO
texto_ordenado = {
    'store'      : True,
    'type'       : "text",
    'analyzer'   : "no_accent",
    'fields'     : { 
        'sort': {
            'type': "keyword" 
        }  
    }
}

clave = {
    'store'      : True,
    'type'       : "text",
    'analyzer'   : "no_accent"
}

# CLAVE CON CAMPOS PARA ORDENAMIENTO
# Aunque su valor por defecto permite ordenadar
# La rutina le adiciona la expresión ".sort"
clave_ordenado = {
    'store'      : True,
    'type'       : "text",
    'analyzer'   : "no_accent",
    'fields'     : { 
        'sort': {
            'type': "keyword" 
        }  
    }
}

"""
# CLAVE -> VALOR COMPLETO NO ANALIZADO
clave = {
    'store' : True,
    'type'  : "keyword"
}

# CLAVE CON CAMPOS PARA ORDENAMIENTO
# Aunque su valor por defecto permite ordenadar
# La rutina le adiciona la expresión ".sort"
clave_ordenado = {
    'store' : True,
    'type'  : "keyword",
    'analyzer': "no_accent",
    'fields'     : { 
        'sort': {
            'type': "keyword" 
        }  
    }
}
"""

# FECHA
fechaHora = {
    'store'           : True,
    'type'            : 'date',
    'format'          : "yyyy-MM-dd HH:mm:ss",
    'ignore_malformed': True
}

# FECHA ORDENADA
fechaHora_ordenado = {
    'store'           : True,
    'type'            : 'date',
    'format'          : "yyyy-MM-dd HH:mm:ss",
    'ignore_malformed': True,
    'fields'          : {
        'sort': {
            'type': "keyword"
        } 
    }
}

# SOLO FECHA
fecha = {
    'store'           : True,
    'type'            : 'date',
    #'ignore_malformed': True,
    'format'          : "YYYY-MM-dd"
}

# FECHA ORDENADA
fecha_ordenado = {
    'store'           : True,
    'type'            : 'date',
    'ignore_malformed': True,
    'format'          : "YYYY-MM-dd",
    'fields'          : {
        'sort': {
            'type': "keyword"
        } 
    }
}

# ENTERO
entero = {
    'store'           : True,
    'type'            : 'integer',
    'ignore_malformed': True
}

# ENTERO ORDENADO
entero_ordenado = {
    'store'           : True,
    'type'            : 'integer',
    'ignore_malformed': True,
    'fields'          : {
        'sort': {
            'type': "keyword"
        } 
    }
}

# DECIMAL
decimal = {
    'store'           : True,
    'type'            : 'float',
    'ignore_malformed': True
}

# DECIMAL ORDENADO
decimal_ordenado = {
    'store'           : True,
    'type'            : 'float',
    'ignore_malformed': True,
    'fields'          : {
        'sort': {
            'type': "keyword"
        } 
    }
}

# NUMERICO LARGO
largo = {
    'store'           : True,
    'type'            : 'long',
    'ignore_malformed': True
}

# NUMERICO LARGO ORDENADO
largo_ordenado = {
    'store'           : True,
    'type'            : 'long',
    'ignore_malformed': True,
    'fields'          : {
        'sort': {
            'type': "keyword"
        } 
    }
}

# VALORES ANIDADOS
def anidados(propiedades):
    modelo = {
        "type"      : "nested",
        "properties": propiedades
    }

    return modelo

# LISTA
lista  = {
  "type"   : "text",
  "index"  : False,
}

# LISTA PARA BUSQUEDA
lista_busqueda = {
  "store"    : True,
  "type"     : "keyword"
}

# VALORES SEPARADOS POR COMA
coma = {
  'store'  : True,
  'type'   : "text"
}