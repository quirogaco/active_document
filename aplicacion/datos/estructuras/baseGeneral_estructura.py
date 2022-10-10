#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from librerias.datos.base  import globales

# Información basica del registro
campos_basicos = [
    "codigo", 
    "nombre", 
    "detalle", 
    "id", 
    "estado_", 
    "creado_en_", 
    "actualizado_en_", 
    "codigo_unidad_", 
    "codigo_organizacion_"
]

# Informacion para salvar
def armar_estructura(estructura, datos):    
    # Arma datos para insertar en la tabla
    definicion  = globales.lee_definicion(estructura)    
    campos      = definicion.get("campos", {})

    # Procesa datos
    campos_keys = campos.keys()
    atributos   = {}
    resultado   = {
        "estructura_": estructura,
    }

    # Asocia datos a base o atributos_
    for campo, valor in datos.items():
        if (campo in campos_keys):            
            if (campo in campos_basicos):
                resultado[campo] = valor
            else:                
                tipo = campos[campo].get("tipo", "texto")

                # Validar fecha y fecha hora
                if (tipo == "fecha"):
                    valor = valor.strftime('%Y-%m-%d')
                    #valor = str(valor)
                    
                if (tipo == "fechaHora"):
                    valor = str(valor)

                atributos[campo] = valor

    resultado["atributos_"] = atributos    

    return resultado

def normaliza_estructura(estructura, datos, estricto):  
    # Información basica
    definicion  = globales.lee_definicion(estructura)    
    campos      = definicion.get("campos", {})

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