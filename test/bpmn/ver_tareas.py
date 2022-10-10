#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import pycamunda.task

def leer_tarea(camunda_url, tarea_id):
    tarea  = pycamunda.task.Get(
        url = camunda_url,
        id_ = tarea_id
    )   

    return tarea

def tarea_modifica_variable(camunda_url, tarea_id, variables={}):
    tarea_variable = pycamunda.task.LocalVariablesModify(
        url = camunda_url,
        task_id = tarea_id
    ) 

    for key, valor in variables.items():
        tarea_variable.add_variable(key, valor) 

    tarea_variable()

    return tarea_variable

def tarea_completa(camunda_url, tarea_id, variables={}):
    tarea = pycamunda.task.Complete(
        url                      = camunda_url,
        id_                      = tarea_id,
        with_variables_in_return = True
    ) 

    for key, valor in variables.items():
        tarea.add_variable(key, valor) 

    tarea()

    return tarea

url      = "http://172.22.116.189:3600/engine-rest"
tarea_id = "e4f04b46-583b-11eb-bffa-0242ac120005"                           

#""" 
# Tarea lee
print("")
print("TAREA")
tarea = leer_tarea(url, tarea_id)
print("tarea:", tarea)

"""
# Asigna variables
variables = {
    "aprobado": True
}
tarea_variable = tarea_modifica_variable(url, tarea_id, variables)
print("tarea_variable:", tarea_variable)
"""

"""
# Tarea completa
#variables = {}
tarea_completa = tarea_completa(url, tarea_id, variables)
print("tarea_completa:", tarea_completa)
"""