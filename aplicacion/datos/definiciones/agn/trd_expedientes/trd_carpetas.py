#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint, datetime

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
from aplicacion.trd                         import comunes as comunes_trd

import random

# Documentos por expedientes
def trd_documentos(_r):
    lista = []

    # Caga Carpetas
    DOCUMENTOS_CLASE = globales.lee_clase("agn_documentos_trd")
    sesion           = sqalchemy_comunes.nuevaSesion("base") 
    filtros          = and_( DOCUMENTOS_CLASE.expediente_id == _r.id, DOCUMENTOS_CLASE.tabla == "TRD")
    documentos       = sesion.query(DOCUMENTOS_CLASE).filter( filtros ).all()    
    for documento in documentos:
        #print("documento ARCHIVOS:")
        #pprint.pprint(documento.archivos)
        datos = {
            "id"                 : documento.id,
            "tipo_nombre"        : documento.tipo_nombre,
            "detalle"            :  documento.detalle,
            "fecha_creacion"     : documento.fecha_creacion,
            "fecha_incorporado"  : documento.fecha_incorporado,
            "soporte"            : documento.soporte,
            "folios_fisicos"     : documento.folios_fisicos,
            "folios_electronicos": documento.folios_electronicos,
            "tipo_archivo"       : documento.tipo_archivo,
            "tamano"             : documento.tamano,
            "fecha_funcion"      : documento.fecha_funcion,
            "valor_huella"       : str(random.getrandbits(random.randint(10, 99)))
        }
        lista.append(datos)
    sesion.close()

    lista = sorted(lista, key = lambda item: item['fecha_creacion'])

    return lista

def serie_subserie(_r):
    nombre = _r.serie_nombre
    if (_r.subserie_nombre not in ["", None]):
        nombre += "/" + _r.subserie_nombre

    return nombre

def fecha_inicial(_r):
    fecha      = ""
    documentos = trd_documentos(_r)
    if len(documentos) > 0:
        fecha = documentos[0]["fecha_creacion"]
    
    return fecha

def fecha_final(_r):
    fecha      = ""
    documentos = trd_documentos(_r)
    if len(documentos) > 0:
        fecha = documentos[len(documentos)-1]["fecha_creacion"]
    
    return fecha

def vence_gestion(_r):
    vence = _r.creado_en_
    vence = vence +  datetime.timedelta(_r.gestion_serie*365)
    
    return vence

def vence_central(_r):
    vence = _r.creado_en_
    vence = vence +  datetime.timedelta(_r.central_serie*365)
    
    return vence

def folios_fisicos(_r):
    folios     = 0
    documentos = trd_documentos(_r)
    for documento in documentos:
        folios += documento["folios_fisicos"]
    
    return folios

def folios_electronicos(_r):
    folios     = 0
    documentos = trd_documentos(_r)
    for documento in documentos:
        folios += documento["folios_electronicos"]
    
    return folios

def total_documentos(_r):
    return len(trd_documentos(_r))

def tipo_expediente(_r):
    fisicos      = 0
    electronicos = 0
    tipo       = "FISICO"
    documentos = trd_documentos(_r)
    for documento in documentos:
        if documento["soporte"] == "ELECTRONICO":
            electronicos += 1
        if documento["soporte"] == "FISICO":
            fisicos += 1
    
    if (fisicos > 0) and (electronicos > 0):
        tipo = "HIBRIDO"

    if (fisicos == 0) and (electronicos > 1):
        tipo = "ELECTRONICO"

    return tipo

def nombre(_r):
    return ("Carpeta " + str(_r.carpeta_nro))

campos = {
    #################
    # CARPETA DATOS #
    #################
    "carpeta_nro"          : tipos.entero(propiedades={"titulo": "Número de orden/carpeta", "reporte": "SI"}), 
    "caja"                 : tipos.texto(propiedades={"titulo": "Caja", "reporte": "SI"}), 
    "tomo"                 : tipos.entero(propiedades={"titulo": "Tomo", "defecto":1, "reporte": "SI"}), 
    "ubicacion_topografica": tipos.texto(propiedades={"titulo": "Ubicación topografica", "longitud": 60, "defecto":'', "reporte": "SI"}), 
    # Transferencia
    "caja_transferencia"   : tipos.clave(propiedades={"titulo": "Caja transferencia", "longitud": 60, "reporte": "SI"}), 
    # Documentos de la carpeta
    "documentos"           : tipos.clave(propiedades={"columna": "no", "titulo": "Documentos", "propiedad": trd_documentos}),
    "nombre"               : tipos.clave(propiedades={"columna": "no", "titulo": "Nombre carpeta", "propiedad": nombre}),
    
    ##############################
    # DATOS HEREDADOS EXPEDIENTE #
    ##############################
    "expediente_id"     : tipos.clave(propiedades={"titulo": "Expediente id", "longitud": 60}),    
    "expediente_nombre" : tipos.texto(propiedades={"columna": "no", "titulo": "Nombre del expediente", "reporte": "SI"}),  
    "dependencia_id"    : tipos.clave(propiedades={"columna": "no", "titulo": "Id de la dependencia", "reporte": "SI"}),       
    "dependencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Nombre de la dependencia", "reporte": "SI"}),   
    "acceso"            : tipos.json(propiedades={"columna": "no", "titulo": "Acceso", "reporte": "SI"}), 
    "acceso_modo"       : tipos.texto(propiedades={"columna": "no", "titulo": "Acceso modo", "reporte": "SI"}), 
    "tipo_expediente"   : tipos.texto(propiedades={"columna": "no", "titulo": "Tipo expediente", "reporte": "SI"}), 
    "ubicacion"         : tipos.texto(propiedades={"columna": "no", "titulo": "Ubicación archivo", "longitud": 60, "defecto":'GESTION', "reporte": "SI"}), 
    "etapa"             : tipos.texto(propiedades={"columna": "no", "titulo": "Etapa", "longitud": 60, "defecto":'GESTION', "reporte": "SI"}), 
    "estado"            : tipos.texto(propiedades={"columna": "no", "titulo": "Estado", "longitud": 60, "defecto":'ABIERTO', "reporte": "SI"}),  
    "transferido"       : tipos.clave(propiedades={"columna": "no", "titulo": "Si esta transferido", " reporte": "SI"}),  
    # Retención vencimiento
    "vence_gestion"     : tipos.fecha(propiedades={"columna": "no", "titulo": "Vence en archivo de gestión", "propiedad": vence_gestion, "reporte": "SI"}),
    "vence_central"     : tipos.fecha(propiedades={"columna": "no", "titulo": "Vence en archivo central",    "propiedad": vence_central, "reporte": "SI"}),

    ##################################
    # DATOS HEREDADOS SERIE/SUBSERIE #
    ##################################
    # Serie
    "serie_id"                  : tipos.clave(propiedades={"columna": "no", "titulo": "Serie id", "longitud": 60}),
    "serie_nombre"              : tipos.texto(propiedades={"columna": "no", "titulo": "Serie nombre", "longitud": 250, "reporte": "SI"}),
    "gestion_serie"             : tipos.entero(propiedades={"columna": "no", "titulo": "Retención en gestión serie", "reporte": "SI"}),    
    "central_serie"             : tipos.entero(propiedades={"columna": "no", "titulo": "Retención en central serie", "reporte": "SI"}),     
    "eliminacion_serie"         : tipos.texto(propiedades={"columna": "no", "titulo": "Eliminación", "reporte": "SI"}), 
    "seleccion_serie"           : tipos.texto(propiedades={"columna": "no", "titulo": "Selección", "reporte": "SI"}), 
    "conservacion_serie"        : tipos.texto(propiedades={"columna": "no", "titulo": "Conservación", "reporte": "SI"}), 
    "micro_digitalizacion_serie": tipos.texto(propiedades={"columna": "no", "titulo": "Micro digitalización", "reporte": "SI"}),         
    
    # SubSerie
    "subserie_id"                  : tipos.clave(propiedades={"columna": "no", "titulo": "SubSerie id", "longitud": 60}),
    "subserie_nombre"              : tipos.texto(propiedades={"columna": "no", "titulo": "SubSerie nombre", "longitud": 250, "reporte": "SI"}),    
    "gestion_subserie"             : tipos.entero(propiedades={"columna": "no", "titulo": "Retención en gestión subserie", "reporte": "SI"}),    
    "central_subserie"             : tipos.entero(propiedades={"columna": "no", "titulo": "Retención en central subserie", "reporte": "SI"}),  
    "eliminacion_subserie"         : tipos.texto(propiedades={"columna": "no", "titulo": "Eliminación", "reporte": "SI"}), 
    "seleccion_subserie"           : tipos.texto(propiedades={"columna": "no", "titulo": "Selección", "reporte": "SI"}), 
    "conservacion_subserie"        : tipos.texto(propiedades={"columna": "no", "titulo": "Conservación", "reporte": "SI"}), 
    "micro_digitalizacion_subserie": tipos.texto(propiedades={"columna": "no", "titulo": "Micro digitalización", "reporte": "SI"}),            

    ##########################
    # Información documentos #
    ##########################
    "folios_fisicos"     : tipos.texto(propiedades={"columna": "no", "titulo": "Folios fisicos",      "propiedad": folios_fisicos,      "reporte": "SI"}), 
    "folios_electronicos": tipos.texto(propiedades={"columna": "no", "titulo": "Folios electronicos", "propiedad": folios_electronicos, "reporte": "SI"}), 
    "total_documentos"   : tipos.texto(propiedades={"columna": "no", "titulo": "Total documentos",    "propiedad": total_documentos,    "reporte": "SI"}),
    "fecha_inicial"      : tipos.fecha(propiedades={"columna": "no", "titulo": "Fecha inicial",       "propiedad": fecha_inicial,       "reporte": "SI"}), 
    "fecha_final"        : tipos.fecha(propiedades={"columna": "no", "titulo": "Fecha final",         "propiedad": fecha_final,         "reporte": "SI"})
}

referencias = [
    # Expediente Trd
    {
        "campoReferencia"    : "expediente_id",
        "atributosReferencia": [{
            # Basicas
            "expediente_nombre" : "nombre",
            "dependencia_nombre": "dependencia_nombre",
            "dependencia_id"    : "dependencia_id",
            "version"           : "version",
            "estado"            : "estado",
            "tipo_expediente"   : "tipo_expediente",
            "transferido"       : "transferido",
            "acceso"            : "acceso",
            "acceso_modo"       : "acceso_modo",            
            
            # Serie
            "serie_id"                  : "serie_id", 
            "serie_nombre"              : "serie_nombre",            
            "serie_gestion"             : "serie_gestion",
            "serie_central"             : "serie_central",
            "serie_eliminacion"         : "serie_eliminacion",  
            "serie_seleccion"           : "serie_seleccion", 
            "serie_conservacion"        : "serie_conservacion",  
            "serie_micro_digitalizacion": "serie_micro_digitalizacion",            
            
            # SubSerie
            "subserie_id"                  : "subserie_id", 
            "subserie_nombre"              : "subserie_nombre",            
            "subserie_gestion"             : "subserie_gestion",
            "subserie_central"             : "subserie_central",
            "subserie_eliminacion"         : "subserie_eliminacion",  
            "subserie_seleccion"           : "subserie_seleccion", 
            "subserie_conservacion"        : "subserie_conservacion",  
            "subserie_micro_digitalizacion": "subserie_micro_digitalizacion"               
        }],
        "estructuraDestino": "agn_expedientes_trd",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Carpetas TRD",
    "clase"       : "agn_carpetas_trd",
    "estructura"  : "agn_carpetas_trd",    
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

############
# Archivos #
############    
indexamiento = {
    "documentos":  {
        "tipoElastic": {
            'tipo'       : 'anidados',
            "propiedades": {
                'id'               : tipos.clave(propiedades={"titulo": "Id archivo"}),
                "tabla"            : tipos.texto(propiedades={"titulo": "Tabla TRD/TVD"}),                 
                'expediente_id'    : tipos.clave(propiedades={"titulo": "Expediente id"}),
                "expediente_nombre": tipos.texto(propiedades={"titulo": "Expediente nombre"}), 
                'serie_id'         : tipos.clave(propiedades={"titulo": "Serie id"}),
                "serie_nombre"     : tipos.texto(propiedades={"titulo": "Serie nombre"}), 
                'subserie_id'      : tipos.clave(propiedades={"titulo": "SubSerie id"}),
                "subserie_nombre"  : tipos.texto(propiedades={"titulo": "SubSerie nombre"}), 
                "detalle"          : tipos.texto(propiedades={"titulo": "Detalle"}), 
                'tipo_id'          : tipos.clave(propiedades={"titulo": "Tipo documental id"}),
                "tipo_nombre"      : tipos.texto(propiedades={"titulo": "Tipo documental nombre"}), 
                "carpeta_nro"      : tipos.texto(propiedades={"titulo": "Carpeta nro"}), 
                "fecha_creacion"   : tipos.fecha(propiedades={"titulo": "Fecha de creaci?n"}), 
                "fecha_incorporado": tipos.fecha(propiedades={"titulo": "Fecha de incorporaci?n"}), 
                "funcion_resumen"  : tipos.texto(propiedades={"titulo": "Funcion"}), 
                "tamano"           : tipos.entero(propiedades={"titulo": "Tama?o"}), 
                'padre_id'         : tipos.clave(propiedades={"titulo": "Id padre"}),
                "tipo"             : tipos.texto(propiedades={"titulo": "tipo"})
            }
        }
    }
}


# Campos elastic
camposIndexamiento = indexamiento.copy()
camposElastic      = campos.copy()
camposElastic.update(camposIndexamiento)

# Publica
elementos_comunes.publicaValidaElastic(definicion, camposElastic)