#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import pycamunda.task

def tarea_completa(camunda_url, tarea_id, variables={}):
    tarea = pycamunda.task.Complete(
        url                      = camunda_url,
        id_                      = tarea_id,
        with_variables_in_return = True
    ) 

    for key, valor in variables.items():
        tarea.add_variable(key, valor) 

    return tarea()

url      = "http://127.0.0.1:3600/engine-rest"
tarea_id = "46737fff-14d4-11ed-9899-0242ac120006"                           

# Tarea completa
variables = {
    "estado"  : "TERMINADO",
    "etapa"   : "FINAL",    
    "accion"  : "RADICAR",
    "aprobado": "SI"
}
tarea_completa = tarea_completa(url, tarea_id, variables)
print("tarea_completa:", tarea_completa)
