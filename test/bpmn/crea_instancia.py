#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import pycamunda.processdef


def inicia_instancia(camunda_url, proceso_id, key="bk", variables={}):
    iniciar_instancia = pycamunda.processdef.StartInstance(
        url                      = camunda_url,
        id_                      = proceso_id,
        business_key             = "bk",# que sea unico es importante
        #case_instance_id         = "ci",
        #skip_custom_listeners    = True,
        #skip_io_mappings         = True,
        with_variables_in_return = True
    )   

    for key, valor in variables.items():
        iniciar_instancia.add_variable(key, valor) 
    #print(iniciar_instancia) 
    instancia = iniciar_instancia()

    return instancia

url           = "http://localhost:3600/engine-rest"
despliegue_id = "Gestion_proceso:1:55faad9f-14d3-11ed-9899-0242ac120006"             

print("")
print("INSTANCIA")
variables = {
    "estado"  : "PENDIENTE",
    "etapa"   : "ASIGNACION",    
    "accion"  : "ASIGNAR",
    "aprobado": "NO"
}
pprint.pprint(variables)
instancia = inicia_instancia(url, despliegue_id, "001", variables)
print(instancia.id_)