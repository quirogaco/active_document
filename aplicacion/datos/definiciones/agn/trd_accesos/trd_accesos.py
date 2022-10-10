#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pprint

# Definiciones sql
from librerias.datos.base                import globales

# Base general con atributos basicos
from aplicacion.datos.clases.clases_base    import base_general
from librerias.datos.sql                    import sqalchemy_tipo_campos as tipos
from librerias.datos.sql                    import sqalchemy_clase_dinamica
from librerias.datos.base                   import globales
from aplicacion.datos.definiciones._comunes import elementos_comunes
from librerias.datos.sql                    import sqalchemy_comunes

# Usuarios autorizados
def usuarios_autorizados(_r):
    lista = []
    """
    # Caga Carpetas 
    USUARIOS_CLASE = globales.lee_clase("usuarios")
    GRUPOS_CLASE = globales.lee_clase("grupo_usuarios")
    sesion           = sqalchemy_comunes.nuevaSesion("base") 
    filtros          = and_( DOCUMENTOS_CLASE.expediente_id == _r.id, DOCUMENTOS_CLASE.tabla == "TRD")
    documentos       = sesion.query(DOCUMENTOS_CLASE).filter( filtros ).all()        
    for documento in documentos:
        datos = {
            "id"                 : documento.id,
            "tipo_nombre"        : documento.tipo_nombre,
            "tipo_detalle"       : documento.tipo_nombre + ' / ' + documento.detalle,
            "detalle"            : documento.detalle,
            "fecha_creacion"     : documento.fecha_creacion,
            "fecha_incorporado"  : documento.fecha_incorporado,
            "soporte"            : documento.soporte,
            "folios_fisicos"     : documento.folios_fisicos,
            "folios_electronicos": documento.folios_electronicos,
            "tipo_archivo"       : documento.tipo_archivo,
            "tamano"             : documento.tamano,
            "fecha_funcion"      : documento.fecha_funcion,
            "observacion"        : documento.observacion,
            "valor_huella"       : str(random.getrandbits(random.randint(10, 99)))
        }
        lista.append(datos)
    sesion.close()
    """

    return lista

campos = {
    # Elemento de permisos
    "elemento_tipo": tipos.clave_obligatorio(propiedades={"titulo": "Elemento tipo", "longitud": 60}),
    "elemento_id"  : tipos.clave_obligatorio(propiedades={"titulo": "Elemento id", "longitud": 60}),    
    "autorizacion" : tipos.texto_obligatorio(propiedades={"titulo": "Autorización", "longitud": 60}),   
    "autorizados"  : tipos.json(propiedades={"titulo": "Usuarios autorizados", "defecto": 'json'}), 
    "usuarios_autorizados": tipos.clave(propiedades={"columna": "no", "titulo": "Usuarios autorizados", "propiedad": usuarios_autorizados}),
}

definicion = {
    "descripcion" : "Autorizaciones de acceso (Tabla de acceso)",
    "clase"       : "agn_accesos_trd",
    "estructura"  : "agn_accesos_trd",    
    "campos"      : campos,
    "referencias" : [],
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