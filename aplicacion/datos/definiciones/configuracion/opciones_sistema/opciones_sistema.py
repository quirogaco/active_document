#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint

from librerias.utilidades import basicas  

# Definiciones sql
from librerias.datos.sql                 import sqalchemy_declarativa_base as dbase
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base import base_general
from librerias.datos.sql                 import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                 import sqalchemy_clase_dinamica
from librerias.datos.base                import globales
from librerias.datos.validacion          import valida 
from librerias.datos.elastic             import elastic_utilidades, elastic_operaciones

campos = {
    "clase"            : tipos.texto_obligatorio(propiedades={"titulo": "Clase",                  "longitud": 60}), 
    #"codigo"          : tipos.texto_obligatorio(propiedades={"titulo": "Codigo de la opción",    "longitud": 60}), 
    "titulo"           : tipos.texto_obligatorio(propiedades={"titulo": "Titulo de la opción",    "longitud": 120}), 
    "ruta"             : tipos.texto(            propiedades={"titulo": "Ruta",                   "longitud": 60}), 
    "componente"       : tipos.texto_obligatorio(propiedades={"titulo": "Componente",             "longitud": 60}), 
    "icono"            : tipos.texto(            propiedades={"titulo": "icono",                  "longitud": 60}),
    "tipo"             : tipos.texto_obligatorio(propiedades={"titulo": "Tipo (importar)",        "longitud": 60}),
    "navegar"          : tipos.texto_obligatorio(propiedades={"titulo": "Navegar",                "longitud": 20}),   
    "padre"            : tipos.texto(            propiedades={"titulo": "Padre (Nivel superior)", "longitud": 120}),
    "entidad"          : tipos.texto(            propiedades={"titulo": "Entidad  especifica",    "longitud": 60})
}

definicion = {
    "descripcion" : "Opciones del sistema",
    "clase"       : "config_opciones_sistema",
    "estructura"  : "opciones_sistema",
    "campos"      : campos,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {}
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

# Publica definicion de estructura
globales.carga_definicion(definicion["estructura"], definicion)

##### VALIDACIÓN #######
# Genera modelo de validación
validador = valida.definirModelo(definicion["estructura"], definicion["campos"])
# Publica modelo de validacion
globales.carga_validador(definicion["estructura"], validador)

##### ELASTIC #######
# Genera modelo de elastic
elastic_modelo, runtime, querytime = elastic_utilidades.generaModelo(definicion["campos"], definicion["indexamiento"], definicion["estructura"])

# Registra modelo de elastic
elastic_utilidades.registraModelo(
    definicion["estructura"], 
    elastic_modelo, 
    definicion["indexamiento"], 
    definicion.get("campoIndice", "id") 
)
elastic_operaciones.creaIndice(definicion["estructura"], "base")