#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
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
    "accion"    : tipos.texto_obligatorio(propiedades={"titulo": "Accion", "longitud": 20, "reporte": "SI"}), 
    "codigo"    : tipos.texto_obligatorio(propiedades={"titulo": "Codigo del usuario", "longitud": 50, "reporte": "SI"}),   
    "ip_maquina": tipos.texto_obligatorio(propiedades={"titulo": "Ip maquina", "longitud": 50, "reporte": "SI"}),  
    "estado"    : tipos.texto_obligatorio(propiedades={"titulo": "Estado acción", "longitud": 120, "reporte": "SI"}),  
    "accion_en" : tipos.fecha_obligatorio(propiedades={"titulo": "Fecha evento", "reporte": "SI"}), 
}

referencias = []

definicion = {
    "descripcion" : "Log de ingresos",
    "clase"       : "config_logs_ingreso",
    "estructura"  : "logs_ingreso",    
    "campos"      : campos,
    "referencias" : referencias,
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