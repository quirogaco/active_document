#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_leer
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes

############################
# INFORMACION DEL RADICADO #
############################
def carga_radicado(_r):    
    if getattr(_r, "_radicado", None) is None:
        # print("")
        # print("")
        # print("")
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print("RELACIONES", _r.tipo, _r.origen_id)
        radicado = {}
        if (_r.tipo == "ENTRADA"):
            radicado = sqalchemy_leer.leer_un_registro("radicados_entrada", _r.origen_id)

        if (_r.tipo == "SALIDA"):
            radicado = sqalchemy_leer.leer_un_registro("radicados_salida", _r.origen_id)

        if (_r.tipo == "INTERNO"):
            radicado = sqalchemy_leer.leer_un_registro("radicados_interno", _r.origen_id)
        
        if radicado == None:
            setattr(_r, "_radicado", {})
        else:
            setattr(_r, "_radicado", radicado)

def nro_radicado(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("nro_radicado", "")

def fecha_radicado(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("fecha_radicado", None)

def tercero_nombres_apellidos(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("tercero_nombres_apellidos", "")

def tercero_razon_social(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("tercero_razon_social", "")

def tercero_clase(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("tercero_clase", "")

def tercero_tipo_tercero_nombre(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("tercero_tipo_tercero_nombre", "")
    
def asunto(_r):
    carga_radicado(_r)
    
    return _r._radicado.get("asunto", "")

campos = {
    # Clasificación
    # fuente: VENTANILLA,PQRS,TRAMITE -> tipo: ENTRADA o INTERNO.
    # fuente: GESTION  -> tipo:TRAMITE
    # relacion: GENERA,REPONE,COLABORA?..    
    "fuente"          : tipos.texto_obligatorio(propiedades={"titulo": "Origen de gestión", "longitud": 60}),         
    "tipo"            : tipos.texto_obligatorio(propiedades={"titulo": "Tipo de origen", "longitud": 60}),  
    "relacion"        : tipos.clave_obligatorio(propiedades={"titulo": "Tipo de relación ", "longitud": 60}),  
    "origen_id"       : tipos.clave_obligatorio(propiedades={"titulo": "Id del elemento origen ", "longitud": 60}),         
    "gestion_id"      : tipos.clave_obligatorio(propiedades={"titulo": "Id del elemento origen ", "longitud": 60}),         
    
    # Informacion del radicado
    "nro_radicado"               : tipos.clave(propiedades={"columna": "no", "titulo": "Número radicado", "longitud": 50,    "propiedad": nro_radicado}), #, "propiedad": nro_radicado}),
    "fecha_radicado"             : tipos.clave(propiedades={"columna": "no", "titulo": "Número radicado", "longitud": 50,    "propiedad": fecha_radicado}),
    "tercero_nombres_apellidos"  : tipos.clave(propiedades={"columna": "no", "titulo": "Nombres apellidos", "longitud": 250, "propiedad": tercero_nombres_apellidos}),
    "tercero_razon_social"       : tipos.clave(propiedades={"columna": "no", "titulo": "Razón social", "longitud": 250,      "propiedad": tercero_razon_social}),
    "tercero_clase"              : tipos.clave(propiedades={"columna": "no", "titulo": "Clase remitente", "longitud": 250,   "propiedad": tercero_clase}),
    "tercero_tipo_tercero_nombre": tipos.clave(propiedades={"columna": "no", "titulo": "Tipo remitente", "longitud": 250,    "propiedad": tercero_tipo_tercero_nombre}), 
    "asunto"                     : tipos.clave(propiedades={"columna": "no", "titulo": "Asunto", "longitud": 50,             "propiedad": asunto}),
}

definicion = {
    "descripcion" : "Gestión relaciones",
    "clase"       : "gestor_peticion_relaciones",
    "estructura"  : "gestor_peticion_relaciones",    
    "campos"      : campos,
    "referencias" : [],
    "campoIndice" : "id",
    #"indexa"      : "si",
    "indexamiento": {}
}

# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

# Campos elastic
camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)