#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint

import pycamunda.processdef

def leer_despliegue_xml(camunda_url, despliegue_id, variables={}):
    despliegue = pycamunda.processdef.GetXML(
        url = camunda_url,
        id_ = despliegue_id
    
    )   

    return despliegue()

url           = "http://127.0.0.1:3600/engine-rest"
despliegue_id = "Gestion_proceso:1:55faad9f-14d3-11ed-9899-0242ac120006"     

print("")
despliegue_xml = leer_despliegue_xml(url, despliegue_id)
print("despliegue xml:", despliegue_xml)


import xml.etree.ElementTree as ET
tree = ET.ElementTree(ET.fromstring(despliegue_xml))
print(tree)