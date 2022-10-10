#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime

import orjson

import pycamunda.deployment
import pycamunda.base
import pycamunda.processdef
import pycamunda.processinst

# Crea definición de despliegue (DEFINICION DE FLUJO)
def crear_definicion(camunda_url, nombre, fuente, tenant_id, ruta_archivo_bpmn):
    # Despliegue de proceso (DEFINICIóN)
    crea_despliegue_camunda = pycamunda.deployment.Create(
        url       = camunda_url, 
        name      = nombre, 
        source    = fuente, 
        tenant_id = tenant_id        
    )  

    print("...")
    print("")
    pprint.pprint(dir(crea_despliegue_camunda))
    print("")
    print("")
    

    """
    crea_despliegue_camunda = pycamunda.deployment.Create(
        url       = camunda_url, 
        name      = nombre, 
        source    = fuente, 
        tenant_id = tenant_id        
    )
    """


    # Adiciona archivo BPMN
    # Archivo BPMN
    archivo_bpmn  = open(ruta_archivo_bpmn)
    crea_despliegue_camunda.add_resource(file=archivo_bpmn)    
    
    # Crea el despliegue en servidor
    definicion = crea_despliegue_camunda()
    
    # Cierar archivo
    archivo_bpmn.close()
    
    return definicion

# Crea instancia del flujo desplegado
def inicia_instancia(camunda_url, despliegue_id, key, variables={}):
    # Crea instancia
    iniciar_instancia = pycamunda.processdef.StartInstance(
        url                      = camunda_url,
        id_                      = despliegue_id,
        business_key             = "bk",        
        with_variables_in_return = True
        #case_instance_id         = "ci",
        #skip_custom_listeners    = True,
        #skip_io_mappings         = True,
    )   

    # Variable de la instancia
    for key, valor in variables.items():
        iniciar_instancia.add_variable(key, valor) 
    
    instancia = iniciar_instancia()

    return instancia


# NAVEGADOR: http://172.26.87.179:8080/camunda/app/admin
# http://192.168.72.212:8080/camunda    demo/demo

url        = "http://172.26.87.179:8080/engine-rest"

#lista = pycamunda.processdef.GetList(url)
#pprint.pprint(lista())

#"""
print("")
print("DESPLIEGUE")
definicion    = crear_definicion(url, "CORTO", "GESTOR", "ESAP", "D:/gestor_2021_vite/test/bpmn/diagrama.bpmn")
print(definicion)
definicion_id = list(definicion.deployed_process_definitions.keys())[0]

print(definicion_id)
#"""

"""
print("")
print("INSTANCIA")
variables = {
    'texto'   : 'texto',
    'numero'  : 89,
    'fecha'   : str(orjson.dumps(datetime.datetime.now(), option=orjson.OPT_OMIT_MICROSECONDS ), 'utf-8'),
    'aprobado': "SI"
}
pprint.pprint(variables)
instancia = inicia_instancia(url, definicion_id, "key", variables)
print(instancia)
"""