#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#########
# TEXTO #
#########

# TEXTO GRANDE, solo busquedas
# No tiene ordenamiento: ordenado
# No tiene valor fijo: keyword
# EJ. asunto, detalle
texto_base = {
    'store'      : True,
    'type'       : "text",
    'term_vector': 'with_positions_offsets',  # Terms, positions, and character offsets are stored.
    'analyzer'   : "no_accent" 
}

# TEXTO
# Busquedas abiertas: indexado base.
# Ordenar: normalizado
# Busqueda exacto: normalizado
texto = {
    'type'       : "text",
    'store'      : True,
    'analyzer'   : "no_accent",  
    'term_vector': 'with_positions_offsets',
    'fields'     : { 
        'normalizado': {
            "type"      : "keyword",
            "normalizer": "normalizado" 
        }
    }
}

#########
# FECHA #
#########
# Busquedas abiertas: indexado base.
# Ordenar: normalizado
# Busqueda exacto: normalizado
fecha = {    
    'type'      : 'date',
    'store'     : True,
    'format'    : "YYYY-MM-DD'T'HH:mm:ss+00:00||yyyy-MM-dd'T'HH:mm:ss||yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis||strict_date_optional_time",
    "null_value": 0,
    'ignore_malformed': True,
    'fields'     : { 
        'normalizado': {
            "type"      : "keyword",
            "normalizer": "normalizado"
        }
    }
}

#########
# CLAVE #
#########
# Valor exacto sin analizar
clave = {
    'store': True,
    'type' : "keyword",
    'fields'     : { 
        'normalizado': {
            "type"      : "keyword",
            "normalizer": "normalizado" 
        }
    }    
}

############
# ANIDADOS #
############
# Lista de objetos
def anidados(propiedades):
    modelo = {
        "type"      : "nested",
        "properties": propiedades
    }

    return modelo

#######################
# JSON SON ESTRUCTURA #
#######################
objeto = {
    "type" : "object"
}

########################
# LISTA TEXTO ORDENADO #
########################
lista_texto  = {
    'store'      : True,
    'type'       : "text",
    'term_vector': 'with_positions_offsets',  # Terms, positions, and character offsets are stored.
    'analyzer'   : "no_accent" 
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
    'fields'     : { 
        'normalizado': {
            "type"      : 'integer'
        }
    }
}

#############################
# ANTERIOR NO APLICAN AHORA #
#############################

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


# LISTA
lista  = {
    "type"   : "text",
    "index"  : False,
}


# VALORES SEPARADOS POR COMA
coma = {
    'store'  : True,
    'type'   : "text"
}

#############################
# Tipos de campos           #
# Indexamiento estructuras  #
#############################
texto_elastic = {
    'tipoElastic': 'texto'
}