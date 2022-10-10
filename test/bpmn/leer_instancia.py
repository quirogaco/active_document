#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import pycamunda.task

import pycamunda.processinst


def leer_instancia(camunda_url, instancia_id, variables={}):
    instancia = pycamunda.processinst.Get(
        url = camunda_url,
        id_ = instancia_id
    
    )   

    return instancia()

url          = "http://127.0.0.1:3600/engine-rest"
instancia_id = "4671d244-14d4-11ed-9899-0242ac120006"     

print("")
print("instancia")
instancia = leer_instancia(url, instancia_id)
print("instancia:", instancia)
pprint.pprint(dir(instancia))
print("")
print("**********************")
print(
    instancia.business_key,
    instancia.case_instance_id,
    instancia.definition_id,
    instancia.id_,
    instancia.links,
    instancia.load(),
    instancia.suspended,
    instancia.tenant_id,
    instancia.variables
)