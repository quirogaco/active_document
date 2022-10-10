#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import pycamunda.task

import pycamunda.processinst


def leer_actividad(camunda_url, instancia_id):
    instancia = pycamunda.processinst.GetActivityInstance(
        url = camunda_url,
        id_ = instancia_id
    
    )

    return instancia()

url          = "http://127.0.0.1:3600/engine-rest"
instancia_id = "4671d244-14d4-11ed-9899-0242ac120006"     

print("")
print("actividad")
actividad = leer_actividad(url, instancia_id)
actividado_objeto = actividad.child_activity_instances[0]
#pprint.pprint(dir(actividado_objeto))

#print("actividado_objeto:", actividado_objeto)
print("")
print("**********************")
print(
    '\n activity_id:', actividado_objeto.activity_id,
    '\n activity_name:', actividado_objeto.activity_name,
    '\n activity_type:', actividado_objeto.activity_type,
    '\n id_:', actividado_objeto.id_,
    '\n execution_ids:', actividado_objeto.execution_ids,
    '\n name:', actividado_objeto.name,
    '\n parent_activity_instance_id:',actividado_objeto.parent_activity_instance_id,
    '\n process_instance_id:', actividado_objeto.process_instance_id
)