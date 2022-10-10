#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes
from librerias.datos.sql                    import sqalchemy_comunes

# Calcula vencimiento
def calcula_vencimiento(_r):
    vence_en = None
    if (_r.estado == "ENTREGADO"):
        vence_en = _r.fecha_entrega + datetime.timedelta(15)

    if (_r.estado == "RENOVADO"):
        vence_en = _r.fecha_renovacion + datetime.timedelta(15)

    return vence_en

campos = {
    "expediente_id"    : tipos.clave_obligatorio(propiedades={"titulo": "Expediente id", "longitud": 60}),  
    "expediente_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Nombre expediente", "longitud": 256}),  
    "archivo_etapa"    : tipos.texto_obligatorio(propiedades={"titulo": "Etapa de archivo", "longitud": 60}),   # GESTION, CENTRAL    
    "usuario_id"       : tipos.clave_obligatorio(propiedades={"titulo": "Usuario id", "longitud": 60}), 
    "usuario_nombre"   : tipos.texto(propiedades={"columna": "no", "titulo": "Nombre usuario", "longitud": 256}),  

    "estado"          : tipos.clave_obligatorio(propiedades={"titulo": "Estado", "longitud": 60, "defecto": "PRESTADO"}), # PRESTADO,DEVUELTO
    "archivo_origen"  : tipos.clave_obligatorio(propiedades={"titulo": "Expediente id", "longitud": 60, "defecto": "TVD"}), 
    "motivo"          : tipos.texto(propiedades={ "titulo": "Detalle", "longitud": 256}),  
    "anotacion"       : tipos.texto(propiedades={ "titulo": "Anotación", "longitud": 256}),  

    "fecha_peticion"   : tipos.fecha(propiedades={"titulo": "Fecha petición"}), 
    "fecha_entrega"    : tipos.fecha(propiedades={"titulo": "Fecha entrega"}), 
    "fecha_devolucion" : tipos.fecha(propiedades={"titulo": "Fecha devolución"}), 
    "fecha_renovacion" : tipos.fecha(propiedades={"titulo": "Fecha renovación"}), 
    "fecha_vencimiento": tipos.fecha(propiedades={"columna": "no", "titulo": "Fecha vencimiento", "propiedad": calcula_vencimiento}), 
    "vencido"          : tipos.clave_obligatorio(propiedades={"titulo": "Vencido", "longitud": 60, "defecto": "NO"}),
    "renovaciones"     : tipos.entero(propiedades={"titulo": "Número de renovaciones"}), 
}

referencias = [
    # Expedientes tvd
    {
        "campoReferencia"    : "expediente_id",
        "atributosReferencia": [{
            "expediente_nombre": "nombre"
        }],
        "estructuraDestino": "agn_expedientes_tvd",
        "campoDestino"     : "id",            
    },

    # Usuario peticionario
    {
        "campoReferencia"    : "usuario_id",
        "atributosReferencia": [{
            "usuario_nombre": "nombre"
        }],
        "estructuraDestino": "usuarios",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Prestamo de expediente TVD",
    "clase"       : "agn_prestamos_tvd",
    "estructura"  : "agn_prestamos_tvd",    
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