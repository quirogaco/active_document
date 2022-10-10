#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from parent_import import parentdir

from parent_import import parentdir
modelo = parentdir.parentdir.librerias.bpmn.modelo


def diagrama_corto():
    output_directory = "D:/gestor_2021/test/bpmn/"
    output_file      = "service.bpmn"

    # Crea objeto diagrama
    bpmn_grafo = modelo.crea_grafo()
    
    # Crea proceso
    proceso_id = modelo.crea_proceso(bpmn_grafo, nombre_proceso="gestion")
    #print("proceso_id:", proceso_id)

    # Crea actividad de inicio
    [iniciar_id, _] = modelo.iniciar_evento(bpmn_grafo, proceso_id, "iniciar") 
    
    # Crea tarea servicio externos
    [tarea_externa_id, _] = modelo.tarea_servicio_externo(bpmn_grafo, proceso_id, "llamado_externo")

    # Vincula tarea humana->tarea servicio
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, iniciar_id, tarea_externa_id)

    # Crea actividad final
    [finalizar_id, _] = modelo.finalizar_evento(bpmn_grafo, proceso_id, "finalizar")

    # Vincula tareas humanas-finalizar
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, tarea_externa_id, finalizar_id)
    
    # Salva definicion bpmn
    modelo.exportar_grafo(bpmn_grafo, output_directory, output_file)

diagrama_corto()
