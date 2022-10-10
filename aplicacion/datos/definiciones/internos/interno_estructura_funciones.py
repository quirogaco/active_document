#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import pprint, datetime

from librerias.datos.base import globales

##########################
# Datos de la estructura #
##########################
campos_basicos = [
    'radicado_en',
    'radicado_por',
    'nro_radicado',
    'fecha_radicado',
    'asunto',
    'dependencia_envia_id',
    'funcionario_envia_id',
    'dependencia_recibe_id',
    'funcionario_recibe_id',
    'tipo_firma',
    'atributos_'
    
    "id", 
    "estado_", 
    "creado_en_", 
    "actualizado_en_", 
    "codigo_unidad_", 
    "codigo_organizacion_"
]

# Guarda los datos en la _estructura
def armar_estructura(estructura, datos):
    # Arma datos para insertar en la tabla
    definicion = globales.lee_definicion(estructura)    
    campos     = definicion.get("campos", {})

    # Arma datos para insertar en la tabla
    atributos = {}
    resultado = {
        "estructura_": estructura,
    }

    # Asocia datos a base o atributos_
    for campo, valor in datos.items():
        #print("campo:", campo, valor, type(valor))
        if (campo in campos_basicos):
            # Notificación
            if isinstance(valor, list):
                valor = ','.join(valor) 
            resultado[campo] = valor
        else:    
            campo_radicado = campos.get(campo, None)
            if campo_radicado != None:             
                tipo = campo_radicado.get("tipo", "texto")
                # Validar fecha y fecha hora
                if (tipo == "fecha"):
                    valor = valor.strftime('%Y-%m-%d')
                        
                if (tipo == "fechaHora"):
                    valor = str(valor)

                atributos[campo] = valor

    resultado["atributos_"] = atributos    

    return resultado

# Saca los datos  de la _estructura
def normaliza_estructura(estructura, datos, estricto):  
    # Preprara datos _atributos_
    atributos  = datos.get("atributos_", {})  
    try:
        del datos["atributos_"]  
    except:
        pass
    # Normaliza los datos a diccionario plano
    if estricto == True:
        resultado = {}
        for campo in campos_basicos:            
            valor            = datos[campo]
            resultado[campo] = valor
    else:
        resultado = datos     

    # Información de los atributos    
    resultado.update(atributos) 

    return resultado

globales.carga_procesamiento("radicados_interno", "armar_estructura",     armar_estructura)
globales.carga_procesamiento("radicados_interno", "normaliza_estructura", normaliza_estructura)