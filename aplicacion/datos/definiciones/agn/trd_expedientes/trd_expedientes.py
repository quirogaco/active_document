#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint, datetime

from sqlalchemy import and_
import random

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
        datos = {
            "id"                 : documento.id,
            "tipo"               : documento.tipo_nombre,
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

    lista = sorted(lista, key = lambda item: item['fecha_creacion'])

    contador = 0
    control = ""
    for item in lista:
        item["control"] = ""
        if (item["soporte"] in ["FISICO", "DIGITALIZADO"]):
            # Un solo folio fisico
            if (item["folios_fisicos"] == 1):
                contador += 1
                control  = str(contador)

            # Varios folios fisicos
            if (item["folios_fisicos"] > 1):
                contador += 1
                control = str(contador)
                contador += item["folios_fisicos"] - 1
                control += " - " + str(contador)                 

        item["control"] = control     

    return lista

# Codigo
def codigo(_r):
    codigo = _r.serie_codigo
    if (_r.subserie_codigo not in ["", None]):
        codigo = _r.subserie_codigo         

    return codigo

def serie_subserie(_r):
    nombre = _r.serie_nombre
    if (_r.subserie_nombre not in ["", None]):
        nombre += "/" + _r.subserie_nombre

    return nombre

def fecha_inicial(_r):
    fecha = ""
    documentos = trd_documentos(_r)
    if len(documentos) > 0:
        fecha = documentos[0]["fecha_creacion"]
        fecha = fecha.date()
      
    return fecha

def fecha_final(_r):
    fecha = ""
    documentos = trd_documentos(_r)
    if len(documentos) > 0:
        fecha = documentos[len(documentos)-1]["fecha_creacion"]
        fecha = fecha.date()
    
    return fecha

def anos_gestion(_r):
    anos = 0
    if (_r.serie_gestion) not in [0, None]:
        anos = _r.serie_gestion 
    elif (_r.subserie_gestion) not in [0, None]:
        anos = _r.subserie_gestion

    return anos

def anos_central(_r):
    anos = 0
    if (_r.serie_central) not in [0, None]:
        anos = _r.serie_central
    elif (_r.subserie_central) not in [0, None]:
        anos = _r.subserie_central

    return anos

def vence_gestion(_r):
    vence = ""
    sumar = 0
    inicio = _r.fecha_final
    if inicio != "":                 
        sumar = anos_gestion(_r)
        vence = inicio + datetime.timedelta(days = (sumar*365))
     
    return vence

def vencido_gestion(_r):
    vencido = "NO"
    if (_r.vence_gestion != "") and (_r.vence_gestion < datetime.date.today()):
        vencido = "SI"

    return vencido

def vence_central(_r):
    vence = ""
    sumar = 0
    inicio = _r.fecha_final
    if inicio != "":             
        sumar = anos_central(_r)
        vence = inicio + datetime.timedelta(days = (sumar*365))
        
    return vence

def vencido_central(_r):
    vencido = "NO"
    if (_r.vence_central != "") and (_r.vence_central < datetime.date.today()):
        vencido = "SI"

    return vencido

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

def carpetas(_r):
    CARPETAS_CLASE = globales.lee_clase("agn_carpetas_trd")
    sesion         = sqalchemy_comunes.nuevaSesion("base") 
    filtros        = (CARPETAS_CLASE.expediente_id == _r.id)
    carpetas       = sesion.query(CARPETAS_CLASE).filter( filtros ).all()
    total_carpetas = len(carpetas)    
    sesion.close()
        
    return total_carpetas

# Acceso
def acceso(_r):
    acceso = comunes_trd.recuperar_accesos("expediente", _r.id) 

    return acceso

# Acceso
def acceso_modo(_r):
    acceso_tipo = acceso(_r).get("autorizacion", "PUBLICA") 

    return acceso_tipo

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

    if (fisicos == 0) and (electronicos > 0):
        tipo = "ELECTRONICO"

    return tipo

def dependencias_gestion(_r):
    dependencias = _r.dependencia_datos.get("dependencias_gestion", [])

    return dependencias

#################
# TRANSFERENCIA #
#################
# Esta tranaferido SI/NO
def transferido(_r):
    estado = "NO"

    TRANSFERENCIA_CLASE = globales.lee_clase("agn_transferencias_exp_trd")
    sesion              = sqalchemy_comunes.nuevaSesion("base") 
    filtros             = (TRANSFERENCIA_CLASE.expediente_id == _r.id)
    resultado           = sesion.query(TRANSFERENCIA_CLASE).filter( filtros ).first()
    if resultado != None:
        estado = "SI"

    sesion.close()

    return estado

###############
# DISPOSICION #
###############
# Esta transferido SI/NO
def transferido(_r):
    estado = "NO"

    TRANSFERENCIA_CLASE = globales.lee_clase("agn_transferencias_exp_trd")
    sesion              = sqalchemy_comunes.nuevaSesion("base") 
    filtros             = (TRANSFERENCIA_CLASE.expediente_id == _r.id)
    resultado           = sesion.query(TRANSFERENCIA_CLASE).filter( filtros ).first()
    if resultado != None:
        estado = "SI"

    sesion.close()

    return estado

def eliminacion(_r):
    dato = _r.serie_eliminacion
    if (_r.subserie_eliminacion not in [None, ""]):
        dato = _r.subserie_eliminacion

    return dato

def seleccion(_r):
    dato = _r.serie_seleccion
    if (_r.subserie_seleccion not in [None, ""]):
        dato = _r.subserie_seleccion

    return dato

def conservacion(_r):
    dato = _r.serie_conservacion
    if (_r.subserie_conservacion not in [None, ""]):
        dato = _r.subserie_conservacion

    return dato

def micro_digitalizacion(_r):
    dato = _r.serie_micro_digitalizacion
    if (_r.subserie_micro_digitalizacion not in [None, ""]):
        dato = _r.subserie_micro_digitalizacion

    return dato

def disposicion_final(_r):
    dato = []
    if (_r.eliminar != "NO") and (_r.eliminacion == "SI"):    
        dato.append("ELIMINACION")

    if _r.seleccion == "SI":    
        dato.append("SELECCION")
    
    if _r.conservacion == "SI":    
        dato.append("CONSERVACION")
    
    if _r.micro_digitalizacion == "SI":    
        dato.append("MEDIO TECNICO")
    
    return " /".join(dato)

campos = {
    ####################
    # EXPEDIENTE DATOS #
    ####################
    # TRD/TVD
    "tabla": tipos.clave(propiedades={"titulo": "TRD/TVD", "longitud": 60, "reporte": "SI"}),
    "nombre": tipos.texto_obligatorio(propiedades={"titulo": "Nombre", "longitud": 250, "reporte": "SI"}),   
    "observacion": tipos.texto(propiedades={"titulo": "Observacion", "longitud": 512, "reporte": "SI"}),   
    "codigo": tipos.texto_obligatorio(propiedades={"columna": "no", "titulo": "Codigo",  "propiedad": codigo, "reporte": "SI"}),   
    "carpetas": tipos.clave(propiedades={"columna": "no", "titulo": "Carpetas", "propiedad": carpetas, "reporte": "SI"}),       

    "ubicacion": tipos.texto(propiedades={"titulo": "Ubicación", "longitud": 60, "defecto":'GESTION', "reporte": "SI"}), 
    "caja": tipos.texto(propiedades={"titulo": "Caja", "longitud": 60, "defecto":'', "reporte": "SI"}), 
    "ubicacion_topografica": tipos.texto(propiedades={"titulo": "Ubicación topografica", "longitud": 60, "defecto":'', "reporte": "SI"}), 
    "etapa": tipos.texto(propiedades={"titulo": "Etapa", "longitud": 60, "defecto":'GESTION', "reporte": "SI"}), 
    "estado": tipos.texto(propiedades={"titulo": "Estado", "longitud": 60, "defecto":'ABIERTO', "reporte": "SI"}), 
    "tipo_expediente": tipos.texto(propiedades={"columna": "no", "titulo": "Tipo expediente", "propiedad": tipo_expediente, "reporte": "SI"}), 
    "anos_gestion": tipos.entero(propiedades={"columna": "no", "titulo": "Años gestion", "propiedad": anos_gestion, "reporte": "SI"}),   
    "anos_central": tipos.entero(propiedades={"columna": "no", "titulo": "Años central", "propiedad": anos_central, "reporte": "SI"}),    
    
    # Retencion vencimiento
    "vence_gestion": tipos.fecha(propiedades={"columna": "no", "titulo": "Vence en archivo de gestión", "propiedad": vence_gestion, "reporte": "SI"}),
    "vence_central": tipos.fecha(propiedades={"columna": "no", "titulo": "Vence en archivo central",    "propiedad": vence_central, "reporte": "SI"}),

    # Transferencia
    "vencido_gestion": tipos.clave(propiedades={"columna": "no", "titulo": "Vencido gestion",  "propiedad": vencido_gestion, "reporte": "SI"}),
    "caja_transferencia": tipos.clave(propiedades={"titulo": "Caja transferencia", "longitud": 60, "reporte": "SI"}), 
    "anotacion": tipos.texto(propiedades={"titulo": "Anotación transferencia", "longitud": 250, "reporte": "SI"}), 
    "transferido": tipos.clave(propiedades={"columna": "no", "titulo": "Si esta transferido",  "propiedad": transferido, "reporte": "SI"}),

    # Disposicion
    "vencido_central": tipos.clave(propiedades={"columna": "no", "titulo": "Vencido central",  "propiedad": vencido_central, "reporte": "SI"}),
    "disposicion_aplicada": tipos.clave(propiedades={"titulo": "Disposicion", "longitud": 128, "reporte": "SI"}), 
    "disposicion_fecha": tipos.fecha(propiedades={"titulo": "Fecha disposicion", "reporte": "SI"}), 
    "eliminacion": tipos.clave(propiedades={"columna": "no", "titulo": "Eliminacion",  "propiedad": eliminacion, "reporte": "SI"}),
    "seleccion": tipos.clave(propiedades={"columna": "no", "titulo": "Seleccion",  "propiedad": seleccion, "reporte": "SI"}),
    "conservacion": tipos.clave(propiedades={"columna": "no", "titulo": "Conservacion",  "propiedad": conservacion, "reporte": "SI"}),
    "micro_digitalizacion": tipos.clave(propiedades={"columna": "no", "titulo": "Micro_digitalizacion",  "propiedad": micro_digitalizacion, "reporte": "SI"}),
    "disposicion_final": tipos.texto(propiedades={"columna": "no", "titulo": "Accion de disposicion", "propiedad": disposicion_final, "reporte": "SI"}),
    "eliminar": tipos.texto(propiedades={"titulo": "Permite eliminacion", "reporte": "SI"}),

    ##########################
    # Información documentos #
    ##########################
    "acceso": tipos.json(propiedades={"columna": "no", "titulo": "Acceso", "propiedad": acceso}),  
    "acceso_modo": tipos.texto(propiedades={"columna": "no", "titulo": "Acceso modo", "propiedad": acceso_modo, "reporte": "SI"}),   
    "documentos": tipos.clave(propiedades={"columna": "no", "titulo": "Documentos", "propiedad": trd_documentos}),
    "folios_fisicos": tipos.texto(propiedades={"columna": "no", "titulo": "Folios fisicos",      "propiedad": folios_fisicos,      "reporte": "SI"}), 
    "folios_electronicos": tipos.texto(propiedades={"columna": "no", "titulo": "Folios electronicos", "propiedad": folios_electronicos, "reporte": "SI"}), 
    "total_documentos": tipos.texto(propiedades={"columna": "no", "titulo": "Total documentos",    "propiedad": total_documentos,    "reporte": "SI"}),
    "fecha_inicial": tipos.fecha(propiedades={"columna": "no", "titulo": "Fecha inicial",       "propiedad": fecha_inicial,       "reporte": "SI"}), 
    "fecha_final": tipos.fecha(propiedades={"columna": "no", "titulo": "Fecha final",         "propiedad": fecha_final,         "reporte": "SI"}), 

    ##################################
    # DATOS HEREDADOS SERIE/SUBSERIE #
    ##################################
    "serie_subserie": tipos.texto(propiedades={"columna": "no", "titulo": "Serie/Subserie nombre", "propiedad": serie_subserie, "reporte": "SI"}),
    "ubicacion_id": tipos.texto(propiedades={"columna": "no", "titulo": "Ubicacion id", "reporte": "SI"}),
    "ubicacion_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Ubicacion nombre", "reporte": "SI"}),
    "dependencia_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia nombre", "reporte": "SI"}),    
    "dependencia_codigo": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia codigo", "reporte": "SI"}),          
    "dependencia_id": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia id", "reporte": "SI"}),     
    #"dependencia_datos": tipos.json(propiedades={"columna": "no", "titulo": "Dependencia datos"}), 
    "dependencia_gestion": tipos.texto(propiedades={"columna": "no", "titulo": "Dependencia datos", "propiedad": dependencias_gestion}), 
       
    # Serie padre
    "serie_id": tipos.clave(propiedades={"titulo": "Serie id", "longitud": 60}),
    "serie_version": tipos.entero(propiedades={"columna": "no", "titulo": "Version Trd", "reporte": "SI"}),    
    "serie_codigo": tipos.texto(propiedades={"columna": "no", "titulo": "Serie codigo", "reporte": "SI"}),    
    "serie_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "Serie nombre", "reporte": "SI"}),   
    "serie_gestion": tipos.entero(propiedades={"columna": "no", "titulo": "Retención en gestión serie", "reporte": "SI"}),    
    "serie_central": tipos.entero(propiedades={"columna": "no", "titulo": "Retención en central serie", "reporte": "SI"}), 
    "serie_eliminacion": tipos.texto(propiedades={"columna": "no", "titulo": "Eliminación", "reporte": "SI"}), 
    "serie_seleccion": tipos.texto(propiedades={"columna": "no", "titulo": "Selección", "reporte": "SI"}), 
    "serie_conservacion": tipos.texto(propiedades={"columna": "no", "titulo": "Conservación", "reporte": "SI"}), 
    "serie_micro_digitalizacion": tipos.texto(propiedades={"columna": "no", "titulo": "Micro digitalización", "reporte": "SI"}),    
    "ubicaciones_gestion": tipos.texto(propiedades={"columna": "no", "titulo": "Ubicaciones gestion"}),
    "dependencias_gestion": tipos.clave(propiedades={"columna": "no", "titulo": "Dependencias gestion"}),     

    # SubSerie padre
    "subserie_id": tipos.clave(propiedades={"titulo": "SubSerie id", "longitud": 60}),
    "subserie_codigo": tipos.texto(propiedades={"columna": "no", "titulo": "SubSerie codigo", "reporte": "SI"}), 
    "subserie_nombre": tipos.texto(propiedades={"columna": "no", "titulo": "SubSerie nombre", "reporte": "SI"}),    
    "subserie_gestion": tipos.entero(propiedades={"columna": "no", "titulo": "Retención en gestión Subserie", "reporte": "SI"}),    
    "subserie_central": tipos.entero(propiedades={"columna": "no", "titulo": "Retención en central Subserie", "reporte": "SI"}), 
    "subserie_eliminacion": tipos.texto(propiedades={"columna": "no", "titulo": "Eliminación", "reporte": "SI"}), 
    "subserie_seleccion": tipos.texto(propiedades={"columna": "no", "titulo": "Selección", "reporte": "SI"}), 
    "subserie_conservacion": tipos.texto(propiedades={"columna": "no", "titulo": "Conservación", "reporte": "SI"}), 
    "subserie_micro_digitalizacion": tipos.texto(propiedades={"columna": "no", "titulo": "Micro digitalización", "reporte": "SI"})
}

referencias = [
    # Serie Trd
    {
        "campoReferencia": "serie_id",
        "atributosReferencia": [{
            "dependencia_codigo": "dependencia_codigo",
            "dependencia_nombre": "dependencia_nombre",
            "dependencia_id": "dependencia_id",
            "ubicaciones_gestion": "ubicaciones_gestion",
            "dependencias_gestion": "dependencias_gestion",

            "serie_version"             : "version",
            "serie_codigo"              : "codigo",  
            "serie_nombre"              : "nombre",  
            "serie_gestion"             : "gestion",   
            "serie_central"             : "central",
            "serie_eliminacion"         : "eliminacion",
            "serie_seleccion"           : "seleccion",
            "serie_conservacion"        : "conservacion",
            "serie_micro_digitalizacion": "micro_digitalizacion"
        }],
        "estructuraDestino": "agn_serie_trd",
        "campoDestino"     : "id",            
    },

    # SubSerie Trd
    {
        "campoReferencia": "subserie_id",
        "atributosReferencia": [{
            "subserie_codigo"              : "codigo",              
            "subserie_nombre"              : "nombre",  
            "subserie_gestion"             : "gestion",   
            "subserie_central"             : "central",
            "subserie_eliminacion"         : "eliminacion",
            "subserie_seleccion"           : "seleccion",
            "subserie_conservacion"        : "conservacion",
            "subserie_micro_digitalizacion": "micro_digitalizacion"
        }],
        "estructuraDestino": "agn_subserie_trd",
        "campoDestino"     : "id",            
    }
]

definicion = {
    "descripcion" : "Expedientes TRD",
    "clase"       : "agn_expedientes_trd",
    "estructura"  : "agn_expedientes_trd",    
    "campos"      : campos,
    "referencias" : referencias,
    #"referencias" : [],
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
                "tipo"             : tipos.texto(propiedades={"titulo": "tipo"}),
                "control"          : tipos.texto(propiedades={"titulo": "control"}),
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