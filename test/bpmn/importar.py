# coding=utf-8
"""
Test unit, using simple graph made in BPMNEditor editor for import/export operation
"""
import os, pprint

import bpmn_python.bpmn_diagram_visualizer as visualizer
import bpmn_python.bpmn_diagram_rep as diagram



def importar():
    directory = "D:/gestor_2021/test/bpmn/"
    entra     = "corto_expression.bpmn"
    salida    = "corto_expression_sale.bpmn"

    bpmn_grafo = diagram.BpmnDiagramGraph()
    bpmn_grafo.load_diagram_from_xml_file(directory + entra)
    bpmn_grafo.export_xml_file(directory, salida)
    #pprint.pprint(bpmn_grafo.sequence_flows)

importar()