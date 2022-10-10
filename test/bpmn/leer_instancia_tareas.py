#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import pycamunda.task
import pycamunda.processdef

import pycamunda.execution

# Tarea vigente
def leer_instancia_tareas(camunda_url, instancia_id):
    tareas  = pycamunda.task.GetList(
        url                 = camunda_url,
        process_instance_id = instancia_id
    )   

    return tareas()[0]

camunda_url  = "http://localhost:3600/engine-rest"
instancia_id = "4671d244-14d4-11ed-9899-0242ac120006"                       

print("")
print("INSTANCIAS")
tarea = leer_instancia_tareas(camunda_url, instancia_id)
actividad_key = tarea.task_definition_key
print(tarea)
print("")
print("despliegue:", tarea.process_definition_id)
print("instancia:", tarea.process_instance_id)
print("actividad nombre, key:", tarea.name, actividad_key)
print("TAREA ID:", tarea.id_)

# print("")
# print("")
# print("******************************")
# print(
#     pycamunda.execution.Execution(
#         url=camunda_url, 
#         _id=instancia_id
#     )   
# )

# # XML Proceso
# def leer_despliegue_xml(camunda_url, despliegue_id, variables={}):
#     despliegue = pycamunda.processdef.GetXML(
#         url = camunda_url,
#         id_ = despliegue_id
    
#     )   

#     return despliegue()

# url           = "http://localhost:3600/engine-rest"
# despliegue_id = "Gestion_proceso:1:55faad9f-14d3-11ed-9899-0242ac120006"     

# print("")
# despliegue_xml = leer_despliegue_xml(url, despliegue_id)
# print("despliegue xml:", despliegue_xml)


# import xml.etree.ElementTree as ET
# tree = ET.ElementTree(ET.fromstring(despliegue_xml))
# ns   = {'bpmn2':"http://www.omg.org/spec/BPMN/20100524/MODEL"}
# #tareas = tree.findall('bpmn2:process/bpmn2:userTask', ns)
# tarea = tree.find('bpmn2:process/bpmn2:userTask[@id="Asignacion_1"]', ns)
# pprint.pprint( tarea.items() )
# print( tarea )