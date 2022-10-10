#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, builtins,time, pprint
import pandas as pd
import numpy as np

import configuracion_base

from librerias.utilidades import basicas  
from librerias.flujos     import flujos_insertar_sql
from librerias.datos.sql  import sqalchemy_comunes
from librerias.datos.sql  import sqalchemy_insertar
from librerias.datos.base import globales

def valide_numero(valor):
    try:
        valor = int(valor)
    except:
        valor = 0

    return valor

def valide_texto(valor, longitud=-1):
    valor = str(valor).replace(".0", "")
    if valor in ['(null)', 'null', 'nan', None, np.nan]: 
        valor = ""

    if longitud > 0:
        valor = valor[0:longitud]

    return valor

contador = 0
sesion = sqalchemy_comunes.nuevaSesion('base')

"""
# RADICADOS
RADICADO_CLASE = globales.lee_clase("db_migrado_radicado_pqrs")
radicados = pd.read_excel(open('MIGRACIÓN_PQRSD_19012021.xlsx', 'rb'), sheet_name='RADICADO') 
for index, radicado in radicados.iterrows():
    contador += 1
    print(index, radicado['id'])
    data = {
      'id'             : radicado['id'],
      'tipo_radicado'  : radicado['tipo_radicado'],
      'fecha_radicado' : radicado['fecha_radicado'],
      'nro_radicado'   : radicado['nro_radicado'],
      'fecha_documento': radicado['fecha_documento'],
      'folios'         : radicado['folios'],
      'asunto'         : radicado['asunto'],
      'id_tabla_asunto': valide_numero(radicado['id_tabla_asunto']),
      'asunto_form_web': str(radicado['asunto_form_web'])[:50]
    }
    sqalchemy_insertar.insertar(sesion, RADICADO_CLASE, data, False)
    sesion.commit()
    if contador > 2000:
        sesion.commit()
        contador = 0
        #break   
"""
# TERCERO
TERCERO_CLASE = globales.lee_clase("db_migrado_tercero_pqrs")
terceros = pd.read_excel(open('MIGRACIÓN_PQRSD_19012021.xlsx', 'rb'), sheet_name='REMITENTE-DESTINATARIO') 
for index, tercero in terceros.iterrows():
    print(index, tercero['id'])
    data = {
      'id'                : valide_texto(tercero['id']),
      'tipoidentificacion': valide_texto(tercero['tipoidentificacion']),
      'nroidentificacion' : valide_texto(tercero['nroidentificacion']),
      'primer_nombre'     : valide_texto(tercero['primer_nombre']),
      'segundo_nombre'    : valide_texto(tercero['segundo_nombre']),
      'primer_apellido'   : valide_texto(tercero['primer_apellido']),
      'segundo_apellido'  : valide_texto(tercero['segundo_apellido']),
      'nombres'           : valide_texto(tercero['nombres']),
      'direccion'         : valide_texto(tercero['direccion']),
      'correoelectronico' : valide_texto(tercero['correoelectronico']),
      'telefonofijo'      : valide_texto(tercero['telefonofijo']),
      'telefonomovil'     : valide_texto(tercero['telefonomovil']),
      'peti_genero'       : valide_texto(tercero['peti_genero']),
      'ciud_id'           : valide_texto(tercero['ciud_id']),
      'depa_id'           : valide_texto(tercero['depa_id']),
      'pais_id'           : valide_texto(tercero['pais_id'])
    }
    sqalchemy_insertar.insertar(sesion, TERCERO_CLASE, data, False)
    sesion.commit()
    if contador > 2000:
        sesion.commit()
        contador = 0
        #break   

"""
# FUNCIONARIOS
FUNCIONARIO_CLASE =  globales.lee_clase("db_migrado_funcionario_pqrs")
funcionarios = pd.read_excel(open('MIGRACIÓN_PQRSD_19012021.xlsx', 'rb'), sheet_name='FUNCIONARIOS') 
for index, funcionario in funcionarios.iterrows():
    contador += 1
    print(index, funcionario['usua_id'])
    data = {
      'id'                 : valide_texto(funcionario['usua_id']),
      'carg_id'            : valide_texto(funcionario['carg_id']),
      'unid_id'            : valide_texto(funcionario['unid_id']),
      'func_primernombre'  : valide_texto(funcionario['func_primernombre']),
      'func_primerapellido': valide_texto(funcionario['func_primerapellido']),
      'func_estado'        : valide_texto(funcionario['func_estado'])
    }
    sqalchemy_insertar.insertar(sesion, FUNCIONARIO_CLASE, data, False)
    sesion.commit()
    if contador > 2000:
        sesion.commit()
        contador = 0
        #break   

# ANEXOS
ANEXO_CLASE = globales.lee_clase("db_migrado_anexo_pqrs")
anexos = pd.read_excel(open('MIGRACIÓN_PQRSD_19012021.xlsx', 'rb'), sheet_name='ANEXOS') 
for index, anexo in anexos.iterrows():
    contador += 1
    print(index, anexo['id'])
    data = {
      'id'               : valide_texto(anexo['id']),
      'radicado_id'      : valide_texto(anexo['radicado_id']),
      'tipoarchivofisico': valide_texto(anexo['tipoarchivofisico']),
      'repo_id'          : valide_texto(anexo['repo_id']),
      'adju_nombre'      : valide_texto(anexo['adju_nombre'])
    }
    sqalchemy_insertar.insertar(sesion, ANEXO_CLASE, data, False)
    sesion.commit()
    if contador > 2000:
        sesion.commit()
        contador = 0
        #break   

# ANEXOS LOG
ANEXO_CLASE = globales.lee_clase("db_migrado_anexolog_pqrs")
anexos = pd.read_excel(open('MIGRACIÓN_PQRSD_19012021.xlsx', 'rb'), sheet_name='ANEXO-LOG')  
for index, anexo in anexos.iterrows():
    contador += 1
    print(index, anexo['adju_id'])
    data = {
      'id'                   : valide_texto(anexo['adju_id']),
      'requ_id'              : valide_texto(anexo['requ_id']),
      'repo_id'              : valide_texto(anexo['repo_id']),
      'adju_nombre'          : valide_texto(anexo['adju_nombre']),
      'adju_fechacambio'     : anexo['adju_fechacambio'],
      'adju_registradopor'   : valide_texto(anexo['adju_registradopor']),
      'adju_procesoauditoria': valide_texto(anexo['adju_procesoauditoria']),
      'adju_final'           : valide_texto(anexo['adju_final']),
      'traz_id'              : valide_texto(anexo['traz_id']),
      'usua_idejecutor'      : valide_texto(anexo['usua_idejecutor']),
      'usua_idasignado'      : valide_texto(anexo['usua_idasignado']),
      'traz_fecha'           : valide_texto(anexo['traz_fecha']),
      'traz_estado'          : valide_texto(anexo['traz_estado']),
      'descripcion'          : valide_texto(anexo['descripcion'])
    }
    #print("")
    #pprint.pprint(data)
    sqalchemy_insertar.insertar(sesion, ANEXO_CLASE, data, False)
    sesion.commit()
    if contador > 2000:
        sesion.commit()
        contador = 0
        #break   

# TRAZABILIDAD
TRAZABILIDAD_CLASE = globales.lee_clase("db_migrado_trazabilidad_pqrs")
trazas = pd.read_excel(open('MIGRACIÓN_PQRSD_19012021.xlsx', 'rb'), sheet_name='TRAZABILIDAD') 
for index, traza in trazas.iterrows():
    contador += 1
    print(index, traza['traz_id'])
    data = {
      'id'                   : valide_texto(traza['traz_id'], 20),
      'requ_id'              : valide_texto(traza['requ_id']),
      'usua_idejecutor'      : valide_texto(traza['usua_idejecutor']),
      'usua_idasignado'      : valide_texto(traza['usua_idasignado']),
      'traz_fecha'           : traza['traz_fecha'],
      'traz_estado'          : valide_texto(traza['traz_estado']),
      'traz_fechacambio'     : valide_texto(traza['traz_fechacambio']),
      'traz_registradopor'   : valide_texto(traza['traz_registradopor']),
      'traz_procesoauditoria': valide_texto(traza['traz_procesoauditoria']),
      'traz_descripcion'     : valide_texto(traza['traz_descripcion'])
    }
    sqalchemy_insertar.insertar(sesion, TRAZABILIDAD_CLASE, data, False)
    sesion.commit()
    if contador > 2000:
        sesion.commit()
        contador = 0
"""

sesion.commit()