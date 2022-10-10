import orjson
import pprint
import logging
import sys

import prefect
from prefect.triggers import all_successful, all_failed
from prefect import task, Flow

logger = prefect.context.get("logger")
#logger.setLevel(logging.CRITICAL)

from parent_import import parentdir

flujos = parentdir.parentdir.librerias.flujos.flujos
valida = parentdir.parentdir.librerias.datos.validacion.valida

definicion = {
    "descripcion": "Definicion de areas y dependencias",
    "generica"   : "baseGeneral",
    "estructura" : "dependencias",
    "campos"     : {
        "codigo": {
            "tipo"       : "texto",
            "obligatorio": "si",
            "longitud"   : 50,
            "unico"      : "si"
        },

        "nombre": {
            "tipo"       : "texto",
            "obligatorio": "si",
            "longitud"   : 512,
            "unico"      : "si"
        },

        "descripcion": {
            "tipo"    : "entero",
            "longitud": 1024,
            #"defecto" : "ESTE VALOR POR DEFECTO"       
            #"defecto" : 876        
        }        
    }
}

modelo = valida.definirModelo("dependencias", definicion["campos"])

"""
datos = {
    'codigo': '01',
    'nombre': '03',
    'descripcion': "03"
}
"""

datos = {
    #'nombre': '03',     
}

print("")
print("")
print("modelo:", modelo)
print("")
print("-------- definicion -------")
pprint.pprint(definicion)
print("")
print("-------- data -------")
pprint.pprint(datos)
print("")
print("")

"""
# Valida datos tarea prefect
@task(name="valida datos pydantic", trigger=all_successful)
def validaDatosTarea(datos, modelo):
    print("<<<<<<<<<<<PASO 1>>>>>>>>>")
    sale = valida.validaDatos(datos, modelo)
    if sale["errores"] != None:
        mensaje = orjson.dumps(sale["errores"])
        raise ValueError(mensaje)

    return sale
"""

@task(name="A", trigger=all_successful)
def paso11(datos):
    print("<<<<<<<<<<<PASO 1111>>>>>>>>>", datos)
    sale = {
        "datos"  : "PASO 11111",
        "errores": None
    }
    
    raise ValueError("ojo")

    return sale

@task(name="B", trigger=all_successful)
def paso22(datos):
    print("<<<<<<<<<<<PASO 2>>>>>>>>>", datos)
    sale = {
        "datos"  : "PASO 2",
        "errores": None
    }
    
    return sale

@task(name="C", trigger=all_successful)
def paso33(datos):
    print("<<<<<<<<<<<PASO 3333>>>>>>>>>", datos)
    sale = {
        "datos"  : "PASO 33333",
        "errores": None
    }
    
    return sale

def crea_flujo():
    with Flow("general") as flujo:
        resultado_1 = paso11({})
        resultado_2 = paso22(resultado_1)
        resultado_3 = paso33(resultado_2)

    return flujo

flujo = crea_flujo()


"""
with Flow("general") as flujo:
    resultado_1 = valida.validaDatosTarea(datos, modelo)
    resultado_2 = paso2(resultado_1)
    resultado_3 = paso3(resultado_2)
"""

estado = flujo.run()

""""
print("")
print("-------RESULTADO-----------")
print("")
if flujos.exitoso(estado):
    resultado = flujos.resultado(flujo, estado, "Valida datos pydantic")
    print("exitoso:", flujos.exitoso(estado), resultado)

if flujos.fallido(estado):
    mensaje = flujos.mensajeError(flujo, estado)
    print("fallido:", flujos.fallido(estado), " - mensaje:", mensaje)
    print("json:", orjson.dumps(mensaje))
"""