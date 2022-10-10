#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint
from parent_import import parentdir

from parent_import import parentdir
modelo = parentdir.parentdir.librerias.bpmn.modelo


def diagrama_corto():
    output_directory = "D:/gestor_2021/test/bpmn/"
    output_file      = "corto.bpmn"

    # Crea objeto diagrama
    bpmn_grafo = modelo.crea_grafo()
    
    # Crea proceso
    proceso_id = modelo.crea_proceso(bpmn_grafo, nombre_proceso="gestion")
    #print("proceso_id:", proceso_id)

    # Crea actividad de inicio
    [iniciar_id, _] = modelo.iniciar_evento(bpmn_grafo, proceso_id, "iniciar") 
    #print("iniciar_id:", iniciar_id, _)

    # Crea tarea humana
    [tarea_id, _] = modelo.tarea_humana(bpmn_grafo, proceso_id, "revision")

    # Vincula inicio->tarea humana
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, iniciar_id, tarea_id, "revisa")

    # Crea tarea servicio externos
    [tarea_externa_id, _] = modelo.tarea_servicio_externo(bpmn_grafo, proceso_id, "llamado_externo")

    # Vincula tarea humana->tarea servicio
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, tarea_id, tarea_externa_id, "revisa_servicio")

    # Crea puerta exclusiva
    [puerta_exclusiva_id, _] = modelo.puerta_exclusiva(bpmn_grafo, proceso_id, "aprobado")

    # Vincula tarea externa
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, tarea_externa_id, puerta_exclusiva_id, "revisa")

    # Crea tarea humana1
    [tarea_id1, _] = modelo.tarea_humana(bpmn_grafo, proceso_id, "revision1")
    # Vincula puerta_exclusiva->tarea humana1
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, puerta_exclusiva_id, tarea_id1, "UNO", '${aprobado=="UNO"}')

    # Crea tarea humana2
    [tarea_id2, _] = modelo.tarea_humana(bpmn_grafo, proceso_id, "revision2")
    # Vincula puerta_exclusiva->tarea humana2
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, puerta_exclusiva_id, tarea_id2, "DOS", '${aprobado=="DOS"}')

    # Crea tarea humana3
    [tarea_id3, _] = modelo.tarea_humana(bpmn_grafo, proceso_id, "revision3")
    # Vincula puerta_exclusiva->tarea humana3
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, puerta_exclusiva_id, tarea_id3, "TRES", '${aprobado=="TRES"}')

    # Crea tarea humana4
    [tarea_id4, _] = modelo.tarea_humana(bpmn_grafo, proceso_id, "revision4")
    # Vincula puerta_exclusiva->tarea humana4
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, puerta_exclusiva_id, tarea_id4, "CUATRO", '${aprobado=="CUATRO"}')

    # Crea actividad final
    [finalizar_id, _] = modelo.finalizar_evento(bpmn_grafo, proceso_id, "finalizar")

    # Vincula tareas humanas-finalizar
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, tarea_id1, finalizar_id)
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, tarea_id2, finalizar_id)
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, tarea_id3, finalizar_id)
    modelo.secuencia_flujo(bpmn_grafo, proceso_id, tarea_id4, finalizar_id)

    

    # Salva definicion bpmn
    modelo.exportar_grafo(bpmn_grafo, output_directory, output_file)

diagrama_corto()
