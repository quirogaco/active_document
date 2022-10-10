#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint, datetime

from librerias.datos.base import globales

##########################
# Datos de la estructura #
##########################
campos_basicos = [
    "radicado_en",
    "radicado_por",
    #"clase_radicado",
    #"canal_radicado",
    "nro_radicado",
    "fecha_radicado",
    'asunto',
    'medio_notificacion',

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
    #"""
    print("")
    print("")
    print("-------------------------------------------")
    print("armar estructura:")
    pprint.pprint(datos)
    #"""
    # Arma datos para insertar en la tabla
    atributos = {}
    resultado = {
        "estructura_": estructura,
    }

    # Asocia datos a base o atributos_
    for campo, valor in datos.items():
        print("campo:", campo, valor, type(valor))
        if (campo in campos_basicos):
            # Notificacion
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

    print("RESULTADO")
    pprint.pprint(resultado)     
    print("-------------------------------------------")
    print("")
    print("")    

    resultado["atributos_"] = atributos    

    return resultado

# Saca los datos  de la _estructura
def normaliza_estructura(estructura, datos, estricto): 
    #"""
    print("")
    print("")
    print("-------------------------------------------")
    print("normaliza_estructura:")
    pprint.pprint(datos) 
    #"""
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

    # Informacion de los atributos    
    resultado.update(atributos) 
    #"""
    print("RESULTADO")
    pprint.pprint(resultado) 
    print("-------------------------------------------")
    print("")
    print("") 
    #"""
    
    return resultado

globales.carga_procesamiento("radicados_entrada", "armar_estructura",     armar_estructura)
globales.carga_procesamiento("radicados_entrada", "normaliza_estructura", normaliza_estructura)