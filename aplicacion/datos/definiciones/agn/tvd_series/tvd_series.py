#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint

from sqlalchemy import and_

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes
from librerias.datos.sql                    import sqalchemy_comunes

# Arbol de SERIE
def tvd_serie(_r):
    arbol = []

    # Caga Series
    SUBSERIE_CLASE = globales.lee_clase("agn_subserie_tvd")
    sesion         = sqalchemy_comunes.nuevaSesion("base") 
    filtros        = and_( SUBSERIE_CLASE.serie_id == _r.id, SUBSERIE_CLASE.tabla == "TVD")
    subseries      = sesion.query(SUBSERIE_CLASE).filter( filtros ).all()
    for subserie in subseries:
        datos = {
            "id"      : subserie.id,
            "codigo"  : subserie.codigo,
            "nombre"  : subserie.nombre,
            "padre_id": _r.id,
            "tipo"    : "subserie"          
        }
        arbol.append(datos)
        arbol.extend(subserie.subserie_arbol)
    sesion.close()

    return arbol

campos = {
    # TRD/TVD
    "tabla"              : tipos.clave(propiedades={"titulo": "TRD/TVD", "longitud": 60}),
    
    # Dependencia padre
    "dependencia_id"    : tipos.clave_obligatorio(propiedades={"titulo": "Dependencia padre id", "longitud": 60}),
    "dependencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia descripción", "longitud": 250}),
    "periodo"           : tipos.texto(propiedades={"columna": "no", "titulo": "Tvd periodo", "longitud": 250}),   
    "activa"            : tipos.texto(propiedades={"columna": "no", "titulo": "Tvd activa", "longitud": 250}),      

    "codigo"            : tipos.clave_obligatorio(propiedades={"titulo": "Codigo", "longitud": 60}),  
    "nombre"            : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 250}), 

    # Retención
    "central"           : tipos.entero(propiedades={"titulo": "Años en archivo central"}), 

    # Disposición
    "eliminacion"         : tipos.texto(propiedades={"titulo": "Eliminación", "defecto": "NO"}),    
    "seleccion"           : tipos.texto(propiedades={"titulo": "Selección", "defecto": "NO"}),  
    "conservacion"        : tipos.texto(propiedades={"titulo": "Conservación", "defecto": "NO"}),  
    "micro_digitalizacion": tipos.texto(propiedades={"titulo": "Micro digitalización", "defecto": "NO"}),  
    "serie_arbol"         : tipos.texto(propiedades={"columna": "no", "tipoElastic": "objeto", "titulo": "Tvd serie", "propiedad": tvd_serie})
}

referencias = [
    # Dependencia Tvd
    {
        "campoReferencia"    : "dependencia_id",
        "atributosReferencia": [{
            "dependencia_nombre": "nombre",
            "periodo"           : "tvd_periodo",
            "activa"            : "tvd_estado",
        }],
        "estructuraDestino": "agn_dependencia_tvd",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Serie Tabla de Valoración",
    "clase"       : "agn_serie_tvd",
    "estructura"  : "agn_serie_tvd",    
    "campos"      : campos,
    "referencias" : referencias,
    "campoIndice" : "id",
    "indexa"      : "si",
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