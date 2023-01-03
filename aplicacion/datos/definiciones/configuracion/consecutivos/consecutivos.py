#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes

campos = {
    "nombre": tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 120, "reporte": "SI"}),  
    "consecutivo": tipos.entero({"titulo": "Valor del consecutivo", "reporte": "SI"}),
    "estado_": tipos.texto_obligatorio(propiedades={"titulo": "Estado", "reporte": "SI"})    
}

definicion = {
    "descripcion" : "Consecutivo",
    "clase"       : "config_consecutivos",
    "estructura"  : "consecutivos",    
    "campos"      : campos,
    "campoIndice" : "id",
    "indexa"      : "si",
    "indexamiento": {},
    "reporte"     : "SI" # Fuente de datos para REPORTES
}
# Crea clase SQLALCHEMY
CLASE = sqalchemy_clase_dinamica.crea_clase( definicion, (base_general.DB_BASE_SIMPLE, globales.CLASE_BASE_SQL) )
globales.carga_clase(definicion["clase"], CLASE)

camposIndexamiento = {}
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)