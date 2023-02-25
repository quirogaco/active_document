    #!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint
from datetime import datetime

from elasticsearch_dsl import Q as Q_dsl

from librerias.datos.base import globales

def campos_lista(campos):
    if (type(campos)) == str:
        campos = [campos]

    return campos

def texto_contiene_valor(texto, modo="ambos"):
    texto          = str(texto).strip().lower()
    lista_texto    = texto.split()
    elementos      = len(lista_texto)
    lista_busqueda = [] 
    for elemento in lista_texto:
        elemento = elemento.strip()
        if (len(elemento) > 0):
            if (elemento not in ['y', 'o']) or (elementos == 1):
                if (elemento[-1] != "*") and modo in ["ambos", "despues"]:
                    elemento = elemento + "*"
                    
                if (elemento[0] != "*") and modo in ["ambos", "antes"]:
                    elemento = "*" + elemento

            lista_busqueda.append(elemento)

    texto_final = " ".join(lista_busqueda)  
    texto_final = texto_final.replace( " y ", " AND ").replace( " o ", " OR ")

    return texto_final

#########
# TEXTO #
#########
# Busca texto contenido en el valor
def contiene_texto(campos, valor, opciones={}):
    valor  = texto_contiene_valor(valor)
    campos = campos_lista(campos)
    query = Q_dsl("query_string", query = valor, fields=campos )

    return query

# Busca texto que esta al comienzo en el valor
def comienza_con(campo, valor, opciones={}):
    valor   = texto_contiene_valor(valor, "despues")
    retorna = None
    if valor != "":
        campos  = campos_lista(campo)
        query   = Q_dsl("query_string", query = valor, fields=campos )
        retorna =  query
    
    return retorna

# Busca texto que esta al final en el valor
def termina_con(campos, valor, opciones={}):    
    valor   = texto_contiene_valor(valor, "antes")
    retorna = None
    if valor != "":
        campos  = campos_lista(campos)
        query   = Q_dsl("query_string", query = valor, fields=campos )
        retorna =  query
    
    return retorna

def termino_query(campo, valor):    
    if ( isinstance(valor, list) ):
        query = Q_dsl("terms", **{campo: valor} )
    else:
        query = Q_dsl("term", **{campo: valor} )

    return query 

# Busca texto igual al valor
def texto_igual(campo, valor, opciones={}):
    # Solo funciona con palabras completas 
    campo = campo + "." + "normalizado"
    query = termino_query(campo, valor)    

    return query

# Busca texto diferente al valor
def texto_diferente(campo, valor, opciones={}):
    # Solo funciona con palabras completas 
    # Hereda lowercase settings analysis
    # valor = str(valor).lower()
    campo = campo + "." + "normalizado"
    query = ~termino_query(campo, valor)

    return query

###################
# CLAVE - KEYWORD #
###################

# Busca texot igual al valor, para claves
def termino_igual(campo, valor, opciones={}):
    query = termino_query(campo, valor)

    return query

# Busca texto contenido en el valor
def contiene_clave(campos, valor, opciones={}):
    valor  = texto_contiene_valor(valor)
    campos = campos + "." + "normalizado"
    campos = campos_lista(campos)
    query  = Q_dsl("query_string", query = valor, fields=campos )

    return query

#########
# TEXTO ANTERIOR #
#########

# Busca texto NO contenido en el valor
def no_contiene_texto(campos, valor, opciones={}):
    valor  = texto_contiene_valor(valor)
    campos = campos_lista(campos)
    query  = ~Q_dsl("query_string", query = valor, fields=campos )

    return query

# Busca texto igual a blanco, nullo
def texto_blanco(campo, opciones={}):
    query = Q_dsl( 
        Q_dsl("match", **{campo: ""})     | \
        Q_dsl("match", **{campo: "None"}) | \
        Q_dsl("match", **{campo: "NONE"})
    )

    return query

# Busca texto igual a blanco, nullo
def texto_no_blanco(campo, opciones={}):
    query = Q_dsl( 
        ~Q_dsl("match", **{campo: ""})     | \
        ~Q_dsl("match", **{campo: "None"}) | \
        ~Q_dsl("match", **{campo: "NONE"})
    )

    return query

###################
# RANGO           #
###################

# Mayor o igual
def mayor_igual(campo, valor, opciones={}):
    #valor = str(valor).replace(" ", "T")
    query = Q_dsl("range", **{campo: {'gte': valor}} )

    return query

# Mayor
def mayor_que(campo, valor, opciones={}):
    #valor = str(valor).replace(" ", "T")
    query = Q_dsl("range", **{campo: {'gt': valor}} )

    return query

# Menor o igual
def menor_igual(campo, valor, opciones={}):
    #valor = str(valor).replace(" ", "T")
    query = Q_dsl("range", **{campo: {'lte': valor}} )

    return query

# Menor
def menor_que(campo, valor, opciones={}):
    #valor = str(valor).replace(" ", "T")
    query = Q_dsl("range", **{campo: {'lt': valor}} )

    return query


filtrosElasticTipo = {
    # TEXTO 
    "texto": {
        "contiene"   : contiene_texto, 
        "nocontiene" : no_contiene_texto, 
        "comienzacon": comienza_con, 
        "terminacon" : termina_con, 
        "="          : texto_igual, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },

    "texto_ordenado" : {
        "contiene"   : contiene_texto, 
        "nocontiene" : no_contiene_texto, 
        "comienzacon": comienza_con, 
        "terminacon" : termina_con, 
        "="          : texto_igual, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },

    # TEXTO BASE
    "texto_base": {
        "contiene"   : contiene_texto, 
        "nocontiene" : no_contiene_texto, 
        "comienzacon": comienza_con, 
        "terminacon" : termina_con, 
        "="          : texto_igual, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },

    # CLAVE
    "clave": {
        #"contiene"   : contiene_texto, 
        "contiene"   : contiene_clave,
        "nocontiene" : no_contiene_texto, 
        "comienzacon": comienza_con, 
        "terminacon" : termina_con, 
        "="          : termino_igual, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco,          
    },

    "clave_ordenado": {
        #"contiene"   : contiene_texto, 
        "contiene"   : contiene_clave,
        "nocontiene" : no_contiene_texto, 
        "comienzacon": comienza_con, 
        "terminacon" : termina_con, 
        "="          : texto_igual, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },

    # estos no son correctos !!!!
    # FECHA
    "fecha": {
        "contiene"   : contiene_texto, 
        "nocontiene" : no_contiene_texto, 
        "="          : texto_igual, 
        ">="         : mayor_igual, 
        "<="         : menor_igual, 
        ">"          : mayor_que, 
        "<"          : menor_que, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },

    "fecha_ordenado": {
        "contiene"   : contiene_texto, 
        "nocontiene" : no_contiene_texto, 
        "="          : texto_igual, 
        ">="         : mayor_igual, 
        "<="         : menor_igual, 
        ">"          : mayor_que, 
        "<"          : menor_que, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },


    "fechaHora": {
        "contiene"   : contiene_texto, 
        "nocontiene" : no_contiene_texto, 
        "="          : texto_igual, 
        ">="         : mayor_igual, 
        "<="         : menor_igual, 
        ">"          : mayor_que, 
        "<"          : menor_que, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },

    "fechaHora_ordenado" : {
        "contiene"   : contiene_texto, 
        "nocontiene" : no_contiene_texto, 
        "="          : texto_igual, 
        ">="         : mayor_igual, 
        "<="         : menor_igual, 
        ">"          : mayor_que, 
        "<"          : menor_que, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },

#[  "entre", "esblanco", "noesblanco" ],

    "entero": {
        "="          : texto_igual, 
        ">="         : mayor_igual, 
        "<="         : menor_igual, 
        ">"          : mayor_que, 
        "<"          : menor_que, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },

    "entero_ordenado" : {
        "="          : texto_igual, 
        ">="         : mayor_igual, 
        "<="         : menor_igual, 
        ">"          : mayor_que, 
        "<"          : menor_que, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },

    "uuid": {
        "contiene"   : contiene_texto, 
        "="          : texto_igual, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },

    # LISTA TEXTO     
    "lista_texto": {
        "contiene"   : contiene_texto, 
        "nocontiene" : no_contiene_texto, 
        "comienzacon": comienza_con, 
        "terminacon" : termina_con, 
        "="          : texto_igual, 
        "<>"         : texto_diferente, 
        "esblanco"   : texto_blanco, 
        "noesblanco" : texto_no_blanco, 
    },
}

expresionesEspanol = {
    "notcontains": "nocontiene",
    "contains": "contiene",
    "startswith": "comienzacon",
    "endswith": "terminacon",
    "isblank": "esblanco",
    "isnotblank": "noesblanco",
    "between": "entre",
    "=": "=",
    "<>": "<>",
    "<": "<",
    ">": ">",
    "<=": "<=",
    ">=": ">="
}

filtrosTipo = {
    "texto": [
        "contiene", 
        "nocontiene", 
        "comienzacon", 
        "terminacon", 
        "=", 
        "<>", 
        "esblanco", 
        "noesblanco" 
    ],

    "clave": [
        "=", 
        "<>", 
        "esblanco", 
        "noesblanco" 
    ],

    "entero": [ 
        "=", 
        "<>", 
        "<", 
        ">", 
        "<=", 
        ">=", 
        "entre", 
        "esblanco", 
        "noesblanco" 
    ],

    "entero_ordenado": [ 
        "=", 
        "<>", 
        "<", 
        ">", 
        "<=", 
        ">=", 
        "entre", 
        "esblanco", 
        "noesblanco" 
    ],

    "flotante": [ 
        "=", 
        "<>", 
        "<", 
        ">", 
        "<=", 
        ">=", 
        "entre",
         "esblanco", 
         "noesblanco" 
    ],

    "fecha": [ 
        "=", 
        "<>", 
        "<", 
        ">", 
        "<=", 
        ">=", 
        "entre", 
        "esblanco", 
        "noesblanco" 
    ],

    "fechaHora": [ 
        "=", 
        "<>", 
        "<", 
        ">", 
        "<=", 
        ">=", 
        "entre", 
        "esblanco", 
        "noesblanco"
    ],

    "logico": [ 
        "=", 
        "<>", 
        "esblanco", 
        "noesblanco" 
    ],

    "objecto": [ 
        "esblanco", 
        "noesblanco" 
    ],

    "lista": [ 
        "esblanco", 
        "noesblanco", 
        "contiene", 
        "nocontiene" 
    ],

    "lista_texto": [
        "contiene", 
        "nocontiene", 
        "comienzacon", 
        "terminacon", 
        "=", 
        "<>", 
        "esblanco", 
        "noesblanco" 
    ]
}