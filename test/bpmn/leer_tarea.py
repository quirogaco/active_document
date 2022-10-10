#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import pycamunda.task

def leer_tarea(camunda_url, tarea_id):
    tarea  = pycamunda.task.Get(
        url = camunda_url,
        id_ = tarea_id
        # process_instance_business_key: puede ser una opcion.
    )   

    return tarea()

url      = "http://127.0.0.1:3600/engine-rest"
tarea_id = "4671d244-14d4-11ed-9899-0242ac120006"     

#""" 
# tarea lee
print("")
print("tarea")
tarea = leer_tarea(url, tarea_id)
print("tarea:", tarea)
pprint.pprint(dir(tarea))