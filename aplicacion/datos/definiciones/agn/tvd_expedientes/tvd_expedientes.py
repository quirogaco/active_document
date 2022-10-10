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
from librerias.datos.sql                    import sqalchemy_comunes

# Carpetas por expedientes
def tvd_carpeta(_r):
    arbol = []

    # Caga Carpetas
    CARPETA_CLASE = globales.lee_clase("agn_carpetas_tvd")
    sesion        = sqalchemy_comunes.nuevaSesion("base") 
    tipos         = sesion.query(CARPETA_CLASE).filter( CARPETA_CLASE.expediente_id == _r.id ).all()
    for tipo in tipos:
        datos = {
            "id"      : tipo.id,
            "nombre"  : tipo.nombre,
            "padre_id": _r.id,
            "tipo"    : "carpeta"          
        }
        arbol.append(datos)
    sesion.close()

    return arbol

def serie_subserie(_r):
    nombre = _r.serie_nombre
    if (_r.subserie_nombre not in ["", None]):
        nombre += "/" + _r.subserie_nombre

    return nombre

def tipo_expediente(_r):
    fisicos      = 0
    electronicos = 0
    tipo       = "FISICO"

    return tipo

"""
# Unidad de conservaci�n
soporte             = Column( Unicode(128), nullable=True, default=u'' )
frecuencia_consulta = Column( Unicode(10), nullable=True,  default=u'BAJO' )
notas               = Column( Unicode(512), nullable=True, default=u'' )
etapa_recomendada   = Column( Unicode(20), nullable=True,  default=u'GESTION' )

###
s_topografica_exp   = Column( Unicode(30), nullable=True, default=u'' ) # signatura_topografica

# Indice electronico y firma del indice
indice_id           = Column( Unicode(50), index=True, nullable=True, default="" )
indice_firma_id     = Column( Unicode(50), index=True, nullable=True, default="" )
fecha_firma         = Column( DateTime, nullable=True, default=None)

# Vencimientos Tvd
vencido_gestion     = Column( Unicode(64), nullable=True, index=True, default=u'NO' ) # Si ya se vencio en gesti�n: "SI", "NO"
vencido_central     = Column( Unicode(64), nullable=True, index=True, default=u'NO' ) # Si ya se vencio en central: "SI", "NO"
# Informac�n transferencia
transferir          = Column( Unicode(64), nullable=True, default=u'SI' )  # Si se permite la transferncia o no
motivo_transferir   = Column( Unicode(256), nullable=True, default=u'' ) # Motivo para transferir o no tranferir. 

# Aplicaci�n Tvd
aplicacion_tvd      = Column( Unicode(64), nullable=True, index=True, default=u'NO' ) # Aplicaci�n Tvd: "ELIMINADO", "CONSERVADO"
aplicacion_id       = Column( Unicode(64), nullable=True, index=True, default=u'NO' ) # Aplicaci�n id del registro
marcado_para        = Column( Unicode(64), nullable=True, index=True, default=u'' )   # MARCADO PARA: "ELIMINAR"

# Descriptores adicionales
descriptores         = Column( json.JSONType, default={} )

# Fecha actualizaci�n de documentos
fecha_documentos      = Column( DateTime, nullable=True, default=None)
"""
campos = {
    # TRD/TVD
    "tabla"              : tipos.clave(propiedades={"titulo": "TRD/TVD", "longitud": 60}),
    
    "numero_orden"        : tipos.entero(propiedades={"titulo": "Numero de orden"}), 
    "nombre"              : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 250}),   
    "codigo"              : tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "defecto":'CODIGO', "longitud": 250}),   
    
    # Serie padre
    "serie_id"    : tipos.clave(propiedades={"titulo": "Serie id", "longitud": 60}),
    "serie_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Serie nombre", "longitud": 250}),
    
    # SubSerie padre
    "subserie_id"    : tipos.clave(propiedades={"titulo": "SubSerie id", "longitud": 60}),
    "subserie_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "SubSerie nombre", "longitud": 250}),    
    
    "serie_subserie": tipos.texto(propiedades={"columna": "no", "titulo": "Serie/Subserie nombre", "longitud": 250, "propiedad": serie_subserie}),
    "dependencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia nombre", "longitud": 250}), 

    # Datos generales
    "ubicacion"      : tipos.texto(propiedades={"titulo": "Nombre",  "longitud": 60,  "defecto":'CENTRAL'}), 
    "periodo"        : tipos.texto(propiedades={"titulo": "periodo", "longitud": 60,  "defecto":'CENTRAL'}), 
    "estado"         : tipos.texto(propiedades={"titulo": "Estado",  "longitud": 60,  "defecto":'ABIERTO'}), 

      
    "tipo_expediente": tipos.texto(propiedades={"columna": "no", "titulo": "Tipo expediente", "propiedad": tipo_expediente, "reporte": "SI"}), 
}

referencias = [
    # Serie Tvd
    {
        "campoReferencia"    : "serie_id",
        "atributosReferencia": [{
            "serie_nombre": "nombre",
            "periodo"     : "periodo",
            "activa"      : "estado",
            "dependencia_nombre": "dependencia_nombre"
        }],
        "estructuraDestino": "agn_serie_tvd",
        "campoDestino"     : "id",            
    },

    # SubSerie Tvd
    {
        "campoReferencia"    : "subserie_id",
        "atributosReferencia": [{
            "subserie_nombre": "nombre",
            "periodo"        : "periodo",
            "activa"         : "estado",
        }],
        "estructuraDestino": "agn_subserie_tvd",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Expedientes Tvd",
    "clase"       : "agn_expedientes_tvd",
    "estructura"  : "agn_expedientes_tvd",    
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