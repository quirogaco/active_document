#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime, random

from librerias.utilidades import basicas  
from . import datos_comunes
from librerias.datos.sql import sqalchemy_filtrar 
from librerias.datos.sql import sqalchemy_modificar 
from aplicacion.especificos.configuracion_general import configuracion_general

def radicado_consecutivo(tipo="ENTRADAS"):
    filtros = [ [ "nombre", "=", tipo ] ]
    entrada = sqalchemy_filtrar.filtrarOrdena(
        estructura="consecutivos", 
        filtros=filtros, 
        ordenamientos=[]
    )[0]
    consecutivo = entrada["consecutivo"] + 1
    sqalchemy_modificar.modificar_un_registro(
        "consecutivos", 
        entrada["id"],
        {"consecutivo": consecutivo}
    )

    return str(consecutivo).rjust(6,'0')

###################
# BASICOS ENTRADA #
###################
campos_basicos_entrada = [
    'radicado_en',
    'radicado_por',
    'nro_radicado' 
]

# DATOS BASICOS DE LA ALIDA (DEL REGISTRO FISICO)
def datos_basicos(datos, tarea_id):    
    radicado_por, radicado_en = datos_comunes.datos_radicador(datos, tarea_id)
    consecutivo = radicado_consecutivo("ENTRADAS")
    radicado = "E-" + basicas.ano() + "-" + consecutivo    
    datos_especificos = {
        'radicado_en'   : radicado_en,
        'radicado_por'  : radicado_por,
        'nro_radicado'  : radicado,
        'fecha_radicado': datetime.datetime.now()
    }
    
    return datos_especificos

def canal_radicado(extendidos):
    # Si es formualrio web se asigna canal web general
    if extendidos.get("formulario_web", None) != None:
        configuracion = configuracion_general.leer_registro_configuracion("radicacion_canales")
        if configuracion != None:
            canales           = configuracion["datos"]        
            canal_radicado_id = canales.get("canal_web", None)
            extendidos["canal_radicado_id"] = canal_radicado_id
    else:
        # debe traerlo extendido
        pass

    return extendidos


# DATOS EXTENDIDOS DE LA SALIDA (atributos_)
def datos_extendidos(datos, tarea_id):    
    extendidos = {            
        'fecha_documento': datos.get('fecha_documento', basicas.fecha()),
        'resuelto_inmediato': datos.get('resuelto_inmediato', 'NO')
    }
    
    for campo, valor in datos.items():
        if (campo not in campos_basicos_entrada) and (campo not in datos_comunes.campos_tercero):
            extendidos[campo] = valor
    
    extendidos = datos_comunes.limpiar_datos(extendidos, ['archivos', 'id'])
    extendidos = canal_radicado(extendidos)

    return extendidos