#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime

import pycamunda.deployment

# Crea definición de despliegue (DEFINICION DE FLUJO)
def crear_definicion(camunda_url, nombre, fuente, tenant_id, ruta_archivo_bpmn):
    # Despliegue de proceso (DEFINICÓN)
    crea_despliegue_camunda = pycamunda.deployment.Create(
        url       = camunda_url, 
        name      = nombre, 
        source    = fuente, 
        tenant_id = tenant_id        
    )  

    # Adiciona archivo BPMN
    # Archivo BPMN
    archivo_bpmn  = open(ruta_archivo_bpmn)
    crea_despliegue_camunda.add_resource(file=archivo_bpmn)    
    
    # Crea el despliegue en servidor
    definicion = crea_despliegue_camunda()
    
    # Cierra archivo
    archivo_bpmn.close()
    
    return definicion

url        = "http://localhost:3600/engine-rest"
definicion = crear_definicion(url, "INTEGRADO", "GESTOR", "ESAP", "D:/gestor_2021_vite/test/bpmn/xml/integrado.bpmn")
#definicion = crear_definicion(url, "APRUEBA", "GESTOR", "ACAPPELLA", "D:/gestor_2021_vite/test/bpmn/xml/aprueba.bpmn")
#definicion = crear_definicion(url, "APRUEBA", "GESTOR", "ACAPPELLA", "D:/gestor_2021_vite/test/bpmn/xml/opciones.bpmn")
#definicion = crear_definicion(url, "APRUEBA", "GESTOR", "ACAPPELLA", "D:/gestor_2021_vite/test/bpmn/xml/atributo.bpmn")

pprint.pprint(definicion)
print("")
print("--------------------------")
#keys = dict( definicion.deployed_process_definitions.keys() )
id = list(definicion.deployed_process_definitions.keys())[0]
print(id)